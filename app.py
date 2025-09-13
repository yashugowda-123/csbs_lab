from flask import Flask

#create app application
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Yashu !!!'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=False)