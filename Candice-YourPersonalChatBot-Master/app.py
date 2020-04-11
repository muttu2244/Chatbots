from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Nous", preprocessors=['chatterbot.preprocessors.clean_whitespace','chatterbot.preprocessors.unescape_html','chatterbot.preprocessors.convert_to_ascii'],
              logic_adapters=["chatterbot.logic.BestMatch", "chatterbot.logic.TimeLogicAdapter","chatterbot.logic.MathematicalEvaluation","chatterbot.logic.SpecificResponseAdapter","chatterbot.logic.UnitConversion"])
conversation = [
    "Hello","Hi there!","That is good to hear","Thank you.","You're welcome.",'What is your name?','My name is Nous','Who are you?',
    'I am a bot','Who created you?','Nous',
    'Where can I buy car insurance?',
    'There are many national and local insurance companies that offer car insurance. Many of these insurers sell other insurance products as well, and may offer discounted rates to policyholders who buy multiple policies from them',
    'How much does car insurance cost?', 'Car insurance rates depend on a number of factors. These include: \
     Personal details like age, sex, and marital status ,Where you live Average annual distance driven , Your vehicle , Your credit, Your coverage amount and type ,'
    'According to the Insurance Information Institute, the average annual car insurance cost was around $866 dollars in 2014.',
    'Is car insurance mandatory?', 'Yes',
    'When should I buy car insurance?', 'You should buy auto insurance before you begin driving, as it’s required in most states (see below). Driving without insurance is often illegal and leaves you financially vulnerable.',
    'Does my vehicle affect my car insurance rates?', 'Yes',
    'What car insurance discounts are available?', 'Available discounts depend on your insurer. However, common car insurance discounts include various affiliation discounts, reduced rates for students, good driver/no-accident discounts, and hybrid vehicle discounts.',
    'What does car insurance cover?', 'Your car insurance coverage depends on the type of policy you purchase',
    'Does my car insurance cover other drivers?','It depends on the specific policy','Does car insurance cover rental cars?','Comprehensive and collision coverage extends to rental cars, while liability insurance does not.',
    'How is the premium determined?','Many factors determine the premium you will pay','What coverage limits meet my needs?','The sum insured for the vehicle is called “Insured’s Declared Value” and should reflect the current market value of the vehicle',
    'What is the period of the policy?','1 year','Is Service Tax applicable and how much is it?','Yes, Service Tax is applicable and would be as per prevailing rule of law.',
    'I have lost the insurance policy. Can I get a duplicate one?','Yes, please approach the same office, which had issued the policy, with a written request. A nominal fee is charged for issuing a duplicate policy copy.',

]

trainer = ListTrainer(bot)

trainer.train(conversation)

'''
bot.set_trainer(ListTrainer)
bot.train(['What is your name?', 'My name is Candice'])
bot.train(['Who are you?', 'I am a bot' ])
bot.train(['Do created you?', 'Tony Stark', 'Sahil Rajput', 'You?'])
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")
'''


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True,port = 5500)
