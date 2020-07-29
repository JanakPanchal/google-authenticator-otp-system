# google-authenticator-otp-system
google authenticator otp system in python

#install pyotp 
pip install pyotp 

#install falcon
pip install pyotp 

# run python file and start flask serve 

# Download Authentivator app from google play store or apple app store

after the downloading the app call register api and generate QR Code after that scan that QR code in Authentivator app in your phone 

# API for registor new user 

http://127.0.0.1:5000/register

request : 
{
    "email" : "janak@gmail.com",
    "uid" : "JBSWY3DPEHPK3PXP"
}

respone : 

{
  "data": "https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl=otpauth://totp/My%20APP:janak%40gmail.com?secret=1&issuer=My%20APP"
}

# API for user otp verification 

http://127.0.0.1:5000/validation

request:
{
    "otp" : "113449",
    "uid" : "JBSWY3DPEHPK3PXP"
}

respone : 

{
  "data": false
}



