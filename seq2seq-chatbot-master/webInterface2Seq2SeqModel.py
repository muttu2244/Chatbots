from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__,static_url_path="/static")

# Routing
@app.route('/message', methods=['POST'])
def reply():
    return jsonify( { 'text': execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, request.form['msg'] ) } )

@app.route("/")
def index():
    return render_template("index.html")

# Init seq2seq model
import tensorflow as tf
import execute

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess)

# start app
if (__name__ == "__main__"):
    app.run(port = 5000)