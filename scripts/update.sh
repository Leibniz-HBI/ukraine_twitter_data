cd /home/ubuntu/ukraine_data
pipenv run python scripts/refresh_files.py
git add *.csv
git add *.sh
git commit -a -m "[add] latest data"
git push git@github.com-ukraine_data:Leibniz-HBI/ukraine_data

