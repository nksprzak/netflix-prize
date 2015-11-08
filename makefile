FILES :=                              \
    .travis.yml                       \
    netflix-tests/md26977-RunNetflix.in   \
    netflix-tests/md26977-RunNetflix.out  \
    netflix-tests/md26977-TestNetflix.out \
    netflix-tests/md26977-TestNetflix.py  \
    Netflix.html                      \
    Netflix.log                       \
    Netflix.py                        \
    RunNetflix.py                     \
    RunNetflix.out                    \
    TestNetflix.out                   \
    TestNetflix.py                    \
    probe.txt


check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  RunNetflix.tmp
	rm -f  TestNetflix.tmp
	rm -rf __pycache__

config:
	git config -l

scrub:
	make clean
	rm -f  Netflix.html
	rm -f  Netflix.log
	rm -rf netflix-tests

status:
	make clean
	@echo
	git branch
	git remote -v
	git status


netflix-tests:
	git clone https://github.com/cs373-fall-2015/netflix-tests.git

Netflix.html: Netflix.py
	pydoc3 -w Netflix

Netflix.log:
	git log > Netflix.log

RunNetflix.tmp: probe.txt RunNetflix.out RunNetflix.py
	./RunNetflix.py < probe.txt > RunNetflix.tmp

TestNetflix.tmp: TestNetflix.py
	coverage3 run    --branch TestNetflix.py >>  TestNetflix.tmp 
	coverage3 report -m                      >> TestNetflix.tmp
