import json
import psycopg2

for i in range(2010, 2019):
    filename = './data/jairbolsonaro-{}.json'.format(i)
    data = json.load(open(filename, 'r'))
    
    conn = psycopg2.connect("dbname=twitterdb user=DB_USER_OWNER password=YOUR_DB_PASSWORD")
    cur = conn.cursor()
    for d in data:
        cur.execute("insert into tweets (tweet, content, time) values (%s, %s, %s)", [json.dumps(d), d['full_text'], d['created_at']])
    
    conn.commit()
