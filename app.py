import sqlite3
from flask import Flask, jsonify , request, jsonify
import pandas as pd
import csv
import json
import os

app = Flask(__name__)

# with open('clips_db.csv', 'r',encoding = CSV_ENCODING ) as f:

@app.route('/getdata', methods=['GET', 'POST', 'DELETE', 'PUT'])
def returndata():
    CSV_ENCODING = 'cp949'
    'sme_string'.encode('utf-8')
    reader = pd.read_csv(os.path.join('u_clips_db_m.csv'), encoding = 'UTF-8', dtype=str)
    a = dict()
    count = 0
    count2 = 0
    count3 =0
    # '{}'.format(5252)
    for i3 in range(len(reader)):
        c =list()
        row = reader.iloc[i3]
        row = dict(row)
        for j in a.keys():
            if (j == row['ori_word']):
                count2 = count2 + 1
                break
        if ((0 == count2)):
            if(count3 ==0):
                count3=count3+1
                for i4 in range(len(reader)):
                    row1 = reader.iloc[i4]
                    row1 = dict(row1)
                    del row1['Unnamed: 0.1']
                    del row1['Unnamed: 0']
                    del row1['word_ind']
                    del row1['word_meaning']
                    if (row['ori_word'] == row1['ori_word']):
                        del row1['ori_word']
                        c.append(row1)
                b = dict()
                b["meaning"] = row['word_meaning']
                b["tracks"] = c
                a[row['ori_word']] = b
            else:
                for j in a .keys():
                    for i4 in range(len(reader)):
                        row1 = reader.iloc[i4]
                        row1 = dict(row1)
                        del row1['Unnamed: 0']
                        del row1['word_ind']
                        del row1['word_meaning']
                        if (j != row1['ori_word']):
                            del row1['ori_word']
                            c.append(row1)
                    break
                b = dict()
                b["meaning"] = row['word_meaning']
                b["tracks"] = c
                a[row['ori_word']] = b

        else:
            count2 = count2 - 1

    json_val = json.dumps(a)
    with open('clips_db.json','w') as make_file:
        json.dump(a, make_file, indent="\t")

    return jsonify(a)

#with open('clips_db.json', 'r', encoding='utf-8') as f:
#   json_data = json.load(f)
#print(json_data)


@app.route('/api/echo-json', methods=['GET', 'POST', 'DELETE', 'PUT'])
def add():
    data = request.get_json()
    print("llllllsdfsdfdsafa")
    print(data)
    # ... do your business logic, and return some response
    # e.g. below we're just echo-ing back the received JSON data
    return jsonify(data)


@app.route('/')
def HelloWorld():
    return "Naver AI Hackerton"


if __name__ == "__main__":
    app.run( host="0.0.0.0", port="5000",debug=False)
