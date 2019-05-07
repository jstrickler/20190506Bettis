#!/usr/bin/env python

from  animal import Animal 

class Mammal(Animal): 
    ''' 
        An animal that gives birth to live offspring 
        (as opposed to laying eggs). 
    ''' 
    def __init__(self, species, name, sound, gestation): 
        Animal.__init__(self, species, name, sound) 
        self._gestation = gestation 

    @property 
    def gestation_period(self):
        """Length of gestation period in days""" 
        return self._gestation 

if __name__ == "__main__": 
    m1 = Mammal("African lion", "Bob","Roarrrr",120)
    print(m1.name, "is a", m1.species, "--", end=' ')
    m1.make_sound()

    print("Number of animals", m1.get_zoo_size())

    m2 = Mammal("Fruit bat", "Freddie", "Squeak!!", 180)
    print(m2.name, "is a", m2.species, "--",end=' ')
    m2.make_sound()

    print("Number of animals", m2.get_zoo_size())
    print("Number of animals", Mammal.get_zoo_size())

    m1.kill() 
    print("Number of animals", Mammal.get_zoo_size())

    print("Gestation period of the", m1.species,"is",m1.gestation_period,"days")
    print("Gestation period of the", m2.species,"is",m2.gestation_period,"days")
