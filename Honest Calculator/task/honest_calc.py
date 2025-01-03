# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
memory = 0
operations = ["+", "-", "*", "/"]


def is_one_digit(v):
    output = (v > -10) and (v < 10) and v.is_integer()
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 =="+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


while True:
    print(msg_0)
    calc = input("").strip()
    x, operation, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
        result = 0
        if operation in operations:
            check(x, y, operation)
            if operation == "+":
                result = x + y
            elif operation == "-":
                result = x - y
            elif operation == "*":
                result = x * y
            elif operation == "/":
                if y != 0:
                    result = x / y
                else:
                    print(msg_3)
                    continue
            print(result)
            print(msg_4)
            check_y_n = input()
            if check_y_n == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        check_y_n = input()
                        if check_y_n == "y":
                            if msg_index < 12:
                                msg_index += 1
                            else:
                                memory = result
                                break
                        elif check_y_n =="n":
                            break
                        else:
                            print(msg_[msg_index])
                            check_y_n = input()
                else:
                    memory = result
            print(msg_5)
            check_y_n = input()
            if check_y_n == "y":
                continue
            elif check_y_n == "n":
                break
            else:
                print(msg_5)
                check_y_n = input()
        else:
            print(msg_2)
    except ValueError:
        print(msg_1)

