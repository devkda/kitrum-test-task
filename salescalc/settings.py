"""
This module contains the settings management used in different parts of application.
Parameters are also can be loaded from environment variables.
"""

import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    chunk_size: int = Field(1000, env='FILE_CHUNK_SIZE')
    csv_delimiter: str = Field(',', env='CSV_DELIMITER')
    csv_header_part: str = Field('Department', env='CSV_HEADER_PART')


settings = Settings()
