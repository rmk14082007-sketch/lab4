import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_zero_height(self):
        # Проверяем, что площадь с нулевой высотой = 0
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        # Квадрат 10x10 -> площадь 100
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_rectangle(self):
        # Прямоугольник 3x5 -> площадь 15
        res = area(3, 5)
        self.assertEqual(res, 15)

    def test_perimeter_square(self):
        # Периметр квадрата 4x4 -> 16
        res = perimeter(4, 4)
        self.assertEqual(res, 16)

    def test_perimeter_rectangle(self):
        # Периметр прямоугольника 2x5 -> 14
        res = perimeter(2, 5)
        self.assertEqual(res, 14)

    def test_negative_sides_area(self):
        # Отрицательная сторона -> ожидаем ValueError
        with self.assertRaises(ValueError):
            area(-1, 5)

    def test_negative_sides_perimeter(self):
        # Отрицательная сторона -> ожидаем ValueError
        with self.assertRaises(ValueError):
            perimeter(2, -3)
