from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str

    database_url: str

    redis_url: str

    environment: str

    GEMINI_API_KEY: str

    JWT_SECRET_KEY: str

    JWT_ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    
    class Config:
        env_file = ".env"


settings = Settings()