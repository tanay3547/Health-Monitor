import os
import sys
import sqlite3
from sqlite3 import Error
import pandas as pd
import datetime

class SqlHandler:
    def __init__(self):
        # Location of database on system
        self.db_loc = os.path.join("..", "resources", "database", "healthit.db")
        self.db_loc = ":memory:"

        # Connection to database
        self.__connection = None
        self.__create_connection()

        # tells if user is logged in
        self.logged = False

        # userid is unique id that will be linked with other tables
        self.__userid = None

        # Other user related var
        # dataframe will hold users dataframe on memory
        self.record_db = None
        self.activity_db = None

        # private info
        # Maybe new class?
        self.__username = None
        self.__password = None
        self.__age = None
        self.__gender = None
        self.__weight = None
        self.__height = None

    def __del__(self):
        # Save (commit) the changes
        self.__connection.commit()
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        self.__connection.close()

    def __create_connection(self):
        """
        create a database connection to the SQLite database
        :return: True if successful else False
        """
        self.__connection = None
        try:
            self.__connection = sqlite3.connect(self.db_loc)
            self.__create_db()
        except Error as e:
            print(e)
            return False

        return True

    def __create_table(self, create_table_sql):
        """
        create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return: True if successful else False
        """
        try:
            c = self.__connection.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
            return False

        return True

    def __create_db(self):
        """
        Create tables and database using sister functions
        :return:  Function will return True if login successful else false
        """

        """
        table: userinfo
        username: less than 21 char
        password: str
        age: int max 999, Default 0
        gender:
            M (Male)
            F (Female)
            U (Unknown) Default
            B (Both)
        weight: float 000.00, min 0 Default
        height: float 000.00, min 0 Default
        """
        sql_create_user_info_table = """ CREATE TABLE IF NOT EXISTS userinfo (
                                                id integer NOT NULL PRIMARY KEY,
                                                username varchar(20) NOT NULL UNIQUE,
                                                password text NOT NULL,
                                                age integer(3) DEFAULT 0,
                                                gender char(1) DEFAULT 'U',
                                                weight DECIMAL(5,2) DEFAULT 0,
                                                height DECIMAL(5,2) DEFAULT 0,
                                                CHECK (age >= 0 AND 
                                                    weight >= 0 AND 
                                                    height >= 0 AND
                                                    (
                                                        gender == 'M' OR
                                                        gender == 'F' OR
                                                        gender == 'U' OR
                                                        gender == 'B'
                                                    )
                                                ) 
                                            );"""

        """
        Table: userrecord
        heartrate: int(3), Default 0
        bloodpressurehigh: int(3), Default 0
        bloodpressurelow: int(3), Default 0
        caloriesin: int(5), Default 0
        caloriesout: int(5), Default 0
        begin_date: timestamp, Default current timestamp
        """
        sql_create_user_record_table = """CREATE TABLE IF NOT EXISTS userrecord (
                                            id integer PRIMARY KEY,
                                            userinfo_id integer NOT NULL,
                                            heartrate integer(3) NOT NULL DEFAULT 0,
                                            bloodpressurehigh integer(3) NOT NULL DEFAULT 0,
                                            bloodpressurelow integer(3) NOT NULL DEFAULT 0,
                                            caloriesin integer(5) NOT NULL DEFAULT 0,
                                            caloriesout integer(5) NOT NULL DEFAULT 0,
                                            begin_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                            FOREIGN KEY (userinfo_id) REFERENCES userinfo (id) ON DELETE CASCADE,
                                            CHECK (heartrate >= 0 AND 
                                                bloodpressurehigh >= 0 AND 
                                                bloodpressurelow >= 0 AND 
                                                caloriesin >= 0 AND 
                                                caloriesout >= 0
                                            ) 
                                        );"""

        """
        Table: useractivity
        description: text
        duration: float 000.00, min 0 Default
            activity duration = begin_date - end_date
        begin_date: timestamp, Default current timestamp
        end_date: timestamp, Default current timestamp
        """
        sql_create_user_activity_table = """CREATE TABLE IF NOT EXISTS useractivity (
                                            id integer NOT NULL PRIMARY KEY,
                                            userinfo_id integer NOT NULL,
                                            description text NOT NULL,
                                            duration DECIMAL(5,2) NOT NULL,
                                            begin_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                            end_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                            FOREIGN KEY (userinfo_id) REFERENCES userinfo (id) ON DELETE CASCADE
                                            CHECK (duration >= 0 
                                            )
                                        );"""

        # create a database connection and than create tables
        if self.__connection:
            # create userinfo table
            self.__create_table(sql_create_user_info_table)

            # create userrecord table
            self.__create_table(sql_create_user_record_table)

            # create useractivity table
            self.__create_table(sql_create_user_activity_table)
        else:
            print("Error! cannot create the database without connection.")
            return False

        return True

    def signup(self, username, encrypted_password):
        """
        :param username:
        :param encrypted_password:
        :return:
        """
        try:
            cursor = self.__connection.cursor()
            cursor.execute("INSERT INTO userInfo(username, password) VALUES(?, ?)", (username, encrypted_password))
            self.__connection.commit()
            self.login(username, encrypted_password)
            self.logged = True
        except Error as e:
            self.logged = False
            print(e)
            return False
        return True

    def login(self, username, encrypted_password):

        """
        looks up given user name and encrypted password into SQL database table
        if found than will extract userUniqueId and other information from this table
        after that it will Query all data of this user from other table

        :param username: string
        :param encrypted_password: string

        :return: Function will return True if login successful else false
        """
        try:
            cursor = self.__connection.cursor()
            cursor.execute("""SELECT id FROM userinfo 
                            WHERE username=:username 
                            AND password=:password""", {'username': username, 'password': encrypted_password})
            self.__userid = cursor.fetchone()
            self.logged = True
        except Error as e:
            self.logged = False
            print(e)
            return False

        return True

    def updateuserinfo(self, username: str, encrypted_password: str, age: int, gender: str, weight: float, height: float):

        if not self.__userid:
            print("Need a valid logged in session to update information")
            return False
        try:
            cursor = self.__connection.cursor()
            cursor.execute("""UPDATE userInfo 
                            SET username=?,
                            password=?,
                            age=?,
                            gender=?,
                            weight=?,
                            height=?
                            WHERE id=?""", (username, encrypted_password, age, gender, weight, height, self.__userid)
                           )
            self.__connection.commit()
        except Error as e:
            print(e)
            return False
        return True

    def setinfo(self, table: str, dataframe):
        """
        :param table: userrecord or useractivity
        :param dataframe: pd.dataframe
        :return:
        """
        if not self.__userid:
            print("Need a valid logged in session to update information")
            return False

        dataframe['userinfo_id'] = 1
        try:
            dataframe.to_sql(name=table, con=self.__connection, if_exists='replace', index=False)
        except Error as e:
            self.logged = False
            print(e)
            return False
        return True

    def get_userinfodb(self):
        """
        Function will bring data from userrecord table
        :return:  Function will return True if it gets data from SQL db else false
        """
        record_db = False
        if not self.__userid:
            print("Need a valid logged in session to update information")
            return False
        try:
            sql_string = ("SELECT * from userinfo WHERE id=%s" % self.__userid)
            # sql_string = "SELECT * from userinfo"
            record_db = pd.read_sql_query(sql_string, self.__connection)
        except Error as e:
            print(e)
            return False

        return record_db

    def get_userrecorddb(self):
        """
        Function will bring data from userrecord table
        :return:  Function will return True if it gets data from SQL db else false
        """
        record_db = False
        if not self.__userid:
            print("Need a valid logged in session to update information")
            return False
        try:
            sql_string = ("SELECT * from userrecord WHERE userinfo_id=%s" % self.__userid)
            # sql_string = "SELECT * from userrecord"
            record_db = pd.read_sql_query(sql_string, self.__connection)
        except Error as e:
            print(e)
            return False

        return record_db

    def get_useractivitydb(self):
        """
        Function will bring data from useractivity table
        :return:  Function will return True if it gets data from SQL db else false
        """
        activity_db = False
        if not self.__userid:
            print("Need a valid logged in session to update information")
            return False
        try:
            sql_string = ("SELECT * from useractivity WHERE userinfo_id=%s" % self.__userid)
            # sql_string = "SELECT * from useractivity"
            activity_db = pd.read_sql_query(sql_string, self.__connection)
        except Error as e:
            print(e)
            return False

        return activity_db


if __name__ == '__main__':
    temp = SqlHandler()
    print(temp.signup("username", "encrypted_password"))
    print(temp.get_userinfodb())
    print(temp.get_userrecorddb())
    print(temp.get_useractivitydb())

    # Create the dataframe
    userrecorddb = pd.DataFrame({
        'heartrate': [120, 139, 2],
        'bloodpressurehigh': [100, 239, 256],
        'bloodpressurelow': [100, 0, 90],
        'caloriesin': [12458, 48484, 11311],
        'caloriesout': [65, 2595, 10099]
    })
    temp.setinfo("userrecord", userrecorddb)
    print(temp.get_userrecorddb())

    # Create the dataframe
    useractivitydb = pd.DataFrame({
        'description': ['running', 'still running', 'are we done now?'],
        'duration': [100.00, 239.12, 256],
        'begin_date': [pd.Timestamp(2014, 1, 23),
                       pd.Timestamp(datetime.datetime.now()),
                       datetime.datetime.now()],
        'end_date': [pd.Timestamp(2014, 1, 23),
                       pd.Timestamp(datetime.datetime.now()),
                       datetime.datetime.now()]
    })
    temp.setinfo("useractivity", useractivitydb)
    print(temp.get_useractivitydb())

    exit(0)
