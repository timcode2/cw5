Парсер вакансий с сервиса HH.ru. Отслеживает вакансии десяти выбранных мной компаний. Полученные данные храняться в БД Postgres. Есть возможность фильтрации вакансий с помощью методов ниже:

- get_companies_and_vacancies_count(): получает список всех компаний и количество вакансий у каждой компании.
- get_all_vacancies(): получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
- get_avg_salary(): получает среднюю зарплату по вакансиям.
- get_vacancies_with_higher_salary(): получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
- get_vacancies_with_keyword(): получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.
