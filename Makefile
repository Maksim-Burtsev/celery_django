run:
	python manage.py runserver

migrate:
	python manage.py makemigrations && python manage.py migrate

shell:
	python manage.py shell

su:
	python manage.py createsuperuser

test:

	python manage.py test

req:
	pip3 freeze >  requirements.txt