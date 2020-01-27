import mysql.connector
import difflib
from difflib import get_close_matches

# MYSQL credentials 
con = mysql.connector.connect(
                                user = "ardit700_student",
                                password = "ardit700_student",
                                host = "108.167.140.122",
                                database = "ardit700_pm1database"
                             )
cursor = con.cursor()
 
# Query the entire dataset
query = cursor.execute("SELECT * FROM Dictionary")
results = cursor.fetchall()
 
# Converting 'list' into a dictionary with 'keys' and 'values'
data = dict(results)
 
def translate(w):
    w = w.lower()
    if w in data:           # Check if the word is in dictionary
        return data[w]
    elif w.title() in data:     # If user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:     # In case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:    # To recommend best match
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.upper()     
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")    # Prompt user for input
output = translate(word)        # Call the function
if type(output) == list:        
    for item in output:         # Iterating with condition
        print(item)
else:
    print(output)

