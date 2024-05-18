#!/usr/bin/env python3

"""
Hello for new users to use our clone of AirBnB
"""


def greet_user(name):
    """Greet the user with a hello message."""
    greeting = f"Hello, {name}!"
    return greeting


def main():
    """Main function to run the greet_user function."""
    user_name = input("Enter your name: ")
    print(greet_user(user_name))


if __name__ == "__main__":
    main()
