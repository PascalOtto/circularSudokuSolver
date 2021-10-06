from constraint import *


def solve_constraint():
    given_fields = dict()
    for x in range(6):
        for y in range(6):
            given_fields[(x, y)] = [1, 2, 3, 4, 5, 6]

    given_fields[(0, 0)] = [2]
    given_fields[(0, 2)] = [4]
    given_fields[(0, 5)] = [6]

    given_fields[(1, 0)] = [4]
    given_fields[(1, 5)] = [3]

    given_fields[(2, 1)] = [6]
    given_fields[(2, 4)] = [4]

    given_fields[(3, 2)] = [2]

    given_fields[(4, 1)] = [2]
    given_fields[(4, 3)] = [6]
    given_fields[(4, 5)] = [4]

    given_fields[(5, 0)] = [1]
    given_fields[(5, 3)] = [5]

    problem = Problem(RecursiveBacktrackingSolver())

    for i in list(given_fields.keys()):
        problem.addVariable(i, given_fields[i])

    for x in range(6):
        affected_variables = set()
        for y in range(6):
            affected_variables.add((x, y))
        problem.addConstraint(AllDifferentConstraint(), affected_variables)

    for y in range(6):
        affected_variables = set()
        for x in range(6):
            affected_variables.add((x, y))
        problem.addConstraint(AllDifferentConstraint(), affected_variables)

    solution = problem.getSolution()
    solution = sorted(solution.items())
    print(solution)


def main():
    solve_constraint()


if __name__ == "__main__":
    main()
