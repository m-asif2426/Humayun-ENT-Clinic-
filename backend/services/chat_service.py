"""
Keyword-based FAQ chatbot for Wajid ENT Clinic.
Replace `get_response()` with an AI API call (OpenAI, Gemini, etc.) later.
"""

from __future__ import annotations

FAQ: list[dict] = [
    {
        "keywords": ["appointment", "book", "schedule", "visit", "consult", "appoint"],
        "reply": (
            "To book an appointment:\n"
            "1️⃣  Fill the form on our website\n"
            "2️⃣  Call us: 0309-8742674\n"
            "3️⃣  WhatsApp: 0309-8742674\n\n"
            "We will confirm your slot shortly! 📅"
        ),
    },
    {
        "keywords": ["time", "timing", "hours", "open", "close", "available", "when", "waqt"],
        "reply": (
            "🕐 Clinic Hours:\n"
            "• Mon – Thu & Sat: 10:00 AM – 9:00 PM\n"
            "• Friday: 4:00 PM – 9:00 PM (evening only)\n"
            "• Sunday: Closed\n\n"
            "For same-day visits, please call ahead."
        ),
    },
    {
        "keywords": ["address", "location", "where", "direction", "kabirwala", "kahan"],
        "reply": (
            "📍 Wajid ENT Clinic is located at:\n"
            "Jhang Road, opposite Al Shifa Orthopedic Hospital, Kabirwala, Punjab.\n\n"
            "Search 'Wajid Clinic Kabirwala' on Google Maps for directions."
        ),
    },
    {
        "keywords": ["fee", "fees", "cost", "price", "charges", "kitna", "how much"],
        "reply": (
            "For fee details, please call us at 0309-8742674.\n"
            "Our team will provide information based on your consultation type."
        ),
    },
    {
        "keywords": ["ear", "hearing", "tinnitus", "wax", "otitis", "vertigo", "balance"],
        "reply": (
            "👂 Ear conditions we treat:\n"
            "• Hearing loss & audiological assessment\n"
            "• Ear infections (Otitis Media / Externa)\n"
            "• Tinnitus (ringing in the ears)\n"
            "• Ear wax (cerumen) removal\n"
            "• Eardrum perforations & repair\n"
            "• Vertigo & balance disorders\n\n"
            "Book a consultation for proper diagnosis. 📅"
        ),
    },
    {
        "keywords": ["nose", "sinus", "allergy", "rhinitis", "sneezing", "blocked", "septum", "polyp", "naak"],
        "reply": (
            "👃 Nose & Sinus conditions we treat:\n"
            "• Endoscopic Sinus Surgery (FESS)\n"
            "• Nasal polyp removal\n"
            "• Deviated septum (Septoplasty)\n"
            "• Allergic rhinitis\n"
            "• Chronic sinusitis\n\n"
            "Dr. Humayun Babar specialises in minimally invasive endoscopic procedures."
        ),
    },
    {
        "keywords": ["throat", "tonsil", "voice", "swallow", "snoring", "hoarse", "larynx", "gala"],
        "reply": (
            "🗣️ Throat conditions we treat:\n"
            "• Tonsillectomy & Adenoidectomy\n"
            "• Voice & hoarseness disorders\n"
            "• Swallowing difficulties\n"
            "• Chronic throat infections\n"
            "• Snoring & sleep apnea evaluation\n\n"
            "Book a consultation for an expert assessment."
        ),
    },
    {
        "keywords": ["rhinoplasty", "nose job", "cosmetic", "aesthetic", "reshape"],
        "reply": (
            "✨ Cosmetic Nose Surgery by Dr. Rana Humayun Babar:\n"
            "• Cosmetic Rhinoplasty (Nose Job)\n"
            "• Nose tip refinement\n"
            "• Bridge correction\n"
            "• Functional + Aesthetic combined surgery\n\n"
            "Call 0309-8742674 for a personalised consultation."
        ),
    },
    {
        "keywords": ["doctor", "dr", "qualification", "experience", "specialist", "humayun"],
        "reply": (
            "👨⚕️ Dr. Rana Humayun Babar:\n"
            "• MBBS, RMP, MS (ENT)\n"
            "• Otorhinolaryngologist & ENT Surgeon\n"
            "• Endoscopic Sinus Surgery Specialist\n"
            "• Cosmetic Rhinoplasty Expert\n"
            "• 8+ years experience | 5000+ patients treated\n\n"
            "Available at Wajid ENT Clinic, Kabirwala."
        ),
    },
    {
        "keywords": ["emergency", "urgent", "serious", "critical"],
        "reply": (
            "For urgent cases, call us immediately at 0309-8742674.\n\n"
            "For life-threatening emergencies please go to the nearest A&E.\n"
            "Clinic hours: Mon-Sat 10 AM – 9 PM (Friday: 4 PM – 9 PM)."
        ),
    },
    {
        "keywords": ["phone", "number", "contact", "call", "whatsapp"],
        "reply": (
            "📞 Contact Information:\n"
            "• Phone / WhatsApp: 0309-8742674\n"
            "• Address: Jhang Road, opp. Al Shifa Orthopedic Hospital, Kabirwala\n\n"
            "Use the WhatsApp button on this page for quick messaging."
        ),
    },
]

DEFAULT = (
    "Thank you for your message! For the most accurate help please:\n"
    "📞 Call: 0309-8742674\n"
    "💬 WhatsApp: 0309-8742674\n\n"
    "Or fill the Appointment form on this page. Our team is happy to assist! 😊"
)


def get_response(message: str) -> str:
    """Return a keyword-matched FAQ answer or the default fallback."""
    lower = message.lower()
    for item in FAQ:
        if any(kw in lower for kw in item["keywords"]):
            return item["reply"]
    return DEFAULT
