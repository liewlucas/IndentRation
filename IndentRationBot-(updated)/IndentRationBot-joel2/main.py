import logging
import telebot
import telegram
from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove, ForceReply, bot, update
from telegram.ext import *
import responses as R
import DBSetpUp as D
import Account as A
import itertools
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib

API_Key = '2115199713:AAECtuiBBVQDnHXD3eW9gtByOAz0KC_Mcws'
tb = telegram.Bot(token = API_Key)
logger = logging.getLogger(__name__)
browser = webdriver.Chrome(executable_path="C:/Users/indentration2021/Desktop/chromedriver.exe")
browser.get("https://indentyourration.web.app/")
rationoptions = ['MON 53 L', 'MON 53 D', 'MON 200 L', 'MON 200 D', 'TUE 53 L', 'TUE 53 D', 'TUE 200 L', 'TUE 200 D',
                 'WED 53 L', 'WED 53 D', 'WED 200 L', 'WED 200 D', 'THU 53 L', 'THU 53 D', 'THU 200 L', 'THU 200 D',
                'FRI 53 L', 'FRI 53 D', 'FRI 200 L', 'FRI 200 D', 'SAT 53 L', 'SAT 53 D', 'SUN 53 L', 'SUN 53 D', 'DONE']
USERNAME, PASSWORD, PIN, REGISTERAGAIN, CONFIRM, INDENT, PINCHECK, FINISH = range(8)

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)-8s :: (%(name)s) > %(message)s'
)

logger = logging.getLogger(__name__)

hash = hashlib.sha256()

def encryption_key(userchatid):
    password_provided = userchatid
    password = password_provided.encode()

    salt = b"\xb9\x1f|}'S\xa1\x96\xeb\x154\x04\x88\xf3\xdf\x05"

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=salt,
                     iterations=100000,
                     backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def hash(text):
    hash_output = hashlib.sha256(text.encode()).hexdigest()
    return hash_output

def help_command(update, context):
    update.message.reply_text("Welcome to indentrationbot." + '\n\n' + "To start this bot and register your account use /start" + '\n\n' + "To indent or reindent your ration use /indent" + '\n\n' +"To delete your account, use /deleteaccount")

def start_command(update, context):
    userchatid = update.message.chat.id
    userchat_id = hash(str(userchatid))
    try:
        account_chatid = str(D.get_chatid(userchat_id))
        update.message.reply_text("Your account has already been registered, please use /indent to indent your ration or use /deleteaccount to delete and reregister your account")
        return ConversationHandler.END
    except:
        update.message.reply_text("Welcome to indentrationbot. Please input your Username and password to indenrationwebsite to use this bot")
        update.message.reply_text(
            "To indent or reindent your ration use /indent" + '\n\n' + "To delete your account, use /deleteaccount" + '\n\n' + "To cancel the conversation, use /cancel")
        update.message.reply_text("What is your username?", reply_markup=ForceReply(selective=True), )
        D.insert_acc(A.Account(userchat_id, '', '', ''))
        return USERNAME

def username (update:Update, context: CallbackContext) -> int:
    userchatid = str(update.message.chat.id)
    userchat_id = hash(userchatid)
    inputusername = str(update.message.text)
    f = Fernet(encryption_key(userchatid))
    encrypted = f.encrypt(inputusername.encode())
    D.insert_username(userchat_id, encrypted)
    input_username=R.username_response(inputusername)
    update.message.reply_text(input_username)
    update.message.reply_text("What is your password?", reply_markup=ForceReply(selective=True),)
    return PASSWORD

def password (update:Update, context: CallbackContext) -> int:
    userchatid = str(update.message.chat.id)
    userchat_id = hash(userchatid)
    inputpassword = str(update.message.text)
    f = Fernet(encryption_key(userchatid))
    encrypted = f.encrypt(inputpassword.encode())
    D.insert_password(userchat_id, encrypted)
    input_password = R.password_response(inputpassword)
    update.message.reply_text(input_password)
    update.message.reply_text("Please provide a 4-digit pin", reply_markup=ForceReply(selective=True), )
    return PIN

