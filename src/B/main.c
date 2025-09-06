#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  int cakes;
  int flour_left;
  int sugar_left;
} CakeResult;

struct {
  int floor;
  int sugar;
} Units = {
    .floor = 100,
    .sugar = 50,
};
#define min(a, b) a < b ? a : b

CakeResult cake_calculator(int flour, int sugar) {
  int nfloor, nsugar, ncakes;
  CakeResult answer;

  { // number of cakes which can be made with:

    nfloor = flour / Units.floor; // `floor` floor
    nsugar = sugar / Units.sugar; // `sugar` sugar
  }
  ncakes = min(nfloor, nsugar); // number of cakes which can be made
  answer.cakes = ncakes;
  answer.flour_left = flour - (Units.floor * ncakes); // remeaning floor
  answer.sugar_left = sugar - (Units.sugar * ncakes); // remeaning sugar
  return answer;
}

int main() {
  char flour_str[100], sugar_str[100];

  // Read input from stdin
  if (!fgets(flour_str, sizeof(flour_str), stdin) ||
      !fgets(sugar_str, sizeof(sugar_str), stdin)) {
    fprintf(stderr, "Error: Failed to read input\n");
    return 1;
  }

  // Remove newline characters
  flour_str[strcspn(flour_str, "\n")] = 0;
  sugar_str[strcspn(sugar_str, "\n")] = 0;

  // Convert inputs to integers
  char *endptr;
  int flour = strtol(flour_str, &endptr, 10);
  if (*endptr != '\0') {
    fprintf(stderr, "Input Error: Invalid flour value\n");
    return 1;
  }

  int sugar = strtol(sugar_str, &endptr, 10);
  if (*endptr != '\0') {
    fprintf(stderr, "Input Error: Invalid sugar value\n");
    return 1;
  }

  // Call the cake calculator function
  CakeResult result = cake_calculator(flour, sugar);

  // Print the result to stdout
  printf("%d %d %d\n", result.cakes, result.flour_left, result.sugar_left);

  return 0;
}
