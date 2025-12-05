EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016


def water_column_height(tower_height, tank_height):
    water_in_tank = 3 / 4 * tank_height
    total_height = tower_height + water_in_tank
    return total_height


def pressure_gain_from_water_height(height):
    pressure = WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height / 1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    if pipe_length == 0 or friction_factor == 0 or fluid_velocity == 0:
        return 0.0
    numerator = friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)
    denominator = 2000 * pipe_diameter
    pressure_loss = - numerator / denominator
    return pressure_loss


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    if fluid_velocity == 0 or quantity_fittings == 0:
        return 0.0
    velocity_squared = fluid_velocity * fluid_velocity
    numerator = 0.04 * WATER_DENSITY * velocity_squared * quantity_fittings
    denominator = 2000
    pressure_loss = - numerator / denominator
    return pressure_loss


def reynolds_number(hydraulic_diameter, fluid_velocity):
    if fluid_velocity == 0:
        return 0.0
    numerator = WATER_DENSITY * hydraulic_diameter * fluid_velocity
    reynolds = numerator / WATER_DYNAMIC_VISCOSITY
    return reynolds


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    if fluid_velocity == 0:
        return 0.0
    ratio = larger_diameter / smaller_diameter
    k = (0.1 + 50 / reynolds_number) * (ratio ** 4 - 1)
    pressure_loss = -k * WATER_DENSITY * (fluid_velocity ** 2) / 2000
    return pressure_loss


def kpa_to_psi(pressure_kpa):
    return pressure_kpa * 0.14503774


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_wall_height = float(input("Height of water tank walls (meters): "))
    length_tank_to_lot = float(input("Length of supply pipe from tank to lot (meters): "))
    fitting_count = int(input("Number of 90° angles in supply pipe: "))
    length_lot_to_house = float(input("Length of pipe from supply to house (meters): "))

    column_height = water_column_height(tower_height, tank_wall_height)
    pressure = pressure_gain_from_water_height(column_height)

    supply_diameter = 0.28687
    supply_friction = 0.013
    supply_velocity = 1.65

    house_diameter = 0.048692
    house_friction = 0.018
    house_velocity = 1.75

    pressure += pressure_loss_from_pipe(
        supply_diameter, length_tank_to_lot, supply_friction, supply_velocity
    )

    pressure += pressure_loss_from_fittings(
        supply_velocity, fitting_count
    )

    R = reynolds_number(supply_diameter, supply_velocity)

    pressure += pressure_loss_from_pipe_reduction(
        supply_diameter, supply_velocity, R, house_diameter
    )

    pressure += pressure_loss_from_pipe(
        house_diameter, length_lot_to_house, house_friction, house_velocity
    )

    print(f"Pressure at house: {pressure:.1f} kilopascals")

    pressure_psi = kpa_to_psi(pressure)
    print(f"Pressure at house: {pressure_psi:.1f} psi")


if __name__ == "__main__":
    main()
