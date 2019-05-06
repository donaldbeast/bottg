import telebot
from telebot import types

bot = telebot.TeleBot("754425814:AAEEy96xObIJS5xA6oVFay-PWYgN0gt38KA")
 
adres = ""
number = ""
time = ""
df = ""
chat_id = "484759206"
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	#bot.reply_to(message, "Добро пожаловать!")
    bot.send_message( message.chat.id, "Добро пожаловать!" )
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_zakaz = types.InlineKeyboardButton(text='Сделать заказ', callback_data='zakaz'); 
    keyboard.add(key_zakaz); #добавляем кнопку в клавиатуру
    key_otziv= types.InlineKeyboardButton(text='Оставить отзыв', callback_data='otziv');
    keyboard.add(key_otziv);
    key_contact= types.InlineKeyboardButton(text='Узнать контакты', callback_data='contact');
    keyboard.add(key_contact);
    key_cena= types.InlineKeyboardButton(text='Прайс-лист', callback_data='cena');
    keyboard.add(key_cena);
    question = 'Чем могу помочь?';
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    

@bot.message_handler(['text'])
def func(message):
           
	get_msg(message);
def get_number(message):
                global number;
                number = message.text;
                keyboard = types.InlineKeyboardMarkup(); # клавиатура
                key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
                keyboard.add(key_yes); #добавляем кнопку в клавиатуру
                key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
                keyboard.add(key_no);
                question = 'Ваш адрес '+str(adres)+', удобное вам время '+str(time)+', ваш контактный телефон '+str(number)+'?';
                bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
def get_time(message):
                global time;
                time = message.text;
                bot.send_message(message.from_user.id,'Укажите контактный номер');
                bot.register_next_step_handler(message.text, get_number());
def get_adres(call): #получаем время
                bot.reply_to(call,"dsadsa");             
                global adres;
                adres = call;
                bot.send_message(call.from_user.id, 'В какое время вам будет удобно ?');
                bot.register_next_step_handler(call, get_time());





    
    
                               
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    
        if call.data == "zakaz": #call.data это callback_data, которую мы указали при объявлении кнопки
        #код сохранения данных, или их обработки
            #bot.send_message(call.message.chat.id, 'Пожалуйста,укажите\n Адрес:\nВремя:  \nКонтактный телефон:');
        #@bot.message_handler(content_types=['text'])
        #def reply(message):
        	#bot.reply_to(484759206, message.text);
        	#bot.send_message(call.message.chat.id, 'Спасибо');
            #@bot.message_handler(content_types=['text'])
            #def start(message):
                #if call.data == "zakaz":
            bot.send_message(call.from_user.id,"Пожалуйста укажите\nАдрес:\nУдобное Вам Время:\nКонтактный телефон:")
            @bot.message_handler(content_types=['text'])
            def send(call):
                
                bot.forward_message(227539575, call.from_user.id, call.message_id);
                bot.send_message(call.from_user.id,"Спасибо за заказ, с Вами свяжутся")
            #bot.send_message(call.from_user.id, "Укажите ваш адрес");
            #bot.register_next_step_handler(call, get_adres(call)); #следующий шаг – функция get_adres 
            #bot.forward_message(484759206, call.message.chat.id, call);
            #func(message);
            
            
            


    
             
               
        
        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
                if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки

                    bot.send_message(call.message.chat.id, 'Спасибо за заказ! : )');
                elif call.data == "no":
                    ... #переспрашиваем
#bot.send_message(message.from_user.id, 'Ваш адрес '+str(adrres)+', удобное вам время '+str(time)+', ваш контактный телефон '+str(number)+'?')
        if call.data == "otziv":
            bot.send_message(call.message.chat.id, 'Напишите отзыв');
            @bot.message_handler(content_types=['text'])
            def send(call):
           
                bot.forward_message(227539575, call.from_user.id, call.message_id);
                bot.send_message(call.from_user.id,"Спасибо за отзыв!")
        elif call.data == "contact":
    	    bot.send_message(call.message.chat.id, 'Наш instagram - instagram.com/alexacleaning \nНаш сайт - alexa-cleaning.kz \nНаши номера: \n+7 702 443 65 87 \n+7 (7172) 39 67 64 ' );
        elif call.data == "cena":
    	    photo = open('1.png', 'rb')
    	    photo2 = open('2.png', 'rb')
    	    bot.send_message(call.message.chat.id, 'Ознакомьтесь с нашими услугами');
    	    bot.send_photo(call.message.chat.id, photo)
    	    bot.send_photo(call.message.chat.id, photo2)
bot.polling( none_stop = True) 	
