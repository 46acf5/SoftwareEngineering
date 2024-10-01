from triangle_area import heron_area

def get_triangle_sides():

    try:
        a = float(input("Введите длину первой стороны треугольника: "))
        b = float(input("Введите длину второй стороны треугольника: "))
        c = float(input("Введите длину третьей стороны треугольника: "))
        return a, b, c
    except ValueError:
        print("Ошибка: введите числовые значения для сторон.")
        return get_triangle_sides()

def main():

    print("Программа для вычисления площади треугольника по формуле Герона")
    a, b, c = get_triangle_sides()

    try:
        area = heron_area(a, b, c)
        print(f"Площадь треугольника со сторонами {a}, {b}, {c} равна {area:.2f}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
