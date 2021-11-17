from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

import requests 

app = FastAPI()

db = []

# class Project(BaseModel):
#     name: str
#     description: str
#     url: str
#     tags: list
class suggestions(BaseModel):
    name: str
    message: str
    time: datetime
    url: str

@app.get('/')
def index():
    return {'Hello' : 'World'}

@app.get('/suggestions')
def get_suggestions():
     
    return db

@app.get('/suggestions/{suggestions_id}')
def get_suggestion(suggestions_id: int):
    return db[suggestions_id-1]

@app.post('/suggestions')
def create_suggestions(suggestions: suggestions):
    db.append(suggestions.dict())
    return db[-1]

@app.delete('/suggestions/{suggestions_id}')
def delete_suggestions(suggestions_id: int):
    db.pop(suggestions_id-1)
    return {}

# @app.get('/projects')
# def get_projects():
#     return db

# @app.get('/projects/{project_id}')