#!/usr/bin/env python3

from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

# Class Method
Pet.create_table()

pet1 = Pet.create("spot", "dog", "chihuahua", "feisty")
pet2 = Pet.create("rover", "dog", "boxer", "chill")
# spot2 = Pet("spot", "dog", "chihuahua", "feisty")

# Instance Method
# spot1.save()
# spot2.save()

# spot1.update("bud")


import ipdb; ipdb.set_trace()
