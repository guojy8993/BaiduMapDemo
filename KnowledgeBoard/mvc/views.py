#coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from mvc.models import Doc
from com.hiapp.common.exceptions import exception
from mvc.models import User
import logging

logging.basicConfig(filename="/tmp/knowledgeboard.log",level=logging.INFO)
logger = logging.getLogger(__name__)
"""
DOC
"""
def to_add_doc(request):
    return render_to_response("pages/add_doc.html",context_instance = RequestContext(request)) 
def get_docs(request):
    docs = Doc.objects.order_by("-create_at")
    return render_to_response("pages/doc_list.html",{"doc_list":docs},context_instance = RequestContext(request))

def add_doc(request):
    title = request.POST.get("title")
    content = _process_article(request.POST.get("content"))
    user_id = request.session.get("user_id")
    author = User.objects.get(id=user_id).user
    Doc.objects.create(title=title,content=content,author=author)
    return render_to_response("pages/add_doc.html",context_instance = RequestContext(request))

def _process_article(article):
    parray = article.split("\n")
    result = ""
    for p in parray:
        result += "     %s \x0a"%p.strip()
    return result;
"""
USER
"""
def goto_register(request):
    return render_to_response("users/register_user.html",context_instance = RequestContext(request))
def user_register(request):
    
    post_data = request.POST
    try:
        #username
        if "user" not in post_data or post_data["user"].strip()=="":
            raise exception.RegistParamsInComplete(param="user")
        dbuser = User.objects.filter(user=post_data["user"]).first()
        if dbuser is not None:
            raise exception.UsernameAlreadyUsed(username=post_data["user"])
        
        #passwd
        if "password" not in post_data or post_data["password"].strip()=="":
            raise exception.RegistParamsInComplete(param="password")
        
        #email
        if "email" not in post_data or post_data["email"].strip()=="":
            raise exception.RegistParamsInComplete(param="email")
        dbemail = User.objects.filter(email=post_data["email"]).first()
        if dbemail is not None:
            raise exception.RegisterEmailALreadyUsed(email=post_data["email"])
    except exception.RegistParamsInComplete as e1:
        logger.info("[*]%s"%e1.msg)
        return render_to_response("users/register_user.html",context_instance = RequestContext(request))
    except exception.UsernameAlreadyUsed as e2:
        logger.info("[*]%s"%e2.msg)
        return render_to_response("users/register_user.html",context_instance = RequestContext(request))
    except exception.RegisterEmailALreadyUsed as e3:
        logger.info("[*]%s"%e3.msg)
        return render_to_response("users/register_user.html",context_instance = RequestContext(request))
    else:    
        User.objects.create(user=post_data["user"],password=post_data["password"],email=post_data["email"])
        return goto_login(request) # forward the request 

def user_list(request):
    user_list = User.objects.order_by("-id").all()
    return render_to_response("users/list_user.html",{"users":user_list},context_instance = RequestContext(request))

def goto_login(request):
    return render_to_response("users/login.html",context_instance = RequestContext(request))

def user_login(request):
    
    post_data = request.POST 
    try:        
        #username
        if "user" not in post_data or post_data["user"].strip()=="":
            raise exception.LoginParamsInComplete(param="user")
        if "password" not in post_data or post_data["password"].strip()=="":
            raise exception.LoginParamsInComplete(param="user")
        dbuser = User.objects.filter(user=post_data["user"]).first()
        if dbuser is None:
            raise exception.UserNotExist(user=post_data["user"])
        if not dbuser.password == post_data["password"]:
            raise exception.UsernamePasswordNotMatch()
    except exception.LoginParamsInComplete as e1 :
        logger.info("[*]%s"%e1.msg)
        return goto_login(request)
    except exception.UserNotExist as e2:
        logger.info("[*]%s"%e2.msg)
        return goto_login(request)    
    except exception.UsernamePasswordNotMatch as e3:
        logger.info("[*]%s"%e3.msg)
        return goto_login(request)    
    else:    
        #user match password
        request.session["user_id"] = dbuser.id
        return render_to_response("users/index.html",context_instance = RequestContext(request))
        
    
    
    
    
    
    
    
        
    
    
    
    
# Here when submitting form with post method ,i encountered a problem :  CSRF cookie not set or so ;  
# The help messgae provide 4 steps to resolve this problem:
# 1. configure MIDDLEWARE_CLASSES in settings.py with 'django.middleware.csrf.CsrfViewMiddleware' 
# 2. add csrf_token tag within a form 
# 3. in view functionality use django.template.RequestContext instead of Context (note that --here i mean  all view functionalities ))
# 4. make sure browser accept cookies ;
# and instruction3 deserver more attention ;