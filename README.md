# RoboTradeMangermentSystem

heroku git:remote -a robotraderwebservice
git add.
git commit -am "make it better"
git push herokumaster

git push heroku master
heroku logs --tail
git commit --allow-empty -m "Adjust buildpacks on Heroku"
heroku buildpacks:set heroku/python
git push heroku master
- Create Procfile
heroku ps:scale web=1