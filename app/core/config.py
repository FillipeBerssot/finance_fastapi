from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Finance API"

    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="forbid",
    )


settings = Settings()
