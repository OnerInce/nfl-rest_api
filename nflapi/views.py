from django.http import HttpResponse

def WelcomeView(request):

    message = "<body>Welcome to the Nfl Rest API</body>"
    return HttpResponse(message)
