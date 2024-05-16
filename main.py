def division(a, b):
    try:
        answer = a / b
    except ZeroDivisionError:
        print('Ділити на нуль не можна')
    else:
        print(f'Результат ділення: {round(answer, 2)}')


def square_of_sum(a, b):
    print((a + b) ** 2)


def paired_num(a, b):
    nums = [numb for numb in range(a, b+1) if numb % 2 == 0]
    print(f'Парні числа: {nums}')

def odd_range(a, b):
    print([i for i in range(a, b+1) if i % 2 != 0])

def sum_of_squares(a, b):
    res = a ** 2 + b ** 2
    print(f'Сума квадратів чисел {a} та {b} дорівнює {res}.')


print(' КАЛЬКУЛЯТОР '.center(40, '*'))

while True:
    try:
        a, b = map(int, input('Введіть два числа через пропуск: ').split(' '))
    except:
        print('Не коректне введення.')
        continue
    print(f'''
Оберіть дію для чисел {a} та {b}:
  0. Вихід
  1. Додавання:    {a} + {b}
  2. Віднімання:   {a} - {b}
  3. Множення:     {a} * {b}
  4. Ділення:      {a} : {b}
  5. Піднесення числа {a} до степеня {b}
  6. Сума квадратів чисел {a} та {b}
  7. Різниця квадратів чисел {a} та {b}
  8. Квадрат суми чисел {a} та {b}
  9. Квадрат ріниці чисел {a} та {b}
  10. Усі парні числа між числами {a} та {b}
  11. Усі непарні числа між числами {a} та {b}
    ''')
    user_choice = input('>>> Ваш вибір: ')

    if user_choice == '0':
        break
    elif user_choice == '4':
        division(a, b)
        choice = input('Бажаєте продовжити? (y/n) ')
        if choice == 'y':
            continue
        else:
            print('До побачення')
            break
    elif user_choice == '8':
        square_of_sum(a, b)
        choice = input('Бажаєте продовжити? (y/n) ')
        if choice == 'y':
            continue
        else:
            print('До побачення')
            break
    elif user_choice == '10':
        paired_num(a, b)
        choice = input('Бажаєте продовжити? (y/n) ')
        if choice == 'y':
            continue
        else:
            print('До побачення')
            break
    elif user_choice == '11':
        odd_range(a, b)
        choice = input('Бажаєте продовжити? (y/n) ')
        if choice == 'y':
            continue
        else:
            print('До побачення')
            break
    elif user_choice == '6':
        sum_of_squares(a, b)
        choice = input('Бажаєте продовжити? (y/n)')
        if choice == 'y':
            continue
        else:
            print('До побачення')
            break