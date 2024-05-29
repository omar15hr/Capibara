import requests
from django.conf import settings

def send_email_via_resend(to_email, subject, body):
    url = "https://api.resend.com/v1/send"
    headers = {
        "Authorization": f"Bearer {settings.RESEND_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "from": settings.RESEND_SENDER_EMAIL,
        "to": to_email,
        "subject": subject,
        "html": body
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return True
    else:
        print(f"Error sending email: {response.text}")
        return False
