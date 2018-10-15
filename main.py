from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
form='''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
        <label for="rotate-by">
            Rotate by:
            <input type="text" id="rotate-by" name="rot" value=0 />
        </label>
        <textarea name="text" rows="10" cols="30"></textarea>
        <input type="submit" value="Submit Query"/>
    </form>
    </body>
</html>
'''
@app.route("/")
def index():
    # build the response string
    content= form
    return content

@app.route("/encrypt" , methods=['POST'])
def encrypt_msg():
    rt_by=int(request.form['rot'])
    msg=request.form['text']
    encrypt_msg=rotate_string(msg,rt_by)
    content='''<h1>'''+encrypt_msg+''' </h1>'''
    return content

app.run()
