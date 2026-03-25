from flask import Flask, render_template
from gpiozero import LED
app = Flask(__name__)
led = LED(4) # Change to match your LED!
@app.route("/")
def index():
    return render_template("HTML Code.html")
@app.route("/toggle/<action>")
def LEDControl(action):
    if action == "on":
        led.on()
        return "LED Turned On"
    elif action == "off":
        led.off()
        return "LED Turned Off"
    else:
        return "Invalid Action"
if __name__ == "__main__":
    app.run(host="192.168.1.11", port=80) 
