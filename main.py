import logging
import json
import os
from aiogram import Bot, Dispatcher, executor, types
from config import token

bot = Bot(token=token)

dp = Dispatcher(bot)
if not os.path.exists(f'{os.getcwd()}\\Data'):
    os.mkdir(f'{os.getcwd()}\\Data')

@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    # if not os.path.exists(f'{os.getcwd()}\\Data\\{message.from_user.id}'):
    #     os.mkdir(f'{os.getcwd()}\\Data\\{message.from_user.id}')
    global student_group
    global subgrp
    global engl
    engl = 1
    subgrp = 1
    student_group = 1

    # with open(f"{os.getcwd()}\\Data\\{message.from_user.id}\\id.json", "w") as file:
    #     json.dump(data, file, sort_keys=True, indent=4)
    #     print(json.dumps(data, sort_keys=True, indent=4))
    # json_data = {"id": message.from_user.id, 'Group': student_group, 'LSubgroup': subgrp, 'ESubgroup': engl}
    try:
        with open(f'{os.getcwd()}\\Data\\{message.from_user.id}.json', 'r') as f:
            json_data = json.load(f)
            json_data['ESubgroup'] = engl
    except:
        with open(f'{os.getcwd()}\\Data\\{message.from_user.id}.json', 'w') as f:
            json_data = {"id": "", 'Group': "", 'LSubgroup': "", 'ESubgroup': ""}
            json_data['ESubgroup'] = engl


    with open(f'{os.getcwd()}\\Data\\{message.from_user.id}.json', 'w') as f:
        f.write(json.dumps(json_data))

    await message.answer(f"Ваш ID: {message.from_user.id}")

@dp.message_handler(commands=['return'])
async def alarm(message: types.Message):
    # with open(f"{os.getcwd()}\\Data\\{message.from_user.id}.json", "r") as file:
    #     data = json.load(file)
    #     student_group = data["Group"]
    #     subgrp = data['LSubgroup']
    #     engl = data['ESubgroup']
    #     print(data)
    # await message.answer(f"Ваш ID: {message.from_user.id}")

    # with open(f'{os.getcwd()}\\Data\\{message.from_user.id}.json', 'r') as f:
    #     json_data = json.load(f)
    #     json_data['ESubgroup'] = engl
    #
    # with open('my_file.json', 'w') as f:
    #     f.write(json.dumps(json_data))

    await message.answer("G")



if __name__ == '__main__':
    executor.start_polling(dp)
