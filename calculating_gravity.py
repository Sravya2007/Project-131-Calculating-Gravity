import pandas as pd

star_data = pd.read_csv("star_data.csv")

mass_column = star_data["Mass (M☉)"]

mass_column_kg = []
for mass_data in mass_column:
    mass_data = mass_data * 1.989e+30
    mass_column_kg.append(mass_data)

radius_column = star_data["Radius (R☉)"]

radius_column_m = []
for radius_data in radius_column:
    radius_data = radius_data * 6.957e+8
    radius_column_m.append(radius_data)

star_gravity_list = []
for index, name in enumerate(star_data["Star Name"]):
    G = 6.67 * (10 ** -11)
    g = G * mass_column_kg[index] / (radius_column_m[index] * radius_column_m[index])
    star_gravity_list.append(g)

star_data["Surface Gravity (m/s²)"] = star_gravity_list

print(star_data)

star_data.to_csv("star_data_with_gravity.csv", index = False)