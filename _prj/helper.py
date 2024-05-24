from app_emails.models import Subscriber


def is_post(request):
    return request.method == "POST"

def is_get(request):
    return request.method == "GET"

def get_subslist(category):
    """Extract email addresses from Subscriber Model"""
    subscribers = Subscriber.objects.filter(email_list=category)

    to_email = []
    for subs in subscribers:
        to_email.append(subs.email)
    
    return to_email, ",".join(to_email)
