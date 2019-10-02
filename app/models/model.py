import random

def stud_sorter(student_list, num_tables):
    tables = [{"name": "one", "students": []}, {"name": "two", "students": []}, {"name": "three", "students": []}, {"name": "four", "students": []}, {"name": "five", "students": []}, {"name": "six", "students": []}, {"name": "seven", "students": []}
            ]
    # x = slice(num_tables)
    the_tables = tables[:num_tables]
    random.shuffle(student_list)
    for i in range(len(student_list)):
        # print(student_list[i] + " should sit at " + the_tables[i%len(the_tables)]["name"])
        the_tables[i%len(the_tables)]["students"].append(student_list[i])
    return the_tables
