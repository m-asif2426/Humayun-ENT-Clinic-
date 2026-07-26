# Humayun ENT Clinic — Full Stack Project

## Project Structure

```
wajid-ent-clinic/
├── frontend/               # Static website (HTML + CSS + JS)
│   ├── index.html          # Main website (all 5 pages)
│   └── assets/             # Images and media`
│       ├── doctor_avatar_*.png
│       ├── hero_background_*.png
│       └── clinic_logo_*.png
│
├── backend/                # FastAPI REST API
│   ├── main.py             # App entry point + static file serving
│   ├── config.py           # Settings loaded from .env
│   ├── models.py           # Pydantic request/response models
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example        # Environment variable template
│   ├── .env                # Your actual config (DO NOT COMMIT)
│   ├── routes/
│   │   ├── appointment.py  # POST /appointment
│   │   └── chat.py         # POST /chat
│   └── services/
│       ├── email_service.py  # Email notifications to doctor
│       └── chat_service.py   # FAQ-based chatbot logic
│
├── README.md
└── .gitignore
```

---

## Quick Start

### Step 1 — Install Python dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Step 2 — Configure environment

```bash
cp .env.example .env
```

Then edit `.env` and fill in your Gmail credentials and doctor email.

### Step 3 — Run the server

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Step 4 — Open in browser

```
http://localhost:8000
```

The FastAPI server serves the frontend at `/` and the API at `/appointment` and `/chat`.

---

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/appointment` | Submit appointment request |
| POST | `/chat` | Send chat message to FAQ bot |
| GET | `/health` | Health check |
| GET | `/api/docs` | Swagger UI |
| GET | `/api/redoc` | ReDoc documentation |

---

## Email System — How It Works

### When patient provides email ✅
1. Doctor receives email notification with all patient details
2. Email has **Reply-To** set to patient's email
3. Doctor clicks **Reply** → email goes directly to patient
4. Patient sees doctor's reply in their inbox

### When patient has NO email ⚠️
1. Doctor still receives email notification
2. Email clearly shows: **"No email — call patient at: [phone]"**
3. Doctor must **call the patient** by phone to confirm
4. No email exchange is possible — phone is the only channel

> **Summary**: Email is optional for patients. Phone number is always mandatory.
> The system always notifies the doctor. The response channel depends on what the patient provided.

---

## Email Setup (Gmail)

1. Enable **2-Factor Authentication** on your Gmail: [myaccount.google.com/security](https://myaccount.google.com/security)
2. Create an **App Password**: [myaccount.google.com/apppasswords](https://myaccount.googcle.com/apppasswords)
   - Select: Mail → Windows Computer
   - Copy the 16-character password
3. Add to `.env`:
   ```
   SMTP_USER=your-clinic-email@gmail.com
   SMTP_PASSWORD=xxxx-xxxx-xxxx-xxxx
   DOCTOR_EMAIL=dr.humayun@youremail.com
   ```

---

## Upgrading the Chatbot to AI

The chatbot (`services/chat_service.py`) currently uses keyword matching.
To upgrade to a real AI, replace `get_response()` in `routes/chat.py`:

```python
# Current (FAQ-based)
reply = get_response(request.message)

# Upgrade: OpenAI
from openai import AsyncOpenAI
client = AsyncOpenAI(api_key="...")
response = await client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant at Wajid ENT Clinic, Kabirwala..."},
        {"role": "user", "content": request.message}
    ]
)
reply = response.choices[0].message.content
```

---

## Doctor Info

- **Name**: Dr. Rana Humayun Babar
- **Qualifications**: MBBS, RMP, MS (ENT)
- **Specialty**: Endoscopic Sinus & Cosmetic Nose Surgeon
- **Clinic**: Wajid ENT Clinic, Jhang Road, Kabirwala
- **Phone**: 0309-8742674
