import pyowm

print('OpenWeatherMap by mioe')
print('ubuntu-16.04-amd64')

own = pyowm.OWM('f813aec25d8b0d1b7b6c3c4ff25658d0')
observation = own.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()

print('---')

print(own)
print(observation)
print(weather)
print(location)

print('---')

print('Страна: ' + location.get_country())
print('Город: ' + location.get_name())
print('Долгота: ' + str(location.get_lon()))
print('Широта: ' + str(location.get_lat()))
print('Облачность: ' + str(weather.get_clouds()))
print('Статус: ' + str(weather.get_detailed_status()))
print('Давление: ' + str(weather.get_pressure()))
print('Дождь: ' + str(weather.get_rain()))
print('Снег: ' + str(weather.get_snow()))
print('Время: ' + str(weather.get_reference_time('iso')))
print('Статус: ' + str(weather.get_status()))
print('Восход: ' + str(weather.get_sunrise_time('iso')))
print('Закат: ' + str(weather.get_sunset_time('iso')))
print('Температура: ' + str(weather.get_temperature('celsius')))
print('Видимость: ' + str(weather.get_visibility_distance()))
print('Изображения: ' + weather.get_weather_icon_name())
print('Ветер: ' + str(weather.get_wind()))

print('---')
