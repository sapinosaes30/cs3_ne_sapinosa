def calculate_fuel(cargo_weight):
    ship_weight = 50000
    total_cargo_weight = cargo_weight + ship_weight
    fuel_required = total_cargo_weight * 3
    return fuel_required

while True:
    item = input("What cargo would you like to hold? ")

    if item == "satellite":
        cargo_weight = 1000
        print(calculate_fuel(cargo_weight))
        break
    elif item == "rover":
        cargo_weight = 2500
        print(calculate_fuel(cargo_weight))
        break
    elif item == "supplies":
        cargo_weight = 500
        print(calculate_fuel(cargo_weight))
        break

    else:
        print("Invalid item")

   

            

