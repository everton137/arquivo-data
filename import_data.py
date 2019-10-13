import json
import psycopg2

filename = './data/jairbolsonaro-2019.json'
data = json.load(open(filename, 'r'))

conn = psycopg2.connect("dbname=twitterdb user=DB_USER_OWNER password=YOUR_DB_PASSWORD")
cur = conn.cursor()

for d in data:
    cur.execute("insert into tweets (tweet, content, time) values (%s, %s, %s)", [json.dumps(d), d['full_text'], d['created_at']])

conn.commit()
