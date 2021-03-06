def calculate(num1, num2, operator):
    # проверка деления на ноль
    if (operator == '/') and (num2 == 0):
        return float('inf')

    operators = {
                 '+': num1+num2,
                 '-': num1-num2,
                 '*': num1*num2,
                 '/': num1/num2
                 }

    return operators[operator]


def check_num(num):
    try:
        _ = float(num)
    except ValueError:
        return False
    return True


def main():
    print('Welcome to this simple calculator.')
    print('\nType "exit" to end programm\n')
    while True:
        # число 1
        num1 = input('Number 1: ')
        if num1 == 'exit':  # не придумал ничего лучше
            break
        elif not check_num(num1):
            print('Please input number')
            continue

        # оператор
        operator = input('Operator (+-*/): ')
        if operator == 'exit':
            break
        elif operator not in ['+', '-', '*', '/']:
            print('Only +-*/ are supported')
            continue

        # число 2
        num2 = input('Number 2: ')
        if num2 == 'exit':
            break
        elif not check_num(num2):
            print('Please input number')
            continue

        # результат
        result = calculate(float(num1), float(num2), operator)
        print(f'{num1} {operator} {num2} = ', result)
        print('\n')


if __name__ == '__main__':
    main()
