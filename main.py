import smtplib, ssl

port = 465  # For SSL
#password = input("Type your password and press enter: ")


fromAddres = 'wallemluvii@gmail.com'
toAdress = 'mluviitester@gmail.com'

x = 1



context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("wallemluvii@gmail.com", 'Mluvii123')
    while x <= 1:
        message = """\
        Sbject: TEST01
        
        TEST ODESLANI ZPET """ + str(x)
        server.sendmail(fromAddres, toAdress, message)
        x += 1
        print(x)







