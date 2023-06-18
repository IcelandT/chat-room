# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class ChatLog(Base):
    """ 聊天记录 """
    __tablename__ = "ChatLog"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(15), default=False, nullable=False, comment="名称")
    user_ip = Column(String(15), default=False, nullable=False, comment="地址")
    user_speak = Column(String(100), default=False, nullable=False, comment="内容")
    time = Column(DateTime, default=datetime.now)


class UserModel(Base):
    """ 用户登入 """
    __tablename__ = "User_information"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(15), default=False, nullable=False, unique=True, comment="名称")
    user_passwd = Column(String(200), nullable=False, comment="密码")

