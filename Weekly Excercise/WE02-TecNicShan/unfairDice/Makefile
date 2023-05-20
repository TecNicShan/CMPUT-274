now:
	echo "Empty.  Use me."

push:
	git commit -a
	git push

validate:
	python3 submission_validator.py

clean:
# For MacOS
	-rm .DS_Store
	-rm -r __pycache__
	-rm Drivers/out.*


test:
	make biased
	make histo

histo:
	-(cd Drivers; ln -s ../unfairDice.py .)
	@echo "*** NOTE:  If ln fails, you can ignore it"
#
	python3 Drivers/test11.py > Drivers/out.11
	diff Drivers/out.11 Expected/test11.txt
#
	python3 Drivers/test12.py > Drivers/out.12
	diff Drivers/out.12 Expected/test12.txt
#
	python3 Drivers/test13.py > Drivers/out.13
	diff Drivers/out.13 Expected/test13.txt
#
	python3 Drivers/test14.py > Drivers/out.14
	diff Drivers/out.14 Expected/test14.txt
#
	python3 Drivers/test15.py > Drivers/out.15
	diff Drivers/out.15 Expected/test15.txt
#
	python3 Drivers/test16.py > Drivers/out.16
	diff Drivers/out.16 Expected/test16.txt
#
	python3 Drivers/test17.py > Drivers/out.17
	diff Drivers/out.17 Expected/test17.txt
#
	python3 Drivers/test18.py > Drivers/out.18
	diff Drivers/out.18 Expected/test18.txt
#
	python3 Drivers/test19.py > Drivers/out.19
	diff Drivers/out.19 Expected/test19.txt
#
	python3 Drivers/test20.py > Drivers/out.20
	diff Drivers/out.20 Expected/test20.txt

biased:
	-(cd Drivers; ln -s ../unfairDice.py .)
	@echo "*** NOTE:  If ln fails, you can ignore it"
#
	python3 Drivers/test01.py > Drivers/out.01
	diff Drivers/out.01 Expected/test01.txt
#
	python3 Drivers/test02.py > Drivers/out.02
	diff Drivers/out.02 Expected/test02.txt
#
	python3 Drivers/test03.py > Drivers/out.03
	diff Drivers/out.03 Expected/test03.txt
#
	python3 Drivers/test04.py > Drivers/out.04
	diff Drivers/out.04 Expected/test04.txt
#
	python3 Drivers/test05.py > Drivers/out.05
	diff Drivers/out.05 Expected/test05.txt
#
	python3 Drivers/test06.py > Drivers/out.06
	diff Drivers/out.06 Expected/test06.txt
#
	python3 Drivers/test07.py > Drivers/out.07
	diff Drivers/out.07 Expected/test07.txt
#
	python3 Drivers/test08.py > Drivers/out.08
	diff Drivers/out.08 Expected/test08.txt
#
	python3 Drivers/test09.py > Drivers/out.09
	diff Drivers/out.09 Expected/test09.txt
#
	python3 Drivers/test10.py > Drivers/out.10
	diff Drivers/out.10 Expected/test10.txt
