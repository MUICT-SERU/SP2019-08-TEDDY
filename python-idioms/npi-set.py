def n44():
    student_nationality = ['Thai','Malaysian','Thai','Vietnamese','Vietnamese','Vietnamese','Singaporean','Laos','Cambodian','Cambodian','Chinese']
    unique_nationality = []
    for nationality in student_nationality:
        if nationality not in unique_nationality:
            unique_nationality.append(nationality)

def n45():
    staff_name = ['Catherine','Bryan', 'Kevin', 'Frank', 'Emily', 'Steven', 'George', 'Hallen', 'Sasha', 'Nathan', 'Edward', 'Phillip', 'Scarlet', 'Robert']
    staff_year_of_birth = [1997, 1960, 1971, 1982, 1990, 1995, 1994, 1960, 1983, 1997, 1996, 1960, 1981, 1982]
    unique_year_of_birth = []
    for year in staff_year_of_birth:
        if year not in unique_year_of_birth:
            unique_year_of_birth.append(year)

def n46():
    max_temp = [35.6, 34.7, 34.7, 36.1, 36.4, 36.8, 36.2, 36.2, 35.1, 35.0]
    min_temp = [27.1, 27.0, 26.8, 26.8, 27.0, 27.5, 27.2, 27.2, 26.9, 26.7]
    unique_max_temp = []
    unique_min_temp = []
    for temp in max_temp:
        if temp not in unique_max_temp:
            unique_max_temp.append(temp)
    for temp in min_temp:
        if temp not in unique_min_temp:
            unique_min_temp.append(temp)

def n47():
    grade = ['A','B','B','B','C','D','F','C','C','D','A']\
    student_placeholder = 'John Doe'
    unique_grade = []
    for g in grade:
        if g not in unique_grade:
            unique_grade.append(g)

