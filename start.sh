# Create a virtual environment and activate it in this session
python -m venv .venv/
source .venv/scripts/activate

# Update pip and install the required packages
pip install --upgrade pip
pip install -r requirements.txt

# Migrate database and create first user
python manage.py migrate --noinput
python manage.py create_first_user