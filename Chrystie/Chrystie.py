
# File Name : Chrystie.py
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

class Elevator:
    def __init__(self, current_floor=0, min_floor=0, max_floor=10):
        """
        This is the Elevator's constructor.
        It sets the starting floor and defines the lowest and highest floors.
        @param current_floor int: The floor where the elevator starts.
        @param min_floor int: The lowest floor it can hit.
        @param max_floor int: The highest floor it can reach.
        """
        self._current_floor = current_floor
        self._min_floor = min_floor
        self._max_floor = max_floor

    def __str__(self):
        """
        Returns a friendly description of the elevator.
        @return str: A quick summary of which floor the elevator is on.
        """
        return "Elevator is currently on floor " + str(self._current_floor) + "."

    @property
    def current_floor(self):
        """
        Gets the current floor of the elevator.
        @return int: The floor the elevator is on right now.
        """
        return self._current_floor

    @current_floor.setter
    def current_floor(self, value):
        """
        Sets the elevator's current floor, making sure it's within our allowed range.
        @param value int: The new floor to set.
        @raise ValueError: If the new floor is out of bounds.
        """
        if self._min_floor <= value <= self._max_floor:
            self._current_floor = value
        else:
            raise ValueError("Floor must be between " + str(self._min_floor) + " and " + str(self._max_floor))

    def go_up(self):
        """
        Moves the elevator up one floor (if it's not already at the top).
        @return None: Just prints out the new floor or a note if it's at the top.
        """
        if self._current_floor < self._max_floor:
            self._current_floor += 1
            print("Elevator is moving up to floor " + str(self._current_floor))
        else:
            print("Elevator is already at the top floor.")

    def go_down(self):
        """
        Moves the elevator down one floor (if it's not already at the bottom).
        @return None: Just prints out the new floor or a note if it's at the bottom.
        """
        if self._current_floor > self._min_floor:
            self._current_floor -= 1
            print("Elevator is moving down to floor " + str(self._current_floor))
        else:
            print("Elevator is already at the bottom floor.")


