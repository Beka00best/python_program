import pyowm

c = input('Введите город: ')

API_key = '6f821ce1b7f752205a45ae97186e5051'
owm = pyowm.OWM(API_key)

obs = owm.weather_at_place(c) 
w = obs.get_weather()

temp = w.get_temperature(unit='celsius')['temp']

print('Температура ' + str(temp) + ' С')
