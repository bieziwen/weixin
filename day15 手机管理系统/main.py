from phone import Phone
from db import DB
def muen():
    content='''
    --------------------------------------------
    手机信息管理系统
    1.手机录入
    2.根据手机品牌查询手机
    3.查询全部手机信息
    4.根据手机编号修改手机价格
    5.根据手机编号删除手机记录
    6.退出
    --------------------------------------------
    '''
    return content





def main():
    db=DB()
    while True:
        print(muen())
        number = int(input('请输入您的操作：'))
        if number==1:
            id=int(input('请输入手机编号：'))
            flag=db.is_have_id(id)
            if flag:
                brand=input('请输入手机品牌：')
                model=input('请输入手机型号：')
                price=float(input('请输入手机价格：'))
                count=int(input('请输入数量：'))
                version=input('请输入版本：')
                db.insert(id,brand,model,price,count,version)
                db.find_all()
                db.commit()
                print('添加成功！')
            else:
                print('您输入的手机编号已存在，请重新输入！')
        elif number==2:
            brand=input('请输入你要查询的手机品牌：')
            phone=db.find_by_brand(brand)
            print(phone)
            db.commit()
        elif number==3:
            db.find_all()
            db.commit()
        elif number==4:
            id=int(input("请输入手机编号："))
            price=float(input("请输入手机价格："))
            flag=db.updata_by_id(id,price)
            if flag:
                print('修改成功！')
            else:
                print('您要修改的手机不存在！')
            db.find_all()
            db.commit()
        elif number==5:
            id=int(input("请输入手机编号："))
            flag=db.delete_by_id(id)
            if flag:
                print('删除成功！')
            else:
                print('您要删除的手机不存在！')
            db.find_all()
            db.commit()
        elif number==6:
            print('程序退出成功！')
            break
        else:
            print('您的输入有误，请重新输入!')






if __name__ == '__main__':
    main()
