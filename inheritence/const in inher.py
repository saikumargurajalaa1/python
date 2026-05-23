#hybrid inheritance     #method resolution order


# class A:
#     def __init__(self):
#         print("hi")
# class B():
#     def __init__(self):
#         super().__init__()
#         print("world")
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("cop")
# class D(B,C):
#     def __init__(self):
#         super().__init__(),
#
#         print("chow")
# x=D()
# print(D.mro())

#hirarchial inheritance

# class C:
#     def __init__(self):
#         print("bye")
# class A(C):
#     def __init__(self):
#         super().__init__()
#         print("hi")
# class B(C):
#     def __init__(self):
#         super().__init__()
#         print("byeee")
# z=A()
# Z=B()

#multiple inheritance

# class A:
#     def __init__(self):
#         super().__init__()
#         print("chow")
# class B:
#     def __init__(self):
#
#         print("b")
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print("c")
# z=C()

#multilevel inheritance

# class A:
#     def __init__(self):
#         print("chow")
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("b")
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("c")
#
#
# z = C()
