from whatsapp_chatbot_python import GreenAPIBot, Notification
import json

with open('API.json', 'r') as file:
    data = json.load(file)

bot = GreenAPIBot(data["token"], data["api_key"])

COMMANDS = {
    "start": "🤖 Hello! I'm the bot for IKEA employees.\n"
             "I can show the schedule, contact details, store addresses, and other useful information.\n\n"
             "👨‍💻 Developer: Denis Shulzhenko (OPK-411)\n"
             "📌 Type 'help' to learn more about what I can do.",

    "help": "📌 Available commands:\n"
            "- schedule — show the list of employees\n"
            "- ikea addresses — show IKEA store addresses in Sweden\n"
            "- contacts — contact information for IKEA\n"
            "- ikea job — details about working at IKEA\n"
            "- store hours — show IKEA store working hours\n"
            "- product info — information about popular IKEA products\n"
            "- employee benefits — details about employee benefits at IKEA\n"
            "- events — list of upcoming events and promotions in IKEA stores\n"
            "- career growth — opportunities for career growth in IKEA\n"
            "- job apply — apply for a job at IKEA",

    "contacts": "📞 Contact Information for IKEA:\n"
                "📧 Email: support@ikea.com\n"
                "📞 Phone: +46 700000000\n\n"
                "💼 For job opportunities, type 'ikea job'.",

    "ikea addresses": "📍 IKEA Store Addresses in Sweden:\n"
                      "[IKEA Stockholm - Kungens Kurva](https://www.ikea.com/se/sv/store/stockholm-kungens-kurva)\n"
                      "[IKEA Malmö - Fosie](https://www.ikea.com/se/sv/store/malmo-fosie)\n"
                      "[IKEA Gothenburg - Bäckebol](https://www.ikea.com/se/sv/store/gothenburg-backebol)\n"
                      "[IKEA Helsingborg](https://www.ikea.com/se/sv/store/helsingborg)\n"
                      "[IKEA Uppsala](https://www.ikea.com/se/sv/store/uppsala)\n"
                      "[IKEA Linköping](https://www.ikea.com/se/sv/store/linkoping)\n"
                      "[IKEA Täby](https://www.ikea.com/se/sv/store/taby)\n"
                      "[IKEA Örebro](https://www.ikea.com/se/sv/store/orebro)",

    "ikea job": "💼 IKEA offers great working conditions, including:\n"
            "- Hourly wage: between 100 and 200 SEK, depending on the position and experience.\n"
            "- Flexible working hours and a dynamic team environment.\n"
            "- Opportunities for personal growth and advancement.\n"
            "- Discounts on IKEA products and other employee benefits.\n\n"
            "### Job Requirements:\n"
            "1. **Age**: Must be at least 18 years old.\n"
            "2. **Work Experience**: Previous work experience in retail or customer service is preferred but not required.\n"
            "3. **Language Skills**: Proficiency in Swedish (or English for certain positions).\n"
            "4. **Availability**: Must be available to work flexible hours, including evenings, weekends, and holidays.\n"
            "5. **Team Player**: Ability to work well in a team and collaborate with colleagues to achieve store goals.\n"
            "6. **Communication Skills**: Strong communication skills and ability to interact with customers in a friendly and professional manner.\n"
            "7. **Physical Stamina**: Ability to stand for long periods and lift heavy items (depending on the role).\n"
            "8. **Customer Focus**: A passion for customer service and a desire to help others.\n"
            "9. **Motivation**: Strong motivation to develop and grow within the company.\n"
            "10. **Work Permit**: For non-Swedish residents, a valid work permit may be required.",


    "store hours": "🕒 IKEA Store Hours in Sweden:\n"
                   "📍 IKEA Stockholm - Kungens Kurva: 10:00 AM - 9:00 PM\n"
                   "📍 IKEA Malmö - Fosie: 10:00 AM - 9:00 PM\n"
                   "📍 IKEA Gothenburg - Bäckebol: 10:00 AM - 9:00 PM\n"
                   "📍 IKEA Helsingborg: 10:00 AM - 8:00 PM\n"
                   "📍 IKEA Uppsala: 10:00 AM - 8:00 PM\n"
                   "📍 IKEA Linköping: 10:00 AM - 8:00 PM\n"
                   "📍 IKEA Täby: 10:00 AM - 9:00 PM\n"
                   "📍 IKEA Örebro: 10:00 AM - 8:00 PM",

    "product info": "🛒 Popular IKEA Products:\n"
                    "- [Billy Bookcase](https://www.ikea.com/se/sv/p/billy-bookcase-white-00263850/): Classic bookcase available in multiple sizes.\n"
                    "- [Kallax Shelving Unit](https://www.ikea.com/se/sv/p/kallax-shelving-unit-white-00253847/): Versatile storage solution.\n"
                    "- [Poäng Armchair](https://www.ikea.com/se/sv/p/poang-armchair-birch-veneer-light-brown-20355707/): Comfortable armchair with ergonomic design.\n"
                    "- [Hemnes Dresser](https://www.ikea.com/se/sv/p/hemnes-dresser-white-90324792/): Stylish and spacious dresser for any bedroom.",

    "employee benefits": "💼 IKEA Employee Benefits:\n"
                         "- Discounts on IKEA products.\n"
                         "- Health insurance.\n"
                         "- Flexible working hours.\n"
                         "- Opportunities for career growth and development.\n"
                         "- Paid parental leave and vacation days.\n"
                         "- Access to employee wellness programs.",

    "events": "🎉 Upcoming IKEA Events & Promotions:\n"
              "📅 IKEA Stockholm - Kungens Kurva: Spring Sale, March 20th-25th.\n"
              "📅 IKEA Malmö - Fosie: DIY Workshops, March 27th.\n"
              "📅 IKEA Gothenburg - Bäckebol: Family Day, April 5th.\n"
              "📅 IKEA Helsingborg: Seasonal Sale, April 10th-15th.\n"
              "📅 IKEA Uppsala: Cooking Class, April 12th.\n"
              "📅 IKEA Linköping: Interior Design Consultation, April 17th.",

    "career growth": "📈 Career Growth at IKEA:\n"
                     "- Continuous learning opportunities.\n"
                     "- Leadership development programs.\n"
                     "- Opportunities to work internationally.\n"
                     "- Employee-driven projects for innovation.\n"
                     "- Mentorship programs to help you succeed at IKEA",

    "job apply": "📋 Заявка на роботу: Для подачі на роботу, будь ласка, заповніть форму за наступним лінком:\n" 
                 "[Заявка на роботу в IKEA](https://docs.google.com/forms/d/1yRwykwm4MZopJihvkZ-8ZTruKsF0CT_7XVE_FucR42g/edit)"
}

