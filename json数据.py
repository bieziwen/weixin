import json
user={
    "name":'浩浩',
    'id':1,
}
li=[user,user,user]
result={
    "code":200,
    "msg":True,
    "data":li
}
"""
Python不支持class对象转化为json数据
只有列表和字典能转化为json数据
"""
if __name__ == '__main__':
    # 将Python数据转化为json数据(序列化)
    json_str=json.dumps(result)
    print(type(json_str))
    print(json_str)

    #将json数据转化为json数据(反序列化)
    dic=json.loads(json_str)
    print(type(dic))
    print(dic)

