from application.salary import *
from application.db.people import *
from datetime import *

def main():
    calculate_salary()
    get_employees()
    date = datetime.now()
    print(f'Текущая дата и время {date}')
    print('Но так импортировать модули не хорошо! Я внимательно слушал лекцию)')

if __name__ == '__main__':
    main()