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
"""
    .PHONY: test
    test:
        for test in $(TESTS); do bash test-runner.sh $$test || exit 1; done
"""
django_tests: FORCE
	./pytests.sh
"""
pip: requirements/$(SETTINGS).txt virtual_env_set
	#pip install -r requirements/$(SETTINGS).txt

virtualenv:
	virtualenv --no-site-packages $(VIRTUAL_ENV)
	echo $(VIRTUAL_ENV)
"""
clean: