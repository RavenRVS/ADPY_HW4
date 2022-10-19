def flat_generator(any_list):
    cursor1 = 0
    cursor2 = 0
    while len(any_list) > cursor1:
        nested_lst = any_list[cursor1]
        result = nested_lst[cursor2]
        cursor2 = cursor2 + 1
        yield result
        if len(nested_lst) <= cursor2:
            cursor1 = cursor1 + 1
            cursor2 = 0


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]
for item in flat_generator(nested_list):
    print(item)
