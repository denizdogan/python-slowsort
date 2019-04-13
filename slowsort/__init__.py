def _slowsort(values, i, j):
    if i >= j:
        return

    # get the middle index
    m = int((i + j) / 2)

    # sort both sides of the middle of this index
    _slowsort(values, i, m)
    _slowsort(values, m + 1, j)

    # if the RHS is less than the middle, swap places
    if values[j] < values[m]:
        k = values[m]
        values[m] = values[j]
        values[j] = k

    # continue sorting (slowly!)
    _slowsort(values, i, j - 1)


def slowsort(values):
    """
    Slowly sort a sequence of values in place.
    :param values: Sequence of values
    """
    _slowsort(values, 0, len(values) - 1)


__all__ = ("slowsort",)
