"""
This module contains the settings management used in different parts of application.
Parameters are also can be loaded from environment variables.
"""


from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    chunk_size: int = Field(1000, env='FILE_CHUNK_SIZE')
    csv_delimiter: str = Field(',', env='CSV_DELIMITER')


settings = Settings()
