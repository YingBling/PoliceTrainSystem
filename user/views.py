from django.shortcuts import render


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
        pass
