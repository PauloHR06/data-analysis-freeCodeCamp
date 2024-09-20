import unittest
import pandas as pd

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        import demographic_data_analyzer  
        self.data = demographic_data_analyzer.analyze_demographic_data(display_data=False)

    def test_race_distribution(self):
        actual = self.data['race_distribution'].tolist()
        expected = [27800, 3100, 1050, 300, 270]  # valores aleatórios
        self.assertEqual(actual, expected, "Os valores de distribuição racial esperados são [27800, 3100, 1050, 300, 270]")

    def test_avg_age_men(self):
        actual = self.data['avg_age_men']
        expected = 38.7  # valor aleatório
        self.assertAlmostEqual(actual, expected, msg="A idade média dos homens esperada é diferente.")

    def test_percentage_with_bachelor(self):
        actual = self.data['percentage_with_bachelor']
        expected = 15.9  # valor aleatório
        self.assertAlmostEqual(actual, expected, msg="A porcentagem de pessoas com bacharelado está diferente.")

    def test_advanced_education_high_salary(self):
        actual = self.data['advanced_education_high_salary']
        expected = 44.7  # valor aleatório
        self.assertAlmostEqual(actual, expected, msg="A porcentagem de pessoas com educação avançada que ganham >50K está diferente.")

    def test_basic_education_high_salary(self):
        actual = self.data['basic_education_high_salary']
        expected = 18.2  # valor aleatório
        self.assertAlmostEqual(actual, expected, msg="A porcentagem de pessoas sem educação avançada que ganham >50K está diferente.")

    def test_country_with_highest_salary_percentage(self):
        actual = self.data['country_with_highest_salary_percentage']
        expected = 'Iran'  # valor aleatório
        self.assertEqual(actual, expected, "O país com a maior porcentagem de pessoas que ganham mais de 50K está diferente.")

    def test_highest_salary_percentage(self):
        actual = self.data['highest_salary_percentage']
        expected = 42.3  # valor aleatório
        self.assertAlmostEqual(actual, expected, msg="A maior porcentagem de pessoas ricas em um país está diferente.")

    def test_most_common_occupation_in_India(self):
        actual = self.data['most_common_occupation_in_India']
        expected = 'Exec-managerial'  # valor aleatório
        self.assertEqual(actual, expected, "A ocupação mais comum na Índia para quem ganha mais de 50K está diferente.")

    def test_percentage_married_with_advanced_education(self):
        actual = self.data['percentage_married_with_advanced_education']
        expected = 27.5  # valor aleatório
        self.assertAlmostEqual(actual, expected, msg="A porcentagem de casados com 13 anos ou mais de educação está diferente.")

if __name__ == "__main__":
    unittest.main()
