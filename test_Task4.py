import unittest
from Task4 import (is_independent_set,
                   find_max_independent_set_bruteforce,
                   find_max_independent_set_backtracking)


class TestGraphAlgorithms(unittest.TestCase):

    def test_is_independent_set(self):
        edges = [(0, 1), (1, 2), (2, 3)]
        self.assertTrue(is_independent_set(edges, [0, 2]))
        self.assertTrue(is_independent_set(edges, [1, 3]))
        self.assertFalse(is_independent_set(edges, [0, 1]))
        self.assertFalse(is_independent_set(edges, [1, 2, 3]))

    def test_find_max_independent_set(self):

        for find_max_independent_set in [find_max_independent_set_bruteforce, find_max_independent_set_backtracking]:
            # EXTRA TESTS
            result = find_max_independent_set(1, [])
            self.assertEqual(len(result), 1)

            result = find_max_independent_set(3, [])
            self.assertEqual(len(result), 3)

            result = find_max_independent_set(2, [(0, 1)])
            self.assertEqual(len(result), 1)

            result = find_max_independent_set(3, [(0, 1), (0, 2), (1, 2)])
            self.assertEqual(len(result), 1)

            # TEST 1
            n = 5

            # 1.1
            edges = [(0, 1), (0, 2), (1, 3)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 3)

            # 1.2
            edges = [(0, 1), (0, 3), (1, 2), (1, 3), (2, 4)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 2)

            # 1.3
            edges = [(0, 2), (1, 4), (2, 3), (3, 4)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 3)

            # 1.4
            edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (2, 3), (3, 4)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 2)

            # 1.5
            edges = [(0, 1), (0, 3), (1, 2), (1, 4), (2, 3)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 3)

            # 1.6
            edges = [(0, 3), (0, 4), (1, 2), (1, 3), (2, 4)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 2)

            # TEST 2
            n = 10

            # 2.1
            edges = [(0, 2), (0, 8), (0, 9), (1, 3), (1, 4), (1, 6), (1, 9), (2, 4), (3, 7), (4, 7), (4, 9), (5, 7), (5, 8),
                     (5, 9), (6, 7), (6, 8), (7, 8), (8, 9)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 5)

            # 2.2
            edges = [(0, 1), (0, 4), (0, 9), (1, 3), (1, 5), (2, 4), (2, 9), (3, 5), (4, 5), (4, 6), (4, 7), (4, 8), (5, 6),
                     (5, 8), (8, 9)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 6)

            # 2.3
            edges = [(0, 5), (0, 7), (0, 8), (1, 9), (2, 4), (2, 6), (2, 8), (3, 5), (3, 6), (4, 5), (4, 6), (4, 9), (5, 6),
                     (5, 9), (6, 8), (7, 8), (7, 9)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 4)

            # 2.4
            edges = [(0, 3), (0, 4), (0, 6), (0, 7), (1, 2), (1, 4), (1, 6), (1, 8), (2, 3), (2, 5), (2, 6), (2, 7), (3, 4),
                     (4, 5), (4, 9), (5, 9)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 5)

            # 2.5
            edges = [(0, 1), (0, 2), (0, 4), (0, 5), (0, 7), (1, 5), (2, 3), (2, 4), (2, 5), (2, 7), (2, 9), (3, 7), (4, 6),
                     (4, 8), (5, 9)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 5)

            # 2.6
            edges = [(0, 2), (1, 3), (1, 5), (1, 7), (1, 8), (1, 9), (2, 6), (2, 7), (3, 4), (3, 6), (4, 5), (4, 8), (4, 9),
                     (5, 6), (5, 8), (6, 9)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 5)

            # TEST 3
            n = 15

            # 3.1
            edges = [(0, 4), (0, 5), (0, 6), (1, 13), (2, 14), (3, 12), (3, 13), (4, 8), (6, 10), (6, 13), (7, 11), (7, 14),
                     (8, 10), (9, 12), (12, 13)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 8)

            # 3.2
            edges = [(0, 9), (0, 11), (1, 10), (1, 11), (2, 3), (2, 10), (3, 13), (4, 11), (5, 12), (6, 7), (7, 8), (7, 12),
                     (8, 12), (9, 14), (11, 12)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 9)

            # 3.3
            edges = [(1, 3), (1, 11), (2, 4), (2, 14), (3, 8), (3, 9), (3, 11), (3, 12), (4, 9), (5, 9), (5, 13), (6, 11),
                     (6, 13), (7, 8), (7, 12), (8, 13), (9, 13), (12, 14)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 8)

            # 3.4
            edges = [(0, 1), (0, 13), (1, 3), (1, 5), (2, 11), (5, 6), (5, 9), (6, 7), (6, 8), (7, 10), (7, 12), (7, 14),
                     (9, 14), (10, 11), (10, 13), (10, 14), (11, 13), (12, 14)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 8)

            # 3.5
            edges = [(0, 6), (0, 12), (0, 14), (1, 9), (1, 11), (1, 12), (2, 5), (2, 7), (3, 4), (3, 10), (3, 11), (3, 12),
                     (4, 7), (4, 8), (4, 10), (4, 11), (4, 13), (4, 14), (5, 10), (5, 11), (5, 12), (6, 9), (8, 11),
                     (10, 11), (11, 14)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 8)

            # 3.6
            edges = [(0, 14), (1, 4), (2, 8), (2, 13), (3, 8), (4, 5), (4, 7), (5, 7), (5, 12), (5, 13), (6, 8), (7, 10),
                     (7, 14), (10, 13), (10, 14)]
            result = find_max_independent_set(n, edges)
            self.assertEqual(len(result), 9)


if __name__ == '__main__':
    unittest.main()
