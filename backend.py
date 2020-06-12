import mysql.connector
from difflib import get_close_matches

class Database:

    def __init__(self):
        self.con = mysql.connector.connect(
            user = "ardit700_student",
            password = "ardit700_student",
            host = "108.167.140.122",
            database = "ardit700_pm1database"
        )
        self.cursor = self.con.cursor()
    
    def define(self, word):
        # word = input("Enter a word: ")
        global defn
        defn = []
        self.word = word
        self.cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %self.word)
        results = self.cursor.fetchall()
        if results:
            for result in results:
                defn.append(result[1])
            return defn
        else:
            return defn

    def closest_match(self, word):
        matches = []
        self.word = word # may not need this later
        letter = self.word[0:1] + "%" # take the first letter of the word
        self.cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE '%s'" %letter)
        options = self.cursor.fetchall()
        if options:
            for option in options:
                matches.append(option[0])
            match = get_close_matches(self.word, matches, n=1, cutoff=0.8)
            return match
            #return len(get_close_matches(self.word, matches, n=1, cutoff=0.8))
            #return matches, self.word
        else:
            return match


# a=Database()
# a=Database.define(word)
# print(a.define("rain"))
# print(a.define("paris"))
# print(a.closest_match("zeb"))