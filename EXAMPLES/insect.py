
from  animal import Animal

class Insect(Animal):
    '''
        An animal with 2 sets of wings and 3 pairs of legs
    '''
    def __init__(self, species, name, sound, can_fly=True):
        super().__init__(species, name, sound)
        self._can_fly = can_fly

    @property
    def can_fly(self):
        return self._can_fly

if __name__ == '__main__':
    mon = Insect('monarch butterfly', 'Mary', None)
    scar = Insect('scarab beetle', 'Rupert', 'Bzzz', False)

    for insect in mon, scar:
        flying_status = 'can' if insect.can_fly else "can't"
        print("Hi! I am {0} the {1} and I {2} fly!".format(
                insect.name, insect.species, flying_status
            ),
        )
        insect.make_sound()
        print()
