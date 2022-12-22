import add_to_db
import extract
import view
import logging

def phone_book():
    menu = 0
    while menu != 4:
        menu = view.show_menu()
        match menu:
            case 1:
                logging.log_info("Выбрана команда 1")
                phone_data = view.write_data()
                add_to_db.add_to_txt(phone_data)
                add_to_db.add_to_csv(phone_data)
                logging.log_info("Готово")
            case 2:
                logging.log_info("Выбрана команда 2 ")
                extract.full_output()
                logging.log_info("Готово.")
            case 3:
                logging.log_info("Выбрана команда 3")
                lastname = view.search_data()
                extract.find_data(lastname)
                logging.log_info("Готово.")