import math

class Object():
    def __init__(self, mass, radius, position, fixed, initialvel, colour):
        self.mass = mass
        self.radius = radius
        self.fixed = fixed
        self.colour = colour

        self.g_constant = 0.6
        self.position = position
        self.velocity = initialvel
        self.acceleration = [0,0]

    def calculate_object_forces(self, objects):
        return [obj.get_force(self) for obj in objects]

    def get_force(self, obj):
        direction = [self.position[i] - obj.position[i] for i in range(2)]
        dist = math.sqrt(sum([direction[i] ** 2 for i in range(2)]))

        force = (self.g_constant * obj.mass * self.mass) / ((dist) ** 2)
        unit_direction = [direction[i] / (dist) for i in range(2)]
        directional_force = [unit_direction[i] * force for i in range(2)]
        return directional_force

    def calculate_force(self, forces):
        cum_force = [0,0,0]
        for force in forces:
            cum_force = [cum_force[i] + force[i] for i in range(2)]
        cum_acceleration = [i / self.mass for i in cum_force]
        self.acceleration = cum_acceleration

    def apply_acceleration(self):
        self.velocity = [self.velocity[i] + ((1/60) ** 2)  * self.acceleration[i] for i in range(len(self.acceleration))]

    def update_location(self):
        self.position = [self.position[i] + self.velocity[i] for i in range(2)]

    def orbit_velocity(self, obj):
        direction = [self.position[i] - obj.position[i] for i in range(2)]
        dist = math.sqrt(sum([direction[i] ** 2 for i in range(2)]))

        return math.sqrt((self.g_constant * self.mass) / dist)