def pin(update:Update, context:CallbackContext) -> int:
    userchatid = str(update.message.chat.id)
    userchat_id = hash(userchatid)
    inputpin = (update.message.text)
    input_pin = R.pin_response(inputpin)
    if input_pin == 'Sorry your input was invalid, please input another pin':
        update.message.reply_text(input_pin)
        return PIN
    else:
        try:
            D.insert_pin(userchat_id, hash(inputpin))
            f = Fernet(encryption_key(userchatid))
            username = (f.decrypt(D.get_username(userchat_id))).decode()
            password = (f.decrypt(D.get_password(userchat_id))).decode()
            Username = browser.find_element_by_css_selector("[aria-label=username]")
            Username.send_keys(username)
            Password = browser.find_element_by_css_selector("[aria-label=password]")
            Password.send_keys(password)
            Password.send_keys(Keys.ENTER)
            time.sleep(3)
            try:
                browser.switch_to.alert.accept()
                update.message.reply_text(
                    "Your account does not exist, please input an existing account using /start again")
                Username.clear()
                Password.clear()
                browser.refresh()
                D.delete_data(userchat_id)
                return ConversationHandler.END

            except:
                browser.find_element_by_css_selector("body > div > nav > div > div.block > button").click()
                browser.find_element_by_css_selector(
                    "body > div > nav > div.w-full.px-3.pb-4 > button.w-full.border-b.border-red-400.pb-2.px-3.mt-4.text-gray-200.font-semibold.focus\:outline-none").click()
                update.message.reply_text(input_pin)
            # D.insert_acc(A.Account(userchat_id, R.usernameinput, R.passwordinput, R.pininput))
            return ConversationHandler.END
        except:
            update.message.reply_text(
                'Please try again in 10 seconds by typing DONE as someone else is indenting their ration')
            return REGISTERAGAIN

def registeragain (update:Update, context: CallbackContext) -> int:
    userchatid = str(update.message.chat.id)
    userchat_id = hash(userchatid)
    try:
        f = Fernet(encryption_key(userchatid))
        username = (f.decrypt(D.get_username(userchat_id))).decode()
        password = (f.decrypt(D.get_password(userchat_id))).decode()
        Username = browser.find_element_by_css_selector("[aria-label=username]")
        Username.send_keys(username)
        Password = browser.find_element_by_css_selector("[aria-label=password]")
        Password.send_keys(password)
        Password.send_keys(Keys.ENTER)
        time.sleep(3)
        try:
            browser.switch_to.alert.accept()
            update.message.reply_text(
                "Your account does not exist, please input an existing account using /start again")
            Username.clear()
            Password.clear()
            browser.refresh()
            return ConversationHandler.END
        except:
            browser.find_element_by_css_selector("body > div > nav > div > div.block > button").click()
            browser.find_element_by_css_selector(
                "body > div > nav > div.w-full.px-3.pb-4 > button.w-full.border-b.border-red-400.pb-2.px-3.mt-4.text-gray-200.font-semibold.focus\:outline-none").click()
            update.message.reply_text("Please provide a 4-digit pin", reply_markup=ForceReply(selective=True), )
        # D.insert_acc(A.Account(userchat_id, R.usernameinput, R.passwordinput, R.pininput))
        return ConversationHandler.END
    except:
        update.message.reply_text(
            'Please try again in 10 seconds by typing DONE as someone else is indenting their ration')
        return REGISTERAGAIN

def deleteaccount_command (update, context):
    userchatid = str(update.message.chat.id)
    userchat_id = hash(userchatid)
    replykeyboard = [['Yes', 'No']]
    try:
        account_chatid = str(D.get_chatid(userchat_id))
        try:
            f = Fernet(encryption_key(userchatid))
            account_username = str((f.decrypt(D.get_username(userchat_id))).decode())
            update.message.reply_text("Dear " + account_username + ' are you sure you want to delete your account?', reply_markup=ReplyKeyboardMarkup(replykeyboard, one_time_keyboard=True, selective=True, input_field_placeholder='Delete or Not'))
            return CONFIRM
        except:
            update.message.reply_text('Dear user are you sure you want to delete your account?',
                                      reply_markup=ReplyKeyboardMarkup(replykeyboard, one_time_keyboard=True,
                                                                       selective=True,
                                                                       input_field_placeholder='Delete or Not'))
            return CONFIRM
    except:
        update.message.reply_text("You do not have an account to delete, use /start to register your account")
        return ConversationHandler.END

