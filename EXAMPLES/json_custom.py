#!/usr/bin/env python
# (c)2015 John Strickler
import json

class Bird(object):
    def __init__(self, origin, color):
        self._origin = origin
        self._color = color

    @property
    def origin(self): return self._origin

    @property
    def color(self): return self._color

birds = {
    'Jim': Bird('Norwegian', 'Blue'),
    'Emily': Bird('Patagonian', 'Purple')
}

class BirdEncoder(json.JSONEncoder):
    def default(self, obj):  # must be called 'default'
        if isinstance(obj, Bird):
            return {'origin': obj.origin, 'color': obj.color}

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

encoded_birds = json.dumps(birds, cls=BirdEncoder)

print(encoded_birds)
