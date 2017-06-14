from bicycles import *

david = Customers("David", 200)
lara = Customers("Lara", 500)
vicky = Customers("Vicky", 1000)

wheel1 = Wheels("wheel_model_1", 5, 30)
wheel2 = Wheels("wheel_model_2", 4, 70)
wheel3 = Wheels("wheel_model_3", 6, 200)

frame1 = Frames("aluminum", 10, 150)
frame2 = Frames("carbon",   8,  30)
frame3 = Frames("steel",    15, 100)

Manuf1 = Manufacturer("Manuf1")
Manuf2 = Manufacturer("Manuf2")

trek1 = Bicycle("trek1", "trek_2000", wheel3, frame1, "Manuf1")
trek2 = Bicycle("trek2", "trek_2005", wheel1, frame2, "Manuf1")
gary1 = Bicycle("gary1", "gary_90",   wheel2, frame3, "Manuf2")
gary2 = Bicycle("gary2", "gary_88",   wheel1, frame3, "Manuf2")
bike1 = Bicycle("bike1", "bike_100",  wheel2, frame1, "Manuf2")
bike2 = Bicycle("bike2", "bike_200",  wheel3, frame2, "Manuf2")

Manuf1.produce(trek1)
Manuf1.produce(trek1)
Manuf1.produce(trek2)

Manuf2.produce(gary1)
Manuf2.produce(bike2)
Manuf2.produce(bike1)
Manuf2.produce(gary2)

shop = Bike_shop("shop")

shop.buy(trek1, Manuf1)
shop.buy(trek2, Manuf1)
shop.buy(trek1, Manuf1)
shop.buy(gary1, Manuf2)
shop.buy(bike1, Manuf2)
shop.buy(bike2, Manuf2)

Manuf2.sell(gary2, shop)


# Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget.
shop.offer(david)
shop.offer(lara)
shop.offer(vicky)

# Print the initial inventory of the bike shop for each bike it carries.
print(shop.inventory)

# Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost,
# and how much money they have left over in their bicycle fund.

david.buy(trek1, shop)
david.buy(trek2, shop)
david.buy(trek1, shop)

# After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike,
# and how much profit they have made selling the three bikes.

for i in shop.inventory:
  print("we have " + str(shop.inventory[i]) + " bicycles of the model " + str(i))

print("Profit: ", str(shop.profit))


