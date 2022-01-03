# referralLink
checking if user switched to the bot by correct referral link

Results of work:
- if user switched to bot witout referral link, result is message "Вы не можете начать использовать бот без реферальной ссылки. Перейдите в бот с помощью реферальной ссылки"
- if user switched to bot by correct referral link, result is messsage "Приветствую <user.name>! Твой уникальный код - <user.id>"
- if user swithched to bot incorrect referral link:
                 -- if amount of such usings < bot.config.maxIncorrectAmount, result is message "Ссылка, по которой вы перешли недействительна. Обратитесь к           собственику бота"
                 -- else blocking user chat




To start project you need:
1. specify API_TOKEN for telegram bot api in bot.config.py
2. specify user's name and password in tgbot.settings.py for using PostgreSQL
3. creating superuser by running command python manage.py createsuperuser in the root project folder
4. startting django server by running command python manage.py runserver in the root project folder
5. starting bot polling by running command python app.py in .bot package


