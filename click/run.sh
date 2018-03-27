virtualenv ./venv
source ./venv/bin/activate
pip install click

python cmd.py
python cmd.py --count 100
python cmd.py -c 500
