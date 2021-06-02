# provide function grab all images, videos from db
import mysql.connector

class DB():
    def __init__(self, database=None):
        self.database = database

        #connect to database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )

        # self.cursor = self.db.cursor() #take a cursor


    def createDataBase(self):
        self.cursor.execute("CREATE DATABASE cbDatabase")



    def createTable(self, tableName):
        self.cursor.execute()


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