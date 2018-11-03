users={"name":"赵文浩","password":666}
def is_right(func):
    def wrapper(name,password):
            if name==users['name'] and password==users['password']:
                print('登录成功！')
                func()
            else:
                print('您输入的账号或者密码有误！')
    return wrapper

@is_right
def f():
    pass

if __name__ == '__main__':
    name=input('请输入姓名：')
    password=int(input('请输入密码：'))
    f(name,password)


