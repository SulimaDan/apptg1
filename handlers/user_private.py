from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
from telegram import Update
import random
from telegram import Update
from telegram.ext import CallbackContext

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user.full_name}")

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("I'n a siple bot that can greet you. Just type /start to start")

@router.message(F.photo)
async def get_photo(message:Message):
    await message.reply('This is photo but i need help to you')

@router.message(F.text == "Hello")
async def answer_hello(message: Message):
    await message.answer("Hello! How are you?")
    
    





greetings = [
    "Привіт!", 
    "Добрий день!", 
    "Здоровенькі були!", 
    "Радий бачити!", 
    "Привіт-привіт!"
]

farewells = [
    "До побачення!", 
    "Бувай!", 
    "До зустрічі!", 
    "Щасти!", 
    "Прощавай!"
]


def greet_user(update: Update, context: CallbackContext):
    random_greeting = random.choice(greetings)
    update.message.reply_text(random_greeting)


def farewell_user(update: Update, context: CallbackContext):
    random_farewell = random.choice(farewells)
    update.message.reply_text(random_farewell)

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if any(greet in text for greet in ["привіт", "здравствуйте", "добрий день", "здорово", "хай"]):
        greet_user(update, context)
    elif any(farewell in text for farewell in ["до побачення", "бувай", "прощай", "прощавай", "до зустрічі"]):
        farewell_user(update, context)
    else:
        update.message.reply_text("Не розумію, що ти маєш на увазі.")


    