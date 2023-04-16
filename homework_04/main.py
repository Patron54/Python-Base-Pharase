"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from models import engine, Session, User, Post, Base
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def load_users_data():
    users_data = await fetch_users_data()
    users = [
        User(name=user["name"], username=user["username"], email=user["email"])
        for user in users_data
    ]
    async with Session() as s:
        s.add_all(users)
        await s.commit()

async def load_posts_data():
    posts_data = await fetch_posts_data()
    posts = [
        Post(user_id=post["userId"], title=post["title"], body=post["body"])
        for post in posts_data
    ]
    async with Session() as s:
        s.add_all(posts)
        await s.commit()

async def async_main():
    await create_tables()
    await asyncio.gather(load_users_data(), load_posts_data())


def main():
    asyncio.run(async_main())
    Session.close()


if __name__ == "__main__":
    main()
