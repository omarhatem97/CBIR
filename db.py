# provide function grab all images, videos from db
from os import O_TEMPORARY
from sys import float_info
import mysql.connector

class DB():
    def __init__(self, database=None):
        self.database = database
        #connect to database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database = self.database
        )

        self.cursor = self.db.cursor() #take a cursor


    #for debugging only
    def do(self):
        self.cursor.execute("CREATE TABLE person (name VARCHAR(10), age INT)")
        self.cursor.execute("INSERT INTO person (name, age) VALUES (%S, %S)", ('OMAR', 23))
        self.db.commit()


    def get_db(self):
        return self.db

    def get_cursor(self):
        return self.cursor


    def createDataBase(self):
        '''
            this function typically will be called once on every pc
        '''
        self.cursor.execute("CREATE DATABASE cbDatabase") #creates content based database


    def runCommand(self,command):
        "takes command, execute it"
        self.cursor.execute(command)
        

    def createTable(self, tableName):
        self.cursor.execute("CREATE TABLE {}(arr VARCHAR(250))".format(tableName))


    def printTable(self, name):
        """
            print table of given name
        """
        self.cursor.execute("SELECT * FROM {}".format(name))
        print("table {} :".format(name))
        for i in self.cursor:
            print(i)

    
    def insert_to_images(self, f1, f2, f3, url):
        sql = "INSERT INTO images (f_histogram, f_colorLayout, f_meanColor, url) VALUES (%s, %s, %s, %s)"
        val = (f1, f2, f3 ,url)
        self.cursor.execute(sql, val)
        self.db.commit()


    def insert_to_videos(self):
        pass


    def insert (self, tableName,arr):

        listToString = self.convertArrToStr(arr)
        self.cursor.execute("INSERT INTO {} (arr) VALUES ({}) ".format(tableName,listToString))


    def get_images(self):
        '''
            get all images from database
        '''   
        self.cursor.execute("SELECT * FROM images")
        myImages = self.cursor.fetchall()
        return myImages
    

    def get_videos(self):
        '''
            get all images from database
        '''   
        self.cursor.execute("SELECT * FROM videos")
        myVideos = self.cursor.fetchall()
        return myVideos


    def convertArrToStr(self, l):
        """
            convert array to string, to be able to store it in database
        """
        listToStr = ','.join([str(elem) for elem in l])
        return listToStr


       