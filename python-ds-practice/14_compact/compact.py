def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    new_lst = []
    for elm in lst:
        if not not elm:
            new_lst.append(elm)
    return new_lst

    #Simpler version
    #return [val for val in lst if val]

print(compact([0, 1, 2, '', [], False, (), None, 'All done'])) #Should return [1, 2, 'All done']