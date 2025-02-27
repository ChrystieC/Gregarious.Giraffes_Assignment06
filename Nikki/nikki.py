# File Name : nikki.py
# Student Name: Nikki Carfora
# email:  carfornc@mail.uc.edu
# Assignment Number: Assignment 06 
# Due Date:   2/27/25
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We are modeling the UC campus through different objects/buildings/aspects of the campus in different classes. 

# Brief Description of what this module does. This module creates a class "Crosley" that models Crosley tower's height and then destroys it. 
# Citations: N/A

# Anything else that's relevant: N/A


class Building(object):
    """
    Model a building on campus to be knocked down. Give it at least one property using a getter and a setter, as well as a method. 
    """

    def __init__(self, name, height):
        """
        Constructor
        @param name: the name of the building
        @param height: the height of the building
        """
        self.get_name(name)
        self.set_height(height)
    def get_name(self):
        """
        @return String: the name of the campus object
        """
        return self.__name

    def set_height(self, height):
        """
        Assign a value to the height of the building
        @param type String: the building height to be assigned
        """
        if len(str(height)) == 0:
            raise Exception("Value cannot be blank. Height must be provided")
        else:
            self.__height = height

    def get_height(self):
        """
        @return String: the height of the current object
        """
        return self.__height  # Corrected

    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object. 
        Useful for debugging, documentation, etc.
        """
        return "Campus Object:" + self.__type
    def gets_destroyed(self):
        self.__height = None
        print("They finally knocked down Crosley Tower!")
 
 
