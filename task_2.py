def cosine_distance(a, b):
    if len(a) != len(b):
        print("Векторы должны быть одной длины")
        return
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = (sum(x * x for x in a)) ** 0.5
    norm_b = (sum(y * y for y in b)) ** 0.5
    if norm_a == 0 or norm_b == 0:
        print("Косинус не определён для нулевого вектора")
        return
    print(1 - dot / (norm_a * norm_b))