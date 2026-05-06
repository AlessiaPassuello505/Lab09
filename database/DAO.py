from database.DB_connect import DBConnect
from model.Aeroporto import Aeroporto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from airports a "
        cursor.execute(query)

        for row in cursor:
            result.append(Aeroporto(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesPesati():
            conn = DBConnect.get_connection()
            result = []
            cursor = conn.cursor(dictionary=True)

            # Query per grafo NON orientato:
            # Raggruppiamo per la coppia di ID a prescindere dall'ordine (A-B è uguale a B-A)
            query = """SELECT LEAST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) as ID_A, 
                              GREATEST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) as ID_B, 
                              AVG(f.DISTANCE) as media_distanza
                       FROM flights f 
                       GROUP BY ID_A, ID_B"""

            cursor.execute(query)

            for row in cursor:
                result.append((row["ID_A"], row["ID_B"], row["media_distanza"]))

            cursor.close()
            conn.close()
            return result