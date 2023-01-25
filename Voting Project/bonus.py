# key = student id (str)
# val = num of credits
student_ids = dict()  # key = id, val = name
student_creds = dict()  # key = id, val = creds

students = open('graduates.txt', 'r')

for line in students:
    sid, name, creds = line.strip(), students.readline().strip(), students.readline().strip()

    if sid.isnumeric():
        student_ids[sid] = name
        student_creds[sid] = int(creds)

summer = open('summer2021.txt', 'r')

for line in summer:
    sid, creds = line.strip(), summer.readline().strip()

    if sid in student_creds:
        student_creds[sid] += int(creds)

graduating = list()
nongraduating = list()

for std in student_creds:  # keys
    if student_creds[std] >= 120:
        graduating.append(std)  # append student id
    
    else:
        nongraduating.append(std)

# Printing stuff...
print('Report of graduating students by Alexis:')
print('Name\t\tCredits')

for sid in graduating:
    print('{0}\t{1}'.format(student_ids[sid], student_creds[sid]))

print('\nReport of non-graduating students:')
print('Name\t\tCredits\t\tCredits Needed')

for sid in nongraduating:
    print('{0}\t{1}\t\t{2}'.format(
        student_ids[sid],
        student_creds[sid],
        120 - student_creds[sid]
    ))