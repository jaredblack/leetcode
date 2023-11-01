def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    car_tuples = [(position[i], speed[i]) for i in range(len(position))]
    car_tuples.sort(key=lambda c: c[0])
    front_o_the_fleet = -1
    fleets = 0
    while len(car_tuples):
        pos, speed = car_tuples.pop()
        t = (target - pos) / speed
        if t > front_o_the_fleet:
            fleets += 1
            front_o_the_fleet = t
    return fleets

print(carFleet(10, [0,4,2], [2,1,3]))