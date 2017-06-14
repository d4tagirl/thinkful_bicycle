# FIRST PART
# class Bicycle(object):
#   def __init__(self, name, model, weight, cost):
#     self.name = name
#     self.model = model
#     self.weight = weight
#     self.cost = cost
#
#   def __str__(self):
#     return '%s (%s)' % (self.name, self.model)
#
#   def __unicode__(self):
#     return self.__str__()

# SECOND PART
# class Bicycle(object):
#   def __init__(self, name, model, wheels, frame):
#     self.name = name
#     self.model = model
#     self.weight = 2 * wheels.weight + frame.weight
#     self.cost = 2 * wheels.cost + frame.cost
#
#   def __str__(self):
#     return '%s (%s)' % (self.name, self.model)
#
#   def __unicode__(self):
#     return self.__str__()
  
class Bicycle(object):
  def __init__(self, name, model, wheels, frame, manufacturer):
    self.name = name
    self.model = model
    self.manufacturer = manufacturer
    self.weight = 2 * wheels.weight + frame.weight
    self.cost = 2 * wheels.cost + frame.cost

  def __str__(self):
    return '%s (%s)' % (self.name, self.model)

  def __unicode__(self):
    return self.__str__()

  
  



class Manufacturer(object):
  def __init__(self, name):
    self.name = name
    self.inventory = {}
    self.margin = 0.1
    
  def produce(self, bicycle):
    self.inventory[bicycle] = self.inventory.get(bicycle, 0) + 1
    
  def sell(self, bicycle, shop):
    shop.buy(bicycle, self)
    

 
class Bike_shop(object):
  def __init__(self, name):
    self.name = name
    self.inventory = {}
    self.profit = 0
    self.margin = 0.2

  def buy(self, bicycle, manufacturer):
    self.inventory[bicycle] = 1
    manufacturer.inventory[bicycle] -= 1

  def sell(self, bicycle, customer):
    if self.inventory[bicycle] == 0:
      print("sorry, we don't have that bike at the moment!")
    elif customer.budget <= bicycle.cost * (1 + self.margin):
      print("sorry, you can't afford it!")
    else:
        self.profit += (self.margin * bicycle.cost)
        self.inventory[bicycle] -= 1
        customer.own[bicycle] = customer.own.get(bicycle, 0) + 1
        customer.budget -= bicycle.cost * (1 + self.margin)

  def offer(self, customer):
    print(customer.name,":")
    for i in self.inventory:
      if customer.budget >= i.cost * (1 + self.margin):
        print(i)
    print()

  def __str__(self):
    names = map(str, self.inventory)
    return ', '.join(names)

  def __unicode__(self):
    return self.__str__()



class Customers(object):
  def __init__(self, name, budget):
    self.name = name
    self.budget = budget
    self.own = {}

  def buy(self, bycicle, shop):
    shop.sell(bycicle, self)



class Wheels(object):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost

  def __str__(self):
    return '%s' % self.model



class Frames(object):
  def __init__(self, material, weight, cost):
    self.material = material
    self.weight = weight
    self.cost = cost

  def __str__(self):
    return '%s' % self.material

