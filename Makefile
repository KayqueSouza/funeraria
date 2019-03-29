include .env
UI_DIR=ui

clean:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete
	@rm -rf dist

flake:
	pre-commit run -a -v

test:
	@cd $(DJANGO_PROJECT_DIR) && py.test -vv -s

new-migrations:
	@cd $(DJANGO_PROJECT_DIR) && ./manage.py makemigrations

migrate:
	@cd $(DJANGO_PROJECT_DIR) && ./manage.py migrate

django-shell:
	@cd $(DJANGO_PROJECT_DIR) && ./manage.py shell

run-django:
	@cd $(DJANGO_PROJECT_DIR) && ./manage.py runserver 0.0.0.0:9000

