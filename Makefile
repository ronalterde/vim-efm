test: test.c
	gcc -Wall -o test test.c

error_output.txt: haystack.txt
	python3 query_match.py haystack.txt foo > error_output.txt

.PHONY: clean
clean:
	rm -f test
	rm -f error_output.txt
