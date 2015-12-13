{
	heroku create
	heroku buildpacks:set git://github.com/heroku/heroku-buildpack-python.git
	pip install django-toolbelt
	echo "web: gunicorn --log-file - blackend.wsgi" > Procfile
	git branch heroku_support
	git checkout heroku_support
	git add .
	git commit "heroku support"
	git push heroku heroku_support
	heroku run python manage.py migrate
	heroku run python manage.py collectstatic
	heroku open
}