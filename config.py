from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # These values come from .env (or matching environment variables).
    ollama_url: str
    model_name: str
    db_url: str  # Reserved for later; we do not connect to a database yet.

    # Find .env
    # beside this file, regardless of the terminal's current folder.
    model_config = SettingsConfigDict(
        env_file=Path(__file__).with_name(".env"),
        env_file_encoding="utf-8",
    )


# Read the settings once when the application starts.
settings = Settings()
