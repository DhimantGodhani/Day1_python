def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(str(2) + 'Hello')  # Press Ctrl+F8 to toggle the breakpoint.
    x = 100
    print(type(x))
    x = 'Dhimant'
    print(type(x))
    s = "Hi, {}"
    print(s.format(x))
    s = "Hi, {} and {}"
    print(s.format(x, 100))
    s = "Hi, {0} and {1}"
    print(s.format(x, 100))
    s = "Hi, {1} and {0}"
    print(s.format(x, 100))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
