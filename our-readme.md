## For windows :
Go to : https://www.python.org/downloads/release/python-3100/
Download the Windows installer (64-bit)
During installation : Check "Add Python 3.10 to PATH"

Verify version using : py -3.10 --version

py -3.10 -m venv env
env/scripts/activate

python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

create a .env file and add 'SECRET_KEY'

python create_db.py
python run.py

## For Linux :
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-dev -y

python3.10 -m venv env
source env/bin/activate

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

create a .env file and add 'SECRET_KEY'

python create_db.py
python run.py


