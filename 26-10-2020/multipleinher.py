class ClassA:
    def g1():
        return 'Class A'
class ClassB:
    def g2():
        return 'Class B'

class ClassC(ClassA,ClassB):
    def g3():
        return 'ClassA','ClassB'
        return 'ClassC'
        

a = ClassA
b = ClassB
c = ClassC

print(a.g1())
print(b.g2())
print(c.g3())
    
