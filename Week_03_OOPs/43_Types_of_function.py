
# =============  Types of function  ==============================================================================================================

# 1) Instance method
# 2) static method 
# 3) class method

# ---------------- 1) Instance method --------------------------------------------------------------------------------------------------------------------------------------
#  it should have at least one argument ,like min self , a,b ..

# class A :
#     def f1 ( self ):
#         #code
#         self.a = 5

# # obj1 = A()
# obj1.f1( ) # f1 ( obj1 ) -->> auto like __init__() method

# obj2 = A()
# obj2.f1( ) # f1 ( obj2 )

# obj1.f2(5 ,6 )  # f2 ( obj1 , 4 ,6 )

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# class A :
#     def f1 ( self ):
#         self.a = 5

# obj1 = A ()
# A.f1( obj1 )
# print ( obj1.a) # 5

# A.f1()      # Error
# A.f1( 6)    # Error 
# A.f1( obj1) # Correct

# It is called for instance related task 

# ------------ Static method ------------------------------------------------------------------------------------------------------------------------------------------
# class A :

#     @staticmethod
#     def f1 ( ):
#         print ( "Hello ")
    
    
#     @staticmethod
#     def f2 ( a , b ) : 
#         print ( a ,b)


# # staticmethod -->> its work for staticsmethod not for isinstance , and its not called auto for object 

# # A.f1()
# # A.f2(2,8)

# # Hello 
# # 2 8

# obj1 = A
# obj1.f1()
# obj1.f2 ( 10 , 20 )

# # Hello 
# # 10 20


# ------------ Class  method ------------------------------------------------------------------------------------------------------------------------------------------


# in  Class method mimimum one argument is to have it 

# class A :

#     @classmethod
#     def f1 ( cls ):
#         cls.x = 10

# A.f1()      # f1( A )
# obj1 = A()
# obj1.f1()
# print( A.x)


# ----------------------------------------------------------------------------------------------------------------------------------------------



class Car:
    def __init__(self, brand, speed):
        self.brand = brand        # Attribute
        self.speed = speed

    def accelerate(self):         # Method
        self.speed += 10


