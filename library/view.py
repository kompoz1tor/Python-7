# Функция "def input_number()" проверяет является ли число целочисленным
# Если не является числом, предлагает еще раз ввести число. Функция выполняется если мы вводим число, иначе выводит "Ошибка"
def input_number() -> int:
    while True:
        try:
            number = int(input('Введите число: '))
            return number
        except:
            print('Ошибка')

# Функция "input_operation()" проверяет является ли значение символом из списка
# Если не является, предлагает еще раз ввести символ операции которую нужно сделать.
def input_operation():
    while True:
        operation = input('Введите операцию: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите коректную операцию: ')

# Функция вывода значения в консоль
def print_to_console(value_text):
    print(value_text)
 
# При выходе из выполнения вычислений программы, выводит сообщение
def log_off():
    print('До свидания!')

def print_division_by_zero():
    print('На ноль делить нельзя: ')
        