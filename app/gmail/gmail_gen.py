import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY","")
MODEL = os.getenv("GEMINI_MODEL","gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing.")

  prompt = f"""
Your are a professional Gmail writing assistant.

convvert the user's voice command into a professional email.

Rules:
- Do not copy the command literally.
- Do not explain everything.
- Do not invent names, dates , prices , comapnies , attachments , or facts.
- Keep the email natural and concise.

Output exactly:

SUBJECT: <subject>
BODY:
<email body>

User command:
{command}
"""

  url = (
      f"https://generativelanguage.googleapis.com/"
      f"vlbeta/nodels/{MODEL}:generativeContent"
  )
  
