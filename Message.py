from twilio.rest import Client

account_sid = 'ACcd65f6468777e1ba55920c1d0f853c66'
auth_token = 'f97db0d0d6a6010702cc95708ed8be3c'
my_twilio_number = '(201)297-4038'
xuqh_cell = '+8615094347232'
maomao_cell = '+8615852189072'


class Message:
    """text message class"""
    twi_client = Client(account_sid, auth_token)

    def __init__(self, to_num, from_num, content):
        self.to_num = to_num
        self.from_num = from_num
        self.content = content

    def send(self):
        """
        send message
        :return:
        """
        message = self.twi_client.messages.create(to=self.to_num, from_=self.from_num, body=self.content)

# msg = Message(to_num='+8615094347232', from_num='(201)297-4038', content='test drive')
# msg.send()
