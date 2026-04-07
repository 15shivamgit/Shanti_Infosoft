# def change(func):
#   def wrapper():
#     return func().upper()
#   return wrapper

# # @change
# def hello():
#   return "Hello"

# print(hello())
# a = change(hello)
# print(a())



# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Shivam"

# print(myfunction())


#! execution time calculate
import time
def timer(func):
  def wrapper(*args):
    start = time.time()
    func(*args)
    print(f"Time teken by {func.__name__}() : {time.time() - start} secs")
  return wrapper

@timer
def hello():
  print("Hii")
  time.sleep(2)

@timer
def square(a):
  time.sleep(4)
  print(a**2)

@timer
def power(a,b):
  print(a**b)


hello()
square(6)
power(5,3)