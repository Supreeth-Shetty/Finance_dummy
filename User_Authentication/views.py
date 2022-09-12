from django.shortcuts import render
from django.http import request
from logger.logger import Applogs


log = Applogs('logger\logs\projectlogs.log', 'DEBUG')
log.getlogger(__file__)

# Create your views here.
def home(request):
    log.info("Landed on home page!")
    return render(request,'index.html')