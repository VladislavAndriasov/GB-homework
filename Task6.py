subj = {}
with open('test.txt', 'r') as file:
    for line in file:
        if '(лаб)' or '(пр)' or '(л)' or '—' in line:
            line = line.replace('(лаб)', ' ')
            line = line.replace('(пр)', ' ')
            line = line.replace('(л)', ' ')
            line = line.replace('—', '0')
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
