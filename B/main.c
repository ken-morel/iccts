#include <stdlib.h>

#define min(a, b) a < b ? a : b

typedef int *CakeAnswer;
// 0 -> n cakes made
// 1 -> n floor remeaning
// 2 -> n sugar remeaning

struct {
  int floor;
  int sugar;
} Units = {
    .floor = 100,
    .sugar = 50,
};

CakeAnswer makeAnswer() {
  CakeAnswer ans = (CakeAnswer)calloc(3, sizeof(int));
  if (ans == NULL)
    exit(51);
  return ans;
}

CakeAnswer cake_calculator(int floor, int sugar) {
  int nfloor, nsugar, ncakes;
  CakeAnswer answer = makeAnswer(); // Creating the answer

  { // number of cakes which can be made with:

    nfloor = floor / Units.floor; // `floor` floor
    nsugar = sugar / Units.sugar; // `sugar` sugar
  }

  ncakes = min(nfloor, nsugar); // number of cakes which can be made
  answer[0] = ncakes;
  answer[1] = floor - (Units.floor * ncakes); // remeaning floor
  answer[2] = sugar - (Units.sugar * ncakes); // remeaning sugar
  return answer;
}
