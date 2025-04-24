from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
    # try:
    #     jobs_list=Job.objects.all()
    # except Exception:
    #     print(Exception)
    #     context={'error':'Sorry No Jobs Available Right Now'}
    #     return render(request,'home.html',context)
    jobs_list=Job.objects.all()
    
    context={'jobs_list': jobs_list}
    return render(request,'home.html',context)