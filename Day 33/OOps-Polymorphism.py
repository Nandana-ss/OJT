# Polymorphism 
# Poly means 'many' and Morphism means 'forms'. In Polymorphism, the functions are of the same name but their functionalities are different

class Jasmine():
    def color(self):
        print("Jasmine flower comes in white, pink, blue, orange, yellow, purple, and red color")
    
    def scientific_name(self):
        print("Jasminum sambac is the scientific name of Jasmine")
    
    def family(self):
        print("Jasmine is from the Oleaceae family")

class Lily():
    def color(self):
        print("Lilies commonly grow in white, yellow, pink, red, and orange color.")
    
    def scientific_name(self):
        print("Lilium is the scientific name of Lily")
    
    def family(self):
        print("Lily is from the Liliaceae family")

obj_jasmine = Jasmine()
obj_lily = Lily()

for flower in (obj_jasmine, obj_lily):
    flower.color()
    flower.scientific_name()
    flower.family()

