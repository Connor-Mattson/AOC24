import argparse

class Solver:
    def __init__(self, file_pth):
        self.file_pth = file_pth
        self.loc_A = []  # The first list of locations (LHS)
        self.loc_B = []  # The second list of locations (RHS)
        self.parse_input()

    def solve_part_1(self):
        """
        Current Solution Time Complexity: O(nlog(n))
        Current Solution Space Complexity: O(n)
        :return: The sum of the distances between the left and right list
        """
        # Sort both lists in ascending order
        self.loc_A.sort()
        self.loc_B.sort()

        # Linear pass over lists to sum up the differences
        assert len(self.loc_A) == len(self.loc_B)
        sol = 0
        for i in range(len(self.loc_A)):
            sol += abs(self.loc_A[i] - self.loc_B[i])
        return sol

    def solve_part_2(self):
        """
        Current Solution Time Complexity: O(n)
        Current Solution Space Complexity: O(n)
        :return:
        """
        # Create a hashmap that stores the freq. of values in the right list.
        right_cnt = {}  # Maps int -> int
        for v in self.loc_B:
            if v not in right_cnt:
                right_cnt[v] = 1
            else:
                right_cnt[v] += 1

        # Linear pass over lists to calculate the similarity score.
        sol = 0
        for i in range(len(self.loc_A)):
            if self.loc_A[i] in right_cnt:
                sol += (self.loc_A[i] * right_cnt[self.loc_A[i]])
        return sol

    def parse_input(self):
        # Read in all lines from the file
        l = None
        with open(self.file_pth, 'r') as f:
            l = f.readlines()
            f.close()

        # Parse Lines into two separate lists (left list and right list)
        for line in l:
            line = line.strip()  # Remove trailing whitespace
            line = line.split('   ')  # Split by tab (3 spaces)
            self.loc_A.append(int(line[0]))
            self.loc_B.append(int(line[1]))

if __name__ == '__main__':
    """
    Solve the Historian Hysteria problem. Run `python -m D01_Historian_Hysteria --help` for CLI usage.
    """
    # CLI Args
    parser = argparse.ArgumentParser(
        prog='D01_Historian_Hysteria.py',
        description='Solve the Historian Hysteria problem (Day 1, 2024); Takes path to .txt as input.',
        epilog='Download the official testcase from https://adventofcode.com/2024'
    )
    parser.add_argument("-p", default="test_cases/1.txt", help="The path to the File containing the chief's location lists. See test_cases for example, or download the official test from AOC website.")
    args = parser.parse_args()

    # Instantiate the Solver and call the solve methods.
    sol = Solver(args.p)
    print("Part 1 Solution:", sol.solve_part_1())
    print("Part 2 Solution:", sol.solve_part_2())