import argparse

class Solver:
    def __init__(self, file_pth):
        self.file_pth = file_pth
        self.reports = []  # List of lists containing the reports
        self.parse_input()
        print(self.reports)

    def solve_part_1(self):
        """
        Current Solution Time Complexity: O(nm), n is no. reports, m is no. elements in report
        Current Solution Space Complexity: O(nm)
        :return: The no. of safe reports
        """
        sol = 0
        for report in self.reports:
            increasing = True
            safe = True
            for i in range(len(report)):
                if i == 0 or not safe: continue
                if i == 1: increasing = report[i] > report[i - 1]

                # Case 1: Neither increase nor decrease
                if report[i] == report[i - 1]:
                    safe = False

                # Case 2: Monotonicity
                if ((report[i] > report[i - 1]) != increasing):
                    safe = False

                # Case 3: Difference by > 3.
                if abs(report[i] - report[i - 1]) > 3:
                    safe = False

            if safe:
                sol += 1

        return sol

    def solve_part_2(self):
        """
        Current Solution Time Complexity: O(nm), n is no. reports, m is no. elements in report
        Current Solution Space Complexity: O(nm)
        :return: The no of safe reports including the problem dampener.
        """
        sol = 0
        for report in self.reports:
            increasing = True
            safe = True
            dampener_used = False  # Flag for keeping track of the dampener.
            i = -1
            while i < len(report) - 1:
                i += 1
                if i == 0 or not safe: continue
                if i == 1: increasing = report[i] > report[i - 1]

                # Case 1: Neither increase nor decrease
                if report[i] == report[i - 1]:
                    safe = False

                # Case 2: Monotonicity
                if ((report[i] > report[i - 1]) != increasing):
                    safe = False

                # Case 3: Difference by > 3.
                if abs(report[i] - report[i - 1]) > 3:
                    safe = False

                # Try using the dampener!
                if not safe and not dampener_used:
                    print(report, i, end=" ")
                    report[i:] = report[i + 1:]
                    print(report)
                    dampener_used = True
                    safe = True
                    i = 0

            if safe:
                sol += 1

            if dampener_used:
                print(safe)

        return sol

    def parse_input(self):
        # Read in all lines from the file
        l = None
        with open(self.file_pth, 'r') as f:
            l = f.readlines()
            f.close()

        # Parse lines from the .txt file into a sequence of reports
        for line in l:
            line = line.strip()  # Remove trailing whitespace
            line = line.split(' ')  # Split by space
            self.reports.append([int(l) for l in line])  # Cast to list<int>

if __name__ == '__main__':
    """
    Solve the Historian Hysteria problem. Run `python -m D02_Red_Nosed_Reports --help` for CLI usage.
    """
    # CLI Args
    parser = argparse.ArgumentParser(
        prog='D02_Red_Nosed_Reports.py',
        description='Solve the Red Nosed Reports problem (Day 2, 2024); Takes path to .txt as input.',
        epilog='Download the official testcase from https://adventofcode.com/2024'
    )
    parser.add_argument("-p", default="test_cases/2.txt", help="The path to the File containing the reports. See test_cases for example, or download the official test from AOC website.")
    args = parser.parse_args()

    # Instantiate the Solver and call the solve methods.
    sol = Solver(args.p)
    print("Part 1 Solution:", sol.solve_part_1())
    print("Part 2 Solution:", sol.solve_part_2())