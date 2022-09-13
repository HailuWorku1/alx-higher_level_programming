#!/usr/bin/python3

"""
A script that lists all states from database hbtn-0e_0_usa
"""

if __name__ == '__main__':
            import MySQLdb
            import sys
            my_db = MySQLdb.connect(user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3],
                                    host='localhost',
                                    port=3306)
            c = my_db.cursor()
            c.execute("SELECT * FROM states ORDER BY id ASC")
            states = c.fetchall()

            for state in states:
                print(state)
