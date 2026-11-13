print("="*8+"ИГРОВОЙ КАЛЬКУЛЯТОР"+"="*8)
print("")

equation = []
operator_dict = {
    "сумма": "+",
    "плюс": "+",
    "+": "+",
    "остаток": "-",
    "минус": "-",
    "-": "-",
    "произведение": "*",
    "умножить": "*",
    "*": "*",
    "деление": "/",
    "разделить": "/",
    "/": "/",
    "степень": "**",
    "^": "**"
}
def int_check(num):
    try: return(int(num))
    except ValueError:
        return(False)

while True:
    user_num_one = input("введите первое число: ")
    if int_check(user_num_one) != False or int_check(user_num_one) == 0:
        equation.append(user_num_one)
        break
    else:
        print("это не число!")

while True:
    operator = input("введите нужный оператор: ").lower()
    if operator in operator_dict:
        equation.append(operator_dict[operator])
        break
    else:
        print("такого оператора нет!")

while True:
    user_num_two = input("введите второе число: ")
    if int_check(user_num_two) != False or int_check(user_num_two) == 0:
        if "/" in equation and int(user_num_two) == 0:
            print("на 0 делить нельзя!")
            equation.append(False)
            break
        else:
            equation.append(user_num_two)
            break
    
    print("это не число!")

if False in equation:
    print("вы ввели некорректное выражение. перезапустите программу.")
else:
    print(f"результат: {eval(''.join(equation))}")