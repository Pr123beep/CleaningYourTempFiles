def find_earliest_on_time(t, test_cases):
    results = []

    for n, k, a in test_cases:
        # Normalize installation times to modulo 2k
        mods = [ai % (2 * k) for ai in a]

        # Calculate the lowest common time that satisfies the conditions for all rooms
        max_mod = max(mods)  # Start checking from the largest mod as it's the minimum possible time
        time = max_mod
        found = False

        # We will check for the synchronization of light on times within the limit
        while time <= 2 * k * 10 ** 6:  # Arbitrary large number for upper bound in reasonable range
            # Check if this time matches light 'on' time for all rooms
            if all((time - mod) % (2 * k) == 0 for mod in mods):
                results.append(time)
                found = True
                break
            time += 2 * k

        if not found:
            results.append(-1)

    return results


# Example input from the problem description (assuming it has been properly parsed)
t = 9
test_cases = [
    (4, 4, [2, 3, 4, 5]),
    (4, 3, [2, 3, 4, 5]),
    (4, 3, [3, 4, 8, 9]),
    (3, 3, [6, 2, 1]),
    (1, 1, [1]),
    (7, 5, [14, 34, 6, 25, 46, 7, 17]),
    (6, 5, [40, 80, 99, 60, 90, 50]),
    (6, 5, [64, 40, 50, 68, 70, 10]),
    (2, 1, [1, 1000000000])
]

# Find the earliest time when all lights are on
results = find_earliest_on_time(t, test_cases)

# Output results
results
