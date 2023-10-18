# 4.	Реализовать класс для логирования сообщений в файл. Сообщения выводятся в формате:
# [<статус>] <время вывода>: <сообщение>,
# где статус - DEBUG, INFO, WARN, ERROR, CRITICAL.
# При этом считается, что в проекте может использоваться только один экземпляр класса-логгера.

import time
from enum import Enum


class Status(Enum):
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    CRITICAL = 5


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def log(self, type, message):
        t = time.localtime()
        curtime = time.strftime("%H:%M:%S", t)
        print(f"[{type}] {curtime}: {message}")


if __name__ == "__main__":
    s = Singleton()
    s.log(Status.INFO.name, "hello")  # @todo наверное вид стоит как то по адекватнее передавать ?
