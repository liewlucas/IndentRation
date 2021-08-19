import logging 
import telebot 
from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove, ForceReply, bot, update 
from telegram.ext import * 
import responses as R 
 
API_Key = '1787995820:AAGe0oyoYOeGs-HDSxPQkKO8Vxf0IHS213s' 
tb = telebot.TeleBot(API_Key) 
logger = logging.getLogger(__name__) 
 
USERNAME, PASSWORD = range(2) 
 
def start_command(update, context): 
    global userchatid 
    userchatid = update.message.chat.id 
    update.message.reply_text("Welcome to indentrationbot. Please input your Username and password") 
    update.message.reply_text("What is your username?", reply_markup=ForceReply(selective=True),) 
    return USERNAME 
 
def username(update:Update, context: CallbackContext) -> int: 
    global inputusername 
    global input_username 
    inputusername = str(update.message.text) 
    input_username=R.username_response(inputusername) 
    update.message.reply_text(input_username) 
    update.message.reply_text("What is your password?", reply_markup=ForceReply(selective=True),) 
    return PASSWORD 
    # return ConversationHandler.END 
 
def password (update:Update, context: CallbackContext) -> int: 
    global inputpassword 
    global input_password 
    inputpassword = str(update.message.text) 
    input_password = R.password_response(inputpassword) 
    update.message.reply_text(input_password) 
    return ConversationHandler.END 
 
def cancel(update, context): 
    user = update.message.from_user 
    logger.info("User %s canceled the conversation.", user.first_name) 
    update.message.reply_text( 
        'restart the bot to indent your ration' 
    ) 
 
def error(update, context): 
    print(f"update {update} caused error {context.error}") 
 
def handle_message(update, context): 
    text = str(update.message.text) 
 
def main(): 
        updater = Updater(API_Key, use_context=True) 
        dp = updater.dispatcher 
 
        credential_handler = (ConversationHandler( 
        entry_points=[CommandHandler('start', start_command)], 
        states={ 
            USERNAME: [MessageHandler(Filters.all, username)], 
            PASSWORD: [MessageHandler(Filters.all, password)] 
         }, 
        fallbacks=[CommandHandler('cancel', cancel)], 
    )) 
 
        # dp.add_handler(CommandHandler("indent", indent_command)) 
        dp.add_error_handler(error) 
        dp.add_handler(credential_handler) 
        dp.add_handler(MessageHandler(Filters.text, handle_message)) 
 
        updater.start_polling(0) 
        updater.idle() 
 
main()
