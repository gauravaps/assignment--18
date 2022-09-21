# write a python program to merge two dictionary into one dictionary..

'''dict1={"name":"gaurav","address":"rewa","state":"mp"}
dict2={"mail":"gaurav@.com","mobile":7318,"company":"tcs"}
dict3={**dict1,**dict2}
print(dict3)'''


'''dict1={"name":"gaurav","address":"rewa","state":"mp"}
dict2={"mail":"gaurav@.com","mobile":7318,"company":"tcs"}
new=(dict(dict1,**dict2))
print(new)'''

'''def merge(dict1,dict2):
    return (dict2.update(dict1))

dict1={"name":"gaurav","address":"rewa","state":"mp"}
dict2={"mail":"gaurav@.com","mobile":7318,"company":"tcs"} 

print(merge(dict1,dict2))
print(dict2)'''

dict1={"name":"gaurav","address":"rewa","state":"mp"}
dict2={"mail":"gaurav@.com","mobile":7318,"company":"tcs"}
dict3=dict1.update(dict2)
print(dict1)
