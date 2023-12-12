def readUsers(input): #function to read in user txt file and return dict with ids and users.
# Open the file in read mode
    with open('users.txt', 'r') as file:
    # Read the contents of the file
        text = file.read()
 
    users = {}
    lines = text.split('\n')
# Parses text in file and puts into dict
    for line in lines:
        parts = line.split(',')
        name = parts[0].strip()
        number = parts[1].strip()
        users[number] = name
    return users