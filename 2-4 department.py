department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

line1 = (
    f'Department1 name:{department1:<10}'
    f'Manager:{depart1_m:<10}'
    f'COURSE_FEES:{COURSE_FEES_SEC:<10.2f}'
    f'The End'
)
line2 = (
    f'Department2 name:{department2:<10}'
    f'Manager:{depart2_m:<10}'
    f'COURSE_FEES:{COURSE_FEES_Python:<10.2f}'
    f'The End'
)

lenght = len(line1)
print('=' * lenght)
print(line1)
print('=' * lenght)
print(line2)
print('=' * lenght)