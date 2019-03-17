'''
def method():
    print('inside method')
print('outside method')

class Student:
    def m1(self):
        for item in range(1, 10):
            print(item)
print('hello')
'''

print('.....................................................................................................................')

"""
class Student:

    studCount =0  #variable

    def __init__(self, id, nm):#method..if methods name is __init__-- nothing but contructor
        self.studId = id  #variables
        self.studName = nm#variables

    def __str__(self): # method
        return '{}{}'.format(self.studId,self.studName)

    def __repr__(self):# method
        return str(self)


def showinformation():#function
    num = 10  #variable
    print('inside show information')# stmt inside function...
print('outside show information')
"""
print('.....................................................................................................................')
'''
var1 = 10  #globle variables - variables declared/initiazed at module/file level
# everywhere in an application -- bydefault variable scope if public in python

def newFunction():
    var2=20   #local variable -- variable which we write inside method/function/constructor


class Student:
    var3=30  #classLevel -- var which we declare of initlize at class level --
        # as long as class # static variable

    def __init__(self,id,nm): #id,nm -- local variables..
        self.studId=id
        self.studName=nm
        #self -- this -- current object cha ref
        # instance variables-- as long as object is there
    def newMethod(self):
        self.studAddress = "Pune"  #instance...

'''
print('.....................................................................................................................')

# ref thru set -- first check inside object -- if found-- modify if not found..add new fields but only inside that object..
#clssname thru set -- first check inside class-- if found-- modify -- if not fount...simple add karega...in class level-- will be avaible for all objects..
#ref thru get//access -- first check inside that ref..if found..retrive..if not found..check at class level...if found..retrive..if not found..error
#cls thru get/access - check at class level...if found..retrive..if not found..error




class Student:
    collegeName = "PICT"

    def __init__(self, id, name, age):
        self.studId = id
        self.studName = name
        self.studAge = age


s1 = Student(10, "AAA", 25)
s2 = Student(11, "BBB", 26)
s3 = Student(12, "CCC", 27)

print(s1.studId)  # 10
print(s1.studName)  # AAA
print(s1.studAge)  # 25
print(s1.collegeName)  # PICT

s1.studName = "ABABAB"
Student.collegeName = "COEP"

print('s1Name :', s1.studName, s1.collegeName)#ABABAB,COEP
print('s2Name :', s2.studName, s2.collegeName)#BBB,COEP

print(s1.__dict__)#10,ABABAB,25
print(s2.__dict__)#11,BBB,26

print('.......................................NEW CODE.............................................................................')

'''
class Student:
    collegeName = "PICT"

    def __init__(self, id, name, age):
        self.studId = id
        self.studName = name
        self.studAge = age
        glblvar = 20

    def newMethod(self):
        self.studAdderss = "Pune"
        Student.CollegeId = 10212
        #print(glblvar)


s1 = Student(10, "AAA", 25)
s2 = Student(11, "BBB", 26)
#print(glblvar) #20
s1.collegeName = "AAAA"
s1.collegeName = "BBBB"

s2.newMethod()
s2.collegeName = "ppp"
s2.newMethod()

print(Student.__dict__)  # 2  collenm,clgid
print(s1.__dict__)  # 4 id nm age clgnm
print(s2.__dict__)  # 4 -- id nm age addrs
'''

glblvar = 10


def newFunction():
    global glblvar
    glblvar = 20
    print('inside function ', glblvar)  # 20


print('outside function ', glblvar)  # 10
newFunction()

print('....................................................NEW CODE................................................................')

"""
print('inside empinfo module...')


class Employee:

    empCount = 0

    def __init__(self,eid,enm,esal,eage,edept):
        print(self.__hash__())
        self.empName=enm
        self.empAge=eage
        self.empId=eid
        self.empSalary=esal
        self.empDept=edept
        self.ecount=3
        Employee.empCount+=2

emp1 = Employee(10,"AAAA",220392.2,33,'Comp')
emp2 = Employee(11,"BBAA",320392.2,31,'IT')
emp3 = Employee(11,"BBAA",320392.2,31,'IT')


print(emp1.__dict__)#10,AAAA,220,33,Co2,3
print(emp2.__dict__)#11,BBAA,320,33,Co3,3
print(emp3.__dict__)
print(Employee.__dict__)#empcount2
Employee.emppcount=200


print(emp1.emppcount)#200
print(emp2.emppcount)#200
print(Employee.emppcount)#200

emp1.newCount=10
emp2.newCount=20
emp1.newccount=30
emp1.empCount=300

print(emp1.empCount)#300
print(emp2.empCount)#200
print(Employee.empCount)#2 ->6

print(emp1.__dict__)#10,AAAA,220,33,Co2,3
print(emp2.__dict__)#11,BBAA,320,33,Co3,3
print(Employee.__dict__)
"""
print('....................................................NEW CODE not getting..please clear the doubts................................................................')
"""
print('inside empinfo module...')


class Employee:
    empCount = 0
    companyName = "Infy"

    def __init__(self, eid, enm, esal):
        self.empName = enm
        self.empId = eid
        self.empSalary = esal
        Employee.empCount += 1

    def displayEmpInformation(self):
        print('---------------------------------------------')
        print('EmpId : ', self.empId)
        print('EmpName : ', self.empName)
        print('EmpSalary : ', self.empSalary)
        print('EmpCount : ', self.empCount)

    @staticmethod
    def showEmpInformation():
        print('inside show info..')
        print('---------------------------------------------')
        print(Employee.empCount)

    @classmethod
    def printEmpInformation(cls):
        print('EmpCount : ', cls.empCount)


emp1 = Employee(10, "AAAA", 220392.2)  # 1
emp2 = Employee(11, "BBAA", 320392.2)  # 2
emp3 = Employee(11, "BBAA", 320392.2)  # 3
print(emp1.__dict__)  # 3
print(emp2.__dict__)  # 3
print(Employee.__dict__)  # 3

emp1.ecnt = 20

Employee.empCount = emp1.ecnt + Employee.empCount  # ec -- 20+3
# empcount-- 23 -- enct--20 --

emp1.printEmpInformation()  # 23+10 -- 33

emp2.printEmpInformation()  ##33 --23

emp2 = Employee(11, "BBAA", 320392.2)  # 24 --- empid-34

Employee.printEmpInformation()  # ecount--34 eid 44 -ecnt-20

print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)  # 4,14
"""
print('....................................................not getting..please clear the doubts................................................................')
"""
class Employee:

    empcount=10

    def __init__(self):
        print('inside constructor...')
        self.empName = "A"

    def displayEmpInformation(self):
        print('inside instance method')
        print(self.empcount)#static field access
        print(Employee.empcount) #static field access
        print(self.empName) #access instance field

        self.empName="B"#instane field set
        Employee.empcount=20 #static fields set



    @staticmethod
    def showEmpInformation():
        print('inside static method')
        Employee.empcount=10
        print(Employee.empcount)

    @classmethod
    def printEmpInformation(cls):
        print('inside class method')
        Employee.empcount = 10
        print(Employee.empcount)



emp1 = Employee()
Employee.printEmpInformation()
emp1.printEmpInformation()
"""
print('....................................................not getting..please clear the doubts................................................................')
