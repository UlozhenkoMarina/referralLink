import json
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.webhook import KickChatMember

import config
import replies
import aiohttp

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

#function for getting user identifier and name by referral_link
#input str:referral_link
#output json{int:id, str:name}
async def getIdByUrl (referral_link):
   async with aiohttp.ClientSession() as session:
       async with session.get(config.getUserByLinkUrl+referral_link+'/') as response:
            return await response.json()

#function for getting frequency of referral_link by user
#input int:chat_id, str:referral_link
#output json{int:amount}
async def getAmountByChat (chat_id, referral_link):
   async with aiohttp.ClientSession() as session:
       async with session.get(config.getFrequencyByChat+str(chat_id)+'/'+referral_link+'/') as response:
            return await response.json()

#function for increasing frequency of referral_link by user
#input int:chat_id, str:referral_link
async def postFrequencyByUser(chat_id, referral_link):
    async with aiohttp.ClientSession() as session:
        async with session.get(config.postFrequencyByChat +str(chat_id) + '/' + referral_link + '/'):
            pass

#function for sending message for incorrect referral_link and blocking user if frequency > config.maxIncorrectLink
#input Message:message, str:referral_link
async def incorrectLink(message, referral_link):
    amount = await getAmountByChat(message.chat.id, referral_link)
    if amount['amount'] < config.maxIncorrectAmount:
        await postFrequencyByUser(message.chat.id, referral_link)
        await message.reply(replies.replIncorrectLink)
    else:
         await KickChatMember(chat_id=message.chat.id, user_id=message.from_user.id).get_response()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    referral_link = message.text.replace("/start ", '')
    #checking if referral link meets requirements
    if len(referral_link) != 8 or not referral_link.isdecimal():
        await incorrectLink(message, referral_link)
        return
    #replying for starting without using referral link
    if referral_link == '':
        await message.reply(replies.replWithoutLink)
    else:
         res = await getIdByUrl(referral_link)
         if res['id'] != -1:
             #replying for using correct referral link
            await message.reply(replies.replCorrectLink.format(res['name'], res['id']))
         else:
            #replying for using incorrrect referral link
            await incorrectLink(message, referral_link)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)