# Функція для завантаження даних співробітників із schedule.json
def load_schedule():
    with open("schedule.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Функція для обробки вхідних повідомлень
@bot.router.message()
def message_handler(notification: Notification) -> None:
    text = notification.message_text.strip().lower()  # Перетворюємо введений текст на нижній регістр для зручності порівняння

    # Обробка команди 'start'
    if text == "start":
        response = COMMANDS["start"]

    # Обробка команди 'help'
    elif text == "help":
        response = COMMANDS["help"]

    # Обробка команди 'contacts'
    elif text == "contacts":
        response = COMMANDS["contacts"]

    # Обробка команди 'ikea addresses'
    elif text == "ikea addresses":
        response = COMMANDS["ikea addresses"]

    # Обробка команди 'ikea job'
    elif text == "ikea job":
        response = COMMANDS["ikea job"]

    # Обробка команди 'store hours'
    elif text == "store hours":
        response = COMMANDS["store hours"]

    # Обробка команди 'product info'
    elif text == "product info":
        response = COMMANDS["product info"]

    # Обробка команди 'employee benefits'
    elif text == "employee benefits":
        response = COMMANDS["employee benefits"]

    # Обробка команди 'events'
    elif text == "events":
        response = COMMANDS["events"]

    # Обробка команди 'career growth'
    elif text == "career growth":
        response = COMMANDS["career growth"]

    # Обробка команди 'job apply'
    elif text == "job apply":
        response = COMMANDS["job apply"]

    # Обробка команди 'schedule' для показу списку співробітників
    elif text == "schedule":
        schedule_data = load_schedule()  # Завантажуємо дані співробітників із schedule.json
        employee_list = "\n".join([name for name in schedule_data.keys()])
        response = f"📋 List of employees:\n{employee_list}\n\nPlease type the name of the employee to see their details (e.g., 'Fredrik Olofsman')."

    # Обробка введення імені співробітника для детальної інформації
    elif text.title() in [name.title() for name in load_schedule().keys()]:
        employee_name = text.title()  # Коректне форматування імені
        schedule_data = load_schedule()  # Завантажуємо дані співробітника із schedule.json

        employee = schedule_data[employee_name]
        response = f"📅 {employee_name}'s schedule: {employee['schedule']}\n\n"
        response += f"📚 Education: {employee['education']}\n"
        response += f"🎂 Age: {employee['age']}\n"
        response += f"🏠 Address: {employee['address']}\n"
        response += f"💼 Experience: {employee['experience']}\n"
        response += f"❤️ Marital Status: {employee['marital_status']}\n"
        response += f"📞 Phone: {employee['phone']}\n"
        response += f"✉️ Email: {employee['email']}\n"
        response += f"💬 WhatsApp: {employee['whatsapp']}"

    # Обробка невідомих команд
    else:
        response = "❌ Command not found. Type 'help' to see the available commands."

    notification.answer(response)

# Запускаємо бота
bot.run_forever()