# coding=utf-8


import demjson


# encode
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
json_data = demjson.encode(data)
print json_data  # [{"a":1,"b":2,"c":3,"d":4,"e":5}]


# decode
json = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
print demjson.decode(json)  # {u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}
