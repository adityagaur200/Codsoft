import requests

API_URL = 'https://wttr.in/'

def get_weather(city):
    response = requests.get(f'{API_URL}{city}?format=4')
    if response.status_code == 200:
        data = response.text.strip()
        return data.split('\n')
    else:
        print('Failed to retrieve weather data.')
        return None

def main():
    print('Welcome to the Weather Forecast App!')
    user_input = input('Enter a city name: ')

    weather_info = get_weather(user_input)

    if weather_info:
        print('\nWeather Information for', user_input + ':')
        print('Weather:', weather_info[0])
        
    else:
        print('No weather information available.')

if __name__ == '__main__':
    main()
