#!usr/bin/env python3

import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description="Compares two configuration files "
                    "and shows a difference.")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument('-f', '--format',
                        choices=["stylish", "plain", "json"],
                        default="stylish",
                        help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
