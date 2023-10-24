# 3.	Реализуйте декоратор, который измеряет время выполнения функции и выводит его в консоль, в виде класса.
# Реализуйте дополнительный класс-декоратор для вывода полученного времени в формате HTML: <html><body>Время</body></html>.
# Оба декоратора должны также обеспечивать ведение истории вызовов исходной функции в формате:
# <время вызова>: function <имя функции> called with arguments <аргументы>
# Используйте данные декораторы вместе на примерах из задачи 5 семинара 1.

from functools import wraps
import time


class BaseDecorator:
    def __init__(self, function):
        self.function = function
        self.log_list = list()

    @property
    def __name__(self):
        return self.function.__name__

    def log(self,*args, **kwargs):
        t = time.localtime()
        curtime = time.strftime("%H:%M:%S", t)
        self.log_list.append(f"<{curtime}>: function <{self.function.__name__}> called with arguments <{args}{kwargs}>")

class TimerDecorator(BaseDecorator):
    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.function(*args, **kwargs)
        self.runtime = time.perf_counter() - start

        self.log(*args, **kwargs)

        print(f"{self.runtime:.10f}")
        return result
    
    @property
    def __name__(self):
        return self.function.__name__


class HtmlOutputDecorator(BaseDecorator):
    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)

        self.log(*args, **kwargs)

        print(f"<html><body>{self.function.runtime:.10f}</body></html>")

        return result


@HtmlOutputDecorator
@TimerDecorator
def func(count = 1):
    i = 1
    for j in range(1, count):
        i *= j
    return i


if __name__ == "__main__":
    func(9999)
