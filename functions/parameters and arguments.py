"""#position argument

def student(name,age):
    print(name,"age is",age)
student(23,"ram")#wrong argument
student("ram",23)#correct argument
"""

"""#keyword argument

def student(name,age,marks):
    print(name,"age is",age,"marks are",marks)
student(marks=45,age=23,name="ram")
student(marks=65,age=23,name="sita")"""

"""#default arguments

def student(name,age=23,marks=45):#age and marks are default args
    print(name,"age is",age,"marks are",marks)
student("ram")
student("sita",36)"""
"""
#multiple arguments

def sai_values(*args):
    s=0
    for i in args:
        s=s+i
    print("sum of all numbers is", s)
sai_values(1,2,3,4)"""


"""#return

def sai(*args):
    return args
print(sai(1,2,3,4))"""







