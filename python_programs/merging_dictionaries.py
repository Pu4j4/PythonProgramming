#merging two dictionaries keeping the max values for duplicate keys

# dict1 = {"a": 12, "b": 10, "c":3}
# dict2 = {"a": 15, "b": 5, "c":2}
# mydict = dict1.copy()
# for key,value in dict2.items():
#     if key in mydict:
#         mydict[key] =max(mydict[key], value)
#     else:
#         mydict[key] = value
# print(mydict)

#using functions
def merge_dicts(dict1,dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = max(merged.get(key,value), value)
    return merged
a={"a":"3","b":"2","c":"7"}
b={"a":"1","b": "5","c":"8"}
print(merge_dicts(a,b))