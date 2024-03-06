import Main, Keyboard
from aiogram import types, F, Router
import Gen
import asyncio
from hashlib import md5
import os
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from PIL import Image, ImageFilter
from aiogram.types import Message, FSInputFile, CallbackQuery,ContentType, BufferedInputFile
from aiogram import flags
from mysql.connector import connect
import urllib
from db import data_b_recieve, data_b_add
import shelve
import os


SESSION = []
STEP = 0
all_map_img_count = 0


router = Router()

@router.message(Command("image"))
async def upload_photo(msg: Message):
    await msg.answer("ewfv3")
    '''
    photo = msg.photo[0]
    id = photo.file_id
    file = await Main.bot.get_file(id)
    file_path = file.file_path
    absolut_path = os.path.dirname(__file__) + "\\" + os.path.normpath(file_path.split("/")[-1])
    ext = os.path.normpath(file_path.split("/")[-1])
    urllib.request.urlretrieve(f"http://api.telegram.org/file/bot{Main.TOKEN}/{file_path}", absolut_path)
    #await msg.answer(absolut_path)
    '''
    
    img = open(r"C:\Users\salim\Imagin\imagination\file_81.jpg", "rb")
    try:
        await msg.answer_photo(
        BufferedInputFile(file=img.read(), filename="my_file"),
        caption="Размазанное изображение"
        )

    except Exception as e:
        print(e)
    else:
        print("OK")





@router.message(Command("start"))
async def start(msg: Message):
    SESSION.clear()
    await msg.answer("Добро пожаловать!!!" + str(SESSION), reply_markup=Keyboard.menu_link)


@router.message(F.text=="Вперед")
async def next(msg: Message):
    global STEP
    if len(SESSION) == 0:
        await answer("Загрузите изображение")
    elif len(SESSION) == 1:
        await msg.answer("В данный момент только одно изображение ")
    elif len(SESSION) > 1 and STEP < len(SESSION):
        img_file = open(SESSION[STEP][0], "rb")
        STEP += 1
        try:
            await msg.answer_photo(
        BufferedInputFile(file=img_file.read(), filename="my_file"),
        caption="Размазанное изображение", reply_markup=Keyboard.menu
        )
    

        except Exception as e:
            print(e)
        else:
            print("OK")
        
    elif len(SESSION) > 1 and STEP == len(SESSION):
        await msg.answer("Это последнее изображение")
    await msg.answer(f"step - {STEP}, len _session{len(SESSION)}")


@router.message(F.text == "Назад")
async def back(msg: Message):
    global STEP
    if len(SESSION) == 0:
        await answer("Загрузите изображение")
    elif len(SESSION) == 1:
        await msg.answer("В данный момент только одно изображение ")
    elif len(SESSION) > 1 and (STEP == 1 or STEP == 0):
        await msg.answer("Это  первое изображение")
    elif len(SESSION) > 1 and STEP > 1:
        img_file = open(SESSION[STEP-2][0], "rb")
        STEP -= 1
        try:
            await msg.answer_photo(
        BufferedInputFile(file=img_file.read(), filename="my_file"),
        caption="Размазанное изображение", reply_markup=Keyboard.menu
        )
    

        except Exception as e:
            print(e)
        else:
            print("OK")
        
    
    await msg.answer(f"step - {STEP}, len _session{len(SESSION)}")


@router.message(F.text == "Первое изображение")
async def first(msg: Message):
    img_file = open(SESSION[0][0], "rb")
    try:
        await msg.answer_photo(
        BufferedInputFile(file=img_file.read(), filename="my_file"),
        caption="Размазанное изображение"
        )
    except Exception as e:
            print(e)
    else:
            print("OK")


@router.message(F.text == "Действия")
async def load_img(msg: Message, state: FSMContext):
    await msg.answer("Выберите действие", reply_markup=Keyboard.menu)


