import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client

load_dotenv()

print("SUPABASE_URL:", os.getenv("SUPABASE_URL"))
print("KEY prefix:", (os.getenv("SUPABASE_SERVICE_ROLE_KEY") or "")[:12])

app = FastAPI()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_ROLE_KEY")
)

class Lead(BaseModel):
    name: str
    company: str | None = None
    message: str
    score: int
    status: str
    reason: str

@app.post("/callback")
def callback(lead: Lead):
    data = lead.model_dump()

    result = supabase.table("leads").insert(data).execute()

    print("Saved lead:", data)

    return {
        "ok": True,
        "saved": data
    }