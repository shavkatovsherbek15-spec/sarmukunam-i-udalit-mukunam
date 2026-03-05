set -o errexit

pip install -r requirements.txt

python manage.py collecstatic --noinput

python manage.py migrate