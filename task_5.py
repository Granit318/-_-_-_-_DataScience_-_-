def percent_query(queries):
    counts = {}
    for query in queries:
        if counts.get(len(query.split())) is None:
            counts[len(query.split())] = 1
        else:
            counts[len(query.split())] += 1

    total = len(queries)
    for num in sorted(counts):
        if num == 1:
            print(f"1 слово: {counts[num] / total * 100:.0f}%")
        elif 1 < num < 5:
            print(f"{num } слова: {counts[num] / total * 100:.0f}%")
        else:
            print(f"{num } слов: {counts[num] / total * 100:.0f}%")
