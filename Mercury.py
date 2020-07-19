from flask import Flask, render_template, request, redirect, send_file
import automate
import os
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

Places = ["Madurai","Bangalore","Ariyalur","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode",
            "Kallakurichi","Kanchipuram","Kanniyakumari","Karur","Krishnagiri","Nagapattanam",
            "Namakkal","Nilgiri","Perambalur","Pudukkottai","Ramanathapuram","Salem","Sivaganga","Sivakasi","Thanjavur",
            "Theni","Tuticorin","Trichy","Tirunelveli","Tiruppur","Tiruvallur","Tiruvannamalai",
            "Vellore","Villuppuram","Virudhunagar"
        ]

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Scan':
            name = request.form['name']
            automate.scan()
            return redirect('/' + name)

        elif request.form['submit_button'] == 'Send':
            name = request.form['aname']
            automate.send()
            return redirect('/' + 'sendtophone copy')

        elif request.form['submit_button'] == 'Print':
            automate.print()

        elif request.form['submit_button'] == 'Download':
            name = request.form['name']
            return redirect('/' + name)

        elif request.form['submit_button'] == 'Shutdown':
            os.system("shutdown /s /t 0")

    return render_template('astro.html', len = len(Places), Places = Places)


@app.route('/<name>', methods=['POST','GET'])
def name(name):
    filename = "L:/Horoscope/" + name + ".jpg"
    return send_file(filename,mimetype='image/jpeg',as_attachment=False)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)