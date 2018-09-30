fruit = ['mango', 'orange', 'apple', 'banana', 'palm', 'guava']
print(fruit)

#using sort() method
fruit.sort()
print(fruit)

#using reverse() method
fruit.reverse()
print(fruit)

#using del keyword
del fruit[3] # this work only on index or slice
print(fruit)

#using remove() method
fruit.remove('palm')    #this works on elements
print(fruit)

#using pop() method
fruit.pop(2)    #this removes using index
print(fruit)

#using clear() method
fruit.clear()
print(fruit)

name = ['anjali', 'prince', 'anku', 'anjali', 'prince', 'anku']
#using count() method
print(name.count('anjali'))