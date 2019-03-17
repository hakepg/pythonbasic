
class Emp:
     def __init__(self,id,nm,age,sal,gen):
        self.empId=id
        self.empName=nm
        self.empAge=age
        self.empSalary=sal
        self.empGen=gen

     def __str__(self):
        return '\n Id: {}, Name: {}, Age: {}, Salary: {}, Gender: {}'.format(self.empId, self.empName, self.empAge, self.empSalary, self.empGen)
        
     def __repr__(self):
        return str(self)

     def __eq__(self, other):
        return self.empSalary==other.empSalary

     def __hash__(self):
        return self.empSalary.__hash__()


e1 = Emp(id=1, nm="A", age="24", sal=34567, gen="M")
e2 = Emp(id=2, nm="b", age="26", sal=54567, gen="M")
e3 = Emp(id=3, nm="ef", age="28", sal=374567, gen="F")
e4 = Emp(id=4, nm="fff", age="34", sal=67567, gen="M")
e5 = Emp(id=5, nm="hnk", age="29", sal=56567, gen="F")
e6 = Emp(id=6, nm="ncb", age="29", sal=34567, gen="M")
e7 = Emp(id=7, nm="kfb", age="23", sal=34567, gen="F")
#print(e1)

setOfEmps = {e1,e2,e3,e4,e5,e5,e6,e7}
print( setOfEmps)
print('\n')
emp = len(setOfEmps)
print("Total no. of Emp :", emp)


