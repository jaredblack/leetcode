import itertools
import math

# I did this for the DP topic exam but
# the solution I came up with (which didn't quite work)
# and the solution I based my working solution off of were
# not really DP
def closestCost(baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
    closest = -math.inf

    def get_new_closest(new, curr_closest):
        if abs(target - new) < abs(target - curr_closest):
            curr_closest = new
        elif abs(target - new) == abs(target - curr_closest) and new < curr_closest:
            curr_closest = new
        return curr_closest

    def help(cost, target, topping_index):
        nonlocal closest
        closest = get_new_closest(cost, closest)

        if topping_index == len(toppingCosts):
            return

        for ct in range(3):
            help(cost + toppingCosts[topping_index]*ct, target,topping_index+1)
    
    for cost in baseCosts:
        help(cost, target, 0)
    return closest

print(closestCost([10],[1],1))