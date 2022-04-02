import requests
import json


FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/v13.0/me/'



class Bot(object):
    def __init__(self,access_token, api_url=FACEBOOK_GRAPH_URL):
        self.access_token = access_token
        self.api_url = api_url

    def send_text_message(self, psid, message, messaging_type="RESPONSE"):
        headers = {
            "Content-Type": 'application/json'

        }


        data = {
            'messaging_type' : messaging_type,
            'recipient' : {'id' : psid},
            'message' : {'text' : message}
        }


        params = {'access_token' : self.access_token}
        self.api_url = self.api_url + 'messages'
        response = requests.post(self.api_url,
                                headers=headers,params=params,
                                data=json.dumps(data))
        print(response.content)





######################################################
    data = (('job role', 'job description', 'https://joblink', '+23412345678'), ('job role', 'job description', 'https://joblink', '+23412345678'), ('job role', 'job description', 'https://joblink', '+23412345678'))

    def generateJson(data):
        mydata = []
        for x in data:
            thedata = { "title" : x[0],
                    "image_url" : "https://optional-image-url.png",
                    "subtitle": x[1],
                    "default_action": {
                        "type": "web_url",
                        "url": x[2],
                        "webview_height_ratio": "COMPACT"
                     },
                    "buttons":[
                    { "type":"phone_number",
                    "title":"Call HR",
                    "payload":x[3]}
                    ]
                }
            mydata.append(thedata)
        jsonData = json.dumps(mydata)
        print(jsonData)
        return jsonData
    def send_generic(self, recipient_id, thedata):
        payload = {
          "recipient":{
            "id":"{0}".format(recipient_id)
          },
          "message":{
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"generic",
                "elements":"{}".format(thedata)
              }
            }
          }
        }

        request_endpoint = 'https://graph.facebook.com/v2.6/me/messages'
        response = requests.post(
            request_endpoint,
            params =  {'access_token' : self.access_token},
            json = payload,
            headers = {'content-Type':'application/json'})
        result = response.json()
        #return result






        #send_generic("recipient_id", data)

#send_generic(psid, data)




###########################################

bot = Bot('EAAEKSC8Gt98BACMUATFucv852wKlYEqcRTgOgsgT1BiS0t5zYzLjwyAezyUFlN24SNFh2gcTZCtCAn9YCJuwXo7FsfXRx5hMLZCsKhb9Jc4rkn8GRyCFmDYAnkFzy5sLFZA8hAP1qomZCh8NfGPbAKfTU148qLMlnToF1AXmXCN1fIRPzEPk')
#bot.send_generic(5047598941972643, data)


#bot.send_generic(5047598941972643, data)
