import sys
import random
import csv
import datetime

from flask import Flask, render_template
from flask import request


sys.dont_write_bytecode = True
with open('./ab_testing.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['Version', 'pageLoadTime', 'clickTime'])


# Simple python Flask server
app = Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True


# This is the main HTTP endpoint
# A/B versions displayed randomly
@app.route('/', methods=['GET'])
def root():
    probability = random.uniform(0, 1)
    if probability < 0.5:
        return render_template('A.html')
    else:
        return render_template('B.html')


# This end point receives the data posted from our client
@app.route('/data', methods=['POST'])
def get_data():
    # get the data
    json = request.get_json()
    version = json['version']

    # convert epoch timestamps to formatted version
    click_time = json['clickTime'] / 1000.0
    click_time_formatted = datetime.datetime.fromtimestamp(
        click_time).strftime('%Y-%m-%d %H:%M:%S.%f')
    page_load_time = json['pageLoadTime'] / 1000.0
    page_load_time_formatted = datetime.datetime.fromtimestamp(
        page_load_time).strftime('%Y-%m-%d %H:%M:%S.%f')

    # write to csv file
    with open('./ab_testing.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([
            version, page_load_time_formatted, click_time_formatted])
    return "OK"


# run in debug mode
if __name__ == '__main__':
    app.run(debug=True)
