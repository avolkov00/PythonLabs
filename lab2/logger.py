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
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

class Logger(Singleton):
    def __init__(cls):
        cls.f = open("workfile", "a", encoding="utf-8")

    def log(self, type, message):
        """Внутренняя функция логирования"""
        t = time.localtime()
        curtime = time.strftime("%H:%M:%S", t)
        formatted_message = f"[{type.name}] {curtime}: {message}\n"
        self.f.write(formatted_message)
        print(formatted_message)

    def debug(self, message):
        """Дебаг"""
        self.log(Status.DEBUG, message)

    def info(self, message):
        """Информация"""
        self.log(Status.INFO,message)

    def warn(self, message):
        """Предупреждение"""
        self.log(Status.WARN,message)

    def error(self, message):
        """Ошибка"""
        self.log(Status.ERROR,message)

    def critical(self, message):
        """Критичная ошибка"""
        self.log(Status.CRITICAL, message)



if __name__ == "__main__":
    s = Singleton()
    s.log(
        Status.INFO, "hello"
    )
