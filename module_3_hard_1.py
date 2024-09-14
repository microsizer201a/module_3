
sum_ = 0
def calculate_structure_sum(*args):
    global sum_
    for i in args:
        if isinstance(i, int):
            sum_ += i
        if isinstance(i, str):
            sum_ += len(i)
        if isinstance(i, list):
            if i[0] == None:
                first = 0
            else:
                first = i[0]
            if len(i) <= 1:
                sum_ += first
            else:
                sum_ += first + calculate_structure_sum(i[1:])
        if isinstance(i, tuple):
            if i[0] == None:
                first = 0
            else:
                first = i[0]
            if len(i) <= 1:
                sum_ += first
            else:
                sum_ += first + calculate_structure_sum(i[1:])
        if isinstance(i, set):
            if i[0] == None:
                first = 0
            else:
                first = i.pop()
            if len(i) <= 1:
                sum_ += first
            else:
                sum_ += first + calculate_structure_sum(i.pop())
        if isinstance(i, dict):
            values_ = i.values()
            keys_ = i.keys()
            first_value = values_[0]
            first_key = len(keys_[0])
            if len(i) <= 1:
                sum_ += first_value + first_key
            else:
                sum_ += first_value + first_key + calculate_structure_sum(i[1:])
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
