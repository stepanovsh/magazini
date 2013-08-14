requirements:
	@echo "Installing requirements"
	@pip install -r requirements.txt

db:
	python manage.py syncdb --settings=magazini.settings.local

run:
	python manage.py runserver --settings=magazini.settings.local

collectstatic:
        python manage.py collectstatic --settings=magazini.settings.local


default:
	@make requirements
	@make db
	@make run

