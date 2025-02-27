# File Name : module1.py
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

class building:
    """
    Describes nippert stadium
    """
    def __init__(self, name, year_built, capacity):
        self._name = name
        self._year_built = year_built
        self._capacity = capacity

class NippertStadium(building):
    def __init__(self, name, year_built, capacity, num_sports, home_team):
        super().__init__(name, year_built, capacity, num_sports)
        self._home_team = home_team

    def __str__(self):
        return super().__str__() + f", Home Team: {self._home_team}"

    def __repr__(self):
        return f"NippertStadium('{self._name}', {self._year_built}, {self._capacity}, {self._num_sports}, '{self._home_team}')"

    @property
    def home_team(self):
        return self._home_team

    @home_team.setter
    def home_team(self, new_team):
        self._home_team = new_team

    def host_game(self):
        print(f"{self._home_team} is playing at {self._name}!")




class stadium (object):
    """
    this will describe nippert stadium and everytime someones scores"""

    def __init__(self, name, occupancy):
        """
        constructor
        @param name: the name of the stadium
        @param occupancy: the number of people it can hold
        """
        self.set_name
        self.set_occupancy(occupancy)

    def get_name(self):


"""

"""
class NippertStadium(object):
    """
    Model Nippert Stadium at the University of Cincinnati, detailing its occupancy and size.
    """
    def __init__(self, capacity, field_size):
        """
        Constructor
        @param capacity int: The maximum occupancy of the stadium
        @param field_size String: The dimensions of the field
        """
        self.set_capacity(capacity)
        self.set_field_size(field_size)

    def get_capacity(self):
        """
        @return int: The maximum occupancy of the stadium
        """
        return self.__capacity
    
    def set_capacity(self, capacity):
        """
        Assign a value to the stadium capacity
        @param capacity int: The maximum occupancy to be assigned.
        """
        if capacity <= 0:
            raise Exception("NippertStadium Class: Capacity must be a positive integer.")
        else:
            self.__capacity = capacity
    
    def get_field_size(self):
        """
        @return String: The field size of the stadium
        """
        return self.__field_size
    
    def set_field_size(self, field_size):
        """
        Assign a value to the field size of the stadium
        @param field_size String: The field dimensions to be assigned.
        """
        if len(field_size.strip()) == 0 or field_size is None:
            raise Exception("NippertStadium Class: Field size must be provided.")
        else:
            self.__field_size = field_size
        
    def announce_score(self):
        """
        Print a message indicating the Bearcats have scored.
        """
        print("The Bearcats Scored!")
        
    def print_details(self):
        """
        Print the stadium capacity and field size.
        """
        print(f"Capacity: {self.__capacity}, Field Size: {self.__field_size}")
        
    def __str__(self):
        """
        @return String: A human-readable representation of the stadium. 
        """
        return f"Capacity: {self.__capacity}, Field Size: {self.__field_size}"

    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the stadium object.
        """
        return f"NippertStadium({self.__capacity}, '{self.__field_size}')"

  
if __name__ == "__main__":
    print("Nippert Stadium class test logic...")
    stadium = NippertStadium(40000, "120 yards x 53.3 yards")
    print("Capacity attribute of NippertStadium object:", stadium.get_capacity())
    print("Field Size attribute of NippertStadium object:", stadium.get_field_size())
    print("Updating stadium details...")
    stadium.set_capacity(41000)
    stadium.set_field_size("125 yards x 55 yards")
    print("Capacity attribute of NippertStadium object:", stadium.get_capacity())
    print("Field Size attribute of NippertStadium object:", stadium.get_field_size())
    
    print("\nTesting the announce_score method...")
    stadium.announce_score()
    
    print("\nTesting the repr method...")
    print("From __repr__():", stadium.__repr__())
    stadiumCopy = eval(stadium.__repr__())
    print("Copied stadium:", stadiumCopy.__str__())
    print("Capacity attribute of copied NippertStadium object:", stadiumCopy.get_capacity())
    print("Field Size attribute of copied NippertStadium object:", stadiumCopy.get_field_size())

