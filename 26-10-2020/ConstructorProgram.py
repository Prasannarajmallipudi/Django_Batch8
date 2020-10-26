class Employee:
    ''' This Employee class Gives information
        of Employee name and Employee ID '''
    def __init__(self,name,empnumber):
        self.name = name
        self.empnumber = empnumber

    def show(self):
        return {'name':self.name,'empnumber':self.empnumber} #key:value

abc = Employee('Prasanna Raj',2422)
print(abc.show()) 
        
        
    
