from telegram import bot


def username_response(input_text):
    global usernameinput
    usernameinput = str(input_text)
    
    try:
        replymessage = "Your username is"
        arrayofreply = [replymessage, usernameinput]
        fullreply = ' '
        reply = (fullreply.join(arrayofreply))
        return reply
    except:
        return "Sorry your input was invalid"


def password_response(input_text):
    global passwordinput
    passwordinput = str(input_text)
    
    try:
        replymessage = "Your password is"
        arrayofreply = [replymessage, passwordinput]
        fullreply = ' '
        reply = (fullreply.join(arrayofreply))
        return reply
    except:
        return "Sorry your input was invalid"


def pin_response(input_text):
    global pininput
    pininput = str(input_text)
    if len(pininput) == 4:
        try:
            pin_input = int(input_text)
            replymessage = "Your Account has been Registered!"
            arrayofreply = [replymessage, 'use /indent to indent your rations. For more information on how to use this bot, use /help']
            fullreply = ' '
            reply = (fullreply.join(arrayofreply))
            return reply
        except:
            return 'Sorry your input was invalid, please input another pin'
    else:
        return 'Sorry your input was invalid, please input another pin'

def ration_response(input_text):
    global rationinput
    rationinput = str(input_text)

    try:
        replymessage = "Your option is"
        arrayofreply = [replymessage, rationinput]
        fullreply = ' '
        reply = (fullreply.join(arrayofreply))
        return reply
    
    except:
        return "Sorry your input was invalid"