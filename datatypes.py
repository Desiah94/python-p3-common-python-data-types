# you can define strings using single quotes or double quotes
"I'm a string"
'Me too!'

#built inn str() constructor
str("I'm a string")

# String Interpolation- embedding a varible in a string
dog_name = "Lucy"
print(f"Say hello to my dog {dog_name}")

name_greeting = "Desiah"
greeting_word = " Wassup"
print(f"{greeting_word} my name is {name_greeting}")

# display all prices with two decimal places:
price_1 = 3
price_2 = 2.5

print(f"Item 1 costs ${price_1:.2f}")
# => Item 1 costs $3.00
print(f"Item 2 costs ${price_2:.2f}")
# => Item 2 costs $2.50

# open shell type python
"hello"
# "hello"
"hello".upper()
# "HELLO"
"HELLO".lower()
# "hello"
"hello".capitalize()
# "Hello"
"hello" + "world"
# "helloworld"
"hello" * 3
# "hellohellohello"
 

# "hello" is a string literal becomes a instance of string class
type("hello")
# => <class 'str'>

# Use dir() function on python object will display a list of all 
# the methods that available. 
dir("hello")
# => ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ... ]

# if it has a double underscore- magic/dunder method


#INT(INTEGERS) AND FLOATS
# Integers are whole numbers, like 7.
# Floats are decimal numbers, like 7.3.

# Use Int() and float() constructor to covert to these data types
int("1")
# => 1
int(1.1)
# => 1
float("1.1")
# => 1.1


#Sequence Types- Used to store data- rules change to orgganize and access data

# LIST uses square brackets
# run python shell type python 
[1, 2, 3, 4, 5]
list()
# run python shell type python 
# list_abc = ['a','b','c']
#list_abc[0]
# => 'a'
#list_abc[1]
# => 'b'
#list_abc[2]
# => 'c'

#TUPLES use parenthesis 
# Tuples use a ()-immutable means tuple will never change
# methods to create new data only like .pop() or .inser()
(1, 2, 3)
# => (1, 2, 3)
tuple([1, 2, 3])
# => (1, 2, 3)

# SETS-unindexed , unordered and unchangeable
# set() constructor or curly brackets
#takes in the list or tuple as an argument using ([])
# it renders no duplicates 
set([1, 2, 4, 2, 4])
# {1, 2, 4}


#DICTIONARIES KEY/VALUE PAIRS OLD JAVASCRIPT OBJECT
#each key points to a specific value
#write in curly brackers
{ "key1": "value1", "key2": "value2"}
# access use square bracket notation and pass in the symbol for the key access is need
my_dict = { "key1": 1, "key2": 2 }
my_dict["key2"]
# => 2


#.get() method used to see if a key exist will return none if so
my_dict = { "key1": "value1", "key2": "value2" }
#print(my_dict["key3"])
# => KeyError: 'key3'

print(my_dict.get("key3"))
# => None


# dict() class constructor.
dict(x = 1, y = 2)
# => {'x': 1, 'y': 2}

#NONE-ABSENCE OF A VALUE
#no_value
# => NameError: name 'no_value' is not defined

no_value = None
print(no_value)
# => None

#Booleans
#There are only two values of the Boolean data type: True and False
not True
# => False
not False
# => True
not 1
# => False
not 0
# => True
not ''
# => True
not None
# => True
not []
# => True
not ()
# => True
not {}
# => True

