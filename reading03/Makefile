#Makefile for hello.c (Reading 03)

all: hello-dynamic hello-static hello-debug hello-profile

hello-dynamic: hello.o
	gcc -o hello-dynamic hello.o

hello-static: hello.o
	gcc -static -static-libgcc -static-libstdc++ -o hello-static hello.o
hello-debug: hello.o
	gcc -g -o hello-debug hello.o
hello-profile:
	gcc -g -pg -o hello-profile hello.o
hello.o: hello.c
	gcc -c hello.c
clean:
	rm *.o hello-*
