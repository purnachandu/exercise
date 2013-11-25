import unittest
from ex import check

class Mytest(unittest.TestCase):
    def test(self):
        result=["1990","jan","d","40"]
        self.assertEqual(check("year,month,a,b,c,d","1990,jan,30,20,15,40"),
                         result)

if __name__ == '__main__':
    unittest.main()

    
