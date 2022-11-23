# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_object_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_object_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_object_parameters(line, obj):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    parameters = line.split()
    obj.R = float(parameters[1])
    obj.color = parameters[2]
    obj.m = float(parameters[3])
    obj.x = float(parameters[4])
    obj.y = float(parameters[5])
    obj.Vx = float(parameters[6])
    obj.Vy = float(parameters[7])
    pass


def create_line(object):
    if object.type == "star":
        return "Star" + " " + str(object.R) + " " + str(object.color) + " " + str(object.m) + " " + str(object.x) + " "\
               + str(object.y) + " " + str(object.Vx) + " " + str(object.Vy) + 2 * "\n"
    if object.type == "planet":
        return "Planet" + " " + str(object.R) + " " + str(object.color) + " " + str(object.m) + " " + str(object.x) + " " \
               + str(object.y) + " " + str(object.Vx) + " " + str(object.Vy) + 2 * "\n"


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.writelines(create_line(obj))


if __name__ == "__main__":
    print("This module is not for direct call!")
