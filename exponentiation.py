def expo(number, days):
    days_count = 0
    for day in range(days):
        days_count += 1
    result = 2 ** days_count
    return number * result

print(expo(0.01, 30))
