from gtts import gTTS
from playsound import playsound

print('please fill out the ..... and the ..... and the ..... blank')

while True:
    fillers = input('enter the words in order and comma between:') #first,second,third
    try:
        words = fillers.split(',')
        final = f'please fill out the {words[0]} and the {words[1]} and the {words[2]} blank'
    except IndexError:
        print('wrong format entered')
        fillers
    else:
        langauge = 'en'
        the_audio = gTTS(text=final , lang=langauge , slow=False)
        the_audio.save('audio.mp3')
        playsound('audio.mp3') #please fill out the first and the second and the third blank (in voice)






















