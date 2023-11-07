import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    """DB configuration environment variables.

    Args:
        BaseSettings (_type_): Base setting checker.
    """
    _db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')
    secret_key: str = os.getenv('SECRET_KEY')
    token_expire: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    forecast_api_key: str = os.getenv('FORECAST_API_KEY')


    @property
    def db_name(self):
        """Getter function.

        Returns:
            str: Database name.
        """
        if os.getenv('RUN_ENV') == 'test':
            return 'test_' + self._db_name
        return self._db_name
