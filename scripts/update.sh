cd /home/ubuntu/ukraine_data
git pull
pipenv run python scripts/refresh_files.py
pipenv run python scripts/split_files.py
git add --ignore-removal *.csv
git commit -m "[add] data for $(date +%F)"
git push git@github.com-ukraine_data:Leibniz-HBI/ukraine_data

