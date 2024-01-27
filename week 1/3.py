no_of_students = int(input('How many students?'))
group_size = int(input('Required group size?'))
no_of_groups = no_of_students // group_size
remaining_no_of_students = no_of_students % group_size
print(f'There will be {no_of_groups} groups with {remaining_no_of_students} students left over.')

