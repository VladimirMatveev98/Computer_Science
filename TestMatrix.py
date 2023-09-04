import unittest
from Matrix import Matrix

class TestMatrix(unittest.TestCase):

    test_1_1 = {(1,1):1,(2,1):1,(3,1):1,(1,2):2,(2,2):2,(3,2):2,
            (1,3):3,(2,3):3,(3,3):3}

    test_1_2 = {(1,1):1,(2,1):2,(3,1):1,(1,2):3,(2,2):4,(3,2):6,
            (1,3):7,(2,3):8,(3,3):9}

    answer_1 = {(1,1):11,(2,1):14,(3,1):16,(1,2):22,(2,2):28,(3,2):32,
                   (1,3):33,(2,3):42,(3,3):48}

    def setUp(self):
        self.matrix = Matrix()
        self.matrix.insert(self.test_1_1)
        self.matrix_2 = Matrix()
        self.matrix_2.insert(self.test_1_2)
        self.m_answer = Matrix()
        self.m_answer.insert(self.answer_1)

    def test_add(self):
        self.assertEqual(self.matrix.mult_matrix(self.matrix_2), self.m_answer)



if __name__ == "__main__":
  unittest.main()
