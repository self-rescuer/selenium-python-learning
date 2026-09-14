def deep_merge(dict1, dict2):
    result={}
    for key in dict1:
        if key in dict2:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                result[key]=deep_merge(dict1[key], dict2[key])
            elif not isinstance(dict1[key], dict) and  isinstance(dict2[key], dict):
                result[key] = dict2[key]
            elif not isinstance(dict2[key], dict) and isinstance(dict1[key], dict):
                result[key] = dict1[key]
            else:
                result[key]=dict2[key]
        else:
            result[key]=dict1[key]
    for key in dict2:
        if key not in dict1:
            result[key]=dict2[key]
    return result
d1 = {
    "a": 1,
    "b": {
        "x": 10,
        "y": 20
    },
    "c": 3,
    "d":{
        "x": 10,
        "y": 20
    }
}

d2 = {
    "b": {
        "y": 99,
        "z": 30
    },
    "c": 100,
    "d":7
}

print(deep_merge(d1, d2))

