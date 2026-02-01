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
    stats["count"] = len(numbers)

    total = 0
    for x in numbers:
            total += x
    stats["sum"] = total
    return stats