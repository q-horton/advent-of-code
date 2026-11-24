#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MIN_LENGTH 32

typedef struct {
  char* data;
  unsigned int length;
  unsigned int capacity;
} String;

typedef struct {
  String* lines;
  unsigned int length;
  unsigned int capacity;
} Input;

long part_one(Input input) {
  for (unsigned int i = 0; i < input.length; i++) {
    printf("%s\r\n", input.lines[i].data);
  }
  return input.length;
}

long part_two(Input input) {
  return 0;
}

Input read_input() {
  // Initialise input structure
  Input input;
  input.lines = calloc(MIN_LENGTH, sizeof(String));
  input.length = 0;
  input.capacity = MIN_LENGTH;

  // Read lines
  String line;
  line.data = calloc(MIN_LENGTH + 1, sizeof(char));
  line.length = 0;
  line.capacity = MIN_LENGTH;

  FILE* file = fopen("input.txt", "r");
  int c = fgetc(file);
  
  while(c != EOF) {
    // Check next char for end of line
    if (c == '\n') {
      // Remove any carriage returns
      if (line.length > 0 && line.data[line.length - 1] == '\r') {
        line.length--;
        line.data[line.length] = '\0';
      } else {
        line.data[line.length] = '\0';
      }

      // Grow input capacity if required
      if (input.length >= input.capacity) {
        input.lines = realloc(input.lines, 2 * input.capacity * sizeof(String));
      }

      // Insert new line to input
      input.lines[input.length] = line;
      input.length++;
      line.data = calloc(MIN_LENGTH + 1, sizeof(char));
      line.length = 0;
      line.capacity = MIN_LENGTH;
    } else {
      // Check other next chars
      if (line.length >= line.capacity) {
        line.data = realloc(line.data, (2 * line.capacity + 1) * sizeof(char));
      }
      line.data[line.length] = c;
      line.length++;
    }

    // Read next char
    c = fgetc(file);
  }

  // Ensure that last line is saved to input
  if (input.length >= input.capacity) {
    input.lines = realloc(input.lines, (input.capacity + 1) * sizeof(String));
  }
  input.lines[input.length] = line;
  input.length++;

  return input;
}

void free_input(Input input) {
  for (unsigned int i = 0; i < input.length; i++) {
    free(input.lines[i].data);
  }
  free(input.lines);
}

int main(int argc, char** argv) {
  Input input = read_input();
  
  if(argc == 1 || (argc == 2 && !strcmp(argv[1], "1"))) {
    printf("Part 1 result:\r\n%ld\r\n", part_one(input));
  } else if (argc == 2 && !strcmp(argv[1], "2")) {
    printf("Part 2 result:\r\n%ld\r\n", part_two(input));
  }

  free_input(input);
  
  return 0;
}
