''' class Hello: # create a class
    a = 10
    b = 20
    def display(): # User Defined Function
        print("Display Function")
        print("APSSDC_Django Workshop")

Hello.display() # Calling function
print(Hello.a)
print(Hello.b)
'''
'''
class Math:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b

# create object for class Math
mt = Math
print("Add is :",mt.add(10,20))
print("Sub is :",mt.sub(50,25))
print("Mul is :",mt.mul(10,10))

print(Math.add(10,10),Math.sub(10,5),Math.mul(10,10))
print(Math.sub(10,5))
print(Math.mul(10,10))
'''
'''
class Apssdc:
    def f1():
        f = ['Python','Java','PHP']
        return f
    def app():
        a = ['Web Development','MAchine Learning','AI']
        return a
obj = Apssdc
    
print(obj.f1())
print(obj.app())
'''

class MathOpertations:
    a,b,c = 10,20,30
    def sumNum():
        return MathOpertations.a + MathOpertations.b + MathOpertations.c
    def multify():
        return MathOpertations.a * MathOpertations.b * MathOpertations.c

sm = MathOpertations
        















