from utils import save_to_data
from db_manager import DBManager

if __name__ == "__main__":
    save_to_data()
    while True:
        print("""
1. Получить список всех компаний и количество вакансий у каждой компании.
2. Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
3. Получить среднюю зарплату по вакансиям.
4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.
5. Получить список вакансий по ключевому слову.
0. Выйти.
        """)
        db_manager = DBManager()
        user_input = int(input("Выберите действие: "))
        if user_input == 1:
            print(db_manager.get_companies_and_vacancies_count())
        elif user_input == 2:
            print(db_manager.get_all_vacancies())
        elif user_input == 3:
            print(round(db_manager.get_avg_salary(), 1))
        elif user_input == 4:
            count = round(db_manager.get_avg_salary(), 1)
            print(db_manager.get_vacancies_with_higher_salary(count))
        elif user_input == 5:
            keyword = input("Введите ключевое слово для поиска: ")
            print(db_manager.get_vacancies_with_keyword(keyword))
        elif user_input == 0:
            break
