# RoboTradeMangermentSystem

heroku git:remote -a robotraderwebservice
git add .
git commit -am "make it better"
git push herokumaster

git push heroku master
heroku logs --tail
git commit --allow-empty -m "Adjust buildpacks on Heroku"
heroku buildpacks:set heroku/python
git push heroku master
- Create Procfile
heroku ps:scale web=1

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

pip install dj_database_url
pip install django-heroku
pip install django-gunicorn

import dj_database_url
import django_heroku
