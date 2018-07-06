import time
import json
from statistics import median
import numpy as np

# class JSONLooker:
#
#     def __init__(self, tuple):
#         self.JSON_item = tuple
#
#     def __repr__(self):
#         retval = ""
#         retval += str(self.JSON_item[0])
#         for item in self.JSON_item[1]:
#             retval += " -- " + str(item)
#         return retval
# start_time = time.time()


def numStudents(assignments, strassignments):
    for i in range(len(assignments)):
        print(strassignments[i] + ":", len(assignments[i].keys()))

def finalScores(assignments, strassignments):
    for i in range(len(assignments)):
        mylist = []
        for k in assignments[i].keys():
            mylist.append(assignments[i][k][":score"])
        print(strassignments[i] + " min:", min(mylist))
        print(strassignments[i] + " max:", max(mylist))
        print(strassignments[i] + " median:", median(mylist))
        print(strassignments[i] + " mean:", np.mean(mylist))

def autoGradeScore(assignments, strassignments):
    for i in range(len(assignments)):
        mylist = []
        for k in assignments[i].keys():
            for key1 in (assignments[i][k].keys()):
                if key1 == ":results":
                    mylist.append(assignments[i][k][key1]["score"])
        print(strassignments[i] + " min:", min(mylist))
        print(strassignments[i] + " max:", max(mylist))
        print(strassignments[i] + " median:", median(mylist))
        print(strassignments[i] + " mean:", np.mean(mylist))

def latenessCheck(assignments, strassignments):
    for i in range(len(assignments)):
        count = 0
        for k in assignments[i].keys():
            for key1 in (assignments[i][k].keys()):
                if key1 == ":results":
                    if assignments[i][k][key1]["output"] != "Results of the" \
                                                            " entire autograder" \
                                                            " run using autograder" \
                                                            " version 0.23 beta.":
                        count += 1
        percent_late = count/len(assignments[i].keys())
        print(strassignments[i] + ": " + str(percent_late))

def moreThanOneSubmission(assignments, strassignments):
    for i in range(len(assignments)):
        count = 0
        for k in assignments[i].keys():
            if assignments[i][k][":history"] != []:
                count += 1
        percent_more_than_one = count/len(assignments[i].keys())
        print(strassignments[i] + ": " + str(percent_more_than_one))

def numNonFinalSubmissions(assignments, strassignments):
    for i in range(len(assignments)):
        mylist = []
        for k in assignments[i].keys():
            mylist.append(len((assignments[i][k][":history"])))
        print(strassignments[i] + " min:", min(mylist))
        print(strassignments[i] + " max:", max(mylist))
        print(strassignments[i] + " median:", median(mylist))
        print(strassignments[i] + " mean:", np.mean(mylist))


if __name__ == '__main__':

    with open('AUTOCOMPLETE_submission_metadata.json', 'r') as data:
        autocomplete = json.load(data)
    with open('HUFFMAN_submission_metadata.json', 'r') as data:
        huffman = json.load(data)
    with open('MARKOV_submission_metadata.json', 'r') as data:
        markov = json.load(data)
    with open('NBODY_submission_metadata.json', 'r') as data:
        nbody = json.load(data)
    with open('PERCOLATION_submission_metadata.json', 'r') as data:
        percolation = json.load(data)

    file_list = [autocomplete, huffman, markov, nbody, percolation]
    file_str_list = ["Autocomplete", "Huffman", "Markov", "Nbody", "Percolation"]

    print("The number of students that attempted submissions:")
    print(numStudents(file_list, file_str_list))
    print("\n")
    print("Range of student final scores:")
    print(finalScores(file_list, file_str_list))
    print("\n")
    print("Range of student autograde scores:")
    print(autoGradeScore(file_list, file_str_list))
    print("\n")
    print("Percentage students that lost points because of lateness:")
    print(latenessCheck(file_list, file_str_list))
    print("\n")
    print("Percentage students that had more than one submission:")
    print(moreThanOneSubmission(file_list, file_str_list))
    print("\n")
    print("Number of non-final submissions per student:")
    print(numNonFinalSubmissions(file_list, file_str_list))



# print("Runtime", (time.time() - start_time))
# dict = {"Hi": ["Hello", "Salud"], "Dog": ["Canine", "Hound", "Husky"]}
# for item in dict:
#     looker = JSONLooker((item, dict[item]))
#     print(looker)







