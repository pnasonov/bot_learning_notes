"""Lesson - callback data count and random number"""
import sys

sys.path.append("..")
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)
number = 0


def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Increase", callback_data="btn_increase"),
                InlineKeyboardButton(text="Decrease", callback_data="btn_decrease"),
            ],
            [InlineKeyboardButton(text="Random", callback_data="btn_random")],
        ]
    )

    return ikb


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await message.answer(
        text=f"Current number{number}", reply_markup=get_inline_keyboard()
    )


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("btn"))
async def ikb_callback_handler(callback: types.CallbackQuery) -> None:
    global number

    if callback.data == "btn_increase":
        number += 1
        await callback.message.edit_text(
            f"The current number is {number}", reply_markup=get_inline_keyboard()
        )

    elif callback.data == "btn_decrease":
        number -= 1
        await callback.message.edit_text(
            f"The current number is {number}", reply_markup=get_inline_keyboard()
        )
    elif callback.data == "btn_random":
        number = random.randint(1, 59)
        await callback.message.edit_text(
            f"The current number is {number}", reply_markup=get_inline_keyboard()
        )
    else:
        1 / 0


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
