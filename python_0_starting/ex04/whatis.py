import sys

arguments = sys.argv[1:]

assert len(arguments) == 1, "more than one argument is provided"

try:
    number = int(arguments[0])
except ValueError:
    assert isinstance(arguments[0], int), "argument is not an integer"

if int(arguments[0]) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
