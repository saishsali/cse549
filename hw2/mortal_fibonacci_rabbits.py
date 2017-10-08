def mortal_fibonnaci_rabbits(n, m):
    # There is only one pair of rabbit in the beginning
    rabbit_generations = [1] + [0] * (m - 1)

    for i in range(1, n):
        # New pair of rabbits are born from matured rabbits
        new_rabbits = sum(rabbit_generations[1:])

        # Rabbit pairs mature over a month
        for j in range(m - 1, 0, -1):
            rabbit_generations[j] = rabbit_generations[j - 1]
        rabbit_generations[0] = new_rabbits
    return sum(rabbit_generations)

n, m = raw_input().split()
n, m = int(n), int(m)
print(mortal_fibonnaci_rabbits(n, m))
