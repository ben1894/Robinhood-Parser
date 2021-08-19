import unittest
import RobinhoodParser

class TestGoldFee(unittest.TestCase):
    def singleLine(self):
        line = "Gold Fee Margin GOLD 04/27/2021 $5.00"
        RobinhoodParser.goldFee(line)
        self.assertEqual(RobinhoodParser.goldCost, 5)
    
    def doubleLine(self):
        line = "Gold Fee Margin GOLD 04/27/2021 $5.00"
        RobinhoodParser.goldFee(line)
        RobinhoodParser.goldFee(line)
        self.assertEqual(RobinhoodParser.goldCost, 10)