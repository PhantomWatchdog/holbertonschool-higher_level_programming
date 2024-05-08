#!/usr/bin/env python3
import sys

if __name__ == "__main__":

    args_nb = len(sys.argv) - 1

    print(f"{args_nb} {'argument' if args_nb == 1 else 'arguments'}:"
          if args_nb != 0 else "0 arguments.")

    for i in range(1, args_nb + 1):
        print("{}: {}".format(i, sys.argv[i]))
