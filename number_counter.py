"""
Number Counter Program

This program counts numbers in a given range.
To use it, run 'python number_counter.py'

"""
def main():
    """
    Main function
    """
    print('-----------------------------------------')
    print('Welcome to the Number Counter!')
    print()

    while True:
        try:
            start_value = int(input('Enter a start value (Default: 0): ') or '0')
            if start_value >= 0:
                break
            if start_value < 0:
                print('Negative values are not accepted. Try again.')
        except ValueError:
            print('Opps, you did not enter a numeric value. Try again.')

    while True:
        try:
            end_value = int(input('Enter an end value: '))
            if end_value > 1:
                break
            if end_value < 0:
                print('Negative values are not accepted. Try again.')
            if end_value == 0:
                print('End value cannot be zero. Try again.')
            if end_value == 1:
                print('End value should be greater than one. Try again.')
        except ValueError:
            print('Opps, you did not enter a numeric value. Try again.')

    while True:
        try:
            step_value = int(input('Enter a step value (Default: 1): ') or '1')
            if step_value >= 1:
                break
            if step_value < 0:
                print('Negative values are not accepted. Try again.')
            if step_value == 0:
                print('Step value cannot be zero. Try again.')
        except ValueError:
            print('Opps, you did not enter a numeric value. Try again.')

    print('The numbers are: ', end= '')
    for numbers in range(start_value, end_value, step_value):
        print(numbers, end=' ')

if __name__ == '__main__':
    main()
