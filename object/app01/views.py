from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.
import json,re
from django.shortcuts import HttpResponse,render,redirect
from app01 import models
def add(request):
    # with open("admin.html","rb",encoding="utf-8") as f:
    #     date=f.read()
    #return render(request,"xxx.html")
    name=request.POST.get("name",None)
    id_card=request.POST.get("id",None)
    password=request.POST.get("pwd",None)
    sex=request.POST.get("sex",None)
    xx=models.login.objects.all()
    if name=='' or id_card=='' or password=='' or sex==None:
        return render(request,'add.html',{'error':'请将信息填写完整'})
    for list in xx:
        if list.name==name:
            return render(request, 'add.html', {'error': '该用户名已被注册'})
        elif list.id_card==id_card:
            return render(request, 'add.html', {'error': '该学号已被注册'})
    models.login.objects.create(name=name,id_card=id_card,sex=sex,password=password)
    # stu={"name":name,"id":id,"password":password,"sex":sex}
    # stu=json.dumps(stu)
    # file=open("C:/Users/孙智超/Desktop/郑州python/数据/保存.txt","a")
    # file.write(stu)
    # file.close()
    # return HttpResponse("注册成功")
    # return HttpResponse(f"名字:{name},性别:{sex},学号:{id_card},密码:{password}")
    return redirect('/yezi/')
def loading(request):
    return render(request,"loading.html")
def load(request):
    name = request.POST.get("name", None)
    password = request.POST.get("pwd", None)
    if name == '' or password == '':
        return render(request, 'loading.html', {'error': '请将信息填写完整'})
    xx=models.login.objects.all()
    for list in xx:
        if (request.POST.get('name')==list.name or request.POST.get('name')==list.id_card) and request.POST.get('pwd')==list.password:
            name=list.name
            id=list.id_card
            return redirect( f'/yezi/?name={name}&id={id}')
    return render(request, 'loading.html', {'error': '用户名或密码错误!!!'})
    # try:
    #     file = open("C:/Users/孙智超/Desktop/郑州python/数据/保存.txt","r")
    # except:
    #     return render(request, "loading.html", {"error":"未注册,请先注册" })
    # else:
    #     f=file.read()
    #     pattern=re.compile('{"name": (.*?), "id": (.*?), "password": (.*?), "sex": (.*?)}')
    #     name = re.findall(pattern,f)
    #     for x in name:
    #         name=json.loads(x[0])
    #         id = json.loads(x[1])
    #         password = json.loads(x[2])
    #         if (request.POST.get("name", None) == name or request.POST.get("name", None) == id) and request.POST.get("pwd", None) == password:
    #             file.close()
    #             return redirect("https://www.baidu.com")
    #         else:
    #             error_msg = "登陆失败"
    #     file.close()
    #     return render(request, "loading.html", {"error": error_msg})
def adding(request):
    return render(request, "add.html")
def yezi(request):
    ret=models.login.objects.all()
    cret=models.content.objects.all()
    content=request.GET.get('content')
    print(request.GET.get('name'))
    if content==None:
        content = ''
    return render(request,"yezi.html",{'content':ret,'ret':cret,'id':request.GET.get('id'),'name':request.GET.get('name')})
def delete(request):
    id=request.GET.get('id',None)
    del_id=models.login.objects.get(id=id)
    del_id.delete()
    return redirect('/yezi/')
def change(request):
    id=request.GET.get('id')
    return render(request,"change.html",{'id':id})
    # return redirect("/changing/")
def changing(request):
    error=''
    change_name = request.POST.get("name", None)
    change_idcard = request.POST.get("id_card", None)
    change_pwd = request.POST.get("pwd", None)
    change_sex = request.POST.get("sex", None)
    if change_name == ''or change_sex== None or change_idcard == '' or change_pwd == '':
        return render(request,'change.html',{'error':'请将修改后的信息填写完整'})
    id = request.GET.get('id')
    change = models.login.objects.get(id=id)
    change.name=change_name
    change.id_card=change_idcard
    change.password=change_pwd
    change.sex=change_sex
    change.save()
    return redirect('/yezi/')
def rizhi(request):
    # content=''
    # if request.POST.get('text')==None:
    #     print(content)
    #     return render(request,'日志.html')
    # return render(request, '日志.html',{'content':content})
    try:
        content=request.POST.get('text')
    except:
        return render(request, '日志.html')
    else:
        return render(request, '日志.html', {'content': content})
def content(request):
    name=request.GET.get('name')
    id=request.GET.get('id')
    print(id,name)
    content=request.GET.get('content')
    content=(content)
    models.content.objects.create(content=content)
    return redirect('/yezi/')
def shanchu(request):
    id = request.GET.get('id', None)
    print(id)
    del_id = models.content.objects.get(id=id)
    del_id.delete()
    return redirect('/yezi/')
