# def string_input_check():
# if not(data['people'] and data['people'].strip()): #исключение ввода пустой строки и пробелов
# print("Не спи!!!","\N{slightly smiling face}", "Добавь, чем сегодня займешься!")
# elif data['people'].isnumeric(): # содержит ли строка только числа
# print('Попробуйте внести дело еще раз!','\U0001F612')
# else:
# print("Дело добавлено в список!",'\U0001F607')


mes = input()
if mes.isnumeric():
    print('Не вводите только числа')
else:
    print(mes)
