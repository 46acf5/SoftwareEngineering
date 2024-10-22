def add_film():
    """Добавление нового фильма в список"""
    film = input("Введите название фильма: ")
    with open('films.txt', 'a', encoding='utf-8') as file:
        file.write(f"{film}\n")
    print(f"Фильм '{film}' добавлен в список.")

def view_films():
    """Просмотр всех добавленных фильмов"""
    try:
        with open('films.txt', 'r', encoding='utf-8') as file:
            films = file.readlines()
            if films:
                print("\nСписок любимых фильмов:")
                for i, film in enumerate(films, 1):
                    print(f"{i}. {film.strip()}")
            else:
                print("Список фильмов пуст.")
    except FileNotFoundError:
        print("Файл с фильмами не найден.")

def main():
    while True:
        print("\n1. Добавить фильм")
        print("2. Просмотреть список фильмов")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_film()
        elif choice == '2':
            view_films()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

main()

