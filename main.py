import time
import http.client
import json

def check_web_page():
    web_page_url = '/'
    try:
        connection = http.client.HTTPSConnection(host='google.com', port=443, timeout=10)
        connection.request(method='GET', url=web_page_url)
        response = connection.getresponse()

        if response.status >= 400 < 500:
            send_slack('Web Page is down. Web Page: \'{}\', Status Code: \'{}\''.format(web_page_url, response.status))
        elif response.status >= 500:
            send_slack('There is server errors. Web Page: \'{}\', Status Code: \'{}\''.format(web_page_url, response.status))
    except Exception as e:
        send_slack('Error getting the web page \'{}\'. Message: {}'.format(web_page_url, e))

def send_slack(text):
    slack_connection = http.client.HTTPSConnection(host='hooks.slack.com', port=443, timeout=10)
    slack_connection.request(method='POST', url='url-to-slack-channel', body=json.dumps({'text': text}))
    slack_connection.getresponse()

while True:
    check_web_page()
    time.sleep(1)