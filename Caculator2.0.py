# create a menu function
def menu():
    print("c: calculate numbers\n"
          "q: quit"
          )


# create the calculate function
def calculate():
    x = float(input("please input a number :"))
    y = float(input("please input another number: "))
    operator = input("please input your operator: \n"
                     "+ \n"
                     "_ \n"
                     "* \n"
                     "/ \n"
                     "% \n")
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    elif operator == "*":
        print(x * y)
    elif operator == "/":
        print(x / y)
    else:
        print(x % y)


if __name__ == '__main__':
    menu()
    userSelect = input("please input your select:")
    while userSelect != "q":
        calculate()
        menu()
        userSelect = input("please input your select:")
    print("quit successfully")
