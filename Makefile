run:
	python manage.py runserver

migrate:
	python manage.py makemigrations && python manage.py migrate

shell:
	python manage.py shell

su:
	python manage.py createsuperuser