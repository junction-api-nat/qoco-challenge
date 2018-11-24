from flask import Flask
import data_comparison from src

@app.route("/", methods=['GET'])
def getDisruptions():
  disrupted_transports = data_comparison.handle_data()
  print("Returning disruptions: ", disrupted_transports)
  #return disrupted_transports
    