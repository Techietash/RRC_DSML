# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()



#DASH APPLICATION

import dash
import dash_bootstrap_components as dbc

#Ensure Web App layout is mobile responsive
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])


server = app.server