export TEMPLATE_DIR = templates
DEV_DIR = main
HTML_DIR = templates
UTILS_DIR =
TEST_DIR =
BLOG_DIR = blog
REPO = Backyard
PY_LINT = flake8
PYLINT_FLAGS =

FORCE:

prod:
	-git commit -a
	git pull origin main
	git push origin main

tests:
	echo "testing ... "
	python3 blog/templates/tests.py
    #for test in $(TESTS);   do bash test-runner.sh $$test || exit 1;    done

django_tests: FORCE
	./pytests.sh

install:
	pip3 install -qr virt/requirements.txt --exists-action w

virtualenv:
	virtualenv --no-site-packages $(VIRTUAL_ENV)
	echo $(VIRTUAL_ENV)

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

run:
	python3 manage.py runserver

migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

heroku:
	git push heroku master

clean: