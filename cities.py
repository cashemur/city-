import sqlite3 as sql

con = sql.connect('test.db')


class GameClass:

    def __init__(self, usersValue):
        self.usersValue = usersValue
        self.exist_condition = self.isExist()

    def normalize(self):
        self.usersValue = self.usersValue[0].upper() + self.usersValue[1:].lower()
        return self.usersValue

    def isExist(self):
        with con:
            cur = con.cursor()
            cur.execute(f"SELECT field5 from '_cities' WHERE field5 = '{self.usersValue}' AND field6 = 'false';")
            self.rows = cur.fetchone()
            if self.rows == None:
                return False
            else:
                return True

    def getComputerAnswer(self):
        if self.exist_condition:
            with con:
                self.i = 1
                cur = con.cursor()
                cur.execute(f"UPDATE _cities SET field6 = 'true' WHERE field5 LIKE '{self.usersValue}';")
                while self.usersValue[-self.i] == "ь" or self.usersValue[-self.i] == "ъ" or self.usersValue[-self.i] == "й" or self.usersValue[-self.i] == "ы" or self.usersValue[-self.i] == "э":
                    self.usersValue = self.usersValue[:len(self.usersValue) - self.i]
                    self.i = self.i + 1
                self.i = 1
                cur.execute(f"SELECT field5 from '_cities' WHERE field5 LIKE '{self.usersValue[-self.i].upper()}%' AND field6 = 'false';")
                self.answer = cur.fetchone()
                cur.execute(f"UPDATE _cities SET field6 = 'true' WHERE field5 LIKE '{self.answer[0]}%';")
                while self.answer == None:
                    cur.execute(f"SELECT field5 from '_cities' WHERE field5 LIKE '{self.usersValue[-self.i].upper()}%' AND field6 = 'false';")
                    self.answer = cur.fetchone()
                    self.i = self. i+1
                    cur.execute(f"UPDATE _cities SET field6 = 'true' WHERE field5 LIKE '{self.answer[0]}%';")
                    self.computerAnswer = self.answer[0]
                return self.computerAnswer
        else:
            return "Used"

