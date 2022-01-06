import sqlite3
from Account import Account
import itertools

conn = sqlite3.connect('Account.db', check_same_thread=False)

c = conn.cursor()

# c.execute(""" CREATE TABLE Account(
#                 chat_id text,
#                 username text,
#                 password text,
#                 pin integer
#
#             )""")



# c.execute(""" CREATE TABLE rationoptions(
#               chat_id text,
#               MON53L text,
#               MON53D text,
#               MON200L text,
#               MON200D text,
#               TUE53L text,
#               TUE53D text,
#               TUE200L text,
#               TUE200D text,
#               WED53L text,
#               WED53D text,
#               WED200L text,
#               WED200D text,
#               THU53L text,
#               THU53D text,
#               THU200L text,
#               THU200D text,
#               FRI53L text,
#               FRI53D text,
#               FRI200L text,
#               FRI200D text,
#               SAT53L text,
#               SAT53D text,
#               SUN53L text,
#               SUN53D text
#
#             )""")

c.execute("SELECT * From Account")
print(c.fetchall())

c.execute("SELECT * From rationoptions")
print(c.fetchall())



def insert_acc(acc):
    with conn:
        c.execute("INSERT INTO Account VALUES (:chat_id, :username, :password, :pin)",
                  {'chat_id': acc.chat_id, 'username': acc.username, 'password': acc.password, 'pin': acc.pin})

# print(flat_data)
# c.execute('DELETE FROM Account WHERE chat_id="168554266"')
# print(c.fetchall())

def insert_username(chat_id, inputusername):
    with conn:
        c.execute("""UPDATE ACCOUNT SET username = :inputusername
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'inputusername': inputusername})

def insert_password(chat_id, inputpassword):
    with conn:
        c.execute("""UPDATE ACCOUNT SET password = :inputpassword
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'inputpassword': inputpassword})
def insert_pin(chat_id, inputpin):
    with conn:
        c.execute("""UPDATE ACCOUNT SET pin = :inputpin
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'inputpin': inputpin})

def get_username(chat_id):
    c.execute("SELECT username FROM Account WHERE chat_id=:chat_id", {'chat_id': chat_id})
    return c.fetchone()[0]

def get_password(chat_id):
    c.execute("SELECT password FROM Account WHERE chat_id=:chat_id", {'chat_id': chat_id})
    return c.fetchone()[0]

def get_pin(chat_id):
    c.execute("SELECT pin FROM Account WHERE chat_id=:chat_id", {'chat_id': chat_id})
    return c.fetchone()[0]

def get_chatid(chat_id):
    c.execute("SELECT chat_id FROM Account WHERE chat_id=:chat_id", {'chat_id': chat_id})
    return c.fetchone()[0]

def delete_data(chat_id):
    with conn:
        c.execute("DELETE FROM Account WHERE chat_id=:chat_id", {'chat_id': chat_id})
        c.execute("SELECT * From Account")

def startindent(ro):
    with conn:
        c.execute("INSERT INTO rationoptions VALUES (:chat_id, :MON53L, :MON53D, :MON200L, :MON200D, :TUE53L, :TUE53D, :TUE200L, :TUE200D, :WED53L, :WED53D, :WED200L, :WED200D, :THU53L, :THU53D, :THU200L, :THU200D, :FRI53L, :FRI53D, :FRI200L, :FRI200D, :SAT53L, :SAT53D, :SUN53L, :SUN53D)",
                  {'chat_id': ro.chat_id, 'MON53L': ro.MON53L, 'MON53D': ro.MON53D, 'MON200L': ro.MON200L, 'MON200D': ro.MON200D, 'TUE53L': ro.TUE53L, 'TUE53D': ro.TUE53D, 'TUE200L': ro.TUE200L, 'TUE200D': ro.TUE200D, 'WED53L': ro.WED53L, 'WED53D': ro.WED53D, 'WED200L': ro.WED200L, 'WED200D': ro.WED200D, 'THU53L': ro.THU53L, 'THU53D': ro.THU53D, 'THU200L': ro.THU200L, 'THU200D': ro.THU200D, 'FRI53L': ro.FRI53L, 'FRI53D': ro.FRI53D, 'FRI200L': ro.FRI200L, 'FRI200D': ro.FRI200D, 'SAT53L': ro.SAT53L, 'SAT53D': ro.SAT53D,  'SUN53L': ro.SUN53L, 'SUN53D': ro.SUN53D, })

def updateMON53L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET MON53L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateMON53D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET MON53D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateMON200L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET MON200L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateMON200D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET MON200D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateTUE53L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET TUE53L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateTUE53D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET TUE53D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateTUE200L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET TUE200L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})
def updateTUE200D(chat_id,  option):
    with conn:
        c.execute("""UPDATE rationoptions SET TUE200D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateWED53L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET WED53L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateWED53D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET WED53D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})
