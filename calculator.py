def calculate(num1, num2, operator):
    try:
        _ = float(num1)
        _ = float(num2)
    except:
        return 'Input must be int/float'

    if operator not in ['+', '-', '*', '/']:
        return 'Only +-*/ are supported'

    # если с инпутом всё ок
    return eval(num1 + operator + num2)


def main():
    while True:
        num1 = input()
        if num1 == 'exit':  # не придумал ничего лучше
            break

        operator = input()
        if operator == 'exit':
            break

        num2 = input()
        if num2 == 'exit':
            break

        print(calculate(num1, num2, operator))



if __name__=='__main__':
    main()


# print(type(float('55.5')))