# Домашнее задание к лекции 2.«Iterators. Generators. Yield»

Задание 1. <a href="https://github.com/RavenRVS/ADPY_HW4/blob/master/iter.py">(моё решение) </a> <br>
Доработать класс `FlatIterator` в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов.

```python
class FlatIterator:

    def __init__(self, list_of_list):
        ...

    def __iter__(self):
        ...
        return self

    def __next__(self):
        ...
        return item

```


Задание 2. <a href="https://github.com/RavenRVS/ADPY_HW4/blob/master/gen.py">(моё решение) </a> <br>
Доработать функцию flat_generator, Должен получиться генератор, который принимает список списков и возвращает их плоское представление.
```python
import types


def flat_generator(list_of_lists):

    ...
    yield
    ...

    
```

