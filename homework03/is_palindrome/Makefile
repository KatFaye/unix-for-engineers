CC=	gcc
CFLAGS=	-Wall -g -std=gnu99
TARGET= is_palindrome

all: $(TARGET)

$(TARGET): $(TARGET).o
	$(CC) $(CFLAGS) $^ -o $@

test: $(TARGET) $(TARGET).input $(TARGET).output
	./$(TARGET) < $(TARGET).input > test.txt
	diff -s test.txt is_palindrome.output

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $^

clean:
	rm -f $(TARGET) *.o *.s *.txt
