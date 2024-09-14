
sum_ = 0
def calculate_structure_sum(*args):
    global sum_
    for i in args:
        if isinstance(i, int):
            sum_ += i
        if isinstance(i, str):
            sum_ += len(i)
        if isinstance(i, list):
            for a in i:
                sum_ += calculate_structure_sum(a)
        if isinstance(i, tuple):
            for a in i:
                sum_ += calculate_structure_sum(a)
        if isinstance(i, set):
            for a in i:
                sum_ += calculate_structure_sum(a)
        if isinstance(i, dict):
            for a in i:
                sum_ += calculate_structure_sum(a)
    return sum_

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
