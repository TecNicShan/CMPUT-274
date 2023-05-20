DIFF_ARGS = --strip-trailing-cr

now:
	# Can change this
	make test

push:
	git commit -a
	git push

validate:
	python3 submission_validator.py

pep8:
	# Might have to do, in the VM:  sudo apt install pep8
	pep8 moneybags.py

clean:
# For MacOS
	-rm .DS_Store
	-rm -r __pycache__
	-rm -r test-cases/as-274-21-moneybags.py-test/Outputs
	-rm -r test-cases/as-274-21-moneybags.py-test/Resources
	-rm -r test-cases/as-274-21-moneybags.py-test/Errors

test:
	bash setup.sh
	@echo "**** WARNING *** Copying moneybags.py to directory soln/ ****"
	cp moneybags.py soln
	python3 TestCenter-master/testcenter.py -s soln -t test-cases -e --timeout 5

all:
	bash setup.sh
	@echo "**** WARNING *** Copying moneybags.py to directory soln/ ****"
	cp moneybags.py soln
	python3 TestCenter-master/testcenter.py -s soln -t test-cases --timeout 5
verbose:
	bash setup.sh
	@echo "**** WARNING *** Copying moneybags.py to directory soln/ ****"
	cp moneybags.py soln
	python3 TestCenter-master/testcenter.py -s soln -t test-cases -e -v --timeout 5
all-verbose:
	bash setup.sh
	@echo "**** WARNING *** Copying moneybags.py to directory soln/ ****"
	cp moneybags.py soln
	python3 TestCenter-master/testcenter.py -s soln -t test-cases -v --timeout 5
