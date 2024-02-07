from pydantic_settings import BaseSettings

class Settings (BaseSettings) :
    api_key : str # = your api_key
    patht : str # = your path
    class Config :
        env_file = ".env"

setting = Settings()

