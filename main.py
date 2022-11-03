import unittest
import xmlrunner

if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output='reports')
    runner.run(unittest.TestLoader().discover("."))

