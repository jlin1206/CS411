""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/advance_query1")
def advance_query():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("advancedquery1.html", items=items)


@app.route("/advance_query2")
def advance_query2():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("advancedquery2.html", items=items)

@app.route("/search/<string:search>")
def search(search):
    """ returns rendered homepage """
    items = db_helper.search(search)
    return render_template("search.html", items=items)

@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)

@app.route("/advance_query1")
def advance_query():
    """ returns rendered homepage """
    items = db_helper.advanced_query_1()
    return render_template("advancedquery1.html", items=items)

@app.route("/advance_query2")
def advance_query2():
    """ returns rendered homepage """
    items = db_helper.advanced_query_2()
    return render_template("advancedquery2.html", items=items)