from app import app
from flask import render_template, request
from app.models import model, formopener
import random

@app.route('/')
@app.route('/index')
@app.route('/results', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        class_list_dict = dict(request.form)
        class_list_string = class_list_dict['class_list'][0]
        class_list = class_list_string.split(", ")
        print(class_list)
        # table_names = ["one", "two", "three", "four", "five", "six", "seven"]
        
        random.shuffle(class_list)
        class_length = len(class_list)
        if class_length <= 28:
            if class_length%4 == 0:
                num_tables = class_length/4
                tables = model.stud_sorter(class_list, num_tables)
            else: 
                num_tables = class_length/4 + 1
                tables = model.stud_sorter(class_list, num_tables)
        else: 
            if class_length%5 == 0:
                num_tables = class_length/5
                tables = model.stud_sorter(class_list, num_tables)
            else:
                num_tables = class_length/5 + 1
                tables = model.stud_sorter(class_list, num_tables)
        # for table in range(num_tables):
        #     print(table)
        print(tables)
        stud_groups = []
        for table in tables: 
            stud_groups.append(table["students"])
        # print(stud_groups)
        # stud_groups = formopener(stud_groups)
        return render_template("index.html", stud_groups = stud_groups)
