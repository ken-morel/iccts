# Problem B: Cake Calculator

For this problem we are given the number of flour as `Units.flour` and sugar as `Units.sugar`, needed to pruduce one cake. Then the problem is given an amount of flour, `flour` and sugar `sugar` to calculate the maximum amount of cakes, and remaining flour and sugar after those are produced.

## Description

The simple aim of my algorithm is to be able to compute the maximum amount of cake produced and remaining cake with a small amount of computations and allocation.

## Algorithm

- The amount of flour and sugar available is gotten from input.
- The maximum amount of of cakes pruducable with each is computed through simple integer devision.
- The then maximum number of caked pruduced is taken to be the minimum of the previous, ans stored as first response array value.
- Using this value, the used amount of flour and sugar is calculated and substracted from the provided amounts, that in a one operation so as to reduce allocations without a great impact on code complexity.
- The remaining are then stored as second and third array elements and returned as response array.

The full code sample associated with this response and illustrating this algorithm is available at [./main.c].
