
var1 = "Oxford"
var2 = 10
var3 = True
var4 = [ 5, 10, 20]
var5 = ( 1, 2, 3)
var6 = {10, 20, 30}
var7 = { 'newkey': var6}

my_dict =  { 'key1': 'value1', 'key2': 'value2'}
another_dict = { 1 : 15, 2 : 75, 3 : 150}
and_another_dict = { 'key1': var1, 'key2': var3, 'key3': var7}

#varianter av dicts
lottery_player = {
    'name' : 'Lee',
    'numbers' : (1, 3, 5, 7)
}

#Summera value av key['numbers']
'''print(sum(lottery_player['numbers']))

#Lista med dicts
universities = [
    {
        'name' : var1,
        'location' : 'England'
    },
    {
        'name' : 'MIT',
        'location' : 'US'
    }
]

#Printing key['name'] i dict'en som ligger i listan universities[0]
print(universities[0]['name'])

dict_in_dict = {
    'dict1' : {
        'dict2' : {
            'lista' : var4
        },
    },
}
#printar value av key['lista']
print(dict_in_dict['dict1']['dict2']['lista'])'''

student_dict = {
    '1' : {
        'name' : 'John',
        'grades' : {
        'Science' : 40,
        'Math' : 50,
        'History' : 55,
        },
        'school' : 'MIT'
    },
    '2' : {
        'name' : 'Lee',
        'grades' : {
        'Science' : 55,
        'Math' : 40,
        'History' : 70
        },
        'school' : 'MIT'
    }
}

def average_grade(data):
    grades = data['grades']
    return sum(grades)/len(grades)

#print(average_grade(student_dict))
all_grades = []
count = 0

def average_grade_all_students(student_list):
    for k,v in student_list.items():
        if isinstance(v, dict):
            for ik,iv in v.items():
                if isinstance(iv, dict):
                    for iik,iiv in iv.items():
                        all_grades.append(iiv)
    return sum(all_grades)/len(all_grades)



#average_grade_all_students(student_dict)
print(average_grade_all_students(student_dict))
