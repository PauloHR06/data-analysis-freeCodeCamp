import pandas as pd

def analyze_demographic_data(display_data=True):
    # Leitura do CSV.
    data = pd.read_csv("adult.data.csv")

    # número de raças no df.
    race_distribution = data['race'].value_counts()

    # idade média entre os homens.
    male_population = data[data['sex'] == "Male"]
    avg_age_men = round(male_population['age'].mean(), 1)

    # porcentagem de pessoas com 13 anos ou mais de educação.
    advanced_education = data[data['education-num'] >= 13]
    percentage_with_advanced_education = round((advanced_education.shape[0] / data.shape[0]) * 100, 1)

    # porcentagem de pessoas com bacharelado.
    bachelor_degree = data[data['education'] == "Bachelors"]
    percentage_with_bachelor = round((bachelor_degree.shape[0] / data.shape[0]) * 100, 1)

    # porcentagem de graduados que ganham mais de 50K
    advanced_education_high_salary = round((advanced_education[advanced_education['salary'] == ">50K"].shape[0] / advanced_education.shape[0]) * 100, 1)
    basic_education = data[~data['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    basic_education_high_salary = round((basic_education[basic_education['salary'] == ">50K"].shape[0] / basic_education.shape[0]) * 100, 1)

    # número mínimo de horas trabalhadas por semana
    min_hours_per_week = data['hours-per-week'].min()

    # Porcentagem de pessoas que trabalham o mínimo de horas e ganham mais de 50K
    min_hours_workers = data[data['hours-per-week'] == min_hours_per_week]
    min_hours_high_income = round((min_hours_workers[min_hours_workers['salary'] == ">50K"].shape[0] / min_hours_workers.shape[0]) * 100, 1)

    # país com a maior porcentagem de pessoas que ganham mais de 50K
    salary_above_50K_by_country = data[data['salary'] == ">50K"]['native-country'].value_counts()
    total_population_by_country = data['native-country'].value_counts()
    country_salary_percentage = (salary_above_50K_by_country / total_population_by_country) * 100

    country_with_highest_salary_percentage = country_salary_percentage.idxmax()
    highest_salary_percentage = round(country_salary_percentage.max(), 1)

    # ocupação mais comum entre pessoas que ganham mais de 50K na Índia
    high_salary_occupation_in_India = data[(data['salary'] == ">50K") & (data['native-country'] == "India")]['occupation'].value_counts()
    most_common_occupation_in_India = high_salary_occupation_in_India.idxmax()

    # porcentagem de pessoas casadas com 13 anos ou mais de educação
    married_with_advanced_education = data[(data['marital-status'] == "Married-civ-spouse") & (data['education-num'] >= 13)]
    percentage_married_with_advanced_education = round((married_with_advanced_education.shape[0] / data.shape[0]) * 100, 1)

    if display_data:
        print("Distribuição racial:\n", race_distribution)
        print("Idade média dos homens:", avg_age_men)
        print(f"Porcentagem com 13 anos ou mais de educação: {percentage_with_advanced_education}%")
        print(f"Porcentagem com bacharelado: {percentage_with_bachelor}%")
        print(f"Porcentagem de pessoas com educação avançada que ganham >50K: {advanced_education_high_salary}%")
        print(f"Porcentagem de pessoas sem educação avançada que ganham >50K: {basic_education_high_salary}%")
        print(f"Menor número de horas trabalhadas por semana: {min_hours_per_week} horas/semana")
        print(f"Porcentagem de ricos entre os que trabalham menos horas: {min_hours_high_income}%")
        print("País com maior porcentagem de pessoas que ganham mais de 50K:", country_with_highest_salary_percentage)
        print(f"Maior porcentagem de pessoas ricas em um país: {highest_salary_percentage}%")
        print("Ocupação mais comum na Índia para quem ganha mais de 50K:", most_common_occupation_in_India)
        print(f"Porcentagem de pessoas casadas com 13 anos ou mais de educação: {percentage_married_with_advanced_education}%")

    return {
        'race_distribution': race_distribution,
        'avg_age_men': avg_age_men,
        'percentage_with_advanced_education': percentage_with_advanced_education,
        'percentage_with_bachelor': percentage_with_bachelor,
        'advanced_education_high_salary': advanced_education_high_salary,
        'basic_education_high_salary': basic_education_high_salary,
        'min_hours_per_week': min_hours_per_week,
        'min_hours_high_income': min_hours_high_income,
        'country_with_highest_salary_percentage': country_with_highest_salary_percentage,
        'highest_salary_percentage': highest_salary_percentage,
        'most_common_occupation_in_India': most_common_occupation_in_India,
        'percentage_married_with_advanced_education': percentage_married_with_advanced_education
    }
