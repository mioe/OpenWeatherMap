# Подключаем библиотеку pyown
import pyowm
import datetime

# Для даты
# import datetime
# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# Выводим на экран название программы и автора
print('OpenWeatherMap by mioe')
print('ubuntu-16.04-amd64')

# Инициализируем библиотеку API ключом
own = pyowm.OWM('f813aec25d8b0d1b7b6c3c4ff25658d0')

# Получаем данные из нужного города
observation = own.weather_at_place('Rostov-on-Don,ru')

# Получаем погодные данные
weather = observation.get_weather()
print(weather)

# Получаем данные местоположения
location = observation.get_location()

# Создаем словарь для перевода названия городов
translate = {'Rostov-na-Donu': 'Ростов-на-Дону', 'RU': 'Россия'}
translateStatus = {'Rain':'Дождь'}

# Enter
print('---')

# Создадим функцию которая определяет облачность
def WhatIsCloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'ниче так' #'ясная'

    if 10 < weather.get_clouds() <= 30:
        return 'неплохо' #'немного облачная'

    if 30 < weather.get_clouds() <= 70:
        return 'плохо' #'пасмурная'

    if 70 < weather.get_clouds() <= 100:
        return 'какашка' #'мрачная'

def WhatIsTemperature():     #
    if -30 <= weather.get_temperature('celsius')['temp'] <= -10:
        return 'холодный ад'

    if -10 < weather.get_temperature('celsius')['temp'] <= 0:
        return 'холодрыжество'

    if 0 < weather.get_temperature('celsius')['temp'] <= 5:
        return 'очень холодно'

    if 5 < weather.get_temperature('celsius')['temp'] <= 10:
        return 'лучше не вылезать с кроватки))0)'

    if 10 < weather.get_temperature('celsius')['temp'] <= 20:
        return 'можно погулять'

    if 20 < weather.get_temperature('celsius')['temp'] <= 30:
        return 'ну немного жарковато'

    if 30 < weather.get_temperature('celsius')['temp'] <= 40:
        return 'ад'

    if 40 < weather.get_temperature('celsius')['temp'] <= 60:
        return 'как ты ещё жив'

def WhatIsWind():
    if  0 <= weather.get_wind()['deg'] < 45:
        return 'северный ветер'

    if 45 <= weather.get_wind()['deg'] < 90:
        return 'северо-восточный ветер'

    if 90 <= weather.get_wind()['deg'] < 135:
        return 'восточный ветер'

    if 135 <= weather.get_wind()['deg'] < 180:
        return 'юго-восточный ветер'

    if 180 <= weather.get_wind()['deg'] < 225:
        return 'южный ветер'

    if 225 <= weather.get_wind()['deg'] < 270:
        return 'юго-западный ветер'

    if 270 <= weather.get_wind()['deg'] < 325:
        return 'западный ветер'

    if 325 <= weather.get_wind()['deg'] <= 360:
        return 'северо-западный ветер'


# Выводим на экран данные в дружелюбном формате
print('Дружелюбный прогноз погоды от Миши:')
print('Наше местоположение: ' + translate[location.get_name()] + ' (' + translate[location.get_country()] + '). Наши координаты: ' + str(location.get_lat()) + ' ш. ' + str(location.get_lon()) + ' д.')
print('Итак, погода на ' + datetime.datetime.now().strftime("%Y-%m-%d") + ': на улице ' + WhatIsCloudness() + ' ' + str(weather.get_clouds()) + '%, ' + WhatIsTemperature() + ' ' + str(weather.get_temperature('celsius')['temp']) + ' C.')
print('Дополнительная информация: ' + WhatIsWind() + ' со скоростью ' + str(weather.get_wind()['speed']) + ' м/c, давление ' + str(weather.get_pressure()['press']) + ' мм.')
print('Минимальная температура: ' + str(weather.get_temperature('celsius')['temp_min']) + '     -     ' + 'Максимальная температура: ' + str(weather.get_temperature('celsius')['temp_max']))
print('Статус: ' + translateStatus[(weather.get_status())] + '         ' + 'Дождь: ' +  str(weather.get_rain()) + '         ' + 'Снег: ' + str(weather.get_snow()))