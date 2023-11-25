# imports
import json

class converter:

    # receive announcements
    jsonfile ={'annoucment1': 'help my patient is gone',  'annoucment2': 'help my patient is gone' }
    announcement = jsonfile


    # parse announcements into json file
    with open("announcements.json", "w") as file:
        json.dump(announcement, file, indent=4)
        print('executed parsing')

    # open json file
    with open("announcements.json", "r") as file:
        data = json.load(file)
        print(data)
        print('executed open json file')

    # eddit annoucement
    with open("announcements.json", "w") as file:
        data['annoucment1'] = 'nvm found him' 
        json.dump(data, file, indent=4)
        print('executed eddit annoucement')


