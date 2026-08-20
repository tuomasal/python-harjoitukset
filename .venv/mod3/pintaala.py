import math

radius_str = input("Kerro haluamasi säde:")
radius = float(radius_str)
area = math.pi * (radius**2)
print("ympyrän pinta-ala säteellä on:" + str(area))