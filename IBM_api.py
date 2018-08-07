import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, CategoriesOptions
#credentials
natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='1e884aef-29d4-4c42-8517-1becd329543c',
  password='N8TAri28njkd',
  version='2017-02-27')
#def the method
def analyze_category(input_folder_path, user_id, output_folder_path):
    error_list = list()
    file_path = input_folder_path + user_id + ".txt"
    with open(file_path, 'r',encoding='utf-8') as myfile:
        data=myfile.read()
    try:
        response = natural_language_understanding.analyze(
        text=data,
        features=Features(
        categories=CategoriesOptions()))
    except:
        print(user_id)
        response = ""
    #output
    output_path = output_folder_path + user_id + ".json"
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    with open(output_path, 'w') as outfile:
        json.dump(response, outfile)
    #print(error_list)

def analyze_category_test(input_folder_path, user_id, output_folder_path):
    error_list = list()
    file_path = input_folder_path + user_id + ".txt"
    with open(file_path, 'r',encoding='utf-8') as myfile:
        data=myfile.read()
    try:
        response = natural_language_understanding.analyze(
        text=data,
        features=Features(
        categories=CategoriesOptions()))
    except:
        print(user_id)
        response = {'categories': 'unknown'}
    #output
    output_path = output_folder_path + user_id + ".json"
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    with open(output_path, 'w') as outfile:
        json.dump(response, outfile)
    #print(error_list)

#read users list
with open("C:/Users/zzz19/Documents/work/LDA/user_ids.txt", 'r') as users_list:
    users = users_list.readlines()
#submit the text and store the response
input_folder_path = "C:/Users/zzz19/Documents/work/LDA/Tweets/"
output_folder_path = "C:/Users/zzz19/Documents/work/LDA/IBM_responses/"
for i in range(len(users)):
    user_id = users[i][:-1]
    analyze_category(input_folder_path,user_id,output_folder_path)

