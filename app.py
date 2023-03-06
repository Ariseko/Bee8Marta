from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from PIL import Image, ImageDraw, ImageFont
from keyboard import *
from datetime import datetime


import json
import requests


hookURL = 'https://hook.eu1.make.com/v6cmtv4v3op8r8nkxemhyffi36fqtvj8'
hookURL2 = 'https://hook.eu1.make.com/vf3wrnp93ddef1sw51lhwb0mcx9pe0db'
real_names = {}


class FSMtest(StatesGroup):
    getRealName = State()
    privet = State()
    znakomstvo = State()

    interviewStart = State()
    interviewStep1 = State()
    interviewStep2 = State()
    interviewStep3 = State()
    interviewStep4 = State()
    interviewStep5 = State()
    interviewStep6 = State()
    interviewStep7 = State()
    interviewStep8 = State()
    interviewStep9 = State()
    interviewStepFinal = State()
    interviewStepFinal1 = State()
    interviewStepFinal2 = State()
    interviewStepFinal3 = State()


storage = MemoryStorage()
bot = Bot(token='6197036926:AAEx55Rg-9GJM0sqnCpVsYxIOQIDNLcNG_Y')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    data = {
        'date': f'{dt_string}',
        'username': f'{message.from_user.username}',
    }
    r = requests.post(hookURL, data=json.dumps(data), headers={'Content-Type': 'application/json'})


    await message.answer('Привет, весенняя 🌸\n\nСегодняшний день – только твой! Давай сделаем его еще волшебнее?',
                         reply_markup=davai_kb)
    await FSMtest.privet.set()


@dp.callback_query_handler(state=FSMtest.privet)
async def privet(callback: types.CallbackQuery):
    photo = open('pics/interview/start.jpg', 'rb')
    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption='Впереди тебя ждёт 9 вопросов, благодаря которым мы познакомимся ближе 🧡',
                         parse_mode='html', reply_markup=poehali_kb)
    await callback.answer()

    await FSMtest.znakomstvo.set()


@dp.callback_query_handler(state=FSMtest.znakomstvo)
async def znakomstvo(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='<b>Но для начала немного формальностей ☺️</b>\nВпиши свои '
                                                       'реальные имя и фамилию:', parse_mode='html')

    await callback.answer()
    await FSMtest.getRealName.set()


