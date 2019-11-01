cython:
	python3 setup.py build_ext --inplace
	cp build/temp.linux-x86_64-3.7/dis_func_cyth.o .

clean:
	rm -fr build
	rm *.c
	rm *.html
	rm *.o

bench:
	sudo nice -n -11 python3 dis_func.py
