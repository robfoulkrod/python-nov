

try:
    number = input('gimme a number ')
    number = int(number)
    base_number = 100
    answer = base_number / number
except ValueError as ex:
    print("You must enter a non zero whole number", ex)
except ZeroDivisionError as ex:
    print("Don't use zero, it breaks stuff", ex)
except Exception as ex:  # when there IS an error
    print("something bad happened")
else:  # when there is no error
    print(f'your answer is {answer}')
finally:
    print("I think we are done here")


def can_int(potential_int):
    try:
        value = int(potential_int)
    except:
        return (False, 0)
    else:
        return (True, value)
