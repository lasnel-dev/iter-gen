class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i

count = Counter(5)
#
# print(count.__next__())
# print(count.__iter__())
# print(next(count))
# print(next(count))
# print(next(count))
#
def raise_to_the_degree(number):
    i = 0
    while True:
        result = number**i
        yield result
        if result > 100**20:
            return
        i += 1
#
# res = raise_to_the_degree(3)
# print(res)
# for _ in res:
#     print(_)

# class Helper:
#     def __init__(self, work):
#         self.work = work
#
#     def __call__(self, work):
#         return f"I will help you with {self.work}. Afterwards I will help you with {self.work}"
#
# helper = Helper("homework")
# print(helper("cleaning"))
#
# def helper(work):
#     work_in_memory = work
#
#     def helper(work):
#         return f"I will help you with {work_in_memory}. Afterwards I will help you with {work}"
#
#     return helper
#
# helper = helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))
#
# def checker(*exc_types):
#     def checker(function):
#         def checker(*args, **kwargs):
#             try:
#                 result = function(*args, **kwargs)
#             except (exc_types) as e:
#                 print(f"We have problems {e}")
#             else:
#                 print(f"No problems. Result - {result}")
#         return checker
#     return checker
#
# @checker(NameError, TypeError, SyntaxError)
# def calculate(expe):
#     return eval(expe)
#
# calculate("2*5")
#
# @checker(ZeroDivisionError)
# def divider(a, b):
#     return a/b
#
# divider(1, 5)