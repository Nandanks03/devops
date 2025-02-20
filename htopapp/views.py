from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os
import datetime
import subprocess

def htop_view(request):
    name = "Nandan KS"
    username = os.getenv("USER", "unknown")
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = subprocess.getoutput("top -bn1 | head -20")

    html = f"""
    <h1>System Information</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time.strftime("%Y-%m-%d %H:%M:%S")}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(html)

