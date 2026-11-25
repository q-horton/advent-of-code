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

typedef struct {
  int* data;
  unsigned int length;
} Report;

typedef struct {
  Report* data;
  unsigned int length;
} Reports;

Reports parse_input(Input input) {
  Reports reports;
  reports.data = calloc(input.length, sizeof(Report));
  reports.length = input.length;

  for (unsigned int i = 0; i < input.length; i++) {
    Report* report = &reports.data[i];
    String* line = &input.lines[i];
    report->data = calloc(line->length / 2, sizeof(int));

    unsigned int start = 0;
    for (unsigned int j = 0; j < line->length; j++) {
      if (line->data[j] == ' ') {
        line->data[j] = '\0';
        report->data[report->length] = atoi(&line->data[start]);
        report->length++;
        start = j+1;
      }
    }
    report->data[report->length] = atoi(&line->data[start]);
    report->length++;
  }
  
  return reports;
}

long part_one(Input input) {
  Reports reports = parse_input(input);

  int safe = 0;
  for (unsigned int i = 0; i < reports.length; i++) {
    char unsafe = 0;
    for (unsigned int j = 1; j < reports.data[i].length - 1; j++) {
      int prev = reports.data[i].data[j - 1];
      int curr = reports.data[i].data[j];
      int next = reports.data[i].data[j + 1];
      if (prev == curr || curr == next) {
        unsafe = 1;
        break;
      }
      if (prev > curr) {
        if (curr < next) {
          unsafe = 1;
          break;
        }
        if ((prev - curr > 3) || (curr - next > 3))  {
          unsafe = 1;
          break;
        }
      } else {
        if (curr > next) {
          unsafe = 1;
          break;
        }
        if ((curr - prev > 3) || (next - curr > 3)) {
          unsafe = 1;
          break;
        }
      }
    }
    if (!unsafe) {
      safe++;
    }
  }
  
  return safe;
}

long part_two(Input input) {
  Reports reports = parse_input(input);

  int safe = 0;
  for (unsigned int i = 0; i < reports.length; i++) {
    for (unsigned int k = 0; k < reports.data[i].length; k++) {
      char unsafe = 0;
      for (unsigned int j = 1; j < reports.data[i].length - 2; j++) {
        int prev = (j - 1 < k) ? reports.data[i].data[j - 1] : reports.data[i].data[j];
        int curr = (j < k) ? reports.data[i].data[j] : reports.data[i].data[j + 1];
        int next = (j + 1 < k) ? reports.data[i].data[j + 1] : reports.data[i].data[j + 2];
        if (prev == curr || curr == next) {
          unsafe = 1;
        } else if (prev > curr) {
          if (curr < next) {
            unsafe = 1;
          } else if ((prev - curr > 3) || (curr - next > 3))  {
            unsafe = 1;
          }
        } else {
          if (curr > next) {
            unsafe = 1;
          } else if ((curr - prev > 3) || (next - curr > 3)) {
            unsafe = 1;
          }
        }
      }
      if (unsafe == 0) {
        safe++;
        break;
      }
    }
  }
  
  return safe;
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
        input.capacity = 2 * input.capacity;
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
        line.capacity = 2 * line.capacity;
      }
      line.data[line.length] = c;
      line.length++;
    }

    // Read next char
    c = fgetc(file);
  }

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
  
  if (argc == 1) {
    printf("Part 1 result:\r\n%ld\r\n", part_one(input));
    printf("Part 2 result:\r\n%ld\r\n", part_two(input));
  } else if (argc == 2 && !strcmp(argv[1], "1")) {
    printf("Part 1 result:\r\n%ld\r\n", part_one(input));
  } else if (argc == 2 && !strcmp(argv[1], "2")) {
    printf("Part 2 result:\r\n%ld\r\n", part_two(input));
  }

  free_input(input);
  
  return 0;
}
