def list_sort(lst) -> list[int]:
    if len(lst) == 0:
        return lst
    if all(isinstance(item, int) and not isinstance(item, bool) for item in lst):
        lst = set([elem for elem in lst if elem % 2 == 0])
        return sorted(list(lst))
    else:
        raise TypeError("Список должен состоять из целых чисел")
