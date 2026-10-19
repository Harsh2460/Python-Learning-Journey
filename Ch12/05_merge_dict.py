# Merge Operator
d1 = {"a": 1,"b": 2}
d2 = {"b": 3,"c": 4}

merged = d1 | d2
print(merged)

# Update Operator
d1 = {"a": 1, "b": 2}
d2 = {"b": 5, "c": 3}

d1 |= d2
print(d1)