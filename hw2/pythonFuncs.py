# import Survay

# Filters a survey and prints to screen the corrected answers:
# old_survey_path: The path to the unfiltered survey


def correct_myfile(old_survey_path):
    new_list = []
    old_survey = open('survey1', 'r')
    for line in old_survey:
        split_line = line.split()
        if new_list == [] and validate_survey_input(split_line):
            new_list.append(line)
        elif validate_survey_input(split_line):
            for i, new_list_line in enumerate(new_list):
                if int(split_line[0]) == int(new_list_line[0:8]):
                    new_list[i] = line
                    break
                elif int(split_line[0]) < int(new_list_line[0:8]):
                    new_list.insert(i, line)
                    break
                elif int(split_line[0]) > int(new_list_line[0:8]) and new_list_line == new_list[-1]:
                    new_list.append(line)

    result= open('exp1_result.txt', 'w')
    for line1 in new_list:
        result.write(line1)
        print(line1)
    result.close()




# Check if the given survey input is valid according to the requirments
# line: survey input
def validate_survey_input(line):
    amount_of_input = (len(line) == 9)
    if not amount_of_input:
        return 0

    id = (len(line[0]) == 8 and 0 <= int(line[0]) < 100000000)
    eating_habits = (line[1] == 'Vegan' or line[1] == 'Omnivore' or line[1] == 'Vegetarian')
    age = (10 <= int(line[2]) <= 100)
    gender = (line[3] == 'Woman' or line[3] == 'Man')

    if not (amount_of_input and id and eating_habits and age and gender):
        return 0

    for element in line[4:8]:
        score = (1 <= int(element) <= 10)
        if not score:
            return 0

    return 1


#
# #Returns a new Survey item with the data of a new survey file:
# #survey_path: The path to the survey
# def scan_survey(survey_path):
#     #TODO
#
# #Prints a python list containing the number of votes for each rating of a group according to the arguments
# #s: the data of the Survey object
# #choc_type: the number of the chocolate (between 0 and 4)
# #gender: the gender of the group (string of "Man" or "Woman"
# #min_age: the minimum age of the group (a number)
# #max_age: the maximum age of the group (a number)
# #eating_habits: the eating habits of the group (string of "Omnivore", "Vegan" or "Vegetarian")
# def print_info(s, choc_type, gender, min_age, max_age, eating_habits):
#     #TODO
#
# #Clears a Survey object data
# #s: the data of the Survey object
# def clear_survey(s):
#     #TODO
#
