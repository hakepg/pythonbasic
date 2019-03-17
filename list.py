"""
n=[0,1,2,3,4,5,6,7,8,9,10]

print('display element using while loop')
i=2
while (i<len(n)):
    print(n[i])
    i=i+2


print('display element using for loop')
for n1 in n:"
    print(n1)
print('\n')


print('display element by even no')
for n1 in n:
    if n1%2==0:
        print(n1)


print('display element by index wise')

list=[10,12,13,20,15]
x=len(list)
for i in range(x):
    print(list[i], "is available at +ve index:",i,"and at -Ve index:", i-x)

"""
#listOfElements = [10,30,25,2,2,2,'D',200,200]

"""
for item in range(2,5):
    print(item)

for item in range(5):
    print(item)

cont=print(listOfElements.count(2))

for item in range(listOfElements.count(2)):
    listOfElements.remove(2)
print(listOfElements)

for value in range(len(listOfElements)):
    listOfElements.pop(value)


listOfElements.append([1,2,3])
print(len(listOfElements))
print(listOfElements)

listOfElements.extend([1,2,3,4])
print(len(listOfElements))
print(listOfElements)
print(listOfElements.remove(200))

print(listOfElements.pop(3))

print(listOfElements)
newlist = listOfElements[3::-5]
print('newlist:', newlist)

print('asc order')
for item in listOfElements:
    print(item)

print('desc order')
for item in listOfElements[::-1]:
    print(item)

listOfElements.append(400)
print(listOfElements)

listOfElements.insert(len(listOfElements),400)
print(listOfElements)
print(listOfElements.pop(-4))
print('append', listOfElements)

listOfElements.insert(10,100)
print(listOfElements)
print(listOfElements[2])

print(listOfElements.__len__())
print(len(listOfElements))

for item in listOfElements:
    print(item,':')

print('\n................................................\n')

for item in listOfElements[::-1]:
    print(item)

print(listOfElements[6])

#

listOfElements=[[13,16,45,96,"a"], [10,"A",1,2], ["B", "C", 20, 6, 8], ["A", 20,30], [33, 22, "A"]]
print(listOfElements)


"""
print('..............using sorted list code not understand review again.........................')
"""

listOfElements = [10,20,30,45,1,5,23,223,44552,34,53,2,"A"]
def customFunction(innerlist):
    return innerlist[4]
print(listOfElements.sort(key=customFunction,reverse=True))
print(listOfElements.sort(key=lambda x:x[3]))
listOfNumbers={item:"v"+str(item) for item in range(100)}

listOfNumbers=[]
for item in range(100):
    listOfNumbers.append(item)

print(listOfElements)

print(listOfElements.sort(reverse=True)
#print(listOfElements)
print(sorted(listOfElements))
print(listOfElements)
"""

class Emp:

    def __init__(self, id, nm, age, sal, addr):
        self.empId = id
        self.empName = nm
        self.empAge = age
        self.empSalary = sal
        self.empAddres = addr

    def __str__(self):
        return '\n Id {}, Name :{}, Age : {}, Salary : {}, Address : {}'. format(self.empId, self.empName, self.empAge, self.empSalary, self.empAddres)

    def __repr__(self):
        return str(self)

e1 = Emp(id=1, nm='ppp', age= 34, sal=17000, addr='pune')
e2 = Emp(id=2, nm='gdih', age=23, sal=54000, addr='pusad')
e3 = Emp(id=3, nm='khhj', age=35, sal=45000, addr='mumbai')
e4 = Emp(id=4, nm='rtat', age=31, sal=32000, addr='sangli')
listOfEmp = [e1,e2,e3,e4]
print(listOfEmp)
#print(e1)
def mySortLogic(empOb):
    return empOb.empAddress

#listOfEmp.sort(key=mySortLogic, reverse=True)
listOfEmp.sort(key=lambda emp:emp.empId,reverse=True)
print(listOfEmp)


listOfElements = [[10,2,20,30,20,20,40,50,12],10,20,30,[10,20,30,40,50,50],20]

count= 0

for item in listOfElements:
    if type(item)==list:
        count+=item.count(20)

count+=listOfElements.count(20)

print(count)


class Emp:

    def __init__(self,id,nm,age,sal,addr):
        self.empId = id
        self.empName=nm
        self.empAge=age
        self.empSalary=sal
        self.empAddress=addr

    def __str__(self):
        return '\n Id {}, Name : {}, Age : {} , Salary : {}, Address : {}'.format(self.empId,self.empName,self.empAge,self.empSalary,self.empAddress)

    def __repr__(self):
        return str(self)


e1 = Emp(id=11,nm="AabnsadaA",age=43,sal=413391.3,addr="Pune")
e2 = Emp(addr="acgrPune",nm="ZAsnsadaA",age=33,sal=35391.3,id=73)
e3 = Emp(id=41,nm="wrbnsadaA",age=43,sal=13391.3,addr="Pune")
e4 = Emp(addr="gsAPune",nm="ZAsnsadaA",age=33,sal=39391.3,id=63)
e5 = Emp(id=13,nm="gsdabnsadaA",age=43,sal=553391.3,addr="Pune")
e6 = Emp(addr="dsAPune",nm="ZAsnsadaA",age=33,sal=69391.3,id=53)

listOfEmps = [e1,e2,e3,e4,e5,e6]


print(e1)
print(listOfEmps)

def mySortLogic(empOb):
    return empOb.empName


#listOfEmps.sort(key=mySortLogic,reverse=True)
listOfEmps.sort(key=lambda emp:emp.empId,reverse=True)
#listOfEmps.sort(key=mySortLogic,reverse=True)
print(listOfEmps)