def deleteaccount_confirm (update:Update, context:CallbackContext) -> int:
    userchatid = str(update.message.chat.id)
    userchat_id = hash(userchatid)
    choice = str(update.message.text)
    if choice == 'Yes':
        D.delete_data(userchat_id)
        update.message.reply_text('Your account has been successfully deleted, use /start to register your account')
        return ConversationHandler.END
    elif choice == 'No':
        update.message.reply_text('Your account has not been deleted')
        return ConversationHandler.END

def indent_start(update, context):
    userchatid = str(update.message.chat.id)
    userchat_id = hash(userchatid)
    try:
        f = Fernet(encryption_key(userchatid))
        account_username = str((f.decrypt(D.get_username(userchat_id))).decode())
        update.message.reply_text("Welcome " + account_username + ', please input your 4 digit pin to continue' + '\n\n' + 'You may use /cancel to stop indenting at any time' + '\n\n' + 'Enter DONE to finish')
        return PINCHECK
    except:
        update.message.reply_text('Your account has not been registered, use /start to register your account')
        return ConversationHandler.END

def indent_command(update:Update, context: CallbackContext) -> int:
    global reply_keyboard
    userchatid = str(update.message.chat.id)
    userchat_id = hash(userchatid)
    account_pin = str(D.get_pin(userchat_id))
    reply_keyboard = [['MON 53 L', 'MON 53 D'], ['MON 200 L', 'MON 200 D'], ['TUE 53 L', 'TUE 53 D'],
                      ['TUE 200 L', 'TUE 200 D'], ['WED 53 L', 'WED 53 D'], ['WED 200 L', 'WED 200 D'], ['THU 53 L', 'THU 53 D'], ['THU 200 L', 'THU 200 D'],
                      ['FRI 53 L', 'FRI 53 D'], ['FRI 200 L', 'FRI 200 D'], ['SAT 53 L', 'SAT 53 D'], ['SUN 53 L', 'SUN 53 D'],  ['DONE']]
    pincheck = hash(str(update.message.text))
    if pincheck != account_pin:
        update.message.reply_text('you have entered an invalid pin, please enter your pin again')
        return PINCHECK
    else:
        update.message.reply_text("What would you like to indent",
                                      reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False,
                                                                       selective=True))
        D.startindent(A.rationoptions(userchat_id, 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL',))
        return INDENT

def indent(update:Update, context: CallbackContext) -> int:
    userchatid = str(update.message.chat.id)
    userchat_id = hash(userchatid)
    inputrationoption = str(update.message.text)
    if inputrationoption not in itertools.chain(*reply_keyboard):
        update.message.reply_text('your input is invalid please select another option')
        return INDENT
    elif inputrationoption != 'DONE':
        if inputrationoption == 'MON 53 L':
            if D.getMON53L(userchat_id) == 'NIL':
                D.updateMON53L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getMON53L(userchat_id) == 'YES':
                D.updateMON53L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'MON 53 D':
            if D.getMON53D(userchat_id) == 'NIL':
                D.updateMON53D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getMON53D(userchat_id) == 'YES':
                D.updateMON53D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'MON 200 L':
            if D.getMON200L(userchat_id) == 'NIL':
                D.updateMON200L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getMON200L(userchat_id) == 'YES':
                D.updateMON200L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'MON 200 D':
            if D.getMON200D(userchat_id) == 'NIL':
                D.updateMON200D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getMON200D(userchat_id) == 'YES':
                D.updateMON200D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'TUE 53 L':
            if D.getTUE53L(userchat_id) == 'NIL':
                D.updateTUE53L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getTUE53L(userchat_id) == 'YES':
                D.updateTUE53L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'TUE 53 D':
            if D.getTUE53D(userchat_id) == 'NIL':
                D.updateTUE53D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getTUE53D(userchat_id) == 'YES':
                D.updateTUE53D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'TUE 200 L':
            if D.getTUE200L(userchat_id) == 'NIL':
                D.updateTUE200L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getTUE200L(userchat_id) == 'YES':
                D.updateTUE200L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'TUE 200 D':
            if D.getTUE200D(userchat_id) == 'NIL':
                D.updateTUE200D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getTUE200D(userchat_id) == 'YES':
                D.updateTUE200D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'WED 53 L':
            if D.getWED53L(userchat_id) == 'NIL':
                D.updateWED53L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getWED53L(userchat_id) == 'YES':
                D.updateWED53L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'WED 53 D':
            if D.getWED53D(userchat_id) == 'NIL':
                D.updateWED53D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getWED53D(userchat_id) == 'YES':
                D.updateWED53D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'WED 200 L':
            if D.getWED200L(userchat_id) == 'NIL':
                D.updateWED200L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getWED200L(userchat_id) == 'YES':
                D.updateWED200L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'WED 200 D':
            if D.getWED200D(userchat_id) == 'NIL':
                D.updateWED200D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getWED200D(userchat_id) == 'YES':
                D.updateWED200D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'THU 53 L':
            if D.getTHU53L(userchat_id) == 'NIL':
                D.updateTHU53L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getTHU53L(userchat_id) == 'YES':
                D.updateTHU53L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'THU 53 D':
            if D.getTHU53D(userchat_id) == 'NIL':
                D.updateTHU53D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getTHU53D(userchat_id) == 'YES':
                D.updateTHU53D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'THU 200 L':
            if D.getTHU200L(userchat_id) == 'NIL':
                D.updateTHU200L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getTHU200L(userchat_id) == 'YES':
                D.updateTHU200L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'THU 200 D':
            if D.getTHU200D(userchat_id) == 'NIL':
                D.updateTHU200D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getTHU200D(userchat_id) == 'YES':
                D.updateTHU200D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'FRI 53 L':
            if D.getFRI53L(userchat_id) == 'NIL':
                D.updateFRI53L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getFRI53L(userchat_id) == 'YES':
                D.updateFRI53L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'FRI 53 D':
            if D.getFRI53D(userchat_id) == 'NIL':
                D.updateFRI53D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getFRI53D(userchat_id) == 'YES':
                D.updateFRI53D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'FRI 200 L':
            if D.getFRI200L(userchat_id) == 'NIL':
                D.updateFRI200L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getFRI200L(userchat_id) == 'YES':
                D.updateFRI200L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'FRI 200 D':
            if D.getFRI200D(userchat_id) == 'NIL':
                D.updateFRI200D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getFRI200D(userchat_id) == 'YES':
                D.updateFRI200D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'SAT 53 L':
            if D.getSAT53L(userchat_id) == 'NIL':
                D.updateSAT53L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getSAT53L(userchat_id) == 'YES':
                D.updateSAT53L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'SAT 53 D':
            if D.getSAT53D(userchat_id) == 'NIL':
                D.updateSAT53D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getSAT53D(userchat_id) == 'YES':
                D.updateSAT53D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'SUN 53 L':
            if D.getSUN53L(userchat_id) == 'NIL':
                D.updateSUN53L(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getSUN53L(userchat_id) == 'YES':
                D.updateSUN53L(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
            return INDENT
        if inputrationoption == 'SUN 53 D':
            if D.getSUN53D(userchat_id) == 'NIL':
                D.updateSUN53D(userchat_id, 'YES')
                update.message.reply_text('you have indented ' + inputrationoption)
            elif D.getSUN53D(userchat_id) == 'YES':
                D.updateSUN53D(userchat_id, 'NIL')
                update.message.reply_text(inputrationoption + ' has been unselected')
    elif inputrationoption == 'DONE':
        wrong_date = []
        options_list = D.getrationoptions(userchat_id)
        if (options_list[0][1] == 'YES' or options_list[0][2] == 'YES') and (
                options_list[0][3] == 'YES' or options_list[0][4] == 'YES'):
            wrong_date.append('MON')
        if (options_list[0][5] == 'YES' or options_list[0][6] == 'YES') and (
                options_list[0][7] == 'YES' or options_list[0][8] == 'YES'):
            wrong_date.append('TUE')
        if (options_list[0][9] == 'YES' or options_list[0][10] == 'YES') and (
                options_list[0][11] == 'YES' or options_list[0][12] == 'YES'):
            wrong_date.append('WED')
        if (options_list[0][13] == 'YES' or options_list[0][14] == 'YES') and (
                options_list[0][15] == 'YES' or options_list[0][16] == 'YES'):
            wrong_date.append('THU')
        if (options_list[0][17] == 'YES' or options_list[0][18] == 'YES') and (
                options_list[0][19] == 'YES' or options_list[0][20] == 'YES'):
            wrong_date.append('FRI')
        if not wrong_date:
            try:
                f = Fernet(encryption_key(userchatid))
                username = (f.decrypt(D.get_username(userchat_id))).decode()
                password = (f.decrypt(D.get_password(userchat_id))).decode()
                Username = browser.find_element_by_css_selector("[aria-label=username]")
                Username.send_keys(username)
                Password = browser.find_element_by_css_selector("[aria-label=password]")
                Password.send_keys(password)
                Password.send_keys(Keys.ENTER)
                time.sleep(3)
                try:
                    browser.switch_to.alert.accept()
                    update.message.reply_text(
                        "Your account does not exist, please use /deleteaccount to delete your current account followed by /start to register an existing account")
                    Username.clear()
                    Password.clear()
                    browser.refresh()
                    return ConversationHandler.END
                except:
                    if D.getMON53L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[3]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[3]/div[2]/div/button[1]').click()
                    if D.getMON53D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[3]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[3]/div[2]/div/button[1]').click()
                    if D.getMON200L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[3]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[3]/div[2]/div/button[2]').click()
                    if D.getMON200D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[3]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[3]/div[2]/div/button[2]').click()
                    if D.getTUE53L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[4]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[4]/div[2]/div/button[1]').click()
                    if D.getTUE53D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[4]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[4]/div[2]/div/button[1]').click()
                    if D.getTUE200L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[4]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[4]/div[2]/div/button[2]').click()
                    if D.getTUE200D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[4]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[4]/div[2]/div/button[2]').click()
                    if D.getWED53L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[5]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[5]/div[2]/div/button[1]').click()
                    if D.getWED53D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[5]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[5]/div[2]/div/button[1]').click()
                    if D.getWED200L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[5]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[5]/div[2]/div/button[2]').click()
                    if D.getWED200D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[5]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[5]/div[2]/div/button[2]').click()
                    if D.getTHU53L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[6]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[6]/div[2]/div/button[1]').click()
                    if D.getTHU53D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[6]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[6]/div[2]/div/button[1]').click()
                    if D.getTHU200L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[6]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[6]/div[2]/div/button[2]').click()
                    if D.getTHU200D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[6]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[6]/div[2]/div/button[2]').click()
                    if D.getFRI53L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[7]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[7]/div[2]/div/button[1]').click()
                    if D.getFRI53D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[7]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[7]/div[2]/div/button[1]').click()
                    if D.getFRI200L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[7]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[7]/div[2]/div/button[2]').click()
                    if D.getFRI200D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[7]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[7]/div[2]/div/button[2]').click()
                    if D.getSAT53L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[8]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[8]/div[2]/div/button[1]').click()
                    if D.getSAT53D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[8]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[8]/div[2]/div/button[1]').click()
                    if D.getSUN53L(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[9]/div[2]/button[2]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[9]/div[2]/div/button[1]').click()
                    if D.getSUN53D(userchat_id) == 'YES':
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[9]/div[2]/button[3]').click()
                        browser.find_element_by_xpath('/html/body/div/div/div[5]/div[9]/div[2]/div/button[1]').click()
                    time.sleep(1)
                    # indentdate = browser.find_element_by_xpath('/html/body/div/div/div[5]/div[1]').text
                    browser.find_element_by_css_selector('body > div > div > div.flex.flex-col > button').click()
                    browser.switch_to.alert.accept()
                    time.sleep(2)
                    #browser.find_element_by_xpath('/html/body/div/div/div[4]/div/div/div[1]/button').click()
                    browser.find_element_by_xpath('/html/body/div/div/div[4]/div/div/div[1]/button').click()
                    time.sleep(1)
                    #indented = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div")
                    indented = browser.find_element_by_xpath('/html/body/div/div/div[4]')
                    indented.screenshot('screenshot.png')
                    # time.sleep(1)
                    tb.send_photo(update.message.chat.id,
                                  photo=open(r'screenshot.png','rb'))
                    # time.sleep(1)
                    os.remove('screenshot.png')
                    update.message.reply_text('Ration indent is completed')
                    # update.message.reply_text('you have selected' + str(options_list) + ' for ' + indentdate,
                    #                               reply_markup=ReplyKeyboardRemove(reply_keyboard))
                    # time.sleep(1)
                    browser.find_element_by_css_selector("body > div > nav > div > div.block > button").click() #logout
                    browser.find_element_by_css_selector(
                        "body > div > nav > div.w-full.px-3.pb-4 > button.w-full.border-b.border-red-400.pb-2.px-3.mt-4.text-gray-200.font-semibold.focus\:outline-none").click()
                    D.clearrationoptions(userchat_id)
                    return ConversationHandler.END
            except:
                update.message.reply_text('Please try again in 10 seconds by typing DONE as someone else is indenting their ration')
                return INDENT
        else:
            update.message.reply_text('you have selected meals at 2 different locations on ' + str(
                wrong_date) + ' please unselect one of your options')
            return INDENT

def cancel(update: Update, context: CallbackContext) -> int:
    userchatid = str(update.message.chat.id)
    userchat_id = hash(userchatid)
    try:
        browser.find_element_by_css_selector("body > div > nav > div > div.block > button").click()  # logout
        browser.find_element_by_css_selector(
            "body > div > nav > div.w-full.px-3.pb-4 > button.w-full.border-b.border-red-400.pb-2.px-3.mt-4.text-gray-200.font-semibold.focus\:outline-none").click()
        update.message.reply_text('Bye! I hope we can talk again some day.')
        D.clearrationoptions(userchat_id)
    except:
        D.clearrationoptions(userchat_id)
        update.message.reply_text('Bye! I hope we can talk again some day.')
    return ConversationHandler.END

def error(update, context):
    print(f"update {update} caused error {context.error}")

# def handle_message(update, context):
#     text = str(update.message.text)

def main():
        updater = Updater(API_Key, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler('Help', help_command))
        # Conversation handler for creating account
        account_handler = (ConversationHandler(
        entry_points=[CommandHandler('start', start_command)],
        states={
            USERNAME: [MessageHandler(Filters.all, username)],
            PASSWORD: [MessageHandler(Filters.all, password)],
            PIN: [MessageHandler(Filters.all, pin)],
            REGISTERAGAIN: [MessageHandler(Filters.all, registeragain)],
         },
        fallbacks=[CommandHandler('cancel', cancel)],
    ))
        # Conversation handler for deleting account
        deleteaccount_handler = (ConversationHandler(
        entry_points=[CommandHandler('deleteaccount', deleteaccount_command)],
        states={
            CONFIRM: [MessageHandler(Filters.regex('^(Yes|No)$'), deleteaccount_confirm)],
         },

        fallbacks=[CommandHandler('cancel', cancel)],
    ))
        # Conversation handler for indenting rations
        indent_handler = (ConversationHandler(
            entry_points=[CommandHandler('indent', indent_start)],
            states={

                PINCHECK: [MessageHandler(Filters.regex(r'\d+'), indent_command)],
                INDENT: [MessageHandler(Filters.text(rationoptions), indent)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
    ))
        dp.add_error_handler(error)
        dp.add_handler(account_handler)
        dp.add_handler(deleteaccount_handler)
        dp.add_handler(indent_handler)
        # dp.add_handler(MessageHandler(Filters.text, handle_message))


        updater.start_polling(0)
        updater.idle()

main()