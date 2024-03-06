from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    save_photo = State()
    blure = State()
    sharpen = State()
