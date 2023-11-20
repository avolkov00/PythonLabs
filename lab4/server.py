# Разработать сервер REST API для учёта лабораторных работ студентов с использованием библиотеки aiohttp.
# Сервер должен хранить следующие данные о лабораторных работах:
#   Название лабораторной (обязательно, уникальное поле)
#   Дедлайн (дата в формате день.месяц. год) (обязательно)
#   Описание (опционально)
#   Список студентов, сдавших данную лабораторную работу (опционально)
# Сервер должен поддерживать запросы:
#   Запрос для внесения лабораторной работы в расписание на http://<адрес>:<port>/labs
#      На данном этапе лабораторная работа ещё не выдана, и список студентов пуст.
#      В ответе возвращается URL для дальнейшей работы с данной лабораторной: http://<адрес>:<port>/labs/<название>
#   Запрос для изменения всех полей лабораторной работы, кроме её названия, на http://<адрес>:<port>/labs/<название>.
#      Название изменять нельзя
#   Запрос для удаления лабораторной работы на http://<адрес>:<port>/labs/<название>
#   Запрос для получения данных о лабораторной работе на http://<адрес>:<port>/labs/<название>
#   Запрос для получения данных обо всех лабораторных работах на http://<адрес>:<port>/labs

from aiohttp import web
import json
import datetime


class Lab:
    def __init__(self, name, date):
        self.__name = name  # Название лабораторной (обязательно, уникальное поле)
        self.date = date  # Дедлайн (дата в формате день.месяц. год)
        self.description = None  # Описание (опционально)
        self.students = None  # Список студентов, сдавших данную лабораторную работу (опционально)

    @property
    def name(self):
        return self.__name


class Server:
    """Класс сервера"""

    def __init__(self):
        self.app = web.Application()
        self.url = "http://localhost:8080"
        self.labs = dict()

        self.app.router.add_post('/labs', self.add_lab)
        self.app.router.add_get('/labs', self.get_labs)
        self.app.router.add_get('/labs/{name}', self.get_lab)
        self.app.router.add_patch('/labs/{name}', self.edit_lab)
        self.app.router.add_delete('/labs/{name}', self.delete_lab)

    # @routes.post('/labs') почему-то как метод класса не работает ;(
    async def add_lab(self, request):
        """Добавление лабораторной на сервер"""
        text = await request.text()
        req = dict()
        try:
            req = json.loads(text)
        except Exception as inst:
            print(type(inst))  # the exception type
            print(inst.args)  # arguments stored in .args
            print(inst)  # __str__ allows args to be printed directly,
            return web.Response(status=400, text=str(inst))

        if ('name' not in req) or ('date' not in req):
            return web.Response(status=400, text="Недостаточно аргументов для создания лабораторной работы")

        if req['name'] in self.labs:
            # лабораторная уже существует
            return web.Response(status=409, text="Лабораторная уже существует")
        else:
            self.labs[req['name']] = Lab(name=req['name'], date=req['date'])
            return web.Response(status=200, text="{}/{}".format(self.url, req['name']))

    async def get_labs(self, request):
        """Получить список лабораторных"""
        resp = dict()
        for i in self.labs.keys():
            resp[i] = None
        return web.json_response(status=200, data=resp)

    async def get_lab(self, request):
        pass

    async def edit_lab(self, request):
        pass

    async def delete_lab(self, request):
        pass


if __name__ == '__main__':
    serv = Server()
    web.run_app(serv.app)
