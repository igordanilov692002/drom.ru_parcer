from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    finding_car = State()
    finding_lorry = State()
    finding_Elevator = State()