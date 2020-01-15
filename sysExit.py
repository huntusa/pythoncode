import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit' or 'Exit':
        sys.exit()
    print('You typed ' + response + '.')
