import os
import dotenv


# Load environment variables from .env file
dotenv.load_dotenv('.env')


def get_var(name: str, cast: type):
    if value := os.environ.get(name):
        return cast(value)
    
    raise NameError(f"Environment variable '{name}' not set!")


class Config:
    """Configuration class for the application."""
    
    APP_HOST: str = get_var('APP_HOST', str)
    APP_PORT: int = get_var('APP_PORT', int)
