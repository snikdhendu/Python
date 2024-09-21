import pyttsx3

def main():
    text = input("Enter the text you want to hear: ")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    main()

