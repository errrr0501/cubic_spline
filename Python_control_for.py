rabbits = ['A', 'B', 'C', 'D']
current = 0

#It works, but...
while current < len(rabbits):    #while 0<4
    print(rabbits[current])      #printf rabbit
    current += 1                 # current = 0+1 and than loop 

#This is better
for rabbit in rabbits:          #assign rabbit in rabbits
    print(rabbit)               #print it

word = 'cat'              #print the letter in word 
for letter in word:
    print(letter)      

#--------------------------------------------------
dict_A = {'John': 17, 'Sam': '20', 'Tom':'30'}
for name in dict_A:     #just print the thing in front :
    print(name)
for age in dict_A.values(): #just print the thing after :
    print(age)
for pair in dict_A.items(): #print one pair(one pair is (:))
    print(pair)
for name, age in dict_A.items():
    print(name, 'is', age, 'years old')





#----------------------------------------------------
cheeses = []

for cheese in cheeses:
    print('This shop has some lovely,', cheese)
    break  #cheese is empty so break
else:
    print('This is not much of a cheese shop, is it?') #print this line

cheeses = []
found_one = False
for cheese in cheeses:
    found_one = True
    print('This shop has some lovely,', cheese)
    break #cheese is empty so break
if not found_one:
    print('This is not much of a cheese shop, is it?') #print this line






#------------------------------------------------------------
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
deserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

print(type(list(zip(days, fruits, drinks, deserts))))

for day, fruit, drink, desert in zip(days, fruits, drinks, deserts):
    print("{} drink {}, eat {}, enioy {}.".format(day, drink, fruit, desert))#大括號對應format





#--------------------------------------------------
# for i in range(10):
#    print(i)

# for i in range(1, 5, 2):
#     print(i)

for i in range(2, 0, -1): #2 to 0 count back 
    print(i)     #print it 