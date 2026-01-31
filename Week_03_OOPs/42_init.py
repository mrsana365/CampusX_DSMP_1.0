
# =========== __init__() method ============================================
"""
1) you can define __init__() method in the class ( that is , it is optimal)
2) Similar to the concept of constructor in c++ or java
3) __init__() method invokes implicitly ( automatically ) everytimes 
   when an instance object is created.
4) Therefore , __init__() method is the first method runs for an object , 
   just after the object created
5) in c++ or Java constructor is created if not created but in python there not such thing

"""

# class Test (  ):
#     def __init__(self):
#         print ("helloo  init ")

# t1 = Test ( )

# helloo  init 


# -------  how to define init method  ---------------------------------------------------------------------------------------------------

# class Test :
#     def __init__( self ):
#         #code
#         #code

# 1) It is mandatory to take at least one positional argument in __init__() method
# 1) You can give any name to the first argument of __init__() method but "self" is recommended.
# 1) 
# 1) 
# 1) 
# 1) 

# ----------------------------------------------------------------------------------------------------------------------------------?

class Test :
    def __init__( self ):
        a = 5 # Local variable 
        self.a = 4  # instance object variable 

t1 = Test( )    # __init__( t1 )

# ----------  Job of __init__( ) ------------------------------------------------------------------------------------------------------------------------?

# Just because you are definging  __init__( ) method , you can write any code init But
# You should write code in __init__( ) which you want to run immediately after object creationn

# ideally you should initialize instance objecyt variable



class Test :
    def __init__( self , a, b ):    # a , b  formal argument ( Local Variable)
        self.a = a  #  self.a --> instance object variable , a --> Local variable
        self.b = b  


t1 = Test( )           # __init__( t1 ) this is wrong only taking one variable
t1 = Test( 10 ,20 )    # __init__( t1, 3 ,4 ) this is wrong only taking one variable

t2 = Test( 100 ,200 )  # __init__( t2, 3 ,4 ) this is wrong only taking one variable`





