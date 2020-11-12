all: run
env: programs

PATH = /Users/arthurtainmont/Documents/s19/minishell/minishell/minishell

SRC =	test/test/get_next_line.c \
			test/test/get_next_line_utils.c \
			test/test/get_next_line.h \
			test/test/main.c

RM = rm -rf

run:
	python3 main.py

clean:
	$(RM) __pycache__ utils/__pycache__

fclean:
	$(RM) test/test/a.out
	$(RM) test/test/a.out2
	$(RM) __pycache__ utils/__pycache__

programs:
	gcc $(SRC)
	mv a.out test/test/a.out
	rm test/test/get_next_line.h.gch
	gcc test/test/main2.c -o test/test/a.out2
	pip3 install colorterm

re: fclean programs run
