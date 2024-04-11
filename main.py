# def hello():
#     print("HELLO WORLD, HAPPY CODING :) ")
#     print("DEPLOYMENT DONE ,CI/CD")
#     print("Good dhdhdh")
#     return "DEPLOYMENT COMPLETED !!!!"

# hello()


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
