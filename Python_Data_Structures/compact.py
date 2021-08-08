def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # for item in lst:
    #     if item == False:
    #         lst.remove(item)
    #     if item == []:
    #         lst.remove(item)
    #     if item == '':
    #         lst.remove(item)
    #     if item == 0:
    #         lst.remove(item)
    #     if item == None:
    #         lst.remove(item)
    # return lst
    return [val for val in lst if val]
