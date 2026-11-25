#include <ctype.h>
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

void merge_sort(int* list, int length) {
  if (length <= 1) {
    return;
  }
  merge_sort(list, length / 2);
  merge_sort(&list[length / 2], length - (length / 2));

  int li = 0;
  int ri = length / 2;
  while (li < ri && ri < length) {
    if (list[li] <= list[ri]) {
      li++;
    } else {
      int temp[2] = {list[li], list[li]};
      for (int j = li + 1; j <= ri; j++) {
        temp[j % 2] = list[j];
        list[j] = temp[(j + 1) % 2];
      }
      list[li] = temp[ri % 2];
      li++;
      ri++;
    }
  }
}

int diff(int a, int b) {
  return (a >= b) ? a - b : b - a;
}

long part_one(Input input) {
  // Parse input
  int list_left[input.length];
  int list_right[input.length];
  for (unsigned int i = 0; i < input.length; i++) {
    unsigned int j;
    for (j = 0; j < input.lines[i].length; j++) {
      if (isspace(input.lines[i].data[j])) {
        input.lines[i].data[j] = '\0';
        break;
      }
    }
    list_left[i] = atoi(input.lines[i].data);
    for (j++; j < input.lines[i].length; j++) {
      if (!isspace(input.lines[i].data[j])) {
        break;
      }
    }
    list_right[i] = atoi(&input.lines[i].data[j]);
  }

  // Sort lists
  merge_sort(list_left, input.length);
  merge_sort(list_right, input.length);

  // Find differences
  int total_dist = 0;
  for (unsigned int i = 0; i < input.length; i++) {
    total_dist += diff(list_left[i], list_right[i]);
  }
  
  return total_dist;
}

long part_two(Input input) {
  // Parse input
  int list_left[input.length];
  int list_right[input.length];
  for (unsigned int i = 0; i < input.length; i++) {
    unsigned int j;
    for (j = 0; j < input.lines[i].length; j++) {
      if (isspace(input.lines[i].data[j])) {
        input.lines[i].data[j] = '\0';
        break;
      }
    }
    list_left[i] = atoi(input.lines[i].data);
    for (j++; j < input.lines[i].length; j++) {
      if (!isspace(input.lines[i].data[j])) {
        break;
      }
    }
    list_right[i] = atoi(&input.lines[i].data[j]);
  }

  // Sort lists
  merge_sort(list_right, input.length);

  // Find differences
  int similarity = 0;
  for (unsigned int i = 0; i < input.length; i++) {
    int count = 0;
    for (unsigned int j = 0; j < input.length; j++) {
      if (list_right[j] == list_left[i]) {
        count++;
      } if (list_right[j] > list_left[i]) {
        break;
      }
    }
    similarity += list_left[i] * count;
  }
  
  return similarity;
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
