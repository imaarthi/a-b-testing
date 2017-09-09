from flask import Flask, render_template
from flask import request
import sys
import random
import csv
import os
import datetime


sys.dont_write_bytecode = True
with open('./ab_test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow([
        'version', 'pageLoadTime', 'clickTime'])
print('version', 'pageLoadTime', 'clickTime')

app = Flask(__name__)
app.config['DEBUG'] = True


# Simple python Flask server

@app.route('/', methods=['GET'])
def root():
    probability = random.uniform(0, 1)
    if probability < 0.5:
        return render_template('A.html')
    else:
        return render_template('B.html')


@app.route('/data', methods=['GET', 'POST'])
def get_data():
    json = request.get_json()
    version = json['version']

    # convert epoch timestamps to formatted version
    click_time = json['clickTime'] / 1000.0
    click_time_formatted = datetime.datetime.fromtimestamp(
        click_time).strftime('%Y-%m-%d %H:%M:%S.%f')
    page_load_time = json['pageLoadTime'] / 1000.0
    page_load_time_formatted = datetime.datetime.fromtimestamp(
        page_load_time).strftime('%Y-%m-%d %H:%M:%S.%f')

    print(version, page_load_time_formatted, click_time_formatted)
    # write to csv file
    with open('./ab_test.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([
            version, page_load_time_formatted, click_time_formatted])
    return "OK"


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
