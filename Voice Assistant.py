import speech_recognition as speechRec
import pyttsx3
import openai

openai.api_key = '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'

framework = pyttsx3.init()
voices = framework.getProperty('voices')
framework.setProperty('voices', voices[4].id)

rec = speechRec.Recognizer()
mic = speechRec.Microphone(device_index=1)

conversation = ""
user = "Josh"
bot = "Nkechinyere"

while True:
    with mic as source:
        print("\n Listening")
        rec.adjust_for_ambient_noise(source, duration=0.2)
        audio = rec.listen(source)
    print("not listening")

    try:
        user_input = rec.recognize_google(audio)
    except:
        continue

    prompt = user+":"+user_input+"\n"+bot+":"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    response_str = response["choices"][0]["text"].replace["\n", ""]
    response_str = response_str.split(
        user + ":", 1)[0].split(bot)

    conversation+= response_str +"\m"
    print(response_str)

    framework.say(response_str)
    framework.runAndWait()