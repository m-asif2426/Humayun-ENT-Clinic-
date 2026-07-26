from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import date
import re


class AppointmentRequest(BaseModel):
    name: str
    phone: str
    preferred_date: date
    preferred_time: str
    reason: str
    email: Optional[EmailStr] = None  # Optional – patient may not have email

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Name cannot be empty")
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters")
        return v

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        cleaned = re.sub(r"[\s\-\(\)]", "", v)
        if not re.match(r"^\+?[0-9]{10,15}$", cleaned):
            raise ValueError("Enter a valid phone number (10-15 digits)")
        return v

    @field_validator("reason")
    @classmethod
    def reason_min_length(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 10:
            raise ValueError("Please describe your reason in at least 10 characters")
        return v


class AppointmentResponse(BaseModel):
    success: bool
    message: str
    reference_id: Optional[str] = None


class ChatRequest(BaseModel):
    message: str

    @field_validator("message")
    @classmethod
    def message_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Message cannot be empty")
        return v.strip()


class ChatResponse(BaseModel):
    reply: str
