from service.server import app
from service import weather

if __name__ == '__main__':
    current_weather = weather.get_weather('Barnaul,Russia')
    print(current_weather)
    app.run(host='0.0.0.0')