@router.message(F.photo)
async def load_photo(msg: Message, state: FSMContext):
    global STEP
    count = 1
    photo = msg.photo[0]
    file_id = photo.file_id
    file = await Main.bot.get_file(file_id)
    file_path =  file.file_path
    abs_path_to_file = os.path.dirname(__file__) + "\\" + os.path.normpath(file_path.split("/")[-1])
    urllib.request.urlretrieve(f"http://api.telegram.org/file/bot{Main.TOKEN}/{file_path}", abs_path_to_file)
    if SESSION:
        for i in SESSION:
            if i[0] == abs_path_to_file:
                count = count + 1
            else:
                pass
        SESSION.append((abs_path_to_file, count , " "))
    else:
        SESSION.append((abs_path_to_file, 1, " "))
    STEP += 1
    await msg.answer("Операции:" + str(SESSION), reply_markup=Keyboard.menu)





@router.callback_query(F.data=="smooth")
async def smooth(lb: CallbackQuery):
    global SESSION, STEP, all_map_img_count
    await asyncio.sleep(2)
    img_file = Image.open(SESSION[STEP-1][0])
    new_path = str(img_file.fp.name.split("\\")[:-1]) + str(all_map_img_count) + str(img_file.fp.name.split("\\")[-1])
    img_file = img_file.filter(ImageFilter.SMOOTH)
    img_file.save(new_path)
    SESSION.append((new_path, 1))
    STEP += 1
    img_file = open(new_path, "rb")
    all_map_img_count += 1
    try:
        await lb.message.answer_photo(
        BufferedInputFile(file=img_file.read(), filename="my_file"), reply_markup=Keyboard.menu
        )
    except Exception as e:
            print(e)
    else:
            print("OK")
    
 
@router.callback_query(F.data == "sharp")
async def sharp(lb: CallbackQuery):
    global SESSION, STEP, all_map_img_count
    img_file = Image.open(SESSION[STEP-1][0])
    new_path = str(img_file.fp.name.split("\\")[:-1]) + str(all_map_img_count) + str(img_file.fp.name.split("\\")[-1])
    img_file = img_file.filter(ImageFilter.SMOOTH)
    img_file.save(new_path)
    SESSION.append((new_path, 1))
    STEP += 1
    img_file = open(new_path, "rb")
    try:
        await lb.message.answer_photo(
        BufferedInputFile(file=img_file.read(), filename="my_file"), reply_markup=Keyboard.menu
        )
    except Exception as e:
            print(e)
    else:
            print("OK")

@router.callback_query(F.data == "blur")
async def blur(lb: CallbackQuery):
    global SESSION, STEP, all_map_img_count
    img_file = Image.open(SESSION[STEP-1][0])
    new_path = str(img_file.fp.name.split("\\")[:-1]) + str(all_map_img_count) + str(img_file.fp.name.split("\\")[-1])
    img_file = img_file.filter(ImageFilter.SMOOTH)
    img_file.save(new_path)
    SESSION.append((new_path, 1))
    STEP += 1
    img_file = open(new_path, "rb")
    try:
        await lb.message.answer_photo(
        BufferedInputFile(file=img_file.read(), filename="my_file"), reply_markup=Keyboard.menu
        )
    except Exception as e:
            print(e)
    else:
            print("OK")


@router.callback_query(F.data == "cut")
async def cut(lb: CallbackQuery, fsm: FSMContext):
    await lb.message.answer("Перейдите по ссылке для обрезки фото")

@router.callback_query(F.data == "increas")
async def increas(lb: CallbackQuery, fsm: FSMContext):
    pass

@router.callback_query(F.data == "reduce")
async def reduce(lb: CallbackQuery, fsm: FSMContext):
    await lb.messag.answer("Введите число на которое вы хотите уменьшить или увеличить изображение")

@router.callback_query(F.data == "past")
async def past(lb: CallbackQuery, fsm: FSMContext):
    await lb.message.answer("Перейдите по ссылке для всталения изображения поверх картинки")


