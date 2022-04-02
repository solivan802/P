from flask import Flask,request
import json
from bot import Bot

PAGE_ACCESS_TOKEN = 'EAAEKSC8Gt98BACMUATFucv852wKlYEqcRTgOgsgT1BiS0t5zYzLjwyAezyUFlN24SNFh2gcTZCtCAn9YCJuwXo7FsfXRx5hMLZCsKhb9Jc4rkn8GRyCFmDYAnkFzy5sLFZA8hAP1qomZCh8NfGPbAKfTU148qLMlnToF1AXmXCN1fIRPzEPk'
Greetings = ['Empezar','hi', 'hello', 'how are you?']
data = (('job role', 'job description', 'https://joblink', '+23412345678'), ('job role', 'job description', 'https://joblink', '+23412345678'), ('job role', 'job description', 'https://joblink', '+23412345678'))

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get("hub.verify_token")
        challenge = request.args.get('hub.challenge')
        if token == 'secret':
            return str(challenge)
        return '400'
    else:
        print(request.data)


        data = json.loads(request.data)
        #messaging_event = data['entry'][0]['messaging']
        bot = Bot(PAGE_ACCESS_TOKEN)
        #for message in messaging_event:
            #user_id = message['sender']['id']
            #text_input = message['message'].get('text')
            #response_text = 'I am still learning'
            #if text_input in Greetings:
                #response_text = 'Hello, this is Chatty'

            #bot.send_text_message(user_id, response_text)


        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:


                if messaging_event.get("postback"):
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    message_text = messaging_event["postback"]["title"]
                    response_text = 'Welcome, lets start'
                    buttons = data
                    bot.send_generic(recipient_id, buttons)


                if messaging_event.get("message"):

                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    message_text = messaging_event["message"]["text"]
                    response_text = 'I am still learning'
                    if message_text in Greetings:
                        response_text = 'Hello, this is Chatty'



                if messaging_event.get("delivery"):
                    pass

                if messaging_event.get("optin"):
                    pass




                bot.send_text_message(sender_id, response_text)




        return 'ok', 200

            #############################################################














if __name__ == '__main__':
    app.run(debug=True, port=80)
