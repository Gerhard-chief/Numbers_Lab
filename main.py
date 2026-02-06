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
        stats["negatives_count"] = 0
        stats["positives_count"] = 0
        stats["zeros_count"] = 0
        stats["sum_pos"] = 0
        stats["sum_neg"] = 0
        return stats
    total = 0
    min_val = numbers[0]
    max_val = numbers[0]
    sum_pos = 0
    sum_neg = 0
    pc = 0
    nc = 0
    zc = 0
    for x in numbers:
        total += x
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
        if x == 0:
            zc += 1
        elif x < 0:
            nc += 1
            sum_neg += x
        else:
            pc += 1
            sum_pos +=x
    stats["sum"] = total
    count = len(numbers)
    avg = total / count
    stats["count"] = count
    stats["avg"] = avg
    stats['min'] = min_val
    stats['max'] = max_val
    stats["negatives_count"] = nc
    stats["positives_count"] = pc
    stats["zeros_count"] = zc
    stats["sum_pos"] = sum_pos
    stats["sum_neg"] = sum_neg

    return stats
