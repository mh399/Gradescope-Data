import yaml
import time
import json

class JSONLooker:

    def __init__(self, tuple):
        self.JSON_item = tuple

    def __repr__(self):
        retval = ""
        retval += str(self.JSON_item[0])
        for item in self.JSON_item[1]:
            retval += " -- " + str(item)
        return retval


start_time = time.time()
with open('NBODY_submission_metadata.json', 'r') as data:
         y = json.load(data)
# print(y)
print("Number of Students: ", len(y.keys()))




# for d in y.keys():
#     print(y[d])
    # for k in y[d].keys():
    #     print(k)
    # student_name = y[d][':submitters'][0][':name']
    # print(student_name)
    # student_email = y[d][':submitters'][0][':email']
    # student_netid = y[d][':submitters'][0][':sid']
    # student_section = y[d][':submitters'][0][':Section']

    # most_recent_sub_time = y[d][':created_at']
    # score = y[d][':score']
    # status = y[d][':status']
    # tests = y[d][':results']['tests']


for k in y.keys():
    print(y[k])
    # for d in y[k][':results']['tests'][0].keys():
    #     #     print(d)
    # for a in y[k][':history'][0].keys():
    #     print(a)












# print("Runtime", (time.time() - start_time))

# dict = {"Hi": ["Hello", "Salud"], "Dog": ["Canine", "Hound", "Husky"]}
#
# for item in dict:
#     looker = JSONLooker((item, dict[item]))
#     print(looker)







