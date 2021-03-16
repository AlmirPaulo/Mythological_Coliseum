# from flask import Flask
# from threading import Thread
import requests

database = open('database', 'r').read()




def get_data():
    url = database
    resp = requests.get(url)
    return resp.json()
        







# app = Flask('')

# @app.route('/')
# def home():
#   return"It's Alive!"
  
# def run():
#   app.run(host ='0.0.0.0', port = 8080)

# def keep_alive():
#   t = Thread(target = run)
#   t.start()