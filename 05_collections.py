# collections make processing multiple elements easy
# the manual refers to arrays - this is a Java/JavaScript term
# the most analogous term in Python is the list data structure
band = ["Patti", "Max", "Gary", "Soozie", "Stevie",
        "Nils", "Tom", "Clarence", "Jake", "Danny", "Roy"]

# lists are MUTABLE - not like single values eg string, number, boolean

# lists have an implicit length prop:
print(len(band))  # 11

# list members have an implicit index position in the list

print(band[0])  # Patti
# print(band[11]) # IndexError: list index out of range
# last element is index position length - 1

# re-assignment of list element - SETTER
band[4] = "Steven van Zandt"

print(band)

# removing element(s)
del band[7]

print(band)

#  finding position of elements
print(band.index("Nils"))

# removing elements by finding index first
del band[band.index("Tom")]

print(band)

# adding elements

# append to end
band.append("Alan")

print(band)

# inserting by index position
band.insert(5, "Tom Morello")

print(band)

# there also exists in Python a data structure called tuple
# it is ordered, like list, but immutable - cannot be changed

guitarists = ("Stevie", "Nils", "Tom")

# guitarists[1] = "Nils Lofgren" # TypeError: 'tuple' object does not support item assignment

# furthermore, dictionaries are unordered collections whose members are key: value pairs
band_members = {"vocals": "Bruce", "lead_guitar": "Nils", "drums": "Max"}
