with open('input.txt', 'r') as file:
    celestial_bodies = list(map(lambda x: [
        int(x.rstrip()[1:][:-1].split(", ")[0][2:]), int(x.rstrip()[1:][:-1].split(", ")[1][2:]),
        int(x.rstrip()[1:][:-1].split(", ")[2][2:])], file.readlines()))
    velocities = list(map(lambda x: [0, 0, 0], celestial_bodies))
    print("step 0", celestial_bodies, velocities)
    for step in range(1000):
        for first_body in celestial_bodies:
            for second_body in celestial_bodies:
                if not first_body == second_body:
                    index = celestial_bodies.index(first_body)
                    for coord in range(3):
                        velocity_change = -1 if first_body[coord] > second_body[coord] else 1 if first_body[coord] < \
                                                                                                 second_body[
                                                                                                     coord] else 0
                        velocities[index][coord] = velocities[index][coord] + velocity_change
        for first_body in celestial_bodies:
            for coord in range(3):
                first_body[coord] = first_body[coord] + velocities[celestial_bodies.index(first_body)][coord]
        print("step " + str(step + 1), celestial_bodies, velocities)
    total = []
    for body in range(len(celestial_bodies)):
        pot = 0
        kin = 0
        for coord in range(3):
            pot += abs(celestial_bodies[body][coord])
            kin += abs(velocities[body][coord])
        total.append(pot * kin)
    print(total, sum(total))
