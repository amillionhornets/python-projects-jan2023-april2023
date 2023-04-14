import json

# userInput = {
#     "id": {input("id: ")},
#     "name": {input("Name: ")},
#     "age": {input("Age: ")}
# }

userInput = {
    "id": "3",
    "name": "Fortnite",
    "age": "3"
}

# updatedJSON = userInput.update(data)
# print(updatedJSON)

# Opens the json file in read and write mode then appends the data to the json than dumps it into the file.
with open("pythonProjects\\jsonPro\\person.json", "r+") as jsonFile2:
    file_data = json.load(jsonFile2)
    file_data["student"].append(userInput)
    jsonFile2.seek(0)
    json.dump(file_data, jsonFile2, indent="    ")

# Opens the json file in read mode and read out the file
with open("pythonProjects\\jsonPro\\person.json","r") as jsonFile:
    data = json.load(jsonFile)
    print(data['student'][0]['name'])