import unittest
import RunnerTest
import TournamentTest

ut = unittest.TestSuite()
ut.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
ut.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ut)
