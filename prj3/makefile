myp3:	myp3.tab.o lex.yy.o
		cc -o myp3 lex.yy.o myp3.tab.o

myp3.tab.o:	myp3.tab.c
		cc -c myp3.tab.c

myp3.tab.c:	myp3.y
		bison -d myp3.y

lex.yy.o: lex.yy.c myp3.tab.h
		cc -c lex.yy.c

lex.yy.c:	myp3.l myp3.tab.c
		flex myp3.l
