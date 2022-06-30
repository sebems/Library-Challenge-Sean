from db_handler import DB_Handler
from room import Room
import random
from typing import List

class ROOM_DB_Handler( DB_Handler ):
    
    def __init__(self):
        self.roomDB = DB_Handler('room', 'rooms')
        self.createTable()

    def createTable(self):
        self.roomDB.createTable({
                'roomID': 'integer', 
                'numOccupants': 'integer', 
                'maxOccupants': 'integer',
                'isFull': 'integer'
            })

    def updateTable(self, searchVal, newValue):
        """
            Updates the a given table entry
        """
        self.roomDB.cursor.execute(""" UPDATE rooms 
            SET  numOccupants= ? 
            WHERE roomID= ?
            """, (newValue, searchVal))
        
        self.roomDB.conn.commit()

    def findAllEmptyRooms(self):
        """
            Finds all empty rooms and returns the result
        """
        self.roomDB.cursor.execute(" SELECT * FROM rooms WHERE numOccupants < maxOccupants ")
        query_res = self.roomDB.cursor.fetchall()

        # convert to dict
        res = {}
        #TODO: extract items from list and s
        for sublist in query_res:
            res[sublist[0]] = list(sublist[1:])

        return res

    def findAllRooms(self):
        """
            Finds all rooms and returns the result
        """
        self.roomDB.cursor.execute(" SELECT * FROM rooms")
        query_res = self.roomDB.cursor.fetchall()

        # convert to dict
        res = {}
        #TODO: extract items from list and s
        for sublist in query_res:
            res[sublist[0]] = list(sublist[1:])

        return res

    def getCurrentRoom(self, room_id):
        """
            Gets the Current Room Object
        """
        self.roomDB.cursor.execute(""" SELECT * FROM rooms WHERE roomID = ? """, (room_id,))
        return Room(self.roomDB.cursor.fetchall()[0])

    def insertRoom(self, numOfInputs = 1):
        """
            Inserts n number of entries into table
        """

        for i in range(numOfInputs):
            self.roomDB.cursor.execute(" SELECT * FROM rooms ")
            table_size = len(self.roomDB.cursor.fetchall())
            roomType = int(random.randrange(1, 6))

            self.roomDB.cursor.execute("INSERT INTO rooms VALUES (?, ?, ?, ?)", (table_size + 1, 0, roomType, 0))
        
        self.roomDB.conn.commit()

    #
    def toRoomObject(self, sql_result: List[tuple]) -> List[Room]:
        """
            Converts a List of tuples to a list of rooms
        """

        roomList = []
        for sql_tuple in sql_result:
            roomList.append(Room(sql_tuple))

        return roomList
