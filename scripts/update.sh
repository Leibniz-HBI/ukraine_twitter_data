cd /home/ubuntu/ukraine_data
git pull
pipenv run python scripts/refresh_files.py --chunk_size 250000
git add --ignore-removal *"$(date --date="yesterday" +%F)"*.csv
git commit -m "[add] data for $(date --date='yesterday' +%F)"
git push git@github.com-ukraine_data:Leibniz-HBI/ukraine_data

