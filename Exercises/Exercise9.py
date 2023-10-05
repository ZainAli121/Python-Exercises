import win32com.client as wincl

def pronounce_names(names):
    speaker = wincl.Dispatch("SAPI.SpVoice")
    for name in names:
        speaker.Speak("Shoutout to " + name)

# Test the program
names = ["Zain", "Moiz", "Abdullah"]
pronounce_names(names)
