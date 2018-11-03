phones=[]
class Phone:
    def __init__(self,id,brand,model,price,count,version):
        self.id=id
        self.brand=brand
        self.model=model
        self.price=price
        self.count=count
        self.version=version

    def __str__(self):
        return 'id:%s  品牌：%s  型号：%s  价格：%s 数量：%s  版本：%s'%(self.id,self.brand,self.model,self.price,self.count,self.version)


Apple=Phone(1,'Apple','iphone4s',4999.0,3,'国行')
SONY=Phone(2,'SONY','z3l55',4999.0,10,'智享版')
P7=Phone(3,'华为','Ascend7',2388.0,3,'16G版')
phones.append(Apple)
phones.append(SONY)
phones.append(P7)
