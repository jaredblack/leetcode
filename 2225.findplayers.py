from collections import defaultdict


def findWinners(matches: list[list[int]]) -> list[list[int]]:
    player_losses = defaultdict(int)
    for winner, loser in matches:
        player_losses[loser] += 1
        player_losses[winner] += 0
    zero_losses = []
    one_loss = []
    for player, losses in player_losses.items():
        if losses == 0:
            zero_losses.append(player)
        elif losses == 1:
            one_loss.append(player)
    zero_losses.sort()
    one_loss.sort()
    return [zero_losses, one_loss]