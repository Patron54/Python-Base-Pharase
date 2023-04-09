"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True, pool_size=20)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index =True)
    name = Column(String, nullable = False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index =True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)

    user = relationship("User", back_populates="posts")