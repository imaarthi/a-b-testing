import sys
import random
import csv
import os

from flask import Flask, render_template
from flask import request

# DO NOT TOUCH ANYTHING IN THIS FILE.


#import datetime
# DO not write pyc files.
sys.dont_write_bytecode = True

# ab_test.csv which could be used for testing locally.
# After hosting in heroku, this file will no more be used.
# As Heroku file system is not persistent and it removes
# any file which is created after hosting.
csv_file_ab = './ab_test.csv'
with open(csv_file_ab, 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow([
        'version', 'pageLoadTime', 'clickTime', 'clickHTMLElementId','UniqueSessionID'])

print('version', 'pageLoadTime', 'clickTime', 'clickHTMLElementId','UniqueSession')

# Main Flask app server
app = Flask(__name__) # Simple python Flask server
app.config['DEBUG'] = True
app.static_folder = 'static'

# This is the root endpoint.
@app.route('/', methods=['GET'])
def root():
    probability = random.uniform(0, 1)
    if probability < 0.5:
        return render_template('A.html')
    else:
        return render_template('B.html')

# data endpoint
@app.route('/data', methods=['GET', 'POST'])
def get_data():
    json = request.get_json()
    version = json['version']
    click_time = json['clickTime']
    page_load_time = json['pageLoadTime']
    click_obj_id = json['HtmlElementID']
    unique_session_id = json['UniqueSession']
    # THIS PIECE OF CODE COULD BE USED TO CONVERT TO READ-ABLE TIME
    # BUT HAVING IT IN UNIX TIME MAKES IT EASIER TO
    # COMPARE WITH EYE_TRACKING.

    # convert epoch timestamps to formatted version
    # click_time = json['clickTime'] / 1000.0
    # if click_time != 0:
    #     click_time_formatted = datetime.datetime.fromtimestamp(
    #         click_time).strftime('%Y-%m-%d %H:%M:%S.%f')
    # else:
    #     click_time_formatted = click_time
    # page_load_time = json['pageLoadTime'] / 1000.0
    # page_load_time_formatted = datetime.datetime.fromtimestamp(
    #     page_load_time).strftime('%Y-%m-%d %H:%M:%S.%f')

    print('AB_TESTING:', version , page_load_time , click_time , click_obj_id, unique_session_id)

    # write to csv file
    with open(csv_file_ab, 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([
            version, page_load_time, click_time, click_obj_id, unique_session_id])
    return "OK"


# DO NOT CHANGE ANYTHING HERE
# You might run into issues changing things here
# based on how heroku treats host and port
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
