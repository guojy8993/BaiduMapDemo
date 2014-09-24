#author guojingyu
#date      Sep 17, 2014
from jobs.models import Job
from django.shortcuts import get_object_or_404,render_to_response

def index(request):
    object_list = Job.objects.order_by('-pub_date')[:3]
    return render_to_response('jobs/job_list.html',{'object_list':object_list})

def detail(request,job_id):
    job = get_object_or_404(Job,pk=job_id)
    return render_to_response('jobs/job_detail.html',{'job':job})

def main(request):
    return render_to_response('jobs/home.html',{'greeting':'Welcome to Etiantian Shop'})

