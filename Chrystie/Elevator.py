# File Name : Elevator.py
# Student Name: Chrystie Cadet
# email:  cadetce@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   February 27 2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  In this assignment, my group and I are creating a project to model something real-world and meaningful to all of us, where each member contributes a class and its associated methods. We’ll collaborate by committing our work to GitHub, and the final project will showcase how our object functions through a main.py file that ties everything together.
# Brief Description of what this module does:This module taught me how to use an IDE to manage projects and develop programs by turning problem descriptions and pseudo-code into real computer code. I also learned how to apply the OOP paradigm, use external libraries, and ensure professionalism with proper documentation and structure in coding.
# Citations:
# Anything else that's relevant: Per Bill's Instructions I ommited the __repr__

class Elevator(object):
    """
    Model an elevator that moves between floors.
    """
    
    def __init__(self, current_floor=0, min_floor=0, max_floor=5):
        """
        Constructor
        @param current_floor: the initial floor of the elevator
        @param min_floor: the lowest floor the elevator can go
        @param max_floor: the highest floor the elevator can reach (I have set the default at 5)
        """
        self.__min_floor = min_floor
        self.__max_floor = max_floor
        self.set_current_floor(current_floor)

    def get_current_floor(self):
        """
        @return int: the current floor of the elevator
        """
        return self.__current_floor

    def set_current_floor(self, floor):
        """
        Assign a value to the current floor, ensuring it is within the allowed range.
        @param floor: the desired floor to set
        @raise Exception: if the floor is not between min_floor and max_floor
        """
        if floor < self.__min_floor or floor > self.__max_floor:
            raise Exception("Floor must be between " + str(self.__min_floor) + " and " + str(self.__max_floor))
        else:
            self.__current_floor = floor

    def __str__(self):
        """
        @return String: A description of the elevator's current state.
        """
        return "Elevator is currently on floor " + str(self.__current_floor)

    def go_up(self):
        """
        Moves the elevator up one floor, if it is not already at the maximum floor.
        """
        if self.__current_floor < self.__max_floor:
            self.__current_floor += 1
            print("Elevator is moving up to floor " + str(self.__current_floor))
        else:
            print("Elevator is already at the top floor.")

    def go_down(self):
        """
        Moves the elevator down one floor, if it is not already at the minimum floor.
        """
        if self.__current_floor > self.__min_floor:
            self.__current_floor -= 1
            print("Elevator is moving down to floor " + str(self.__current_floor))
        else:
            print("Elevator is already at the bottom floor.")



