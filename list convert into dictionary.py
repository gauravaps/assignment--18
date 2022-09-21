# write a python program to convert two list into a dictionary in a way that item from
#list1 is the key and item from list2 is the value
key=["name","class","roll","result"]
value=["gaurav",12,101,"pass"]

newdict=dict(zip(key,value))
print(newdict)