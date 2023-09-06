import redis, time
r = redis.Redis(host='localhost', port=6379, decode_responses=True, db=1)
# # r.ping() 
# # r.lpush('foo', [1,2,3,4,5,6,7,8,9])
# # r.lrange('foo', 0, -1)
# numberList='LanguageList'
# a=r.lpush('LanguageList', "Kotlin")
# # plist= ['siuuu', 10.0, 5]
# # b=r.lpush('LanguageList', plist)

# r.expire('LanguageList', 10)
# # r.lpush('shoppingCartKList', )

# # while(r.llen('LanguageList')!=0):

# #     print(r.lpop('LanguageList'))
# # print('a:',a)
# print(r.lrange('LanguageList', 0, -1))
 
# # for i in range(0, r.llen(numberList)):
# #     print(r.lindex(numberList, i))

# # # r.mget({'k1': 'v1', 'k2': 'v2'})
# # r.mset({'k:1': 'v1', 'k:2': 'v2'}) # 这里k1 和k2 不能带引号，一次设置多个键值对
# # print(r.mget("k:1", "k:2"))   # 一次取出多个键对应的值
# # print(r.mget("k:1"))


# user = {"Name":"Pradeep", "Company":"SCTL", "Address":"Mumbai", "Location":"RCP"}

# # r.hset("pythonDict", mapping=user)

# # r.hgetall("pythonDict")

# hm = all([r.hset('pythonDict1', k, v) for k, v in user.items()])
# print(hm)

# # r.hset('cartl:1', 'price', 5)    
# # r.hset('cartl:1', 'name', 'product1')    
# # r.hset('cartl:2', 'price', 5)    
# # r.hset('cartl:2', 'name', 'product2')    
# # print(r.hgetall("cartl"))

# for i in range(1,5):
#     r.hset('cartl:'+str(i), 'price', 5)    
#     r.hset('cartl:'+str(i), 'name', 'product'+str(i))   
cart_list=[]
for key in r.scan_iter("CartList:*"):
    item =r.hgetall(key)
    item["key"]=key
    cart_list.append(item)
    # print(key, r.hgetall(key))
print(cart_list)


    # delete the key
    # r.delete(key)

print('key', len(list(r.scan_iter("cartlii:*"))))
