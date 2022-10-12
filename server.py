from flask import Flask
import random

random_number = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def start():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:number>")
def guess(number):
    if number > random_number:
        return "<h1 style='color: red'>Too high, Try Again!</h1>" \
               "<img src='https://media2.giphy.com/media/3OhXBaoR1tVPW/200w.webp?cid=ecf05e47wdska0mivt3uk9e4r5ks6z9kd1g0thcg7sd7p1vh&rid=200w.webp&ct=g'/>"
    elif number < random_number:
        return "<h1 style='color: blue'>Too low, Try Again!</h1>" \
               "<img src='https://media2.giphy.com/media/3OhXBaoR1tVPW/200w.webp?cid=ecf05e47wdska0mivt3uk9e4r5ks6z9kd1g0thcg7sd7p1vh&rid=200w.webp&ct=g'/>"
    else:
        return "<h1 style='color: green'>Correct. Good Guess!!</h1>" \
               "<img src='https://media3.giphy.com/media/Rznz8HjrKQAOQ/giphy.webp?cid=ecf05e47awnoaiax788ps6nl3u71pmv8yc64szdwfcmaw3o9&rid=giphy.webp&ct=g'/>"



if __name__ == "__main__":

    app.run(debug=True)