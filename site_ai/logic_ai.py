import speech_recognition as sr

def trancribation_ru():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            res = r.recognize_google(audio, language="ru-RU")
        return res
    except:
        return 'Что-то произошло не так, попробуйте позже ... '
    
def trancribation_en():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            res = r.recognize_google(audio, language="en-EN")
        return res
    except:
        return 'Something went wrong, try again later... '
    
        
