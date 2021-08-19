import unittest
import RobinhoodParser

class TestGoldFee(unittest.TestCase):
    def testSingleLine(self):
        RobinhoodParser.goldCost = 0
        line = "Gold Fee Margin GOLD 04/27/2021 $5.00"
        RobinhoodParser.goldFee(line)
        self.assertEqual(RobinhoodParser.goldCost, 5)
    
    def testDoubleLine(self):
        RobinhoodParser.goldCost = 0
        line = "Gold Fee Margin GOLD 04/27/2021 $5.00"
        RobinhoodParser.goldFee(line)
        RobinhoodParser.goldFee(line)
        self.assertEqual(RobinhoodParser.goldCost, 10)

class TestRegularStock(unittest.TestCase):
    def testStockBuy(self):
        RobinhoodParser.tickerDict = {}
        line = "Unsolicited, CUSIP: 277802302 EAST Margin Buy 03/31/2021 7 $1.90 $13.30"
        RobinhoodParser.regularStock(line)
        stock = RobinhoodParser.tickerDict.get("EAST")
        self.assertEqual(stock.name, "EAST")
        self.assertAlmostEqual(stock.avarageCost, 1.90)
        self.assertAlmostEqual(stock.shares, 7)
        print(stock.trades[0])

    def testDoubleStockBuy(self):
        RobinhoodParser.tickerDict = {}

        line = "Unsolicited, CUSIP: 277802302 EAST Margin Buy 03/31/2021 10 $2.00 $20.00"
        RobinhoodParser.regularStock(line)
        line = "Unsolicited, CUSIP: 277802302 EAST Margin Buy 04/31/2021 10 $4.00 $40.00"
        RobinhoodParser.regularStock(line)

        stock = RobinhoodParser.tickerDict.get("EAST")
        self.assertEqual(stock.name, "EAST")
        self.assertAlmostEqual(stock.avarageCost, 3.00)
        self.assertAlmostEqual(stock.shares, 20)
        print(stock.trades[0])

    def testStockBuyAndSell(self):
        RobinhoodParser.tickerDict = {}

        line = "Unsolicited, CUSIP: 277802302 EAST Margin Buy 03/31/2021 10 $2.00 $20.00"
        RobinhoodParser.regularStock(line)
        line = "Unsolicited, CUSIP: 277802302 EAST Margin Sell 04/31/2021 5 $4.00 $40.00"
        RobinhoodParser.regularStock(line)

        stock = RobinhoodParser.tickerDict.get("EAST")
        self.assertEqual(stock.name, "EAST")
        self.assertAlmostEqual(stock.deltaMoney, 10.00)
        self.assertAlmostEqual(stock.shares, 5)
        self.assertAlmostEqual(stock.avarageCost, 2.00)
        print(stock.trades[0])


unittest.main()