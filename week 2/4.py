students = int(input('how many students?'))
sweets = int(input('how many sweets?'))
no_of_sweets_to_student = sweets // students
remaining_sweets = sweets % students
print(f'Each student gets {no_of_sweets_to_student} sweets with {remaining_sweets} sweets left over. ')
