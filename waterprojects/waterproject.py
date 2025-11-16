import math
def water_column_height(tower_height, tank_height):
    water_in_tank = 3/4 * tank_height
    total_height = tower_height + water_in_tank
    return total_height

def pressure_gain_from_water_height(height):
    pressure_per_meter = 9.788998
    pressure = pressure_per_meter * height
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    if pipe_length == 0 or friction_factor == 0 or fluid_velocity == 0:
        return 0.0
    water_density = 998.2
    numerator = friction_factor * pipe_length * water_density * (fluid_velocity**2)
    denominator = 2000 * pipe_diameter
    pressure_loss = - numerator / denominator
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    if fluid_velocity == 0 or quantity_fittings == 0:
        return 0.0
    water_density = 998.2
    velocity_squared = fluid_velocity * fluid_velocity
    numerator = 0.04 * water_density * velocity_squared * quantity_fittings
    denominator = 2000
    pressure_loss = - numerator / denominator
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    if fluid_velocity == 0:
        return 0.0
    water_density = 998.2
    water_dynamics_viscosity = 0.0010016
    numerator = water_density * hydraulic_diameter * fluid_velocity
    reynolds = numerator / water_dynamics_viscosity
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    if fluid_velocity == 0:
        return 0.0
    water_density = 998.2 
    ratio = larger_diameter / smaller_diameter
    k = (0.1 + 50 / reynolds_number) * (ratio**4 - 1)
    pressure_loss = -k * water_density * (fluid_velocity ** 2) / 2000
    return pressure_loss

def main():
    tower_height = float(input("Height of water towers (meters)"))
    tank_wall_height = float(input("Length of supply pipe from tank to lot (meters)"))
    length_tank_to_lot = float(input("Length of supply pipe from tank to lot (meters)"))
    fitting_count = int(input("Number of 90 angles in supply pipe: "))
    length_lot_to_house = float(input("Length of pipe from supply to house (meters)"))

    #2025