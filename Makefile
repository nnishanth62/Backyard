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
	git pull origin master
	git push origin master

tests:
	echo "testing ... "

django_tests: FORCE
	./pytests.sh

clean: