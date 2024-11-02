import unittest
import unittest as ut
import runner_and_tournament as rt


class TournamentTest(ut.TestCase):
    is_frozen = True

    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rt.Runner('Усейн', 10)
        self.runner2 = rt.Runner('Андрей', 9)
        self.runner3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print("Результаты всех тестов:")
        for place, runner in cls.all_results.items():
            print(f'Место {place}: {runner.name}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_usain_and_nick(self):
        tournament = rt.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[1].name == "Усейн")
        self.assertTrue(results[2].name == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_andrey_and_nick(self):
        tournament = rt.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[1].name == "Андрей")
        self.assertTrue(results[2].name == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_all_runners(self):
        tournament = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[1].name == "Усейн")
        self.assertTrue(results[2].name == "Андрей")
        self.assertTrue(results[3].name == "Ник")


if __name__ == '__main__':
    ut.main()
