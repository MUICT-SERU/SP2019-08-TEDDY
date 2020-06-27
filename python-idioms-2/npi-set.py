def n44():
    for nationality in student_nationality:
        if nationality not in unique_nationality:
            unique_nationality.append(nationality)

def n45():
    for year in staff_year_of_birth:
        if year not in unique_year_of_birth:
            unique_year_of_birth.append(year)

def n46():
    for temp in max_temp:
        if temp not in unique_max_temp:
            unique_max_temp.append(temp)
    for temp in min_temp:
        if temp not in unique_min_temp:
            unique_min_temp.append(temp)

def n47():
    unique_grade = []
    for g in grade:
        if g not in unique_grade:
            unique_grade.append(g)

