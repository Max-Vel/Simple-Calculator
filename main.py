print("КАЛЬКУЛЯТОР".center(30))


def func():
    pass


def get_even_numbers(a, b):
    even_numbers = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def remainder_of_division(a, b):
    if a < b:
        return f"Залишок від ділення {a} на {b} складає {a}"
    else:
        return f"Залишок від ділення {a} на {b} складає {a%b}"

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
    elif user_choice == '10':
        print(get_even_numbers(a, b))
    elif user_choice == '12':
        print(remainder_of_division(a, b))