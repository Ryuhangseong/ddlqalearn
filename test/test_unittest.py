import unittest
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from module.HTMLTestRunner_PY3 import HTMLTestRunner
from ddt import ddt, data, unpack, file_data

class demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('0')

    def setUp(self) -> None:
        print('1')

    def tearDown(self) -> None:
        print('2')

    @classmethod
    def tearDownClass(cls) -> None:
        print('3')

    def test_case01(self):
        self.assertEqual(1, 2, "Not")
        # self.assertNotIn('h', 'this', 'No')

    def test_case02(self):
        self.assertEqual(2, 3, "Not")
        # self.assertNotIn('h', 'this', 'No')

    def test_case03(self):
        self.assertEqual(3, 3, "Not")
        # self.assertNotIn('h', 'this', 'No')


@ddt
class demo1(unittest.TestCase):

    @data({"a":"1", "b":"2"})
    def test_demo1_case1(self, data):
        print(data)

    def test_demo1_case2(self):
        print('test_demo 2 case')

    @unittest.SkipTest
    def test_demo1_case3(self):
        print('test_demo 3 case')


class demo2(unittest.TestCase):

    def test_demo2_case1(self):
        print('test_demo2 1 case')

    def test_demo2_case2(self):
        print('test_demo2 2 case')

    def test_demo2_case3(self):
        print('test_demo2 3 case')
        
class demo3(unittest.TestCase):

    
    def test_demo3_case1(self, env):
        if "test" in env:
            print("This is a test env.")
        elif "dev" in env:
            print("This is a dev env.")

    def test_demo3_case2(self):
        print('test_demo3 2 case')

    def test_demo3_case3(self):
        print('test_demo3 3 case')



if __name__ == '__main__':
    
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # suite.addTest(demo1("test_demo1_case2"))
    # unittest.TextTestRunner().run(suite)

    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteline = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner().run(suiteline)

    # discover = unittest.defaultTestLoader.discover('./', 'test*.py')
    # unittest.TextTestRunner().run(discover)
    
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(demo))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(demo1))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(demo2))
    
    curent_dirc = os.path.dirname(os.path.realpath(__file__))
    report_dirc = "\Report"
    now = time.strftime("%Y%m%d-%H%M%S")
    report_name = curent_dirc + report_dirc + "\\" + now + "report.html"
    # fp = open(report_name,"wb")
    # runner = HTMLTestRunner(stream=fp, title="Introduction", description="Examples")
    # runner.run(testsuite)
    # fp.close()
    with open(report_name, "wb") as report:
        runner = HTMLTestRunner(stream=report, title="Introduction", description="Examples")
        runner.run(testsuite)
        report.close()
        
 