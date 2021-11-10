"""Defines all the functions related to the database"""
from math import log
from app import db
import random

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from GameStatistics;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "InputNumber": result[0],
            "SummonerName": result[1],
            "Kills": result[2],
            "Deaths": result[3],
            "Assists": result[4],
            "Rank": result[5],
            "KillParticipation": result[6],
            "CreepScore": result[7],
            "Gold": result[8],
            "Damage": result[9]
        }
        todo_list.append(item)

    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set task = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated status

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set status = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def insert_new_task(text: str) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """

    conn = db.connect()
    query = 'Insert Into tasks (task, status) VALUES ("{}", "{}");'.format(
        text, "Todo")
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From tasks where id={};'.format(task_id)
    conn.execute(query)
    conn.close()

def advanced_query_1(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query_results = conn.execute("SELECT Distinct(SummonerName), `Rank`, LastSeasonRank FROM GameStatistics NATURAL JOIN SummonerStats")
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "SummonerName": result[0],
            "Rank": result[1],
            "LastSeasonRank": result[2]
        }
        todo_list.append(item)

    return todo_list


def advanced_query_2(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'SELECT SummonerName, AVG(Kills), AVG(Deaths), AVG(Assists), AVG(KillParticipation), AVG(CreepScore), AVG(Gold), AVG(Damage)FROM GameStatistics GROUP By SummonerName;'
    query_results = conn.execute(query).fetchall() 
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "SummonerName": result[0],
            "Kills": result[1],
            "Deaths": result[2],
            "Assists": result[3],
            "Rank": result[4],
            "KillParticipation": result[5],
            "CreepScore": result[6],
            "Gold": result[7],
            "Damage": result[8]
        }
        todo_list.append(item)

    return todo_list
