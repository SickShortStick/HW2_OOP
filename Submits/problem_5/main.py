
def Create_Vehicle(vehicle_type, fixed_cost: int, maintenance_cost: int, fuel_consumption: float):
    match vehicle_type:
        case 'TRUCK':
            vehicle = Truck(fuel_consumption, 5000, maintenance_cost, fixed_cost, 0)
        case 'PLANE':
            vehicle = Plane(fuel_consumption, 10000, maintenance_cost, fixed_cost, 0)
        case 'CAR':
            vehicle = Car(fuel_consumption, 500, maintenance_cost, fixed_cost, 0)
        case 'PICKUP':
            vehicle = Pickup(fuel_consumption, 1500, maintenance_cost, fixed_cost, 0)
    print(f'Vehicle {vehicle_type} added with fixed cost: {fixed_cost} , variable cost per km: {maintenance_cost}')


class Vehicle:

    vehicle_id = 1
    all_vehicles = dict()

    fuel_type_consumption_rate = {
        'DIESEL' : 0,
        'JET_FUEL' : 0,
        'GAS' : 0,
        'TRUCK' : 0
    }

    vehicle_types = {
        'TRUCK' : 'DIESEL',
        'PLANE' : 'JET_FUEL',
        'CAR' : 'GAS',
        'PICKUP' : 'GAS'
    }


    total_fixed_maintenance_cost = 0
    total_variable_maintenance_cost = 0
    total_fuel_cost = 0
    total_operational_cost = 0

    def __init__(self, fuel_consumption: float, maximum_weight: int, maintenance: int, fixed_cost: int):
        self.fuel_consumption = fuel_consumption
        self.maximum_weight = maximum_weight
        self.maintenance = maintenance
        self.fixed_cost = fixed_cost
        self.vehicle_id = Vehicle.vehicle_id
        Vehicle.all_vehicles[Vehicle.vehicle_id] = self
        Vehicle.vehicle_id += 1
        self.total_variable_maintenance_cost = 0
        self.total_fuel_cost = 0
        Vehicle.total_fixed_maintenance_cost = fixed_cost

    def set_fuel_price(type_of_fuel, price):
        Vehicle.fuel_type_consumption_rate[type_of_fuel] = price
        print(f'Fuel price for {type_of_fuel} set to {price} per liter.')

    def calculate_trip_cost(self, distance: int):
        Vehicle.total_variable_maintenance_cost += self.maintenance * distance
        Vehicle.total_fuel_cost += Vehicle.fuel_type_consumption_rate[Vehicle.vehicle_types[self.vehicle_type]] * distance
        Vehicle.total_operational_cost += (self.maintenance + Vehicle.fuel_type_consumption_rate[Vehicle.vehicle_types[self.vehicle_type]]) * distance
        self.total_variable_maintenance_cost += self.maintenance * distance
        self.total_fuel_cost += Vehicle.fuel_type_consumption_rate[Vehicle.vehicle_types[self.vehicle_type]] * distance * self.fuel_consumption


class Plane(Vehicle):


    def __init__(self, fuel_consumption, maximum_weight, maintenance, fixed_cost, fuel_price):
        self.vehicle_type = 'Plane'.upper()
        super().__init__(fuel_consumption, maximum_weight, maintenance, fixed_cost)

class Car(Vehicle):

    def __init__(self, fuel_consumption, maximum_weight, maintenance, fixed_cost, fuel_price):
        self.vehicle_type = 'car'.upper()
        super().__init__(fuel_consumption, maximum_weight, maintenance, fixed_cost)

class Truck(Vehicle):

    def __init__(self, fuel_consumption, maximum_weight, maintenance, fixed_cost, fuel_price):
        self.vehicle_type = 'Truck'.upper()
        super().__init__(fuel_consumption, maximum_weight, maintenance, fixed_cost)

class Pickup(Vehicle):

    
    def __init__(self, fuel_consumption, maximum_weight, maintenance, fixed_cost, fuel_price):
        self.vehicle_type = 'Pickup'.upper()
        super().__init__(fuel_consumption, maximum_weight, maintenance, fixed_cost)

class Trip:

    cities = {
        frozenset({'A', 'B'}): 100,
        frozenset({'A', 'C'}): 200,
        frozenset({'A', 'D'}): 150,
        frozenset({'A', 'E'}): 300,
        frozenset({'B', 'C'}): 250,
        frozenset({'B', 'D'}): 180,
        frozenset({'B', 'E'}): 400,
        frozenset({'C', 'D'}): 120,
        frozenset({'C', 'E'}): 350,
        frozenset({'D', 'E'}): 280
    }

    def add_trip(self, vehicle_id: int, first_city, second_city, cargo_weight: int):
        vehicle : Vehicle = Vehicle.all_vehicles.get(vehicle_id)
        if vehicle == None:
            print(f'A vehicle id of {vehicle_id} doesn\'t exist.')
            return
        if cargo_weight > vehicle.maximum_weight:
            print(f'Cargo weight is more than the maximum weight.')
            return
        vehicle.calculate_trip_cost(Trip.cities.get(frozenset({first_city, second_city})))


def report():
    print('End of month report:')
    print(f'''
Total fixed maintenance cost: {Vehicle.total_fixed_maintenance_cost}
Total variable maintenance cost: {Vehicle.total_variable_maintenance_cost}
Total fuel cost: {Vehicle.total_fuel_cost}
Total operational cost: {Vehicle.total_operational_cost}''')
    print('Detailed costs:')
    for vehicle in list(Vehicle.all_vehicles.values()):
        print(f'''
{vehicle.vehicle_type} (ID: {vehicle.vehicle_id}):
Fixed maintenance: {vehicle.fixed_cost}
Variable maintenance: {vehicle.total_variable_maintenance_cost}
Fuel cost: {vehicle.total_fuel_cost}''')

splitted_line = list(input().split())
while splitted_line[0] != 'END_MONTH':
    match splitted_line[0]:
        case 'ADD_VEHICLE':
            Create_Vehicle(splitted_line[1], int(splitted_line[2]), int(splitted_line[3]), float(splitted_line[4]))
        case 'ADD_TRIP':
            trip = Trip()
            trip.add_trip(int(splitted_line[1]), splitted_line[2], splitted_line[3], int(splitted_line[4]))
        case 'SET_FUEL_PRICE':
            Vehicle.set_fuel_price(splitted_line[1], int(splitted_line[2]))
    splitted_line = list(input().split())
report()
