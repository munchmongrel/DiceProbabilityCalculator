from collections import defaultdict

def build_distribution(num_dice, sides):
    dist = defaultdict(int)
    dist[0] = 1

    for _ in range(num_dice):
        new_dist = defaultdict(int)
        for prev_sum, count in dist.items():
            for face in range(1, sides + 1):
                new_dist[prev_sum + face] += count
        dist = new_dist

    return dist

def chance_to_hit_target(num_dice, sides, target):
    dist = build_distribution(num_dice, sides)
    total = sum(dist.values())
    success = sum(count for value, count in dist.items() if value >= target)
    return success / total * 100
