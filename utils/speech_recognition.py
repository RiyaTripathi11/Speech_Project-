import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None
    except sr.RequestError:
        print("Could not request results, check your internet.")
        return None
