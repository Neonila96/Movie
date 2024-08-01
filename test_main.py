from _pytest import unittest

import unittest

from main import MoviesLibrary


class TestMoviesLibrary(unittest.TestCase):

    def test_add_and_recommend_movies(self):
        library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

        library.add_movie('Комедия', 'Весёлый питонист')
        library.add_movie('Комедия', 'Три разраба и тестировщик')

        self.assertEqual(library.recommend('Комедия'), ['Весёлый питонист', 'Три разраба и тестировщик'])

    def test_recommend_empty_genre(self):
        library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

        self.assertEqual(library.recommend('Ужасы'), [])

    def test_shared_movie_list_bug(self):
        library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

        library.add_movie('Комедия', 'Весёлый питонист')

        self.assertEqual(library.recommend('Ужасы'), [])
        self.assertEqual(library.recommend('Романтика'), [])

if __name__ == '__main__':
    unittest.main()