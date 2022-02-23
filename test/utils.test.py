import unittest

import _importqftpy
import numpy as np
import quaternion
import qftpy.utils as utils


class test_unit(unittest.TestCase):
    def test(self):
        unit_ = utils.unit(np.quaternion(1, 2, 3, 4))
        self.assertAlmostEqual(np.abs(unit_), 1.0)


class test_isPure(unittest.TestCase):
    def test(self):
        q1 = np.quaternion(0, 1, 1, 1)
        q2 = np.quaternion(1, 2, 3, 4)
        self.assertTrue(utils.isPure(q1))
        self.assertFalse(utils.isPure(q2))


class test_isScalarQ(unittest.TestCase):
    def test(self):
        q1 = np.quaternion(1, 0, 0, 0)
        q2 = np.quaternion(1, 2, 3, 4)
        self.assertTrue(utils.isScalarQ(q1))
        self.assertFalse(utils.isScalarQ(q2))



if __name__ == '__main__':
    unittest.main()
