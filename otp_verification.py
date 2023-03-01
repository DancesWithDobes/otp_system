#comments

import smtplib
import random

optLength = 6
otp = ""

'''
for num in range(0,6):
    otp += str(random.randint(0,9))

print(otp)

#  otpMessage = 
'''


def get_otp_number(length):

    output = ""

    for num in range(0,length):
        output += str(random.randint(0,length))
    
    return output

otp = get_otp_number(optLength)
message = opt

optMessage = f"Your OPT is: {opt}"
print(optMessage)


x = smtplib.SMTP('smtp.gmail.com', 587)
x.starttls()
x.login("your gmail account", "your app password")




userEmail = input("Enter your email")
x.sendmail('&&&&&&&&&&&&', userEmail, message)


userInput = input("Enter your OTP: ")


if userInput == otp:
    print("OTP correct. Verification successful.")

else:
    print("Incorrect, Try again")