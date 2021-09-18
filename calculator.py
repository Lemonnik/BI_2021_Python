def calculate(num1, num2, operator):
    return eval(num1 + operator + num2)


def check_num(num):
    try:
        float(num)
    except:
        return False
    return True


def main():
    while True:
        # число 1
        num1 = input()
        if num1 == 'exit':  # не придумал ничего лучше
            break
        elif not check_num(num1):
            print('Please input number')
            continue

        # оператор
        operator = input()
        if operator == 'exit':
            break
        elif operator not in ['+', '-', '*', '/']:
            print('Only +-*/ are supported')
            continue

        # число 2
        num2 = input()
        if num2 == 'exit':
            break
        elif not check_num(num2):
            print('Please input number')
            continue

        # результат
        result = calculate(num1, num2, operator)
        print(result)



if __name__=='__main__':
    main()