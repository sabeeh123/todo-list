from django.shortcuts import render

# Create your views here.
def activity_list(request):
    return render(request,'activity_templates/list.html')