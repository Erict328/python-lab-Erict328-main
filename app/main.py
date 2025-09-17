from app.lab import *
from app.data import students

GREEN = "\x1b[32m"
CLEAR = "\x1b[0m"

def run_problem_1():
   average = calculate_student_average(students, "Alice Johnson")
   print(f"{GREEN}==Problem 1=={CLEAR}\nAverage: {average}")

def run_problem_2():
   (lowest, highest) = lowest_highest_grade(students)
   print(f"{GREEN}==Problem 2=={CLEAR}\nLowest: {lowest}\nHighest: {highest}")

def run_problem_3():
   print(f"{GREEN}==Problem 3=={CLEAR}")
   print_feedback(students)

def run_problem_4():
   average = exam_average(students, "Math Test 1")
   print(f"{GREEN}==Problem 4=={CLEAR}\nAverage: {average}")

def run_bonus():
   print(f"{GREEN}==Bonus=={CLEAR}")
   print_report_card("Alice Johnson", students["Alice Johnson"])

def run_all():
   run_problem_1()
   print()
   run_problem_2()
   print()
   run_problem_3()
   print()
   run_problem_4()


import sys

COMMANDS = {
    "1": run_problem_1,
    "2": run_problem_2,
    "3": run_problem_3,
    "4": run_problem_4,
    "bonus": run_bonus,
    "all": run_all,
}

def _usage() -> str:
    return (
        "Usage:\n"
        "  uv run python -m app.main           # run all problems (default)\n"
        "  uv run python -m app.main 1         # run problem 1\n"
        "  uv run python -m app.main 2 4       # run multiple problems\n"
        "  uv run python -m app.main bonus     # run bonus\n"
        "  uv run python -m app.main all       # run all explicitly\n"
        "\n"
        "Valid commands: 1, 2, 3, 4, bonus, all\n"
    )

def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)

    # No args → default to all
    if not args:
        run_all()
        return 0

    # Allow multiple tokens (e.g., "2 4 bonus")
    for i, token in enumerate(args):
        fn = COMMANDS.get(token.lower())
        if fn is None:
            sys.stderr.write(f"Unknown command: {token}\n\n{_usage()}")
            return 2
        fn()
        # Pretty spacer between runs
        if i != len(args) - 1:
            print()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())