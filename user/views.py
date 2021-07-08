import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User


# Create your views here.

def register_view(request):
    # 注册
    # GET 返回页面
    # POST 处理提交数据
    # 两次密码一致，用户名是否存在
    # 插入数据
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # 处理提交数据
        # 1.两次密码一致
        # 2.用户名是否可用
        # 3.提交给数据库
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        # 两次密码一致
        if password_2 != password_1:
            return HttpResponse('两次输入的密码不一致！')
        # 对密码进行哈希处理，计算出定长的，不可逆的值，MD5，sha-256
        # 1.定长输出 2.不可逆，无法反向计算 3.雪崩效应
        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()
        old_users = User.objects.filter(username=username)
        # 有唯一索引要用try
        if old_users:
            return HttpResponse("该用户名已存在！")
        # 提交给数据库
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            print("---create user error! %s" % (e))
            return HttpResponse("该用户名已存在！")
        # 设置免登陆
        request.session['username'] = username
        request.session['uid'] = user.id
        return HttpResponseRedirect('/index')


def login_view(request):
    if request.method == 'GET':
        # 如果发送给服务器的是get请求的话，渲染登录页面
        # 如果存在session的话，跳转到主页，如果不存在的话检查cookie
        if request.session.get('username') and request.session.get('uid'):
            # 这里应该302跳转网站首页
            return HttpResponseRedirect('/index')
        c_username = request.COOKIES.get("username")
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            # 登录状态是以cookie保存的，需要转存到session中
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # 这里应该302跳转网站首页
            return HttpResponseRedirect('/index')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 如果发送给服务器的是post请求的话，验证表单的账号密码
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print("---login user error %s" % (e))
            return HttpResponse("登录失败，用户名或密码错误！")
        # 计算密码的哈希值
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse("登陆失败，用户名或密码错误！")
        # 记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id
        resp = HttpResponseRedirect('/index')
        # 判断用户是否点选了'3天免登陆'
        if 'remember' in request.POST:
            resp.set_cookie('uid', user.id, 3600 * 24 * 3)
            resp.set_cookie('username', username, 3600 * 24 * 3)
        return resp


def logout_view(request):
    c_username, c_uid = request.COOKIES.get('username'), request.COOKIES.get('uid')
    s_username, s_uid = request.session.get('username'), request.session.get('uid')
    resp = HttpResponseRedirect('/index')
    if c_username and c_uid:
        resp.delete_cookie('username')
        resp.delete_cookie('uid')
    if s_username and s_uid:
        del request.session['username']
        del request.session['uid']
    return resp
