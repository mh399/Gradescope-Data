import json


def writeMasterDict(assignments):
    master_dict = {}
    for i in range(len(assignments)):
        for key in assignments[i]:
            master_dict[key] = {}
            output = master_dict[key]
            input = assignments[i][key]
            output["final_submission_time"] = input[":created_at"]
            output["final_score"] = input[":score"]
            output["autograde_score"] = input[":results"]["score"]
            output["non_final_submissions"] = len((input[":history"]))
            if input[":results"]["output"] == "Results of the" \
                                                    " entire autograder" \
                                                    " run using autograder" \
                                                    " version 0.23 beta." or \
                    input[":results"]["output"] == "Your submission timed out. It took " \
                                              "longer than 1200 seconds to run.":
                output["late_multiple"] = 1
            else:
                output["late_multiple"] = float(input[":results"]["output"][-24:-21])
    for k in master_dict:
        print(k, master_dict[k])


def writeSubmissionDict(assignments, strassignments):
    submission_dict = {}
    for i in range(len(assignments)):
        for key in assignments[i]:
            submission_dict[key] = {}
            output = submission_dict[key]
            input = assignments[i][key][":submitters"][0]
            output["assignment"] = strassignments[i]
            output["student_name"] = input[":name"]
            output["email"] = input[":email"]
            if ":sid" in input.keys():
                output["netid"] = input[":sid"]
            else:
                output["netid"] = None
            if "Section" in input.keys():
                output["section"] = input["Section"]
            else:
                output["section"] = None
    for k in submission_dict:
        print(k, submission_dict[k])


def writeHistoryDict(assignments):
    history_dict = {}
    for i in range(len(assignments)):
        for key in assignments[i]:
            history_dict[key] = {}
            for n in range(len(assignments[i][key][":history"])):
                input = assignments[i][key][":history"][n]
                history_dict[key]["s" + str(n+1)] = {}
                output = history_dict[key]["s" + str(n+1)]
                output["submission_time"] = input[":created_at"]
                output["final_score"] = input[":score"]
                if input[":results"] == None:
                    output["autograde_score"] = None
                else:
                    if "score" not in input[":results"].keys():
                        output["autograde_score"] = None
                    else:
                        output["autograde_score"] = input[":results"]["score"]
    for k in history_dict:
        print(k, history_dict[k])


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

    print("\n")
    print("Master Dictionary:")
    print(writeMasterDict(file_list))
    print("\n")
    print("Submissions Information:")
    print(writeSubmissionDict(file_list, file_str_list))
    print("\n")
    print("Historical Submissions Information:")
    print(writeHistoryDict(file_list))