import pyotp

from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

@app.route('/register', methods=['POST'])
def home():
    if (request.method == 'POST'):
        email = request.get_json()
        data = "{}{}".format("https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl=",pyotp.totp.TOTP(email["uid"]).provisioning_uri(email["email"], issuer_name="My APP"))
        return jsonify({'data': data  })

@app.route('/verification', methods=['POST'])
def validateuser():
    if(request.method == 'POST'):
        opt = request.get_json()
        totp = pyotp.TOTP(opt['uid'])
        print("{} {}".format(totp.now() , opt["otp"]))
        if totp.verify(opt["otp"]):
            return jsonify({'data': True  })
        else:
            return jsonify({'data': False})


if __name__ == '__main__':
    app.run(debug=True)

