"""
class emp:

    def __init__(self, id, nm, add, age, sal ):
        self.empid=id
        self.empnm=nm
        self.empadd=add
        self.empage=age
        self.sal=sal


    def __hash__(self):
        return self.empadd.__hash__()+self.empid

    def __eq__(self, other):
        return self.empid==other.empid and self.empadd==other.empadd


e1=emp(id=1, nm="pqr", add="pune", age=34, sal=655667)

class Emp:

    def __init__(self,id,nm,age,address,salary):
        self.empId=id
        self.empName=nm
        self.empAge=age
        self.empAddress=address
        self.empSalary=salary

    def __hash__(self):
        return  self.empAddress.__hash__()+self.empId

    def __eq__(self, other):
        return self.empId==other.empId and self.empAddress==other.empAddress

e1= Emp(id=10,nm="AAAA",age=20,address="Pune",salary=1023.3)
"""
dict=[10,20,12,23,'A','B',50]
print('List Iterations...')
for item in dict:
    print(item)

dict =(10,20,12,23,'A','B',50)
print('tuple iterations...')
for item in dict:
    print(item)

dict ={10,20,12,23,'A','B',50}
print('set iterations...')
for item in dict:
    print(item)

dict = {1:'One',
        2:'Two',
        3:'Three'}
print('dict iterations...')
for item in dict: #bydefault print keys
    print(item)
for item in dict.keys(): #key will print
    print(item)
for item in dict.values(): #values will print
    print(item)
for item in dict.items():
    print(item)
d1=dict.copy()
print(d1)

