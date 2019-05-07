#!/usr/bin/env python

class Animal(object): 
    _COUNT = 0 

    def __init__(self, species, name, sound): 
        self._species = species 
        self._name = name 
        self._sound = sound 
        Animal._COUNT += 1 

    def kill(self): 
        Animal._COUNT -= 1 

    @property 
    def species(self):
        return self._species 
    
    @property 
    def name(self):
        return self._name 

    @property
    def sound(self):
        return self._sound

    @property
    def id(self):
        return "I am the {0}, hear me {1}".format(self.species, self.sound)

    def make_sound(self):
        print(self.sound)

    @classmethod
    def get_zoo_size(cls):
        return cls._COUNT 

if __name__ == "__main__": 
    leo = Animal("African lion", "Leo", "Roarrrrrrr") 
    garfield = Animal("house cat", "Garfield", "Meowwwww") 
    felix = Animal("cartoon cat", "Felix", "Meowwwww") 

    print(leo.name, "is a", leo.species, "--", end=' ')
    leo.make_sound()

    print(garfield.name, "is a", garfield.species, "--", end=' ')
    garfield.make_sound()

    print(felix.name, "is a", felix.species, "--", end=' ')
    felix.make_sound()

    print("Zoo size is:", Animal.get_zoo_size())
    leo.kill()  # :-(
    print("Zoo size is:", Animal.get_zoo_size())
