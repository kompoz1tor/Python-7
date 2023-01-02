# Для калькулятора требуется: первое число, второе число, операция которая выполняется и результат
first_number = 0
second_number = 0
operation = ''
result = 0


# "Геттеры" - получение значений переменных для вывода
def get_first():
    global first_number
    return first_number
    
def get_second():
    global second_number
    return second_number

def get_operation():
    global operation
    return operation

def get_result():
    global result
    return result

# "Сеттеры" - присваивание значений переменных полученных с помощью функций input в других файлах
def set_first(value):
    global first_number
    first_number = value


def set_second(value):
    global second_number
    second_number = value

def set_operation(oper):
    global operation
    operation = oper

# Функция сложения
def addition():
    global first_number
    global second_number
    global result
    result = first_number + second_number

# Функция вычитания
def difference():
    global first_number
    global second_number
    global result
    result = first_number - second_number

# Функция умножения
def multiplication():
    global first_number
    global second_number
    global result
    result = first_number * second_number

# Функция деления
def division():
    global first_number
    global second_number
    global result
        # print('На ноль делить нельзя, введите другое число: ')
    result = first_number / second_number
    if result == int(result):
        result = int(result)
    return False