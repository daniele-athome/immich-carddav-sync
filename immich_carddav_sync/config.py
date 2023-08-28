from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    immich_api_url: str
    immich_api_key: str

    carddav_url: str
    carddav_addressbook: str
    carddav_username: str
    carddav_password: str

    class Config:
        env_prefix = "CARDDAV_SYNC_"
        env_file = ".env"
        case_sensitive = False


settings = Settings()
