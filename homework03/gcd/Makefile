CC=	gcc
CFLAGS=	-Wall 
LD=	gcc
LDFLAGS= -Wall -shared 
AR=	ar
ARFLAGS= rcs
LIB = libgcd
TARGETS= gcd-static gcd-dynamic

all:	$(TARGETS)

gcd-static: main.o $(LIB).a
	$(CC) $(CFLAGS) -static $^ -o $@

gcd-dynamic: main.o $(LIB).so
	$(CC) $(CFLAGS) $^ -o $@

$(LIB).a: gcd.o
	$(AR) $(ARFLAGS) $(LIB).a gcd.o

$(LIB).so: gcd.o
	$(LD) $(LDFLAGS) gcd.o -o $(LIB).so

%.o: %.c #main, gcd
	$(CC) $(CFLAGS) -c -o $@ $^

clean:
	rm -f $(TARGETS) *.o *.a *.so
