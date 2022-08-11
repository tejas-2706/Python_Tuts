import argparse
import sys

def calc(args):
    if args.z == 'add':
        return args.x + args.y

    if args.z == 'mul':
        return args.x * args.y

    if args.z == 'sub':
        return args.x - args.y

    if args.z == 'div':
        return args.x / args.y

    else:
        return "kuch too kad-bad hai daya?!?"

if __name__ == '__main__':
    parsel = argparse.ArgumentParser()
    parsel.add_argument('--x', type=float,
                        default=1.0,
                        help="Enter 1st no..It is for calculation.")

    parsel.add_argument('--y', type=float,
                        default=3.0,
                        help="Enter 2nd no..It is for calculation.")

    parsel.add_argument('--z', type=str,
                        default="add",
                        help="Enter 2nd no..It is for calculation.")

    args = parsel.parse_args()
    sys.stdout.write(str(calc(args)))
