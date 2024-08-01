from _pytest import unittest

from main import MoviesLibrary


def test_add_and_recommend_movies(self):
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

    # Тестируем добавление фильмов в жанр "Комедия"
    library.add_movie('Комедия', 'Весёлый питонист')
    library.add_movie('Комедия', 'Три разраба и тестировщик')

    # Проверяем, что рекомендации по жанру "Комедия" возвращают правильный список фильмов
    self.assertEqual(library.recommend('Комедия'), ['Весёлый питонист', 'Три разраба и тестировщик'])


def test_recommend_empty_genre(self):
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

    # Проверяем, что рекомендации для пустого жанра возвращают пустой список
    self.assertEqual(library.recommend('Ужасы'), [])


def test_shared_movie_list_bug(self):
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

    # Добавляем фильм в жанр "Комедия"
    library.add_movie('Комедия', 'Весёлый питонист')

    # Проверяем, что фильм не добавился в другие жанры
    self.assertEqual(library.recommend('Ужасы'), [])
    self.assertEqual(library.recommend('Романтика'), [])


if __name__ == '__main__':
    unittest.main()