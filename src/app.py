import awsgi
import os
import json
import logging
import flask
from dotenv import load_dotenv
load_dotenv()

with open('config.json') as f:
    config = json.load(f)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

from enums import Language
bn = Language.bn.name
en = Language.en.name

app = flask.Flask(__name__)
app.config.update(config)

import database_helpers, message_helper, rule_helpers, rules

"""
MOBILE
"""

@app.route('/webhook', methods=["POST"])
async def webhook():
    print("webhook triggered")
    try:
        body_object = message_helper.get_body(flask.request.json) 
        if body_object:
            _from, body = body_object
            print(f'_from: {_from}, body: {body}')
            msg, body_args = '', dict()
            if body.lower() in ['hi','hello','99']:
                msg = 'intro'
            elif body.lower() in 'ab':
                default_lang = rule_helpers.get_lang(body.lower())
                print(f"default_lang: {default_lang}")
                database_helpers.update_default_lang(default_lang)
                msg = rule_helpers.get_intro_msg()
                print(f"msg: {msg}")
            elif (body.isdigit()) & (body not in ['0', '99']):
                msg = 'body'
                body_args = rule_helpers.get_response_msg(body)
                print(f"body_args: {json.dumps(body_args)}")
            elif body == '0':
                msg = rule_helpers.get_intro_msg_v2()
            else:
                msg = rule_helpers.get_retry_msg_v2()
            print(f"Message: {msg}")
            await message_helper.send_message(msg, _to=_from, body_args=json.dumps(body_args))
            return flask.jsonify({'status': 'PASSED', 'body_object': body_object, 'message': msg})
        else:
            return flask.jsonify({'status': 'FAILED', 'body_object': body_object})
    except Exception as e:
        print(e)
        return flask.jsonify({'status': 'ERROR', 'error': str(e)})



@app.route("/webhook", methods=["GET"])
async def verify():
    logging.info("verifying webhook")
    verify_token = flask.request.args.get('hub.verify_token')
    if verify_token == config['VERIFY_TOKEN']:
        logging.info("webhook verified")
        print("webhook verified")
        return flask.request.args.get('hub.challenge')
    else:
        return 'Invalid verify token'

"""
WEB APP
"""
@app.route("/")
def index():
    query_responses_json = json.dumps(rule_helpers.get_responses())
    return flask.render_template('index.html', queryResponses=query_responses_json)

@app.route("/readme")
def readme():
    return flask.render_template('/readme.html')

@app.route("/add_query")
async def add_query():
    return flask.render_template('add_query.html')

@app.route("/view_grievances")
async def view_grievances():
    query_responses_json = rule_helpers.get_responses().get('en')
    return flask.render_template('table_view.html', queryResponses=query_responses_json)

@app.route("/export_records", methods=['POST'])
def export_grievance_records():
    data = flask.request.get_json()
    selected_ids = data.get('ids', [])
    print(f'selected_ids to export: {selected_ids}')
    query_responses_json = rule_helpers.get_responses().get('en')
    selected_responses = [record for record in query_responses_json if record['id'] in selected_ids]
    output = rule_helpers.download_csv(selected_responses)
    filename = 'grievances.csv'
    response = flask.Response(output.getvalue(), mimetype='text/csv')
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    return response

@app.route("/delete_records", methods=['POST'])
def delete_grievance_records():
    data = flask.request.get_json()
    selected_ids = data.get('ids', [])
    print(f'selected_ids to delete: {selected_ids}')
    for id in selected_ids:
        database_helpers.remove_record({'language':'en', 'id':id})
    query_responses_json = rule_helpers.get_responses().get('en')
    return flask.render_template('table_view.html', queryResponses=query_responses_json)

@app.route("/submit_response", methods=['POST'])
async def submit_response():
    record = dict(flask.request.form)
    logging.info(f"new record: {record}")
    # database_helpers.add_record(record)
    return flask.redirect('/')

@app.route("/get_edit_response", methods=['POST'])
async def get_edit_response():
    record = dict(flask.request.form)
    logging.info(f"edit record: {record}")
    print(f"edit record: {record}")
    return flask.render_template('edit_query.html', query_response=record)

@app.route("/edit_query_response", methods=['POST'])
async def edit_query_response():
    record = dict(flask.request.form)
    logging.info(f"edited record: {record}")
    print(f"edited record: {record}")
    database_helpers.edit_record(record)
    return flask.redirect(flask.url_for('index'))

@app.route("/remove_query", methods=['POST'])
async def remove_query():
    record = flask.request.json
    logging.info(f"remove record: {record}")
    print(f"remove record: {record}")
    database_helpers.remove_record(record)
    return flask.jsonify(record)

@app.route("/get_faq_questions")
def get_faq_questions():
    query_responses_json = json.dumps(rule_helpers.get_faq())
    return flask.render_template('faq.html', queryResponses=query_responses_json)

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # app.run(host='0.0.0.0', debug=True, port=8080)
