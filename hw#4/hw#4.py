# 1 Create a class Vehicle with Attributes: name, max_speed, and total_capacity.
# Method: fare. It should calculate the price of the trip.
# Formula: total_capacity * 100.
# Example, total_capacity = 50 => fare = 5000

class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def fare(self):
        return self.total_capacity * 100

# 2 Create classes Bus and Car that inherit Vehicle.

class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__( name, max_speed, total_capacity)

class Car(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)

# 3 Create 3 car objects and 2 bus objects

car_1 = Car(name="blue", max_speed=120, total_capacity=4)
car_2 = Car(name="green", max_speed=140, total_capacity=5)
car_3 = Car(name="red", max_speed=160, total_capacity=7)
bus_1 = Bus(name="small", max_speed=110, total_capacity=16)
bus_1 = Bus(name="big", max_speed=90, total_capacity=50)

# 4 Check: if car_1 is instance of Car.
# if car_2 is instance of Vehicle.
# if bus_1 is instance of Car.
# if bus_1 is instance of Vehicle.
print(isinstance(car_1, Car))
print(isinstance(car_2, Vehicle))
print(isinstance(bus_1, Car))
print(isinstance(bus_1, Vehicle), "\n")

# 5 Override fare method for Bus class.
# Here we need to add an extra 10% to the fare.
# Formula: total_fare + 10% of total_fare.
# Example, fare = 50 => total_fare = 5500
class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)

    def fare(self):
        extra_fare = super().fare() // 10
        return super().fare() + extra_fare

# 6 Add used_capacity attribute for Bus.
# It means how many people are on the bus.
# If used_capacity > total_capacity raise an error.
class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity, used_capacity):
        super().__init__(name, max_speed, total_capacity)
        self.used_capacity = used_capacity

    def fare(self):
        extra_fare = super().fare() // 10
        return super().fare() + extra_fare

    def check_capacity(self):
        if self.used_capacity > self.total_capacity:
            return "Error"
        elif self.used_capacity < self.total_capacity:
            return "Good"


# 7 Write a magic method to Bus that would be triggered when len() function is called.
    def __len__(self):
        return len(self.name)

# 8 Create class Engine with attribute volume and method get_volume() that will return volume.

class Engine:
    def __int__(self, volume):
        self.volume = volume

    def get_volume(self):
        return self.volume

# 9 Inherit Engine by Car class
class Engine(Car):
    def __init__(self, volume, name, max_speed, total_capacity):
        super().__init__(name,max_speed,total_capacity)
        self.volume = volume
    def get_volume(self):
        return self.volume

# 10 Check what is inheritance order of the Car class
print(Car.__dict__)
print(Car.mro())