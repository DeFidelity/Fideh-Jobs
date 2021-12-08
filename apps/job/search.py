from django.db.models import Q 
import json
from django.http import JsonResponse 

from .models import Job  

def searchquery(request):
    joblist = []
    data = json.load(request.body)
    query = data['query']
    remote = data['remote']
    
    jobs = Job.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)|Q(detail__icontains=query))
    
    S
    if remote:
        jobs = jobs.filter(remote=remote)
        
    for job in jobs:
        obj = {
            'id':job.id,
            'title':job.title,
            'remote': job.remote,
            'url': job.url,
            
        }
        joblist.append(obj)
        return JsonResponse('jobs': joblist)