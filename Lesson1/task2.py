user_answer = int(input('Введите время в секундах (берите больше, не стесняйтесь):'))
hour = user_answer//3600
minutes = (user_answer % 3600)//60
sec = (user_answer % 3600) % 60
if hour < 10:
    hour = '0'+ str(hour)
if minutes < 10:
    minutes = '0'+ str(minutes)
if sec < 10:
    sec = '0'+ str(sec)
print(f'{hour}:{minutes}:{sec}')