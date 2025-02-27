# File Name : stadium.py
# Student Name: Richie James
# email:  James2c4@mail.uc.edu
# Assignment Number: Assignment 06 
# Due Date:   2/27/25
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We are modeling the UC campus through different objects/buildings/aspects of the campus in different classes. 
# Brief Description of what this module does. This module creates a class "nippert"  stadium, talking about its average score and how many people it holds
# Citations: N/A
# Anything else that's relevant: N/A

class stadium(object):
    """
    Model a building on campus to be knocked down. Give it at least one property using a getter and a setter, as well as a method. 
    """
    def __init__(self, occupancy, score):
        """
        Constructor
        @param occupancy: the number of people in the stadium
        @param score: question asking if the bearcats score
        """
        self.__occupancy = occupancy
        self.set_score(score)
 
    def get_occupancy(self):
        """
        @return String: the number of people in stadium object
        """
        return self.__occupancy
 
    def set_score(self, score):
        """
        Assign a value to the height of the building
        @param type String: the building height to be assigned
        """
        if len(str(score)) == 0:
            raise Exception("Value cannot be blank. Height must be provided")
        else:
            self.__score = score
 
    def get_score(self):
        """
        @return String: the added score for the bearcats
        """
        return self.__score
    def __str__(self):
        """
        @return String: A description of the current string.
        """
        return f"stadium Object: {self.__name}"
 
    def gets_win(self):
        self.__score = None
        print("They finally scored a touchdown!")