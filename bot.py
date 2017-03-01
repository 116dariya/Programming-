import telegram 
import requests 
from bs4 import BeautifulSoup

bot = telegram.Bot(token='349951978:AAE5PtJ1E9VVcTptchBIHcxT_bbQMdqTABc')
updates = bot.getUpdates()
for update in updates:
	print(update.message.text)
	print(update.message.from_user.first_name)

from telegram.ext import Updater
updater = Updater(token='349951978:AAE5PtJ1E9VVcTptchBIHcxT_bbQMdqTABc')
dispatcher = updater.dispatcher

from telegram.ext import CommandHandler
'''
def lolo(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text="всмысле сразу???")

from telegram.ext import CommandHandler
start_handler = CommandHandler('na_donyshke', lolo)
dispatcher.add_handler(start_handler)
'''

def gas(bot, update):
	url = "http://helios.kz/toplivo/tseny-na-benzin/"
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	search = soup.select("#petroil-prices li")[0]
	petroil = search.select("span.name")[0].text
	price = search.select("span.value")[0].text
	wtext = petroil + " - " + price
	bot.sendMessage(chat_id = update.message.chat_id, text= wtext)


gas_handler = CommandHandler('petrol', gas)
dispatcher.add_handler(gas_handler)
'''
def kurs(bot, update):

	url = "http://kurstenge.kz"
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	rows = soup.select("#content table table tr")[:3]
	for tr in rows:
		name = tr.select("td a")[0].text
		rate = float(tr.select("td span.today")[0].text.replace(",", "."))
		wtex = name + " - " + rate
		bot.sendMessage(chat_id = update.message.chat_id, text= wtext)
'''
def kurs(bot, update):
	url = "http://kurstenge.kz"
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	rows = soup.select("#content table table tr")[0]
	name = rows.select("td a")[0].text
	rate = rows(tr.select("td span.today")[0].text.replace(",", "."))
	wtex = name + " - " + str(rate)
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)



kurs_handler = CommandHandler('kurs',kurs)
dispatcher.add_handler(kurs_handler)


updater.start_polling()


