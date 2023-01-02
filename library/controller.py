import view
import model

# Взяли 1 число потом 2 число, потом принимаем какую операцию совершить, далее запускаем операцию "solution" в зависимости от введённого символа операции, и выводим result на экран

def input_first():
    # из view взяли функцию которая принимает значение с клавиатуры
    # и присвоили полученное значение number переменной first_number с помощью функции из "model"
    number = view.input_number()
    model.set_first(number)


#Если при делении второе число ноль - выводим ошибку и вводим число заного
def input_second():
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.print_division_by_zero()
        else:
            model.set_second(number)
            break

# вводим операцию которую нужно сделать с данными
def input_operation():
    oper = view.input_operation()
    model.set_operation(oper)

def solution():
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper == '/':
        model.division()
   
    #result = model.get_result()
    result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())

def start():
    input_first() 
    while True:
        input_operation()
        if model.get_operation() == '=':
            view.log_off()
            break
        input_second()
        solution()
            
    

