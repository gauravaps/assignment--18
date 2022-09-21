# write a python program to create a dictionary that contains three dictionaries (nested).
item={"brand":{"model":2022,"price":5000,
       "rate":{"class":12,"subject":"maths",
       "mobile":{"locatio":"rewa","mail":"gaurav@gmail"}}}}
for i in item:
    if type(item[i]) is dict:
        for k in item[i]:
            print(k,' ',item[i])     
print(item)

