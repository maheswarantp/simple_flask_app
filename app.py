from flask import Flask, Response, render_template
from flask import request, jsonify
from flask_mail import Mail, Message
from datetime import datetime, date
from makePdf import create_bill_pdf


app = Flask(__name__)
mail = Mail(app)

# Mail configs
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'accsharetemp@gmail.com'
app.config['MAIL_PASSWORD'] = 'lwgpeaapizdwjyad'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def sendMail(path_to_pdf_file):
    msg = Message(
        'Here is your electricity bill',
        sender ='accsharetemp@gmail.com',
        recipients = ['benzinsajumanjally@gmail.com']
    )
    with open(path_to_pdf_file, 'rb') as f:
        msg.attach(filename='electricity_bill.pdf', content_type='application/pdf', data=f.read(), disposition=None, headers=None)
    msg.body = 'Here is your electricity bill!!!!'
    mail.send(msg)
    return 'sent'

stringVal = ""
# Show this on server

max_power_this_minute = 0
max_power = 0                       # to pdf connected load
total_power = 0                     # device 1 power
total_energy_hour = 0               
total_energy_day = 0
total_energy_month = 0              # To pdf energy this month
total_cost_hour = 0
total_cost_day = 0
total_cost_month = 0                # to pdf amount?
dynamic_price_current = 0

# PDF made on a button click

# Dynamic price code
"""
device_1_max_power = 0.01          
device_2_max_power = 0.01           
device_3_max_power = 0.01
device_4_max_power = 0.01
device_5_max_power = 0.01

device_1_power = 0.01   #recieve power from Blynk device 1      # device_1_power from api
device_2_power = 0.01   #recieve power from Blynk device 2      # recieve from another api
device_3_power = 0.01   #recieve power from Blynk device 2      # recieve from another api
device_4_power = 0.01   #recieve power from Blynk device 2      # recieve from another api
device_5_power = 0.01   #recieve power from Blynk device 2      # recieve from another api

if device_1_power > device_1_max_power:
    device_1_max_power = device_1_power
if device_2_power > device_2_max_power:
    device_2_max_power = device_2_power
if device_3_power > device_3_max_power:
    device_3_max_power = device_3_power
if device_4_power > device_4_max_power:
    device_4_max_power = device_4_power
if device_5_power > device_5_max_power:
    device_5_max_power = device_5_power



total_power = device_1_power + device_2_power + device_3_power + device_4_power + device_5_power
total_max_power = device_1_max_power + device_2_max_power + device_3_max_power + device_4_max_power + device_5_max_power

dynamic_price_max_value = 10.00
dynamic_price_min_value = 5.00

dynamic_price_next_minute = ((dynamic_price_max_value - dynamic_price_min_value)*(total_power / total_max_power)) + 5.00
# dynamic price has to be pushed to Blynk every minute to which VPIN? ==> V6
"""


@app.route('/', methods=['GET'])
def hello():
    global stringVal, max_power_this_minute, max_power, total_power, total_energy_hour, total_energy_day, total_energy_month, total_cost_hour, total_cost_day, total_cost_month, dynamic_price_current
    stringVal = request.args.get('energykey')
    print(stringVal)
    if len(stringVal.split(' ')) > 1:
        max_power_this_minute, max_power, total_power, total_energy_hour, total_energy_day, total_energy_month, total_cost_hour, total_cost_day, total_cost_month, dynamic_price_current = stringVal.split(' ')
    return "Hello There!!"

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    return data

@app.route('/home')
def home():
    return render_template('index.html.jinja', 
                        max_power_this_minute = max_power_this_minute,
                        max_power = max_power,
                        total_power = total_power,
                        total_energy_hour = total_energy_hour,
                        total_energy_day = total_energy_day,
                        total_energy_month = total_energy_month,
                        total_cost_day = total_cost_day,
                        total_cost_hour = total_cost_hour,
                        total_cost_month = total_cost_month,
                        dynamic_price_current = dynamic_price_current 
)

@app.route('/sendPdf')
def sendPDF():
    global stringVal, max_power_this_minute, max_power, total_power, total_energy_hour, total_energy_day, total_energy_month, total_cost_hour, total_cost_day, total_cost_month, dynamic_price_current
 
    bill_data = {
    'customer_name': 'FISAT',
    'consumer_number': '1234567890',
    'address': 'Hormis Nagar, Mookkannoor',
    'month': datetime.now().month,
    'amount_due': total_cost_month,
    'energy': total_energy_month,
    'bill_generated_on': date.today(),
    'connected_load': max_power
    }

    create_bill_pdf('electricity_bill.pdf', bill_data)
    sendMail('electricity_bill.pdf')
    return 'sent'
 


@app.route('/bye')
def bye():
    return "Bye api"


# if __name__ == "__main__":
#     app.run(debug=True)