# coding=utf-8


dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict2 = {'abc': 456}
dict3 = {'abc': 123, 98.6: 37}


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict1['Name]:", dict1['Name']  # dict1['Name]: Zara
print "dict1['Age']:", dict1['Age']  # dict1['Age']: 7


try:
    print "dict1['Alice']:", dict1['Alice']
except Exception, e:
    print Exception, e  # <type 'exceptions.Exception'> 'Alice'


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict1['Age'] = 8  # update existing entry
dict1['School'] = "DPS School"  # add new entry


print "dict1['Age']: ", dict1['Age']  # dict1['Age']:  8
print "dict1['School']:", dict1['School']  # dict1['School']: DPS School

dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict1['Name']  # delete the value in key 'name'
dict1.clear()  # delete all element in dict
del dict1  # delete the dict itself


dict1 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "dict1['Name']:", dict1['Name']  # dict1['Name']: Manni


try:
    dict1 = {['Name']: 'Zara', 'Age': 7}
except Exception, e:
    print Exception, e  # <type 'exceptions.Exception'> unhashable type: 'list'


# Dict Build-in Functions & Method
# Method - cmp
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Name': 'Mahnaz', 'Age': 27}
dict3 = {'Name': 'Abid', 'Age': 27}
dict4 = {'Name': 'Zara', 'Age': 7}
print "Return Value: %d" % cmp(dict1, dict2)  # Return Value: -1
print "Return Value: %d" % cmp(dict2, dict3)  # Return Value: 1
print "Return Value: %d" % cmp(dict1, dict4)  # Return Value: 0


# Method - len
dict1 = {'Name': 'Zara', 'Age': 7}
print "Length: %d" % len(dict1)  # Length: 2


# Method - str
dict1 = {'Name': 'Zara', 'Age': 7}
print "Equivalent String: %s" % str(dict1)  # Equivalent String: {'Age': 7, 'Name': 'Zara'}


# Method - type
dict1 = {'Name': 'Zara', 'Age': 7}
print "Variable Type: %s" % type(dict1)  # Variable Type: <type 'dict'>


# Function - clear
dict1 = {'Name': 'Zara', 'Age': 7}
print "Start Len: %d" % len(dict1)  # Start Len: 2
dict1.clear()
print "End Len: %d" % len(dict1)  # End Len: 0


# Function - copy
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = dict1.copy()
print "New Dictionary: %s" % str(dict2)  # New Dictionary: {'Age': 7, 'Name': 'Zara'}


# Function - fromkeys
seq = ('name', 'age', 'sex')
dict1 = dict.fromkeys(seq)
print 'New Dictionary: %s' % str(dict1)  # New Dictionary: {'age': None, 'name': None, 'sex': None}

dict1 = dict.fromkeys(seq, 10)
print "New Dictionary: %s" % str(dict1)  # New Dictionary: {'age': 10, 'name': 10, 'sex': 10}

value = (10, 11)
dict1 = dict.fromkeys(seq, value)
print "New Dictionary: %s" % str(dict1)  # New Dictionary: {'age': (10, 11), 'name': (10, 11), 'sex': (10, 11)}

dict1 = dict.fromkeys(('name', 'age', 'sex'), (10, 11))
print "New Dictionary: %s" % str(dict1)  # New Dictionary: {'age': (10, 11), 'name': (10, 11), 'sex': (10, 11)}


# Function - get
dict1 = {'Name': 'Zara', 'Age': 27}
print "Value: %s" % dict1.get('Age')  # Value: 27
print "Value: %s" % dict1.get('Sex')  # Value: None
print "Value: %s" % dict1.get('Sex', 'Never')  # Value: Never


# Function - has_key
dict1 = {'Name': 'Zara', 'Age': 27}
print "Value: %s" % dict1.has_key('Age')  # Value: True
print "Value: %s" % dict1.has_key('Sex')  # Value: False


# Function - items
dict1 = {'Name': 'Zara', 'Age': 27}
print "Value: %s" % dict1.items()  # Value: [('Age', 27), ('Name', 'Zara')]


# Function - keys
dict1 = {'Name': 'Zara', 'Age': 27}
print "Value: %s" % dict1.keys()  # Value: ['Age', 'Name']


# Function - setdefault
dict1 = {'Name': 'Zara', 'Age': 27}
print "Value: %s" % dict1.setdefault('Age', None)  # Value: 27
print "Value: %s" % dict1.setdefault('Sex', 'female')  # Value: 2
print dict1  # {'Age': 27, 'Name': 'Zara', 'Sex': 'female'}


# Function - update
dict1 = {'Name': 'Zara', 'Age': 27}
dict2 = {'Sex': 'female', 'Age': 20}
dict1.update(dict2)
print "Value: %s" % dict1  # Value: {'Age': 20, 'Name': 'Zara', 'Sex': 'female'}


# Function - values
dict1 = {'Name': 'Zara', 'Age': 27}
print "Value: %s" % dict1.values()  # Value: [27, 'Zara']
