import math

base_str = float(input("Anna kannan pituus:"))
height_str = float(input("Anna korkeus:"))

base = float(base_str)
height = float(height_str)

area = base * height 
perimeter = base * 2 + height * 2

area_str = (area)
perimeter_str = (perimeter)

print(f"Suorakulmion pinta-ala on: {area:.2f}, Suorakulmion piiri on: {perimeter:.2f}")
