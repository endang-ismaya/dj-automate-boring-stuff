from _prj.celery import app
from app_dataentries.utils import send_email_notification


@app.task
def send_email_task(mail_subject, message, to_email, attachment):
    """Sending email thru celery"""
    send_email_notification(mail_subject, message, to_email, attachment)
    return "task:send_email_task::completed "
