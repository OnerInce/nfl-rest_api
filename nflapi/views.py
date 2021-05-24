from django.http import JsonResponse

def WelcomeView(request):

    return JsonResponse({'result':'success', 'message':'Welcome to the NFL Rest API'})
