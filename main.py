import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import hide_link
# from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import random
good = ["хорош", "клас", "прекрасно", "здоров", "ок","отлично"]
positive_messages = ["у меня тоже", "прекрасно", "здорово","отлично"]
storage = MemoryStorage()
bad = ["плох","ужас","груст"," отврат"]
bad_messages = ["жаль","досадно"]
f = ['Факт о гарри поттере №1/n',"До 2008-го года было продано более 400 миллионов экземпляров книг о Гарри Поттере, и они были переведены на 67 языков./n"]
g = ['Факт о гарри поттере №2/n','Когда «Назад в Будущее» вышел в кино в Австралии, Майклу Джей Фоксу пришлось сняться в телевизионном ролике для австралийского телевидения и предупредить общественность об опасности цепляния за автомобили на скейтборде.\n']
d = ['Факт о гарри поттере №3/n','Имя Волдеморт происходит от французских слов, означающих "бегство от смерти", и его основной целью является победа над смертью. Во втором романе о Гарри Поттере Роулинг показывает, что фраза "I am Lord Voldemort" – это анаграмма от "Tom Marvolo Riddle", что было его настоящим именем./n']
s = ['Факт о гарри поттере №4/n','Романах о Гарри Поттере цвета играют очень важную роль. Например, оттенки красного цвета символизируют доброту и великодушие. Эти оттенки можно увидеть в красной одежде факультета Хогвартса – Гриффиндора. Также красный цвет присутствует в красных чернилах Гарри и малиновом поезде-экспрессе в Хогвартс. У семьи Уизли – рыжие волосы и красная крыша дома. Зеленый же постоянно ассоциируется с негативными событиями./n']
r = ["Факт о гарри поттере №1 \n,До 2008-го года было продано более 400 миллионов экземпляров книг о Гарри Поттере, и они были переведены на 67 языков.\n",
     "Факт о Назад в Будущее №2 \n','Когда «Назад в Будущее» вышел в кино в Австралии, Майклу Джей Фоксу пришлось сняться в телевизионном ролике для австралийского телевидения \n и предупредить общественность об опасности цепляния за автомобили на скейтборде.\n"]
inline_btn_1 = InlineKeyboardButton('Гарри Поттер', callback_data='button1')
inline_btn_2 = InlineKeyboardButton("Властелин колец", callback_data='button2')
inline_btn_3 = InlineKeyboardButton("да", callback_data='button3')
inline_btn_4 = InlineKeyboardButton("нет", callback_data='button4')
inline_btn_5 = InlineKeyboardButton("38", callback_data='vrant_1')
inline_btn_7 = InlineKeyboardButton("37", callback_data='vrant_2')
inline_btn_8 = InlineKeyboardButton("36", callback_data='otvet1')
inline_btn_9 = InlineKeyboardButton("33", callback_data='vrant_3')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_3, inline_btn_4)
inline_kb3 = InlineKeyboardMarkup(row_width=2).add(inline_btn_5, inline_btn_7, inline_btn_8, inline_btn_9)



class States(StatesGroup):
    dela = State()  # Will be represented in storage as 'Form:name  # Will be represented in storage as 'Form:gender'
    stets2 = State()
    test_stet = State()
    fact_stet = State()
    test_g_1  = State()
    otvet_1 = State()
    vopros2 = State()
    otvet_2 = State()


bot = Bot(token="5819552530:AAHoHsDzP_QwETxdK1ICtbSnED0oCxLbNXA")
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет я кинобот, как дела?")
    await States.dela.set()


@dp.message_handler(state=States.dela)
async def dela(message: types.Message, state):
    await state.update_data(dela=message.text)
    answer = await state.get_data()
    value = answer["dela"].strip().lower()
    if sum([value.find(i)!=-1 for i in good]):
        await message.answer(random.choice(positive_messages))
        if random.choice([True, False]):
            await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG_59jqGSH1Kht1f396OvVF5Fr3X5TyQACkCQAAtAYSEl1lgatPhR9tiwE")
        else:
            await bot.send_message(message.chat.id, text="😌")
        await message.answer("хочешь порешать тесты о фильмах или узнать интересные факты о них")
        await States.stets2.set()
    elif sum([value.find(i)!=-1 for i in bad]):
        await message.answer(random.choice(bad_messages))
        if random.choice([True, False]):
            await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG_6FjqGS5L4I-u1TSgl0emKBRmbPldAACgSUAAkPCSEnndj5CbFMtjiwE")
        else:
            await bot.send_message(message.chat.id, text="😭")
        await message.answer("хочешь порешать тесты о фильмах или узнать интересные факты о них")
        await States.stets2.set()

    else:
        await message.answer("что это, я не знаю помоги")
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG_6NjqGUhKyqVEIqKqAaxRV3o5gOgowACqCMAArIxQUkzscbk9NCHLSwE")


