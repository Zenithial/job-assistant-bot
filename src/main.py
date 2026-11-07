import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from BotState import BotState
from parseCV import parsePDF
from summariseCV import summarise
from formatCvSummary import format_llm_response

load_dotenv()

TOKEN: Final = os.getenv("BOT_TOKEN")

BOT_USERNAME: Final = '@CareerSupport2026Bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = BotState.DEFAULT
    await update.message.reply_text('Hello! I am a career helper bot. What would you like to do?\n1. Upload CV\n2. Analyse job description\n3. Compare CV to a job description\nPlease reply with 1, 2 or 3')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send your CV or a job description, I will read it and give feedback')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')
    
# Responses
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    state = context.user_data.get("state")
    text = update.message.text
    response = "I don't understand that, try again"
    if state == BotState.DEFAULT:
        if text == '1':
            response = "Upload your CV as a PDF or WORD document"
            context.user_data["state"] = BotState.WAIT_FOR_CV
        elif text == '2':
            response = "Copy and paste job description as raw text"
            context.user_data["state"] = BotState.JOB_DESCRIPTION
        elif text == 3:
            response = "Send CV and jov description"
            context.user_data["state"] = BotState.COMPARE_CV_TO_JOB_DESCRIPTION
    elif state == BotState.JOB_DESCRIPTION:
        #to do
        pass

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    state = context.user_data.get("state")
    if state == BotState.WAIT_FOR_CV:
        document = update.message.document
        filename = document.file_name
        if (filename.endswith(".pdf")):
            cv_text = parsePDF(document)
            get_llm_response = summarise(cv_text)
            formatted = format_llm_response(get_llm_response)
            await update.message.reply_text(f"{formatted}")
        else:
            await update.message.reply_text("Please upload a pdf document")
        
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    
if __name__ == '__main__':
    print('Starting bot')
    app = Application.builder().token(TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    
    #Errors
    app.add_error_handler(error)
    
    print('Polling')
    app.run_polling(poll_interval=3)