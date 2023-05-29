from flask import Flask, Response, render_template
from flask import request, jsonify

app = Flask(__name__)
stringVal = ""

device_1_power = 0 
device_1_energy = 0
device_2_power = 0
device_2_energy = 0
device_3_power = 0
device_3_energy = 0
device_4_power = 0
device_4_energy = 0
device_5_power = 0
device_5_energy = 0
device_6_power = 0
device_6_energy = 0
device_7_power = 0
device_7_energy = 0
device_8_power = 0
device_8_energy = 0
  
phase_1_voltage = 0
phase_2_voltage = 0
phase_3_voltage = 0

total_power = 0

total_solar_power = 0
solar_max_power = 0
solar_energy_today = 0
solar_energy_month = 0


dynamic_price_new = 0
dynamic_price_old = 0
dynamic_price_current = 0

energy_hour = 0
energy_day = 0
energy_month = 0

cost_month = 0
cost_day = 0

@app.route('/', methods=['GET'])
def hello():
    global stringVal, device_1_power,device_1_energy,device_2_power,device_2_energy,device_3_power,device_3_energy,device_4_power,device_4_energy,device_5_power,device_5_energy,device_6_power,device_6_energy,device_7_power,device_7_energy,device_8_power,device_8_energy,phase_1_voltage ,phase_2_voltage ,phase_3_voltage ,total_power ,total_solar_power ,solar_max_power ,solar_energy_today ,solar_energy_month ,dynamic_price_new ,dynamic_price_old ,dynamic_price_current ,energy_hour ,energy_day ,energy_month,cost_month,cost_day
    stringVal = request.args.get('energykey')
    print(stringVal)
    if len(stringVal.split(' ')) > 1:
        device_1_power,device_1_energy,device_2_power,device_2_energy,device_3_power,device_3_energy,device_4_power,device_4_energy,device_5_power,device_5_energy,device_6_power,device_6_energy,device_7_power,device_7_energy,device_8_power,device_8_energy,phase_1_voltage,phase_2_voltage,phase_3_voltage,total_power,total_solar_power,solar_max_power,solar_energy_today,solar_energy_month,dynamic_price_new,dynamic_price_old,dynamic_price_current,energy_hour,energy_day,energy_month,cost_month, cost_day, _ = stringVal.split(' ')
    return "Hello There!!"

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    return data

@app.route('/home')
def home():
    return render_template('index.html.jinja', 
                        phase_1_voltage = phase_1_voltage,
                        phase_2_voltage = phase_2_voltage,
                        phase_3_voltage = phase_3_voltage,
                        total_power = total_power,
                        total_solar_power = total_solar_power,
                        solar_max_power = solar_max_power,
                        solar_energy_today = solar_energy_today,
                        solar_energy_month = solar_energy_month,
                        dynamic_price_new = dynamic_price_new,
                        dynamic_price_old = dynamic_price_old,
                        dynamic_price_current = dynamic_price_current,
                        energy_hour = energy_hour,
                        energy_day = energy_day,
                        energy_month = energy_month,
                        cost_month = cost_month,
                        cost_day = cost_day
)

@app.route('/bye')
def bye():
    return "Bye api"


# if __name__ == "__main__":
#     app.run(debug=True)