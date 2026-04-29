Created a virtual environment

py -m venv .venv

Activated the environment

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1

Install the required libraries

.\.venv\Scripts\python.exe -m pip install -r requirements.txt

Start FastAPI server

.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload

Install ngrok

winget install Ngrok.Ngrok

https://ngrok.com/

Added ngrok authtoken

ngrok config add-authtoken YOUR_NGROK_TOKEN

Launched the ngrok
ngrok http 8000

Run the lead sender script

.\.venv\Scripts\python.exe scripts\send_leads.py     