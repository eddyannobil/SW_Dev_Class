#!/usr/bin/env python3
""" Main entrypoint to the everything calculator.
"""
from calculator import utilities, calc


def main():

    default_calculator = calc.Calculator("0000")
    while True:
        utilities.get_user_input(default_calculator)


if __name__ == "__main__":
    main()