def updateWED200L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET WED200L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})
def updateWED200D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET WED200D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateTHU53L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET THU53L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateTHU53D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET THU53D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})
def updateTHU200L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET THU200L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})
def updateTHU200D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET THU200D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateFRI53L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET FRI53L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateFRI53D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET FRI53D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateFRI200L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET FRI200L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateFRI200D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET FRI200D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateSAT53L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET SAT53L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateSAT53D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET SAT53D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateSUN53L(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET SUN53L = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def updateSUN53D(chat_id, option):
    with conn:
        c.execute("""UPDATE rationoptions SET SUN53D = :option
                    WHERE chat_id = :chat_id""", {'chat_id': chat_id, 'option': option})

def getMON53L(chat_id):
    with conn:
        c.execute("SELECT MON53L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getMON53D(chat_id):
    with conn:
        c.execute("SELECT MON53D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getMON200L(chat_id):
    with conn:
        c.execute("SELECT MON200L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getMON200D(chat_id):
    with conn:
        c.execute("SELECT MON200D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getTUE53L(chat_id):
    with conn:
        c.execute("SELECT TUE53L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getTUE53D(chat_id):
    with conn:
        c.execute("SELECT TUE53D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getTUE200L(chat_id):
    with conn:
        c.execute("SELECT TUE200L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getTUE200D(chat_id):
    with conn:
        c.execute("SELECT TUE200D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getWED53L(chat_id):
    with conn:
        c.execute("SELECT WED53L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getWED53D(chat_id):
    with conn:
        c.execute("SELECT WED53D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getWED200L(chat_id):
    with conn:
        c.execute("SELECT WED200L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getWED200D(chat_id):
    with conn:
        c.execute("SELECT WED200D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getTHU53L(chat_id):
    with conn:
        c.execute("SELECT THU53L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getTHU53D(chat_id):
    with conn:
        c.execute("SELECT THU53D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getTHU200L(chat_id):
    with conn:
        c.execute("SELECT THU200L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getTHU200D(chat_id):
    with conn:
        c.execute("SELECT THU200D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getFRI53L(chat_id):
    with conn:
        c.execute("SELECT FRI53L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getFRI53D(chat_id):
    with conn:
        c.execute("SELECT FRI53D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getFRI200L(chat_id):
    with conn:
        c.execute("SELECT FRI200L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getFRI200D(chat_id):
    with conn:
        c.execute("SELECT FRI200D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getSAT53L(chat_id):
    with conn:
        c.execute("SELECT SAT53L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getSAT53D(chat_id):
    with conn:
        c.execute("SELECT SAT53D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getSUN53L(chat_id):
    with conn:
        c.execute("SELECT SUN53L FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getSUN53D(chat_id):
    with conn:
        c.execute("SELECT SUN53D FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})
        return c.fetchone()[0]

def getrationoptions(chat_id):
    with conn:
        c.execute("SELECT * FROM rationoptions WHERE chat_id=:chat_id",{'chat_id': chat_id})
        # print(c.fetchall()[0][2])
        return c.fetchall()

def clearrationoptions(chat_id):
    with conn:
        c.execute("DELETE FROM rationoptions WHERE chat_id=:chat_id", {'chat_id': chat_id})

# print(str(account_username))
# print(str(account_password))
conn.commit()