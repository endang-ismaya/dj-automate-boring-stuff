def is_post(request):
    return request.method == "POST"

def is_get(request):
    return request.method == "GET"