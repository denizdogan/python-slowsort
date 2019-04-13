from hypothesis import assume, given, settings, strategies as st

from slowsort import slowsort


def is_sorted(values):
    last = float("-inf")
    for value in values:
        if value < last:
            return False
        last = value
    return True


@given(st.lists(st.integers()))
@settings(max_examples=500)
def test_slowsort_unsorted_input(values):
    assume(not is_sorted(values))
    slowsort(values)
    assert is_sorted(values)


@given(st.lists(st.integers()))
@settings(max_examples=500)
def test_slowsort_sorted_input(values):
    assume(is_sorted(values))
    slowsort(values)
    assert is_sorted(values)
