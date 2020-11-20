import argparse

parser = argparse.ArgumentParser(prog="doubleit.py")

parser.add_argument("numbers", type=int, nargs="*",
                    help="The integer to be doubled")

parser.add_argument("-v", "--verbose", action="store_true",
                    help="Add debugging output to response")

args = parser.parse_args()

for n in args.numbers:
    if args.verbose:
        print("input", n)
    print(n * 2)
