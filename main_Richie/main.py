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
        name = input("Enter the name of the building: ")
        height = input("Enter the height of the building: ")
        
        # Creating an instance of Building
        building = Building(name, height)
        
        # Displaying object details
        print(building)
        print(f"Building Height: {building.get_height()} meters")
        
        # Simulate destruction
        destroy = input("Do you want to knock down the building? (yes/no): ")
        if destroy.lower() == "yes":
            building.gets_destroyed()
        
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
        occupancy = input("How many people are in the stadium: ")
        score = input("Did the Bearcats score a touchdown? (yes/no): ")
        
        # Creating an instance of stadium
        nippertStadium = stadium(occupancy, score)
        
        # Displaying object details
        print(nippertStadium)
        print(f"Nippert can hold: {nippertStadium.get_occupancy()} people")
        
        # Simulate winning
        win = input("Do you want the Bearcats to win? (yes/no): ")
        if win.lower() == "yes":
            nippertStadium.gets_win()
    
    except Exception as e:
        print("Error:", e)

