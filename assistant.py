import speech_recognition as sr
import pyttsx3 as tts
from helper import helper
r = sr.Recognizer()
m = sr.Microphone()
wakeWords = "Ova"
def SpeakTextLoud(text):
    engine = tts.init()
    engine.say(text)
    engine.runAndWait()

response = {
    "success" : True,
    "error" : None,
    "message" : None
}
def recognizeSpeech(recognizer,microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

        SpeakTextLoud("Hello There, I am OVA ...")
        print("Hello There, I am OVA ...")
        try:
            usersAudio = r.listen(source)
            response["message"] = r.recognize_google(usersAudio)
            if response["message"].lower() == wakeWords.lower():
                SpeakTextLoud("How can I help you?")
                print("How can I help you?")
                userQuestion = r.listen(source)
                response["message"] = r.recognize_google(userQuestion)
                answers = helper(response["message"])
                print(response["message"])
                print(answers)
            else:
                print("I am hearing ")
                print("You said" ,response["message"])
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API Error"
            
        except sr.UnknownValueError:
            response["error"]="Unable to recognise the speech"

    return response

recognizeSpeech(r,m)