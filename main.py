def read_numbers():
    numbers = []
    while True:
        s = input("Enter number (q to finish): ").strip().lower()
        if s == "q":
            return numbers

        s = s.replace(",", ".")
        try:
            x = float(s)
        except ValueError:
            print("Not a number")
            continue

        numbers.append(x)
        
def calc_stats(numbers):
    stats = {}

    if not numbers:
        stats["count"] = 0
        stats["sum"] = 0
        stats['min'] = None
        stats['max'] = None
        stats['avg'] = None
        return stats
    total = 0
    min_val = numbers[0]
    max_val = numbers[0]
    for x in numbers:
        total += x
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    stats["sum"] = total
    stats["count"] = len(numbers)
    stats['avg'] = total/len(numbers)
    stats['min'] = min_val
    stats['max'] = max_val

    return stats
