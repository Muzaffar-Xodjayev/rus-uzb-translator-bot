from aiogram.dispatcher.filters.state import State, StatesGroup


class Message(StatesGroup):
    text = State()


class Channel(StatesGroup):
    body = State()
