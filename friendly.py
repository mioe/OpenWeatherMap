# Подключаем библиотеку pyown
import pyowm

# Выводим на экран название программы и автора
print('OpenWeatherMap by mioe')
print('ubuntu-16.04-amd64')

# Инициализируем библиотеку API ключом
own = pyowm.OWM('f813aec25d8b0d1b7b6c3c4ff25658d0')

# Получаем данные из нужного города
observation = own.weather_at_place('Rostov-on-Don,ru')

# Получаем погодные данные
weather = observation.get_weather()

# Получаем данные местоположения
location = observation.get_location()

# Создаем словарь для перевода названия городов
translate = {'Rostov-na-Donu': 'Ростов-на-Дону'}

# Enter
print('---')

# Создадим функцию которая определяет облачность
def WhatIsCloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'ясная'

    if 10 < weather.get_clouds() <= 30:
        return 'немного облачная'

    if 30 < weather.get_clouds() <= 70:
        return 'пасмурная'

    if 70 < weather.get_clouds() <= 100:
        return 'мрачная'


# Выводим на экран данные в дружелюбном формате
print('Погода в городе ' + translate[location.get_name()] + ' ' + WhatIsCloudness() + ', температура ' + str(weather.get_temperature('celsius')['temp']) + ' градусов цельсия ' + 'скорость ветра ' + str(weather.get_wind()['speed']) + ' м/с.')