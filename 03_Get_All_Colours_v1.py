import csv
import random

# Retrieve colours from csv file adn put them in a list
file = open("Colour Quest/00_colour_list_hex_v3.csv", "r")
all_colours = list(csv.reader(file, delimiter=","))
file.close()

# Remove the first row of the csv
all_colours.pop(0)

print(all_colours)