import pickle
from phone import Phone,phones

class DB:
    def __init__(self):
        # 打开文件，如果文件不存在就创建一个文件
        try:
            with open('phone.data',mode='rb') as f:
                phones_byte=f.read()
                self.phones=pickle.loads(phones_byte)
        except:
            self.phones=[]


    def commit(self):
        '''
        保存数据
        :return:
        '''
        phones_str=pickle.dumps(self.phones)
        with open('phone.data',mode='wb') as f:
            f.write(phones_str)


    def is_have_id(self,id):
        '''
        判断手机编号是否存在
        :param id:
        :return:
        '''
        for phone in self.phones:
            if phone.id==id:
                return False
        else:
            return True



    def insert(self,id,brand,model,price,count,version):
        '''
        插入数据
        :param phone:
        :return:
        '''
        phone = Phone(id, brand, model, price, count, version)
        self.phones.append(phone)



    def find_by_brand(self,brand):
        '''
        通过品牌查找数据
        :param brand:
        :return:
        '''
        for phone in self.phones:
            if phone.brand==brand:
                return phone
            else:
                return '你输入的品牌不存在'

    def find_all(self):
        '''
        查找所有数据
        :return:
        '''
        if self.phones:
            for phone in self.phones:
                print(phone)
        else:
            print('数据库中还没有数据请添加数据！')

    def updata_by_id(self,id,price):
        '''
        通过id修改手机价格
        :param id:
        :param price:
        :return:
        '''
        for phone in self.phones:
            if phone.id==id:
                phone.price=price
                return True
        else:
            return False

    def delete_by_id(self,id):
        for phone in self.phones:
            if phone.id==id:
                self.phones.remove(phone)
                return True
        else:
             return False



if __name__ == '__main__':
    print(phones)
    db=DB()
    print(db.phones)
    db.find_all()