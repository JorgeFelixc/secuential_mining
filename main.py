from pycspade.helpers import spade, print_result
from utility import prefixSpan, getSequences, getListFormated
from flask import Flask, request, jsonify


app = Flask(__name__)
@app.route("/")
def index():
  sequences = getSequences('test/paths_finished.tsv')
  wikiseed = getListFormated(sequences=sequences)

  data = prefixSpan(wikiseed, 450)
  response = jsonify({ 'data': data }) 
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response
  


if __name__ == "__main__":
  app.run()


# def initialize (): 
#   print('This is a Formating...')
#   sequences = getSequences('test/paths_finished.tsv')
#   wikiseed = getListFormated(sequences=sequences)

#   data = prefixSpan(wikiseed, 500)

#   print(data)
  # result = spade(filename='test/zaki.txt', support=0.3, parse=False)
  # print(result['logger'])



# if __name__ == '__main__':
#   initialize()

