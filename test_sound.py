import speech_recognition as sr
import time
import pyaudio
t0 = None
t1 = None
t2 = None
t3 = None
quit = False

p = pyaudio.PyAudio()
print("Available audio input devices:")
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if dev['maxInputChannels'] > 0:
        print(f"Device index {i}: {dev['name']}")

def test_speech_recognition():
    global t0, t1, quit
    t0 = time.time()
    recognizer = sr.Recognizer()
    while not quit:
        with sr.Microphone(device_index=2) as source:
            print("Say something:")
            audio = recognizer.listen(source)
            try:
                print("You said: " + recognizer.recognize_sphinx(audio))
                t1 = time.time()
                print("sphinx: " + str(t1-t0))
                break
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

def test_google():
    global t2, t3, quit
    t2 = time.time()
    while not quit:
        r = sr.Recognizer()
        with sr.Microphone(device_index=2) as source:
            print("[speech recognition] Say something!")
            audio = r.listen(source)
            try:
                recog_results = r.recognize_google(audio)
                latest_voice_command = recog_results.lower()
                print(f"[speech recognition] Google Recognized: {latest_voice_command}")
                t3 = time.time()
                print("google: " + str(t3-t2))
            except sr.UnknownValueError:
                print("[speech recognition] Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("[speech recognition] Could not request results from Google Speech Recognition service; {0}".format(e))
# Run the test
test_speech_recognition()
test_google()