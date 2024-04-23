from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from creds import main
from keyboards import reply
from auth import main as auth

dp = main.dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode="HTML")
    await message.answer('Hello World! I am live!', reply_markup=reply.main_menu())


@dp.message(Command("poll"))
async def poll(msg: types.Message):
    cid = msg.from_user.id
    await main.bot.send_poll(
        chat_id=cid,
        question="Test Question",
        options=["One", "Two"],
        type="regular",
        is_anonymous=False,
        allows_multiple_answers=True
    )


@dp.message(Command("admin"))
async def welcome_admin(msg: types.Message):
    if auth.is_admin(msg.from_user.id):
        await msg.answer("Вітає вам у режимі адміністратора", reply_markup=reply.admin_main())
    else:
        await msg.answer("You haven't access!", reply_markup=reply.main_menu())