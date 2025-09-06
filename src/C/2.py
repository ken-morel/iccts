import math

PROBS = [0.20, 0.15, 0.12, 0.10, 0.08, 0.06, 0.05, 0.05, 0.04, 0.03, 0.02, 0.10]


def findentropy(values: list[float]):
    def _unit(n: float):
        return n * math.log2(n)

    return -sum(map(_unit, values))


def main():
    print(f"The entropy is {findentropy(PROBS)}")


if __name__ == "__main__":
    main()
