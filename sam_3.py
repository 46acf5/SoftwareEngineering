def heron_area(a, b, c):

    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        raise ValueError("Стороны не могут образовать треугольник")

def main():
    one = [12, 25, 3, 48, 71]
    two = [5, 18, 40, 62, 98]
    three = [4, 21, 37, 56, 84]

    try:
        area_max = heron_area(max(one), max(two), max(three))
        print(f"Площадь максимального треугольника равна {area_max:.2f}")
        area_min = heron_area(min(one), min(two), min(three))
        print(f"Площадь минимального треугольника равна {area_min:.2f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