@dp.message_handler(state=States.stets2)
async def test_fact(message: types.Message, state):
    await state.update_data(stets2=message.text)
    answer = await state.get_data()
    value = answer["stets2"].strip().lower()
    if sum([value.find(i)!=-1 for i in ["тест"]]):
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG_6hjqGWatiQkyexNzdOzQ0GwCoBS7QACkCUAAv-NQEnoUdcdJFKzZywE")
        await message.answer("ПОДТВЕРДИТЕ")
        await States.test_stet.set()
    elif sum([value.find(i)!=-1 for i in ["факт"]]):
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG_7JjqGZgQhH4BPLCSblRpanOtx572AAC4x8AAimVQElccyotxFi3hiwE")
        await message.answer("ПОДТВЕРДИТЕ")
        await States.fact_stet.set()


@dp.message_handler(state=States.test_stet)
async def test_fact(message: types.Message, state):
    await state.update_data(stets2=message.text)
    await message.answer("выберите свой тест: Гарри Поттер или Властелин колец")
    await States.test_g_1.set()

#Первый вопрос

@dp.message_handler(state=States.test_g_1)
async def test_GP(message: types.Message, state):
    await state.update_data(test_g_1 = message.text)
    answer = await state.get_data()
    value = answer["test_g_1"].strip().lower()
    if value == "гарри поттер":
        await message.answer("Первый вопрос\nСколько подарков изначально подарили Дадли Дурслю на его одиннадцатилетней?\n38  36\n37   35 ")
        await States.otvet_1.set()
    else:
        await message.answer("нет")


@dp.message_handler(state=States.otvet_1)
async def test_GP(message: types.Message, state):
    await state.update_data(otvet_1=message.text)
    answer = await state.get_data()
    value = answer["otvet_1"].strip().lower()
    if value == "36":
        await message.answer("Лучший знаток!")
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG_79jqGcjTip9LYNgya6jsvz_u_NWZwAC4x8AAimVQElccyotxFi3hiwE")
        await message.answer("продолжим?")
        await States.vopros2.set()
    else:
        await message.answer("Неправильно, но не здавайся, продолжай!")
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG_7tjqGbA7ELPPJejrnRj0xvERdwRpgACkCQAAtAYSEl1lgatPhR9tiwE")

#Второй вопрос

@dp.message_handler(state=States.vopros2)
async  def vopros1_2(message: types.Message, state):
    await state.update_data(vopros2=message.text)
    answer = await state.get_data()
    value = answer["vopros2"].strip().lower()
    if value == "да":
        await message.answer("Второй вопрос\nЧто было у Рубеуса Хагрида вместо волшебной палочки? \nПодвеска  Фляжка\nПосох   Зонтик ")
        await States.otvet_2.set()
    elif value == "нет":
        await message.answer("потвердите")
        await States.stets2.set()


@dp.message_handler(state=States.otvet_2)
async def test_GP(message: types.Message, state):
    await state.update_data(otvet_2=message.text)
    answer = await state.get_data()
    value = answer["otvet_2"].strip().lower()
    if value == "зонтик":
        await message.answer("Очень здорово!")
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG_79jqGcjTip9LYNgya6jsvz_u_NWZwAC4x8AAimVQElccyotxFi3hiwE")
        await message.answer("продолжим?")
        await States.vopros2.set()
    else:
        await message.answer("Неправильно, но ничего страшного! Продолжай делать!")
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG_7tjqGbA7ELPPJejrnRj0xvERdwRpgACkCQAAtAYSEl1lgatPhR9tiwE")

#Конец второго вопроса




@dp.message_handler(state=States.fact_stet)
async def fact(message: types.Message, state):
    await state.update_data(fact_stet=message.text)
    a = random.choice(r)
    await message.answer(f"{a}")
    await States.stets2.set()





if __name__ == '__main__':
    executor.start_polling(dp)