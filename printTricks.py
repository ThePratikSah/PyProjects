#   program for printing variables using {}.

name = 'prince'
age = 16
hobby = 'playing'
address = 'katihar'
print('my name is {}, my age is {}, my hobby is {} and i am from {}'
      .format(name, age, hobby, address))

brother = {'name': 'prince', 'age': 16, 'hobby': 'playing', 'address': 'katihar'}
print(brother['name'])
print('my name is {}, my age is {}, my hobby is {} and i am from {}'
      .format(brother['name'], brother['age'], brother['hobby'], brother['address']))
