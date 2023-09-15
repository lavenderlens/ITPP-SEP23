# an object is a container or wrapper data structure
# it may contain or wrap several parts
# object STATE - variables
# object BEHAVIOUR - functions, that usually work on one or more variables

# examples of object literals - not made with a class (actually a dictionary in Python)
alan_literal = {"name": "Alan", "Age": 56,
                "Instruments": ["trombone", "keyboards", "vox"]}
print(alan_literal)
tom_literal = {"first_name": "Tom", "last_name": "Morello",
               "Instruments": ["guitar"]}
print(tom_literal)

band_of_literals = []
band_of_literals.append(alan_literal)
band_of_literals.append(tom_literal)

# for member in band_of_literals:
#     print(f'{member.name} is {member.age} years old and plays {member.instruments}')
# AttributeError: 'dict' object has no attribute 'name'
# there is no enforced uniformity among literal objects (dictionaries)


class Musician:
    def __init__(self, name, age, instruments):
        self.name = name
        self.age = age
        self.instruments = instruments
    # def __init__(self):
        # set values later for no-args constructor
        # self.name = ""
        # self.age = 0
        # self.instruments = []

    def __str__(self):
        return f'Musician {self.name} is {self.age} years old and plays {self.instruments}'


# alan = Musician()
# alan.name = "Alan"
# alan.age = 21
# alan.instruments = ["trombone", "keyboards", "vox"]
# print(alan)  # <__main__.Musician object at 0x10253a5d0> - without dunder method str
# with str method defined in class: Musician Alan is 21 years old and plays ['trombone', 'keyboards', 'vox']
# TypeError: Musician.__init__() missing 3 required positional arguments: 'name', 'age', and 'instruments'

alan = Musician("Alan", 56, ["trombone", "keyboards", "vox"])
tom = Musician("Tom", 61, ["guitar"])
soozie = Musician("Soozie", 56, ["violin", "guitar", "backing vox"])

band = []
band.append(alan)
band.append(tom)
band.append(soozie)

for member in band:
    # print(member.name)
    # print(member.age)
    # print(member.instruments)
    print(member)

# objects are by default mutable whereas single values are not
