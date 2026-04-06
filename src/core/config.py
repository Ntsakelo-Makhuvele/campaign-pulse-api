from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER : str
    DB_PASS : str
    DB_NAME : str
    DB_HOST : str
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )



import os

class Config:
    def __init__(self):
        self.settings = Settings()
        self.INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

    @property
    def DATABASE_URL(self):
        user = self.settings.DB_USER
        password = self.settings.DB_PASS
        name = self.settings.DB_NAME
        host = self.settings.DB_HOST

        if self.INSTANCE_CONNECTION_NAME:
            # Cloud Run / Unix Socket path
            return (
                f"postgresql+pg8000://{user}:{password}@/{name}"
                f"?unix_sock=/cloudsql/{self.INSTANCE_CONNECTION_NAME}/.s.PGSQL.5432"
            )
        
        # Local / TCP path
        return f"postgresql+pg8000://{user}:{password}@{host}/{name}"