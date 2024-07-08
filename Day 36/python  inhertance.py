class father: 
 def father_name(self):
    print("My father name is Vijayan")

class son(father): 
 pass

obj_father= father() 
obj_son=son() 
obj_son.father_name() 
# Multilevel inheritance


class g_father:
    def g_father_name(self):
        print("my father name is Vijayan")

class father(g_father):
 def father_name(self):
    print("my Mother name is Ansy")

class son(father):
 def son_name(self):
    print("my name is Devika")


 obj_g_father= father() 
 obj_father= father()
obj_son=son()

obj_son.g_father_name() 
obj_son.father_name()
# Multiple Inheritance
class father: # parent class
  def father_name(self):
    print("my father name is selvaraj")

class mother: # parent class
  def mother_name(self):
    print("my father name is vijayan")

class son(mother,father): # child class
  pass

obj_father= father() 
obj_mother=mother() 
obj_son=son() 

obj_son.father_name() 
obj_son.mother_name() 

# obj_mother.father_name() # This statement did not work because mother and father are parents. Output 