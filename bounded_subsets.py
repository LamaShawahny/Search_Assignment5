
def bounded_subsets(lst,n):
    x = 0
    l = [*lst]
    lst=l
    while x <=n:
        yield bounded_iter(lst,x)
        x=x+1

def bounded_iter(lst, n):

        if n == 0:
            yield []
        elif lst:
            for s in bounded_iter(lst[1:], n):
                yield s
            for s in bounded_iter(lst[1:], n - lst[0]):
                yield [lst[0]] + s




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test for bounded_subset_generator
    for s in bounded_subsets(range(51, 54), 105):
        for m in s:
            print(m, end=",")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
