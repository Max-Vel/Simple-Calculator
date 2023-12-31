print('*' * 30)
print("КАЛЬКУЛЯТОР".center(30))
print('*' * 30)

def sum_of_squares(a, b):
    return a**2+b**2


def get_math_func(a, b):
    if a > b:
        ran = list(range(b + 1, a))
    elif a < b:
        ran = list(range(a + 1, b))
    else:
        print(f'\n{a} = {b}')
        return

    num = [str(i) for i in ran if i % 2 == 0]
    new_num = ",".join(num)
    if '0' in new_num:
        new_num = new_num.replace(',0', '')
    print(f'\nThe range is: {ran}.')
    print(f'Answer is: {new_num}.')


def get_add(a, b):
    return f' Додавання   {a} + {b} дає результат  {a + b}'


def get_retail_squares(a, b):
    if a < b:
        n = b**2 - a**2
        return f'Різниця квадратів чисел {b} та {a} складає {n}'
    else:
        n = a ** 2 - b ** 2
        return f'Різниця квадратів чисел {a} та {b} складає {n}'


def get_squares_of_sum(a, b):
    squares_of_sum = (a + b) ** 2
    return f'Квадрат суми чисел {a} та {b} становить {squares_of_sum}.'


def get_even_numbers(a, b):
    even_numbers = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


def get_remainder_of_division(a, b):
    try:
        a % b
    except ZeroDivisionError:
        return "Не можна ділити на ноль, навіть при діленні із залишком!!!\n"
    else:
        if a < b:
            return f"Залишок від ділення {a} на {b} складає {a}\n"
        else:
            return f"Залишок від ділення {a} на {b} складає {a%b}\n"


def get_exponentiate(a, b):
    c = a ** b
    return f'Піднесення числа {a} до степеня числа {b} дорівнює {c}.'


while True:
    try:
        a, b = tuple(map(int, input("Введіть два числа через пропуск: ").split(' ')))
    except:
        print('Некоректне введення.')
        continue


    print(f"""
  Оберіть дію для чисел {a} та {b}:
      0. Вихід
      1. Додавання   {a} + {b}
      2. Віднімання  {a} - {b}
      3. Множення    {a} * {b}
      4. Ділення     {a} : {b}
      5. Піднесення числа {a} до степеня числа {b}
      6. Сума квадратів чисел {a} та {b}
      7. Різниця квадратів чисел {a} та {b}
      8. Квадрат суми чисел {a} та {b}
      9. Квадрат різниці чисел {a} та {b}
      10. Усі парні числа між числами {a} та {b}
      11. Усі непарні числа між числами {a} та {b}
      12. Залишок від ділення числа {a} на число {b}
    """)

    user_choice = input('Ваш вибір: ')

    if user_choice == '0':
        break
    elif user_choice == '1':
        print(get_add(a, b))
    elif user_choice == '5':
        print(get_exponentiate(a, b))
    elif user_choice == '6':
        print(sum_of_squares(a, b))
    elif user_choice == '7':
        print(get_retail_squares(a, b))
    elif user_choice == '8':
        print(get_squares_of_sum(a, b))
    elif user_choice == '10':
        print(get_even_numbers(a, b))
    elif user_choice == '11':
        get_math_func(a, b)
    elif user_choice == '12':
        print(get_remainder_of_division(a, b))

