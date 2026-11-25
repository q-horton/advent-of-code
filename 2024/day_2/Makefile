CC     = gcc
CFLAGS ?= -Wall -Wextra -g
CFLAGS += -std=c99

solution: code.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $< $(LDLIBS)

clean:
	rm -f solution

.PHONY: clean
