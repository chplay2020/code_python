import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

#nghe

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)

#hieu

    if you == "":
        robot_brain = "I can't hear you, say again"
    elif you == "hello":
        robot_brain = "hello Thanh"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you:
        robot_brain = "Bye"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break

#noi

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()