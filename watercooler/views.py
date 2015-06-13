from django.http import HttpResponse

def index(request):
    return HttpResponse("This should be a list of threads")

def thread(request, thread_id):
    return HttpResponse("You're looking at thread %s." % thread_id)
