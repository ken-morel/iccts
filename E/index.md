# Functional completeness of the nand

Basic gates can be defined as such:

```c
#define not(a)     !a
#define and(a, b)  a&&b
#define or(a, b)   a||b
```

The nand is said to be functionally complete because other gates can be expressed from it:
The nand is given by `~(A∧B)` for A and B be two inputs to the gate.

```c

int nand(int a, int b) {
  return not(and(a, b));
}
```

∨

## The `NOT` gate

This is the simpliest of all, it can be obtained by simply taking the input for both nand ports giving.

```c
int nand_not(int a) {
  return nand(a, a);
}
```

![Not gate](./not.png)

## The `AND` gate

Since the `NAND` gate is the negation of the `AND`, the `AND` can be easily gotten by negating the `NAND`'s output, using the previous `not` implemented in nand:

```c
int nand_and(int a, int b) {
  return nand_not(nand(a, b));
  // or harder: nand(nand(a, b), nand(a, b))
}
```

![And gate](./and.png)

## The `OR` gate

The or gate can be easily gotten via the nand by negating both input first before passing them in the nand.

```c
int nand_or(int a, int b) {
  return nand(nand_not(a), nand_not(b));
}
```

![And gate](./or.png)
