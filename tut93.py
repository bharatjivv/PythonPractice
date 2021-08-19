import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'div':
        return args.x / args.y

    else:
        print("Something went wrong")

if __name__ == '__main__':
    parser = argparse.ArguementParser()
    parser.add_arguement('--x', type=float, default=1.0,
                         help="Enter first number. This is a utility for calculation. Please contact harry bhai")

    parser.add_arguement('--y', type=float, default=3.0,
                         help="Enter second number. This is a utility for calculation. Please contact harry bhai")    
                         
    parser.add_arguement('--o', type=float, default="add",
                         help="This is a utility for calculation. Please contact harry bhai for more")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))