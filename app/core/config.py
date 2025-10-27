from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./mediahub.db"
    JWT_SECRET: str = "change-me"
    JWT_ALG: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120
    APP_ENV: str = "dev"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
