class FlatIterator:
    def __init__(self, any_list):
        self.lst = any_list

    def __iter__(self):
        self.cursor1 = 0
        self.cursor2 = 0
        return self

    def __next__(self):
        nested_lst = self.lst[self.cursor1]
        if len(nested_lst) > self.cursor2:
            result = nested_lst[self.cursor2]
            self.cursor2 = self.cursor2 + 1
        else:
            self.cursor1 = self.cursor1 + 1
            if self.cursor1 >= len(self.lst):
                raise StopIteration
            self.cursor2 = 0
            nested_lst = self.lst[self.cursor1]
            result = nested_lst[self.cursor2]
            self.cursor2 = self.cursor2 + 1
        return result


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
