"""
Wajid ENT Clinic – FastAPI Backend
Run: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
"""
import os
import sys

# Ensure Vercel can find the modules inside the 'backend' folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes.appointment import router as appointment_router
from routes.chat import router as chat_router
from config import settings

app = FastAPI(
    title="Wajid ENT Clinic API",
    description="Backend for Wajid ENT Clinic website",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# ── CORS ────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── API routes (must be registered BEFORE static mount) ─────────────────────
app.include_router(appointment_router)
app.include_router(chat_router)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "clinic": settings.CLINIC_NAME}


# ── Serve frontend (register LAST so API routes take priority) ───────────────
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "public")
if os.path.isdir(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
