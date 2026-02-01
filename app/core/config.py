"""Application configuration settings."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    app_name: str = "FastAPI Test Server"
    app_version: str = "1.0.0"
    debug: bool = True
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"


settings = Settings()
