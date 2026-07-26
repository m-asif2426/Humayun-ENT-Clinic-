import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from config import settings
from models import AppointmentRequest


async def send_appointment_notification(
    appointment: AppointmentRequest, reference_id: str
) -> bool:
    """
    Send appointment notification email to the doctor.

    - If patient has email  → Reply-To is set so doctor can reply directly.
    - If patient has no email → Doctor is informed to call the patient by phone.
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"New Appointment – {appointment.name} | {reference_id}"
    msg["From"] = f"{settings.CLINIC_NAME} System <{settings.SMTP_USER}>"
    msg["To"] = settings.DOCTOR_EMAIL

    # If patient has email, doctor can reply directly
    if appointment.email:
        msg["Reply-To"] = f"{appointment.name} <{appointment.email}>"

    has_email = bool(appointment.email)

    # ─── Contact row ────────────────────────────────────────────────────────
    if has_email:
        contact_html = f"""
        <tr>
          <td style="padding:10px 0;border-bottom:1px solid #e2e8f0;">
            <span style="color:#64748b;font-size:13px;">Email</span><br>
            <a href="mailto:{appointment.email}" style="color:#0e9e8e;font-weight:600;">
              {appointment.email}
            </a><br>
            <span style="font-size:12px;color:#16a34a;"
              >&#x2713; Hit Reply to this email to contact the patient directly.</span>
          </td>
        </tr>"""

        action_box = """
        <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;
                    padding:16px;margin-top:24px;">
          <strong style="color:#15803d;">&#x2709; Reply to contact patient</strong><br>
          <span style="font-size:13px;color:#475569;">
            Simply click <em>Reply</em> in your email client — your response
            will go directly to the patient.
          </span>
        </div>"""
    else:
        contact_html = f"""
        <tr>
          <td style="padding:10px 0;border-bottom:1px solid #e2e8f0;
                     background:#fef9c3;">
            <span style="color:#92400e;font-weight:700;">&#x26A0; No Email Provided</span><br>
            <span style="font-size:13px;color:#78350f;">
              Patient has not shared an email address.
              Please contact them <strong>by phone only</strong>.
            </span>
          </td>
        </tr>"""

        action_box = f"""
        <div style="background:#fef9c3;border:1px solid #fde68a;border-radius:10px;
                    padding:16px;margin-top:24px;">
          <strong style="color:#92400e;">&#x260E; Call the patient to confirm</strong><br>
          <a href="tel:{appointment.phone}"
             style="font-size:16px;font-weight:700;color:#1a5f8a;"
          >{appointment.phone}</a><br>
          <span style="font-size:12px;color:#78350f;">
            No email available — phone call is the only way to reach this patient.
          </span>
        </div>"""

    # ─── Full HTML email ─────────────────────────────────────────────────────
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head><meta charset="UTF-8" /></head>
    <body style="font-family:Arial,sans-serif;background:#f0f6fb;
                 padding:24px;margin:0;">
      <div style="max-width:600px;margin:0 auto;background:#fff;
                  border-radius:16px;overflow:hidden;
                  box-shadow:0 4px 20px rgba(0,0,0,0.10);">

        <!-- Header -->
        <div style="background:linear-gradient(135deg,#1a5f8a,#0e9e8e);
                    padding:32px;text-align:center;color:#fff;">
          <h1 style="margin:0;font-size:22px;font-weight:800;">
            New Appointment Request
          </h1>
          <p style="margin:8px 0 0;opacity:.85;font-size:14px;">
            Wajid ENT Clinic &middot; Kabirwala
          </p>
        </div>

        <!-- Reference bar -->
        <div style="background:#f8fafc;padding:10px 32px;
                    border-bottom:1px solid #e2e8f0;
                    display:flex;justify-content:space-between;">
          <span style="font-size:12px;color:#64748b;">Reference ID</span>
          <span style="font-size:12px;font-weight:700;color:#1a5f8a;">
            #{reference_id}
          </span>
        </div>

        <!-- Body -->
        <div style="padding:32px;">
          <h2 style="font-size:16px;color:#0f172a;margin:0 0 20px;">
            Patient Details
          </h2>
          <table style="width:100%;border-collapse:collapse;">
            <tr>
              <td style="padding:10px 0;border-bottom:1px solid #e2e8f0;">
                <span style="color:#64748b;font-size:13px;">Full Name</span><br>
                <strong style="font-size:15px;">{appointment.name}</strong>
              </td>
            </tr>
            <tr>
              <td style="padding:10px 0;border-bottom:1px solid #e2e8f0;">
                <span style="color:#64748b;font-size:13px;">Phone</span><br>
                <a href="tel:{appointment.phone}"
                   style="font-size:15px;font-weight:600;color:#1a5f8a;">
                  {appointment.phone}
                </a>
              </td>
            </tr>
            {contact_html}
            <tr>
              <td style="padding:10px 0;border-bottom:1px solid #e2e8f0;">
                <span style="color:#64748b;font-size:13px;">Preferred Date</span><br>
                <strong>{appointment.preferred_date.strftime('%A, %d %B %Y')}</strong>
              </td>
            </tr>
            <tr>
              <td style="padding:10px 0;border-bottom:1px solid #e2e8f0;">
                <span style="color:#64748b;font-size:13px;">Preferred Time</span><br>
                <strong>{appointment.preferred_time}</strong>
              </td>
            </tr>
            <tr>
              <td style="padding:12px 0 4px;">
                <span style="color:#64748b;font-size:13px;">Reason for Visit</span><br>
                <div style="background:#f8fafc;border-left:3px solid #1a5f8a;
                            padding:12px;border-radius:0 8px 8px 0;
                            margin-top:8px;color:#475569;
                            font-size:14px;line-height:1.6;">
                  {appointment.reason}
                </div>
              </td>
            </tr>
          </table>

          {action_box}
        </div>

        <!-- Footer -->
        <div style="background:#f8fafc;padding:20px 32px;
                    border-top:1px solid #e2e8f0;text-align:center;">
          <p style="margin:0;font-size:12px;color:#94a3b8;">
            Received: {datetime.now().strftime('%d %b %Y at %I:%M %p')}
          </p>
          <p style="margin:4px 0 0;font-size:12px;color:#94a3b8;">
            {settings.CLINIC_NAME} &middot; {settings.CLINIC_PHONE} &middot; Kabirwala
          </p>
        </div>
      </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(html, "html"))

    try:
        await aiosmtplib.send(
            msg,
            hostname=settings.SMTP_HOST,
            port=settings.SMTP_PORT,
            username=settings.SMTP_USER,
            password=settings.SMTP_PASSWORD,
            start_tls=True,
        )
        return True
    except Exception as exc:
        print(f"[EmailService] Failed to send email: {exc}")
        return False
