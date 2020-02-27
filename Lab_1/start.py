import numpy as np
import csv


def start_work():
    students = read_students()
    scores = []
    map = dict()

    for student1 in students:
        for student2 in students:
            if student1.name != student2.name:
                values1 = []
                values2 = []

                for value in student1.values:
                    if value is not ' ' and value is not None:
                        values1.append(int(value))
                    else:
                        values1.append(0)

                for value in student2.values:
                    if value is not ' ' and value is not None:
                        values2.append(int(value))

                score = cosine_similarity(values1, values2)
                string = "(" + student1.name.decode('utf-8', 'ignore').strip() + "," + student2.name.decode('utf-8', 'ignore').strip() + "): " + str(score)
                scores.append(string)

    for string in scores:
        names = string.split(":")[0]
        score = float(string.split(":")[1].strip())
        names.replace("(", "")
        names.replace(")", "")

        key = names.split(",")[0]
        pair = Pair(names.split(",")[1], float(score))

        if key in map:
            temp = map.get(key)

            if temp.value < score:
                map[key] = pair
        else:
            map[key] = pair

    # print(scores)
    answer = []
    i = 1
    for key, value in map.items():
        string = "("+key+","+value.name+")"+": "+str(value.value)
        print(i, string)
        answer.append(string)
        i += 1

    text_file = open("Output.txt", "w")
    text_file.write(str(answer))
    text_file.close()


def read_students():
    name = '/Users/pd/PycharmProjects/MA_Labs/Lab_1/icecream_responses.csv'
    students = []

    with open(name, newline='', encoding='utf-8') as file:
        next(file)
        for string in csv.reader(file):
            value = ''

            for i in range(1, len(string)):
                if string[i] is not '':
                    value += string[i]
                else:
                    value += '0'

            temp = Student(string[0].encode('ascii', 'ignore'), value)
            students.append(temp)

    return students


def cosine_similarity(values1, values2):
    numer = np.sum(np.multiply(values1, values2))
    denom = np.sqrt(np.sum(np.square(values1))) * np.sqrt(np.sum(np.square(values2)))

    if denom is 0:
        return 0.0
    else:
        some = float(numer / denom)
        if some >= 0.000001:
            return some
        else:
            return 0.0


class Student:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def __str__(self):
        return "".join([str(x) + " " for x in self.values])


class Pair:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "(" + self.name.decode('utf-8', 'ignore') + "," + self.value + ")"


class Same:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def __str__(self):
        return "(" + self.name1.decode('utf-8', 'ignore') + "," + self.name2.decode('utf-8', 'ignore') + ")"


start_work()