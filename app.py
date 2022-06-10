from flask import Flask
import pandas as pd
app = Flask(__name__)


df = pd.DataFrame({
    'addresses': [1,2,3,4,5],
    'names': [1,2,3,4,5]
})

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/home')
def hello_world_2():
    return 'Hello, Home!'


@app.route('/data')
def get_data():
    return str(df)
