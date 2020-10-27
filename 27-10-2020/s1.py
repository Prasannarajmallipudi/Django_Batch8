'''class New:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation

obj = New('Prasanna Raj','Multi Skill Tranier')


class Abc:
    def __newfun__(self):
        print("Welcome New Function")
ob = Abc()
ob.__newfun__()
'''
# Multiple Inheritances

class P1:
    def G1(self):
        print("Parent1 Method")
class P2:
    def G2(self):
        print("Parent2 Method")

class C(P1,P2):
    def G3(self):
        print("Child Method")

obj = C()
obj.G1()
obj.G2()
obj.G3()

    















