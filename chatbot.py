#pip install chatterbot

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("BOT")

conversation = [
'Hello',
'My name is bot. I am created by Pranjal Choudhary',
'I like ice-cream',
'I am doing great, what about you ?',
'Oh great to hear that',
'Sorry to hear that',
'I live in your computer',
'I am just a week year old',
'I speak only in english language',
'I have no idea how I am created, must be some genius',
'I like Drake',
'I love competitive programming',
'Thank you' ]

trainer = ListTrainer(bot)
trainer.train(conversation)

while True:
	print("You: ")
	ques = input()
	if ques == 'exit':
		break
	ans = bot.get_response(ques)
	print("Bot: ", ans)
