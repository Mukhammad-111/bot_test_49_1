from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot_config import database


dialog_router = Router()


class Dialog(StatesGroup):
    name = State()
    num_of_dz = State()
    link_to_github = State()


@dialog_router.message(Command("send_homework"))
async def start_dialog(message: types.Message, state: FSMContext):
    await message.answer("Можете отправить домашку ответив на несколько вопросов")
    await message.answer("Как вас зовут?")
    await state.set_state(Dialog.name)


@dialog_router.message(Dialog.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="1", callback_data="num:1"
                ),
                types.InlineKeyboardButton(
                    text="2", callback_data="num:2"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="3", callback_data="num:3"
                ),
                types.InlineKeyboardButton(
                    text="4", callback_data="num:4"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="5", callback_data="num:5"
                ),
                types.InlineKeyboardButton(
                    text="6", callback_data="num:6"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="7", callback_data="num:7"
                ),
                types.InlineKeyboardButton(
                    text="8", callback_data="num:8"
                )
            ]
        ]
    )
    await message.answer("Выберите номер дз", reply_markup=kb)
    await state.set_state(Dialog.num_of_dz)


@dialog_router.callback_query(Dialog.num_of_dz)
async def process_name(callback: types.CallbackQuery, state: FSMContext):
    num_of_dz = callback.data
    await state.update_data(num_of_dz=num_of_dz)
    await callback.message.answer("Оставте ссылку вашего репозиторию")
    await state.set_state(Dialog.link_to_github)


@dialog_router.message(Dialog.link_to_github)
async def process_name(message: types.Message, state: FSMContext):
    link_to_github = message.text
    await state.update_data(link_to_github=link_to_github)
    data = await state.get_data()
    await message.answer("Спасибо принято")
    print(data)
    database.save_home_works(data)
    await state.clear()



