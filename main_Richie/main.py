# main.py
# IS4010-001 Boilerplate Project

#main.py

from Nikki.nikki import *
from Chrystie.Elevator import *
from Dylan.streetlights import *
from Richie.stadium import *
 
 
if __name__ == "__main__":
    
    """
    crosley = Building("Crosley", 1000)
    print("This is the building:", crosley.get_name())
    print("This is the height of the building:", crosley.get_height(), "feet")
    crosley.gets_destroyed()
    """
    try:
        name = "Crosley"
        height = input("Enter the estimated height of Crosley Tower: ")
        
        # Creating an instance of Building
        building = Building(name, height)
        
        # Displaying object details
        print(building)
        print(f"Building Height: {building.get_height()} meters")
        
        # Simulate destruction
        destroy = input("Do you want to knock down the building? (yes/no): ")
        if destroy.lower() == "yes":
            building.gets_destroyed()
        else:
            building.gets_saved()

        
    except Exception as e:
        print("Error:", e)

    """
    streetlight = street_lights(150, "On")
    print("there are", streetlight.get_number(), " of streetlight")
    print()
    """
   

    try:
        number_of_lights = input("Enter the number of street lights: ")
        turn_on_lights = input("Do you want to turn on the lights? (yes/no): ")
        
        # Creating an instance of street_lights
        lights = street_lights(number_of_lights, turn_on_lights)
        
        # Displaying object details
        print(lights)
        
        # Perform action
        lights.lights_turning_on()
    except Exception as e:
        print("Error:", e)

   

    try:
            name = "Nippert"
            occupancy = input("How many people are in the stadium: ")
            score = input("Did the Bearcats score a touchdown? (yes/no): ")
        
            # Creating an instance of stadium
            nippertStadium = stadium(name, occupancy, score)
        
            # Displaying object details
            print(nippertStadium)
            print(f"Nippert can hold: {nippertStadium.get_occupancy()} people")
        
            # Simulate winning
            win = input("Do you want the Bearcats to win? (yes/no): ")
            if win.lower() == "yes":
                nippertStadium.gets_win()
    
    except Exception as e:
       print("Error:", e)


    try:
        current_floor = int(input("Enter the elevator's starting floor: "))
        min_floor = int(input("Enter the minimum floor of the building: "))
        max_floor = int(input("Enter the maximum floor of the building: "))

        building_elevator = Elevator(current_floor, min_floor, max_floor)

        print(building_elevator)

        action = input("Would you like to move the elevator up or down? (up/down/exit): ").lower()

        if action == "up":
                building_elevator.go_up()
        elif action == "down":
                building_elevator.go_down()
        elif action == "exit":
                print("Exiting elevator simulation.")
        else:
            print("Invalid input. Please enter 'up', 'down', or 'exit'.")

    except Exception as e:
        print("Error:", e)




