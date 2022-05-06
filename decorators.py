def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner


@decorator_list
def add_together(a, b):
    return a + b


print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))

#source: https://towardsdatascience.com/how-to-use-decorators-in-python-by-example-b398328163b#:~:text=A%20decorator%20in%20Python%20is,the%20original%20function%20source%20code.

#source: https://www.programiz.com/python-programming/decorator