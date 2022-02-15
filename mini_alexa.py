import speech_recognition as sr
import pyaudio
import datetime
import sys 
import pywhatkit
import pyttsx3
import pyjokes
import wikipedia
import webbrowser

engine=pyttsx3.init()
engine.setProperty("rate",150)
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
r=sr.Recognizer()

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    
def mini_alexa():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print('\n')
        print("speak")
        engine_talk("Hey There")
        audio=r.listen(source)
        try:
            command=r.recognize_google(audio,language='eng-in')
            command=command.lower()
            if 'alex' in  command:
                command=command.raplace('alexa','')
                print('you said' + command)
            else:
                print('you said '+ command)
            if 'hello'in command:
                print('hey there, how can i help you')
                engine_talk('hey there,how can i help you')
            elif 'who are you' in command:
                print('I am mini alexa a k a your virtual assistant master')
                engine_talk('I am mini alexa a k a your virtual assistant master. how can i help you ?')
            elif 'can you do' in command :
                
                print('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
                       open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google.How may i help you ??''')
                engine_talk('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
                       open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google.How may i help you ?''')
            elif 'play' in command:
                song=command.replace('play', '')
                print('playing ' + song)
                engine_talk('palying'+ song)
                pywhatkit.playonyt(song)
                
            elif 'date and time' in command :
                today = datetime.date.today()
                time = datetime.datetime.now().strftime('%I:%M %p')
                d2 = today.strftime("%B %d, %Y")
                print("Today's Date is ", d2, 'Current time is', time)
                engine_talk('Today is : '+ d2)
                engine_talk('and current time is '+ time)
            elif 'time and date' in command :
                today = datetime.date.today()
                time = datetime.datetime.now().strftime('%I:%M:%p')
                d2 = today.strftime("%B %d, %Y")
                print("Today's Date is ", d2, 'Current time is', time)
                engine_talk( 'Current time is '+ time)
                engine_talk('and Today is : '+ d2)
            elif 'time' in command:
                time=datetime.datetime.now().strftime('%I:%M:%p')
                print('The current time is' +time)
                engine_talk('The current time is'+ time)
            elif 'date' in command:
                today = datetime.date.today()
                print("Today's date:", today)
                d2 = today.strftime("%B %d, %Y")
                print("Today's Date is ", d2)
                engine_talk('The todays date is')
                engine_talk(today)
            elif 'tell me about' in command:
                name = command.replace('tell me about' , '')
                info = wikipedia.summary(name, 1)
                print(info)
                engine_talk(info)
            
            elif 'wikipedia' in command:
                name = command.replace('wikipedia' , '')
                info = wikipedia.summary(name, 1)
                print(info)
                engine_talk(info)
            elif 'what is' in command:
                name = command.replace('what is ' , '')
                info = wikipedia.summary(name, 1)
                print(info)
                engine_talk(info)
            elif 'who is ' in command:
                name = command.replace('who is' , '')
                info = wikipedia.summary(name, 1)
                print(info)
                engine_talk(info)
            elif 'what is'in command:
                search = 'https://www.google.com/search?q='+command
                print(' Here is what i found on the internet..')
                engine_talk('searching... Here is what i found on the internet..')
                webbrowser.open_new(search)
            elif 'joke' in command:
                _joke = pyjokes.get_joke()
                print(_joke)
                engine_talk(_joke)
            elif 'search' in command:
                search='https://www.google.com/search?q='+command
                engine_talk('this what is found')
                webbrowser.open(search)
            elif "my location" in command:
                url = "https://www.google.com/maps/search/Where+am+I+?/"
                webbrowser.get().open(url)
                engine_talk("You must be somewhere near here, as per Google maps")
            elif 'locate ' in command :
                engine_talk('locating ...')
                loc = command.replace('locate', '')
                if 'on map' in loc :
                    loc= loc.replace('on map',' ')
                url = 'https://google.nl/maps/place/'+loc+'/&amp;'
                webbrowser.get().open(url)
                print('Here is the location of '+loc)
                engine_talk('Here is the location of '+loc)

            elif 'location of' in command :
                engine_talk('locating ...')
                loc = command.replace('find location of', '')
                url = 'https://google.nl/maps/place/'+loc+'/&amp;'
                webbrowser.get().open(url)
                print('Here is the location of '+loc)
                engine_talk('Here is the location of '+loc)
            elif 'where is ' in command :
                engine_talk('locating ...')
                loc = command.replace('where is', '')
                url = 'https://google.nl/maps/place/'+loc+'/&amp;'
                webbrowser.get().open(url)
                print('Here is the location of '+loc)
                engine_talk('Here is the location of '+loc)
            elif 'bootcamps' in command :
                search = 'http://tathastu.twowaits.in/index.html#courses'
                engine_talk('opening boot camps')
                webbrowser.open(search)
            elif 'python bootcamp' in command :
                search = 'http://tathastu.twowaits.in/kickstart_python.html'
                engine_talk('showing pythonboot camp')
                webbrowser.open(search)
            elif 'open facebook' in command:
                search='https://www.facebook.com/'
                engine_talk('opening facebook')
                webbrowser.open(search)
                
            elif 'open google' in command :
                print('opening google')
                engine_talk('opening google..')
                webbrowser.open_new('https://www.google.co.in/')
            elif 'gmail' in command :
                print('opening gmail ...')
                engine_talk('opening gmail..')
                webbrowser.open_new('https://mail.google.com/')
            elif 'open youtube' in command :
                print('opening you tube ...')
                engine_talk('opening you tube..')
                webbrowser.open_new('https://www.youtube.com/')
            elif 'open instagram' in command :
                print('opening instagram ...')
                engine_talk('opening insta gram...')
                webbrowser.open_new('https://www.instagram.com/')
            elif 'open stack overflow' in command :
                print('opening stackoverflow ...')
                engine_talk('opening stack overflow...')
                webbrowser.open_new('https://stackoverflow.com/')
            elif 'open github' in command :
                print('opening git hub ...')
                engine_talk('opening git hub...')
                webbrowser.open_new('https://github.com/')
            elif 'bye' in command:
                print('good bye, have a nice day !!')
                engine_talk('good bye, have a nice day !!')
                sys.exit()
            elif 'thank you' in command :
                print("your welcome")
                engine_talk('your welcome')
            elif 'stop' in command:
                print(' bye,see you soon')
                engine_talk('bye, see you soon')
                sys.exit()
            elif 'tata' in command:
                print('tata, see you soon')
                engine_talk('tata, see you soon')
                sys.exit()
            else:
                print(' Here is what i found on the internet..')
                engine_talk('Here is what i found on the internet..')
                search = 'https://www.google.com/search?q='+command
                webbrowser.open(search)
        except Exception as ex:
            print(ex)


while True:
    mini_alexa()