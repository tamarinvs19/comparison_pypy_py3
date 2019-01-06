import g0
import g
import unittest
from unittest.mock import patch, MagicMock
from random import randint

def generate_test():
    n, m = randint(1, 10**1), randint(1, 10**2)
    rs = [(randint(1, n), randint(1, n)) for _ in range(m)]
    g = [list() for _ in range(n)]
    h = [list() for _ in range(n)]
    for r in rs:
        a, b = map(int, r)
        g[a-1].append(b-1)
        h[b-1].append(a-1)
    return n, m, g, h
count = 100
test_data = [generate_test() for _ in range(count)]

class TestG(unittest.TestCase):
    @patch('g.my_input', side_effect=test_data)
    @patch('g0.my_input', side_effect=test_data)
    def test_sim_g(self, m_input1, m_input2):
        for i in range(count):
            ans1, ans2 = g.main(), g0.main()
            if ans1 != ans2:
                print(test_data[i][0:3])
            self.assertEqual(ans1, ans2)

if __name__ == '__main__':
    unittest.main()
