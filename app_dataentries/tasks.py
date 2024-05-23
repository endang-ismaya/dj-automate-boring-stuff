import time

from django.core.management import call_command

from _prj.celery import app


@app.task
def celery_test_task():
    time.sleep(10)  # simulation of any task that's going to take 10 seconds
    # send an email
    # mail_subject = "10 Seconds Test Email"
    # message = "This is a test email"
    # from_email = settings.DEFAULT_FROM_EMAIL
    # to_email = "endang.ismaya@gmail.com"

    # mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    # mail.send()

    # send_email_notification(mail_subject, message, to_email)
    # return "Email sent successfully."
    return "Task executed successfully"


@app.task
def import_data_task(file_path, model_name):
    try:
        call_command("importdata", file_path, model_name)
    except Exception as e:
        raise e
    # notify the user by email
    # mail_subject = "Import Data Completed"
    # message = "Your data import has been successful"
    # to_email = settings.DEFAULT_TO_EMAIL
    # send_email_notification(mail_subject, message, [to_email])
    return "Data imported successfully."


# @app.task
# def export_data_task(model_name):
#     try:
#         call_command("exportdata", model_name)
#     except Exception as e:
#         raise e

#     file_path = generate_csv_file(model_name)

#     # Send email with the attachment
#     mail_subject = "Export Data Successful"
#     message = "Export data successful. Please find the attachment"
#     to_email = settings.DEFAULT_TO_EMAIL
#     send_email_notification(mail_subject, message, [to_email], attachment=file_path)
#     return "Export Data task executed successfully."
