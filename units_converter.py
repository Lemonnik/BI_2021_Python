def unit_conv(unit_from, unit_to, value):
    distance_conv = {
                    'mm': {
                            'km': 1e-6,
                            'inch': 0.0393701,
                            'mile': 6.2137e-7
                            },
                    'km': {
                            'mm': 1000000,
                            'inch': 39370.1,
                            'mile': 0.621371
                            },
                    'inch': {
                              'mm': 25.4,
                              'km': 2.54e-5,
                              'mile': 1.5783e-5
                              },
                    'mile': {
                              'mm': 1.609e+6,
                              'km': 1.60934,
                              'inch': 63360
                              }
                    }
    pressure_conv = {
                    'Pa': {
                            'bar': 1e-5,
                            'atm': 9.8692e-6
                            },
                    'bar': {
                            'Pa': 100000,
                            'atm': 0.986923
                            },
                    'atm': {
                            'Pa': 101325,
                            'bar': 1.01325
                            }
                    }

    if unit_from in pressure_conv and unit_to in pressure_conv:
        result = value*pressure_conv[unit_from][unit_to]
    elif unit_from in distance_conv and unit_to in distance_conv:
        result = value*distance_conv[unit_from][unit_to]
    else:
        result = 'Error: cannot convert this units'

    return result


def check_num(num):
    try:
        float(num)
    except ValueError:
        return False
    return True


def main():
    welcome_text = '''
    Welcome to simple units converter!
    You can convert...
    distance units: inch<->mm<->km<->mile
    pressure units: Pa<->bar<->atm
    etc...
    '''
    print(welcome_text)

    allowed_pressure = ['Pa', 'bar', 'atm', 'mm_Hg']
    allowed_distance = ['mm', 'km', 'inch', 'mile']
    allowed = allowed_distance + allowed_pressure
    exit_phrases = ['exit', 'break', 'finish', 'i\'m done']

    while True:
        # convert FROM
        unit_from = input('Input unit you would like to convert FROM: ')
        if unit_from in exit_phrases:
            break
        elif unit_from not in allowed:
            print('Please input correct unit_name')
            continue

        # convert TO
        unit_to = input('Input unit you would like to convert TO: ')
        if unit_to in exit_phrases:
            break
        elif unit_to not in allowed:
            print('Please input correct unit_name')
            continue

        # VALUE
        value = input('Input value to convert: ')
        if not check_num(value):
            print('Please input number')
            continue
        else:
            value = float(value)

        # Converter
        result = unit_conv(unit_from, unit_to, value)
        print(f'{value} {unit_from} = {result} {unit_to}')


if __name__ == '__main__':
    main()
