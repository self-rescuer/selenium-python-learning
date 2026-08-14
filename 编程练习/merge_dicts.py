def merge_dicts(dict1,dict2):
    dict1.update(dict2)
    print(dict1)
dict01={'q':7,'w':7,'e':9}
dict02={'o':6,'w':8}
merge_dicts(dict01,dict02)