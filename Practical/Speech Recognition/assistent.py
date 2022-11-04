# importing speech recognition package from google api
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
from selenium import webdriver  # to control browser operations

num = 1


def assistant_speaks(output):
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    print("PerSon : ", output)

    toSpeak = gTTS(text=output, lang="en", slow=False)
    # saving the audio file given by google text to speech
    file = f"{num}.mp3 "
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)


def process_text(input):
    try:
        if "search" in input or "play" in input:
            # a basic web crawler using selenium
            search_web(input)
            return

        elif "who are you" in input or "define yourself" in input:
            speak = """Hello, I am Person. Your personal Assistant.
			I am here to make your life easier. You can command me to perform
			various tasks such as calculating sums or opening applications etcetra"""
            assistant_speaks(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Qmansys."
            assistant_speaks(speak)
            return

        elif "Qmansys" in input:  # just
            speak = """Qmansys is best iot solution provider."""
            assistant_speaks(speak)
            return

        elif "calculate" in input.lower():

            # write your wolframalpha app_id here
            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index("calculate")
            query = input.split()[indx + 1 :]
            res = client.query(" ".join(query))
            answer = next(res.results).text
            assistant_speaks(f"The answer is {answer}")
            return

        elif "open" in input:

            # another function to open
            # different application availaible
            open_app(input.lower())
            return

        else:

            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if "yes" in str(ans) or "yeah" in str(ans):
                search_web(input)
            else:
                return
    except Exception as error: # pylint: disable=broad-except
        print(error)
        assistant_speaks(
            "I don't understand, I can search the web for you, Do you want to continue?"
        )
        ans = get_audio()
        if "yes" in str(ans) or "yeah" in str(ans):
            search_web(input)


def search_web(input):

    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if "youtube" in input.lower():

        assistant_speaks("Opening in youtube")
        indx = input.lower().split().index("youtube")
        query = input.split()[indx + 1 :]
        driver.get("http://www.youtube.com/results?search_query =" + "+".join(query))
    elif "wikipedia" in input.lower():

        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index("wikipedia")
        query = input.split()[indx + 1 :]
        driver.get("https://en.wikipedia.org/wiki/" + "_".join(query))
    elif "google" in input or "search" in input:

        indx = input.lower().split().index("google")
        query = input.split()[indx + 1 :]
        driver.get("https://www.google.com/search?q =" + "+".join(query))

    else:

        driver.get("https://www.google.com/search?q =" + "+".join(input.split()))

    return

import subprocess, sys
def open_application(input):

    opener = "open" if sys.platform == "darwin" else "xdg-open"


    subprocess.call([opener, input])


# function used to open application
# present inside the system.
def open_app(input):

    if "chrome" in input:
        assistant_speaks("Google Chrome")
        open_application("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        open_application("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        open_application("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        open_application("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
    else:
        assistant_speaks("Application not available")

    return


def get_audio():
    """
    It records audio from the microphone, converts it into text and returns it
    :return: The text that is being spoken by the user.
    """

    rObject = sr.Recognizer()
    audio = ""

    with sr.Microphone() as source:
        print("Speak...")

        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=5)
    print("Stop.")  # limit 5 secs

    try:
        text = rObject.recognize_google(audio, language="en-US")
        print("You : ", text)
        return text

    except Exception:
        assistant_speaks("Could not understand your audio, PLease try again !")
        return 0


# Driver Code
if __name__ == "__main__":
    assistant_speaks("What's your name, Human?")
    name = "Human"
    name = get_audio()
    assistant_speaks(f"Hello, {name}.")

    while 1:

        assistant_speaks("What can i do for you?")
        text = get_audio().lower()

        if text == 0:
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks(f"Ok bye, {name}.")
            break

        # calling process text to process the query
        process_text(text)
