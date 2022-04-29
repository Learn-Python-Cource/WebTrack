import json
import os

from pydantic import BaseModel

basedir = os.path.abspath(os.path.dirname(__file__))
db_url = 'sqlite:///{0}'.format(
    os.path.join(basedir, '..', 'webapp.db'),
)


class AppConfig(BaseModel):
    weather_url: str
    weather_city: list[float]
    weather_api_key: str
    title: str
    db_url: str


def load_from_env():
    return AppConfig(
        weather_url=os.environ['WEATHER_URL'],
        weather_city=json.loads(os.environ['WEATHER_CITY']),
        weather_api_key=os.environ['WEATHER_API_KEY'],
        title=os.environ['TITLE'],
        db_url=db_url,
    )


app_config = load_from_env()
