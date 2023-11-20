import aiohttp
import asyncio
import argparse
import json


class Client:
    """Класс клиента"""
    def __init__(self, url):
        self.url = url

    @staticmethod
    async def print_response(response):
        """Распечатать ответ сервера"""
        print("Status:", response.status)
        print("Content-type:", response.headers['content-type'])
        text = await response.text()
        print("Body:", text)

    async def add_lab(self, lab, date):
        """Добавить новую лабораторную работу"""
        async with aiohttp.ClientSession() as session:
            request = {'name': lab, 'date': date}
            async with session.post(url="{}/{}".format(self.url, 'labs'), data=json.dumps(request)) as response:
                await self.print_response(response)

    async def get_lab(self, text):
        """Получить лабораторную работу"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url="{}/{}".format(self.url, text)) as response:
                await self.print_response(response)

    async def get_labs(self):
        """Получить список всех лабораторных работ"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url="{}/{}".format(self.url, 'labs')) as response:
                await self.print_response(response)

    async def edit_lab(self, lab, date, description, students):
        """Изменить лабоработрую работу"""
        async with aiohttp.ClientSession() as session:
            request = {}
            if date is not None:
                request['date'] = date
            if description is not None:
                request['description'] = description
            if students is not None:
                request['students'] = students

            async with session.patch(url="{}/{}".format(self.url, lab), test=json.dumps(request)) as response:
                await self.print_response(response)

    async def remove_lab(self, lab):
        """Удалить лабораторную работу"""
        async with aiohttp.ClientSession() as session:
            async with session.delete(url="{}/{}".format(self.url, lab)) as response:
                await self.print_response(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Обращения к серверу хранения лабораторных работ')

    #   Запрос для внесения лабораторной работы в расписание на http://<адрес>:<port>/labs
    #      На данном этапе лабораторная работа ещё не выдана, и список студентов пуст.
    #      В ответе возвращается URL для дальнейшей работы с данной лабораторной: http://<адрес>:<port>/labs/<название>
    parser.add_argument('--add', type=str, help="Запрос для внесения лабораторной работы в расписание")

    #   Запрос для изменения всех полей лабораторной работы, кроме её названия, на http://<адрес>:<port>/labs/<название>.
    #      Название изменять нельзя
    parser.add_argument('--edit', type=str,
                        help="Запрос для изменения всех полей лабораторной работы, кроме её названия")

    # Параметры лабораторной работы
    parser.add_argument('--date', type=str, help="Дата лабораторной работы в формате \"день.месяц.год\"")
    parser.add_argument('--description', type=str, help="Описание лабораторной работы")
    parser.add_argument('--students', type=str, help="Студенты выполняющие лабоаторную работу")

    #   Запрос для удаления лабораторной работы на http://<адрес>:<port>/labs/<название>
    parser.add_argument('--remove', type=str, help="Запрос для удаления лабораторной работы")

    #   Запрос для получения данных о лабораторной работе на http://<адрес>:<port>/labs/<название>
    parser.add_argument('--get', type=str, help="Запрос для получения данных о лабораторной работе")

    #   Запрос для получения данных обо всех лабораторных работах на http://<адрес>:<port>/labs
    parser.add_argument('--get_all', action='store_true',
                        help="Запрос для получения данных обо всех лабораторных работах")

    args = parser.parse_args()

    client = Client('http://localhost:8080')

    if args.get_all:
        asyncio.run(client.get_labs())

    if args.get:
        asyncio.run(client.get_lab(args.lab))

    if args.add and not args.date:
        print("Для добавления лабораторной работы требуется дедлайн(--date)")
    elif args.add and args.date:
        asyncio.run(client.add_lab(args.add, args.date))

    if args.edit and not (args.date or args.description or args.students):
        print("Для изменения лабораторной работы требуется изменяемый параметр --date --description или --students")
    elif args.edit:
        asyncio.run(client.edit_lab(args.edit, args.date, args.description, args.students))

    if args.remove:
        asyncio.run(client.remove_lab(args.lab))
