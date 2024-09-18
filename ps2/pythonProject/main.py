# key1=(1,2)
# key2=(3,4)
# key3=(5,6)
# dist={
#     key1:   key1[0]+key1[1],
#     key2:   key2[0]+key2[1],
#     key3:   key3[0]+key3[1]
# }
# # print(dist)
# for x,y in dist.items():
#     print(x,y)
# +----------------------------------------+

# Question 2

# num=(1,2,2,3,3,3,4,4,4,4)
#
# dist={}
#
# for x in num:
#     if x in dist:
#         dist[x]+=1
#     else:
#         dist[x]=1
#
# print(dist)
# for a,b in dist.items():
#     print(f"{a} : {b}")

# question#3

# dist={
#         'name' :'Alice',
#         'age'  :'30',
#         'city' : 'newyork'
#      }
# print(dist['city'])

# question#4

# dist={
#
#     'name':'bob',
#     'age':'25'
# }
#
# dist['age']=26
# print(dist.values())

# question#5

# people=[('john',25),('jane',30),('Alice',25),('Bob',30)]
#
# dist1={
#
# }
# for m,n in people:
#     if n not in dist1:
#         dist1[n]=[]
#
#     dist1[n].append(m)
#
# # print(dist1.items())
# for x,y in dist1.items():
#     print(x,':',y)


# question#6
#
# dist1={ 'a'=10 ,'b'=20  }
# dist2={ 'a'=30 ,'b'=40  }
# dist3={}


# day2
# lamda start
# people = [("John", 25), ("Anna", 22), ("Mike", 30), ("Sophia", 27)]
#
#     sorted_people = sorted(people, key=lambda x: x[1])
#
# print(sorted_people)

# # 2nd
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#
# print(even_numbers)
#
# # 3rd
#
# numbers = [1, 2, 3, 4, 5]
#
# squared_numbers = list(map(lambda x: x**2, numbers))
#
# print(squared_numbers)

#  lamda end

# oop
# 1st
# class Rectangle():
#     def __init__(self,width,height):
#         self.wid=width
#         self.hei=height
#         print(self.wid * self.hei)
# a1=Rectangle(5,6)
# print(a1)

# 2nd


# class Bank:
#     def __init__(self, name):
#         self.name = name
#         self.accounts = []
#
#     def add_account(self, account):
#         self.accounts.append(account)
#
#     def remove_account(self, account):
#
#         self.accounts.remove(account)

# 3rd
#
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.engine_started = False
#
#     def start_engine(self):
#
#         self.engine_started = True
#         print("Engine started.")
#
#     def stop_engine(self):
#         self.engine_started = False
#         print("Engine stopped.")

# 4th
#
#    class ShoppingCart:
#        def __init__(self):
#            self.items = []
#            self.total_price = 0
#
#        def add_item(self, item, price):
#            self.items.append(item)
#            self.total_price += price
#            print(f"Added {item} to the cart.")
#
#        def remove_item(self, item):
#            if item in self.items:
#                self.items.remove(item)
#
#                self.total_price -=[]
#                print(f"Removed {item} from the cart.")
#            else:
#                print(f"{item} not found in the cart.")
#
#        def checkout(self):
#            return self.total_price

# practice
#
# f = open("demofile.txt", 'w')
# f.write("hello world")
# f.close()
# f = open("demofile.txt", 'r')
# x=f.read()
# a = len(x.split())
# print(a)
#
#


#2nd



# f = open("source.txt","w")
# f.write("bootcamp #1")
# f.close()
# f = open("source.txt","r")
# x = f.read()
# r = open("destination.txt","w")
# r.write(x)
# r.close()
# r=open("destination.txt","r")
# w = r.read()
# print(w)

#3rd

# f = open("noted.txt","w")
# f.write("A maiden fair with tresses of old wandered through a verdant glade."
#         " The dappled sunlight filtered through old of the canopy, casting ethereal shadows upon her old visage."
#         " With a heart filled with longing, she sought solace in old nature's embrace")
# f.close()
# f = open("noted.txt","r")
# q = f.read()
# f.close()
# w = open("updated.txt","w")
# w.write(q.replace("old", "new"))
# w.close()
# w = open("updated.txt","r")
# e = w.read()
# w.close()
# print(e)
#
#
#4rth

# f = open("poem.txt","w")
# f.write("A maiden fair with tresses of old wandered through a verdant glade."
#         " The dappled sunlight filtered through old of the canopy, casting ethereal shadows upon her old visage."
#         " With a heart filled with longing, she sought solace in old nature's embrac")
# f.close()
# f = open("poem.txt","r")
# q = f.read()
# f.close()
# w = open("poem.txt","r")
# w.read()
#
# w = open("reversed.txt","w")


#exception handling

# def safe_division(numbers):
#   constant = 100
#
#   for num in numbers:
#     try:
#       result = constant / num
#       print(f"{constant}/{num}={result}")
#     except ZeroDivisionError:
#       print(f"Cannot divide by zero. Skipping value: {num}")
#     except (ValueError, TypeError):
#       print(f"Invalid type: {num}. It must be a number.")
#
#
# my_list = [25, 0, 'a', 5, 2.5, None]
# safe_division(my_list)
#

# 2darray

# ar = []
# row=2
# colm=2
# ar = [row][colm]
# for r in range(2):
#         for c in range(2):
#                ar[r][c] = input('enter value=')
#
# print(ar[2][2])

#decorators

# def even_numbers(n):
#     num = 0
#     while num <= n:
#         yield num
#         num += 2
#
# m = even_numbers(10)
# for num in m:
#     print(num)


#2nd

# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# m = fibonacci(5)
# for num in m:
#     print(num)

#3rd

def read_large_file(filename):

f = open("larefile.txt","w")
f.write("A maiden fair with tresses of old wandered through a verdant glade."
         " The dappled sunlight filtered through old of the canopy, casting ethereal shadows upon her old visage."
        " With a heart filled with longing, she sought solace in old nature's embrac")
f.close()

f = open("larefile.txt","r")
w = f.read()
f.close()

