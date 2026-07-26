from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # SMTP / Email
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "your-email@gmail.com"
    SMTP_PASSWORD: str = "your-app-password"

    # Doctor notification destination
    DOCTOR_EMAIL: str = "doctor@example.com"
    DOCTOR_NAME: str = "Dr. Rana Humayun Babar"
    CLINIC_NAME: str = "Wajid ENT Clinic"
    CLINIC_PHONE: str = "0309-8742674"

    # App
    FRONTEND_URL: str = "http://localhost:8000"
    DEBUG: bool = False

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