@dp.message_handler(state=FSMtest.getRealName)
async def getRealName(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['A'] = 0
        data['B'] = 0
        data['C'] = 0
        data['D'] = 0


    photo = open('pics/interview/question1.jpg', 'rb')

    await bot.send_photo(message.chat.id, photo=photo, caption='1. Какое время года твоё любимое?',
                         reply_markup=interview_kb1)

    real_names.update({f'{message.from_user.id}': f'{message.text}'})

    await FSMtest.interviewStep1.set()


@dp.callback_query_handler(state=FSMtest.interviewStep1)
async def testStep1(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    async with state.proxy() as data:

        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id= callback.message.message_id, reply_markup=None)

    photo = open('pics/interview/question2.jpg', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photo, caption='2. Как выглядит твой идеальный отдых?',
                         reply_markup=interview_kb2)
    await FSMtest.interviewStep2.set()


@dp.callback_query_handler(state=FSMtest.interviewStep2)
async def testStep2(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    async with state.proxy() as data:

        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)
    photo = open('pics/interview/question3.jpg', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photo, caption='3. Что ты делаешь, когда тебе грустно?',
                         reply_markup=interview_kb3)
    await callback.answer()
    await FSMtest.interviewStep3.set()


@dp.callback_query_handler(state=FSMtest.interviewStep3)
async def testStep3(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    async with state.proxy() as data:

        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)
    photo = open('pics/interview/question4.jpg', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photo, caption='4. Как выглядит твой идеальный завтрак?',
                         reply_markup=interview_kb4)
    await callback.answer()
    await FSMtest.interviewStep4.set()


@dp.callback_query_handler(state=FSMtest.interviewStep4)
async def testStep4(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    async with state.proxy() as data:

        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)

    photo = open('pics/interview/question5.jpg', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photo, caption='5. На что ты прежде всего обращаешь внимание '
                                                                     'при первом знакомстве с человеком?',
                         reply_markup=interview_kb5)
    await callback.answer()
    await FSMtest.interviewStep5.set()


@dp.callback_query_handler(state=FSMtest.interviewStep5)
async def testStep5(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    async with state.proxy() as data:

        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)

    photo = open('pics/interview/question6.jpg', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photo, caption='6. Как ты обычно используешь парфюм?',
                         reply_markup=interview_kb6)
    await callback.answer()
    await FSMtest.interviewStep6.set()


@dp.callback_query_handler(state=FSMtest.interviewStep6)
async def testStep6(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    async with state.proxy() as data:

        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)

    photo = open('pics/interview/question7.jpg', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photo, caption='7. Что ты считаешь залогом крутой вечеринки?',
                         reply_markup=interview_kb7)
    await callback.answer()
    await FSMtest.interviewStep7.set()


@dp.callback_query_handler(state=FSMtest.interviewStep7)
async def testStep7(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    async with state.proxy() as data:

        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)

    photo = open('pics/interview/question8.jpg', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photo, caption='8. Как ты относишься к модным трендам?',
                         reply_markup=interview_kb8)
    await callback.answer()
    await FSMtest.interviewStep8.set()


@dp.callback_query_handler(state=FSMtest.interviewStep8)
async def testStep8(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    async with state.proxy() as data:

        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)

    photo = open('pics/interview/question9.jpg', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photo, caption='9. Твои планы на ближайшие выходные:',
                         reply_markup=interview_kb9)
    await callback.answer()
    await FSMtest.interviewStep9.set()


@dp.callback_query_handler(state=FSMtest.interviewStep9)
async def testStep9(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    async with state.proxy() as data:

        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

        sum = {
            'A': f'{data["A"]}',
            'B': f'{data["B"]}',
            'C': f'{data["C"]}',
            'D': f'{data["D"]}',
        }

        answerTotal = max(sum, key=sum.get)
        print(answerTotal)

    await callback.answer()

    if answerTotal == 'A':
        congratsText = 'Если говорить о женщинах-обольстительницах, которые не боятся быть в центре внимания, ' \
                       'то это очевидно твой тип. Ты никогда не боялась выделяться из толпы и спокойно носишь сложные ' \
                       'композиции, которые не рискнуло бы использовать большинство обычных людей. Твоей страстной ' \
                       'натуре нужны яркие насыщенные духи, будоражащие сознание. Поэтому тебе отлично подойдет ' \
                       '<b>восточный</b> парфюм. \n\nНапример: Восточные - Shalimar, Guerlain, MUGLER les exceptions ' \
                       'oriental extreme, ETRO ambra'

    elif answerTotal == 'B':
        congratsText = 'Ты дерзкая, яркая и жизнерадостная натура. Настоящая душа компании, которая смело идёт ' \
                       'навстречу новым идеям и свежим впечатлениям. Подчеркнуть твой характер смогут сочные, ' \
                       'в меру сладкие, искрящиеся <b>фруктовые композиции</b> – ведь с ними ты и сама почувствуешь ' \
                       'себя лакомым кусочком. \n\nНапример: Clinique Happy, Burberry My Burberry Blush, ' \
                       'Vilhelm Parfumerie Mango Skin, Annick Goutal Petite Cherie'

    elif answerTotal == 'C':
        congratsText = 'Ты абсолютно уверена в себе и своих силах. Твоя активная жизненная позиция не терпит суеты, ' \
                       'а все твои шаги всегда логичны и хорошо продуманы. При этом ты не боишься условностей и ' \
                       'любишь экспериментировать со стилем. Мы уверены, что ты можешь смело позволить себе ' \
                       'использовать <b>древесные нотки</b> в стиле унисекс.\n\n Например: Tiffany & Love For Her, ' \
                       'ESCENTRIC MOLECULES molecule 03, Woodissime, Mugler.'

    else:
        congratsText = 'Нет более нежной, мечтательной и утончённой натуры, чем ты. Как настоящий романтик, ты умеешь ' \
                       'создавать домашний уют и веришь в настоящую любовь. Твою женственность хорошо подчеркнут ' \
                       '<b>цветочные нотки</b>. Прислушайся к ним: среди великого разнообразия флористических ' \
                       'композиций можно найти и нежные, и классические, и чувственные аккорды.\n\nНапример: DIOR ' \
                       'Forever And Ever, GIORGIO ARMANI PRIVE PIVOINE SUZHOU, Innocente Fragilite, Chabaud'

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)

    image = Image.open(f"pics/results/{answerTotal}.jpg")

    font = ImageFont.truetype("font/BeelineSans-Regular.ttf", 40)
    boldFont = ImageFont.truetype("font/BeelineSans-Bold.ttf", 40)
    drawer = ImageDraw.Draw(image)

    name = real_names[f'{callback.from_user.id}']

    drawer.text((1388 // 2, 400), f"{name.upper()},", anchor='mm', font=boldFont, fill='white')
    drawer.text((1388 // 2, 445), f"обрати внимание на эти ароматы", anchor='mm', font=font, fill='white')

    image.save(f'peoplePics/new_{callback.from_user.id}_img.png')

    photo = open(f'peoplePics/new_{callback.from_user.id}_img.png', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photo, reply_markup=next_kb, caption=congratsText,
                         parse_mode='html')
    await FSMtest.interviewStepFinal.set()


@dp.callback_query_handler(state=FSMtest.interviewStepFinal)
async def finish1(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id, text='Как здорово было узнать о тебе столько нового! Ты '
                                                               'просто невероятная 💫', reply_markup=next_kb)

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)

    await FSMtest.interviewStepFinal1.set()
    await callback.answer()


@dp.callback_query_handler(state=FSMtest.interviewStepFinal1)
async def finish2(callback: types.CallbackQuery):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    data = {
        'date': f'{dt_string}',
        'username': f'{callback.from_user.username}',
    }
    r = requests.post(hookURL2, data=json.dumps(data), headers={'Content-Type': 'application/json'})

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)

    photo = open(f'pics/interview/final.jpg', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption='На память об этом дне лови самый весенний стикерпак 🌷', reply_markup=sticker_kb)

    await FSMtest.interviewStepFinal2.set()
    await callback.answer()


@dp.callback_query_handler(state=FSMtest.interviewStepFinal2)
async def again(callback: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)
    await bot.send_message(chat_id=callback.from_user.id, text='Хочешь пройти тест заново?', reply_markup=fork_kb)
    await callback.answer()
    await FSMtest.interviewStepFinal3.set()


@dp.callback_query_handler(state=FSMtest.interviewStepFinal3)
async def fork(callback: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)
    if callback.data == 'false':
        await bot.send_message(chat_id=callback.from_user.id, text='Окей) Хорошо проведи время!')
        await callback.answer()
        await state.finish()
    else:
        photo = open('pics/interview/question1.jpg', 'rb')

        await bot.send_photo(callback.from_user.id, photo=photo, caption='1. Какое время года твоё любимое?',
                             reply_markup=interview_kb1)
        await callback.answer()
        await FSMtest.interviewStep1.set()


executor.start_polling(dp, skip_updates=True)
