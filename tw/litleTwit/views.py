from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from models import Message
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.
item = Message.objects.all()[:10]
def login_me(view_func):
    def check(x):
        if x.user.is_authenticated():
            x.session.set_expiry(3*3600)
            x.session.get_expiry_date()
            return view_func(x)
        else:
            auth_ = False
            return render_to_response("index.html",locals())
            #return what ? 
    return check

@csrf_exempt
def _logout(request):
    auth.logout(request)
    auth_ = False
    item = Message.objects.all().order_by('-id')[:10]
    return render_to_response('index.html',locals())

@csrf_exempt
def login(request):
    username = request.POST.get('login','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request,user)
        auth_ = True 
    else:
        auth_ = False 
        return HttpResponseRedirect('..',locals())
    return start(request,auth_ = auth_)


def start(request,auth_ = None):
    name = request.user.username
    item = Message.objects.all().order_by('-id')[:10]
    return render_to_response("index.html",locals());

@csrf_exempt
@login_me
def KeepIt(request):
    name = request.user.username
    msg = request.POST.get('text_user','')
    if msg:
        Message(owner = request.user, body = msg).save()
    return start(request,auth_ = True)

@csrf_exempt
@login_me
def refresh(request):
    # we do not check xml / app header
    # OK ?
    item = Message.objects.all().order_by('-id')[:10]
    res = ''
    for e in item:
        res += '<div class="alert alert-info"><strong>%s</strong>%s</div>'%(e.owner,e.body)
    return HttpResponse(res ,status=200)
    


@csrf_exempt
@login_me   
def search(request):
    msg1 = request.POST.get('findName','')
    res1 = ''
    if (msg1):
        
        try:
            user = User.objects.filter(username=msg1)[:1]
            Answer  = Message.objects.filter(Q(body__iexact=msg1)|Q(owner = user)|Q(body__contains=msg1)).order_by('-id')[:10]
        except:
            print 'expept'
            

    
        
        for e in Answer:
            res1 += '<div><strong>%s</strong>%s</div>'%(e.owner,e.body)
        return HttpResponse(res1,status=200)
    return HttpResponse(status=200)
