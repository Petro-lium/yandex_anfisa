import requests

def what_weather(city):
    """Погода в городе"""
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'


def what_temperature(weather):
    """Определяем температуру"""
    if (weather == '<сетевая ошибка>' or
        weather == '<ошибка на сервере погоды. попробуйте позже>'):
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
            parsed_temperature += char
        try:
            num = int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature

def what_conclusion(parsed_temperature):
    """Система поддержки принятия решения"""
    try:
        # parsed_temperature к типу int
        temperature = int(parsed_temperature)

        # СППР
        if temperature < 18:
            return 'Блин! Очень холодно, лучше чайку!'
        elif 18 <= temperature <= 27:
            return 'Погода класс, в самый раз охладиться!'
        else:
            return 'Очень жарко! Можно еще и лимонад!'
    except ValueError:
        # Если parsed_temperature не удалось преобразовать в число —
        # значит, погодный сервис сломался и надо вернуть фразу "Не могу узнать погоду..."
        return "Не могу узнать погоду..."
