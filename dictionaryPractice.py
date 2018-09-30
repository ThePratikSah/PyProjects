data = {'name': 'Pratik', 'class': 'B.Tech', 'branch': 'CSE', 'roll': 11617}

# printing a particular value using key
print(data['roll'])

# updating a particular value
data['roll'] = 11602
print(data)

# delete a particular value
del data['class']
print(data)

num = data['roll']
print('num is', num)

# removing element using pop method
data.pop('roll')
print(data)
data.clear()
print(data)

data = [2 * i for i in range(1,11)]
print(data)



