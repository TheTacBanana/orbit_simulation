import pygame
from body import *

window = pygame.display.set_mode((1920, 1080))

def create():
    global objects
    objects = []
    objects.append(Object(1000000000, 50, [960, 500], True, [0, 0], (255, 255, 0)))

    objects.append(Object(10000, 5, [960 + 200, 500], False, [0, 28], (255, 0, 0)))

    objects.append(Object(100000, 8, [960 + 300, 500], False, [0, 23], (0, 0, 255)))

    objects.append(Object(1000000, 10, [960 + 600, 500], False, [0, 16], (0, 255, 0)))
    objects.append(Object(100000, 2, [960 + 600, 470], False, [-2.3, 16], (0, 255, 0)))

objects = []
create()

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                window.fill((0,0,0))
                create()
            if event.key == pygame.K_F2:
                running = False

    for i in range(len(objects)):
        if objects[i].fixed:continue
        for j in range(len(objects)):
            if i == j: continue
            direction = [objects[j].position[x] - objects[i].position[x] for x in range(2)]
            dist = math.sqrt(sum([direction[x] ** 2 for x in range(2)]))

            if dist < objects[j].radius + objects[i].radius:
                objects[i].fixed = True

        forces = objects[i].calculate_object_forces([objects[k] for k in range(len(objects)) if k != i])
        objects[i].calculate_force(forces)

        objects[i].apply_acceleration()
    [pygame.draw.circle(window, obj.colour, obj.position, obj.radius, 0) for obj in objects]
    [obj.update_location() for obj in objects if not obj.fixed]

    pygame.display.update()
    window.fill((0,0,0))
    clock.tick(60)