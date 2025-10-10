# <details>
# <summary>6. Transportation Mode Selection
# </summary>
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

# </details>

distance=int(input("Enter your distance"))

if distance<3:
    transport="Walk"
elif distance<=15:
    transport="Bike"
else:
    transport="Car"
print("Ai recommends you the transport of :",transport)