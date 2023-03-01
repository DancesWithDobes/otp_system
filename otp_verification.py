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

opt = get_otp_number(optLength)