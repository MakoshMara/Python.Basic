class MyException(Exception):
    def __init__(self,text):
        self.text = text


try:
    user_data = input('что на что хотите разделить(в формате д/д)?:')
    if int(user_data.split('/')[1]) == 0:
        raise MyException('Делить на ноль нельзя!')
    delimoe = int(user_data.split('/')[0])
except ValueError:
    print('Вы ввели не числа')
except MyException as err:
    print(err)