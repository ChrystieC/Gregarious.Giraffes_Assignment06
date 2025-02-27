# main.py
# IS4010-001 Boilerplate Project

#main.py

from Nikki.nikki import *
from Chrystie.Chrystie import *
from Dylan.streetlights import *

if __name__ == "__main__":
    crosley = Building("Crosley", 1000)
    print("this the building:", crosley.get_name())
    print("this is the height of the building:", crosley.get_height(), "feet")

