from fastapi import APIRouter, BackgroundTasks, HTTPException
from models import AppointmentRequest, AppointmentResponse
from services.email_service import send_appointment_notification
from datetime import datetime
import uuid

router = APIRouter(tags=["Appointment"])


@router.post("/appointment", response_model=AppointmentResponse)
async def book_appointment(
    appointment: AppointmentRequest,
    background_tasks: BackgroundTasks,
):
    """
    Accept an appointment request.
    - Sends an email notification to the doctor in the background.
    - If the patient provided an email, Reply-To is set so the doctor can
      respond directly by email.
    - If not, the email instructs the doctor to call the patient by phone.
    """
    reference_id = (
        f"WEC-{datetime.now().strftime('%Y%m%d')}-"
        f"{str(uuid.uuid4())[:6].upper()}"
    )

    background_tasks.add_task(
        send_appointment_notification, appointment, reference_id
    )

    msg = (
        f"Appointment request received! Reference: {reference_id}. "
        "We will contact you shortly to confirm your slot."
    )
    return AppointmentResponse(success=True, message=msg, reference_id=reference_id)
