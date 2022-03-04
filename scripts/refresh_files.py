import pandas as pd
from sqlalchemy import create_engine
from yaml import safe_load
from pathlib import Path
import click
import datetime

@click.command()
@click.option('--date', type=click.DateTime())
@click.option('--start_date', type=click.DateTime())
@click.option('--end_date', type=click.DateTime())
@click.argument('event_names', nargs=-1) # help="specify which configured event you want to export from the database. Leave empty to export all."
def main(date: datetime.date = None, start_date: datetime.date = None, end_date: datetime.date = None, event_names: list[str] = None):

    event_conf_path = Path("config.yaml")
    db_conf_path    = Path("db_conf.yaml")

    with event_conf_path.open() as file:
        events = safe_load(file)['events']
    with db_conf_path.open() as file:
        db_config = safe_load(file)

    engine = create_engine(f'postgresql://{db_config["db_user"]}:{db_config["db_password"]}@{db_config["db_host"]}:{db_config["db_port"]}/{db_config["db_name"]}')

    if date is not None:
        dates = [date]
    elif start_date is not None: 
        # check if end_date is there:
        if end_date is None:
            end_date = datetime.date.today()
        dates = [_ for _ in pd.date_range(start_date, end_date).format()]
    else:
        # default to yesterdays date
        dates = [datetime.date.today() - datetime.timedelta(days = 1)]
    if len(event_names) != 0:
        events = [event for event in events if event['name'] in event_names]
    for date in dates:
        date = date.strftime('%F')

        for event in events:
            name = event['db_id']

            print(f'Retrieving {date} for {name}')

            query = f"""select
        id,
        event,
        from_search,
        directly_from_search,
        from_stream,
        directly_from_stream,
        from_convo_search,
        directly_from_convo_search,
        from_quote_search, 
        directly_from_quote_search,
        from_timeline_search, 
        directly_from_timeline_search,
        inserted_at,
        last_updated_at,
        created_at 
    from
        twitter.tweets t
    where
        "event" = '{name}' and 
        date_trunc('day', created_at) = '{date}'
    order by id"""

            for index, data in enumerate(pd.read_sql_query(query, con=engine, chunksize=500000)):

                if len(data) > 0:
                    if event['name'] != event['db_id']:
                        # update event too inlcude lang-codes.
                        data['event'] = event['name']

                    # generate file for hydrator (plain txt, each id is a line)
                    file
                    data[['id']].\
                        to_csv(
                            f'{event["target_folder"]}hydrator-{date}-{event["name"]}.csv',
                            index=False,
                            header = False,
                            mode='a'
                        )
                    # dump csv without 'created_at'
                    data.\
                        drop(['created_at'], axis = 1).\
                        to_csv(
                            f'{event["target_folder"]}{date}-{event["name"]}_{index}.csv',
                            index=False
                        )
        
if __name__ == '__main__':
    main()
