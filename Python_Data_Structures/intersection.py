def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # l1[3:] = l2
    # for item in l1:
    #     if l1.count(item) <= 1:
    #         l1.remove(item)
    #         if l1.count(item) >= 1:
    #             l1.remove(item)
    # return l1

    set2 = set(l2)

    return [val for val in l1 if val in set2]
