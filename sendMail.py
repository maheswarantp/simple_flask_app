
# importing libraries
from flask import Flask
from flask_mail import Mail, Message
   
app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'accsharetemp@gmail.com'
app.config['MAIL_PASSWORD'] = 'lwgpeaapizdwjyad'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
   
# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
    msg = Message(
                'Hello',
                sender ='accsharetemp@gmail.com',
                recipients = ['ssmtptest334@gmail.com']
               )
    with open('electricity_bill.pdf', 'rb') as f:
        msg.attach(filename='electricity_bill.pdf', content_type='application/pdf', data=f.read(), disposition=None, headers=None)
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)
    return 'Sent'
   
if __name__ == '__main__':
   app.run(debug = True)