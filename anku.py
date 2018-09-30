name = 'prince'
age = 16
address = 'katihar'
brother = {'name': 'prince', 'age': 16, 'address': 'katihar'}
print(brother['name'])
print('my name is {}, my age is {}, i live at {}'
      .format(brother['name'], brother['age'], brother['address']))
      
name = 'prince'
age = 16
hobby = 'playing games'
address = 'katihar'
print('my name is {}, my age is {}, my hobby is {}, i live at {}'
      .format(name, age, hobby, address))
