# QUESTION 3

# Write a class that has the following methods:
# add_person(person)  if the person has the same social insurance number as someone who was already added, do not add the person and return false, otherwise add the person and return true
# count_with_shoe_size(shoe_size)  returns the number of persons with the requested shoe size
# Do NOT write the class Person. Assume it has reasonable attributes for name, social insurance number, and shoe size.


# class Person(object):
    
#     def __init__(self, name, socIns, shoeSize):
#         self.name = name
#         self.socIns = socIns
#         self.shoeSize = shoeSize
#         self.__stations = list()
    
#     def __iter__(self):
#         return iter(self.__stations)
    
    # checks to see if social insurance number exists and returns false, or add person if it does not exist
    def add_person(self, name, socIns):
        if self.socIns == socIns:
            return False
        else:
            self.name = name
            self.socIns = socIns
            return True
        
    # returns number of persons with requested shoe size
    def count_with_shoe_size(self, shoe_size):
        for shoeSize in self:
            print self.count(shoe_size)
