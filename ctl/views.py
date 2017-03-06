from django.views.generic import TemplateView
from ctl.data.sysctl import Sys
from django.shortcuts import redirect
from ctl.data.latest_news import latest_info, latest_url
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.gzip import gzip_page



class Sysctl(TemplateView):
    """I wanted elementary "views" and think i got simple code.
   Maybe need functions rewrite with redirect to "ajax" post requests;
   but this add larger code jquery.
    """
    
    template_name = "ctl/sysctl.html"
    
    """
    not use's return check status in next functions,
    all commands checked in this project's sysctl module.
    """

    def timers_stop(self):
        Sys.timers_stop()
        return redirect('/')

    def timers_start(self):
        Sys.timers_start()
        return redirect('/')

    def sream_start(self):
        Sys.stream_start()
        return redirect('/')

    def sream_stop(self):
        Sys.stream_stop()
        return redirect('/')
    
    
    def ajax(request):
        """
        'ajax' function creates data  to url
        /ajax in json format as GET method
        """
        
        def sp(cmd):
            return str(cmd).split("\n")
        data = {}
        data['timers'] = Sys.list_timers()
        data['file'] = latest_info()
        data['full_file'] = latest_url()
        data['journal'] = sp(Sys.err())[::-1][0:6]
        data['stream'] = Sys.stream_status()
        data["next_start"] = Sys.next_start_release()
        return HttpResponse(json.dumps(data), content_type = "application/json")
        gzip_page(ajax())