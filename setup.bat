python3 -m pip install -r requirements.txt
cd opendlna\WUI\
python3 -m flask db init
python3 -m flask db migrate
python3 -m flask db upgrade
