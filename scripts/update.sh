cd /home/ubuntu/ukraine_data
git pull
pipenv run python scripts/refresh_files.py
git add --ignore-removal *.csv
git commit -m "[add] latest data"
git push git@github.com-ukraine_data:Leibniz-HBI/ukraine_data

