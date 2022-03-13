def set_stuff(set_a, set_b):
    union_list = set_a.union(set_b)
    a_subset_b = set_a.issubset(set_b)
    a_superset_b = set_a.issuperset(set_b)
    return (union_list, a_subset_b, a_superset_b)
