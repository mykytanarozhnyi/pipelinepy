import smtplib
from email.message import EmailMessage
import os

def send_notification(report_date, kpi_summary):
    msg = EmailMessage()
    msg.set_content(f"Report for {report_date} is Ready.\n\nQuick Summary::\n{kpi_summary}")
    msg['Subject'] = f"🚀 KPI Report Updated: {report_date}"
    msg['From'] = os.getenv("EMAIL_SENDER")
    msg['To'] = os.getenv("EMAIL_RECEIVER")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv("EMAIL_SENDER"), os.getenv("EMAIL_PASSWORD"))
        smtp.send_message(msg)
    print("📧 Email sent successfully!")