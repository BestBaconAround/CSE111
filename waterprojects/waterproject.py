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