#!/usr/bin/env python3

def join_lists(l1, l2):
    """Return a list that contains every value from both l1 and l2, ensuring unique values."""
    # Convert lists to sets to remove duplicates and then back to a list
    return list(set(l1) | set(l2))

def match_lists(l1, l2):
    """Return a list that contains all values found in both l1 and l2."""
    return [value for value in l1 if value in l2]

def diff_lists(l1, l2):
    """Return a list that contains all different values, which are not shared between the lists."""
    return list(set(l1).symmetric_difference(set(l2)))

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 1, 0, -1, -2]
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
