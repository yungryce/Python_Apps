# import sqlite3

# conn = sqlite3.connect('music.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Tracks')
# cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

# cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
#     ('Thunderstruck', 20))
# cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
#     ('My Way', 15))
# conn.commit()

# print('Tracks:')
# cur.execute('SELECT title, plays FROM Tracks')
# for row in cur:
#      print(row)

# cur.execute('DELETE FROM Tracks WHERE plays < 100')
# conn.commit()

# cur.close()



from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, friends INTEGER)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue