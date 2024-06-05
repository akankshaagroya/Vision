import pyttsx3
import datetime
import time
import webbrowser
from playsound import playsound
from plyer import notification




def speak(audio): 
  engine=pyttsx3.init()
  voices=engine.getProperty('voices',)
  engine.setProperty('voices',voices[1].id)
  engine.say(audio)
  engine.runAndWait()

def tellTime(): 
  time=str(datetime.datetime.now())
  hour= time[11:13]
  minute=time[14:16]
  speak("The time is " + hour + "Hours and" + minute + "Minutes")

speak("Hello I am Vision, your medical assistant")
speak("What is your name")
user= input("Enter the patient's name:")
speak("Hello nice to meet you"+user)



speak("what is your age?")
age= input("Enter the patient's age:")

speak("Would you like to get tips about your condition?")
precaution=input("Would you like to get tips about your condition?")
precaution.lower()
if precaution=="yes":
    Diabetes, Bloodpressure, Covid_19, Thyroid, Arthritis= 1,2,3,4,5
    print("Select your conditions from below or enter your condition")
    print("1:Diabetes")
    print("2:Blood Pressure")
    print("3:Covid-19")
    print("4:Thyroid")
    print("5:Arthritis")
    speak("Please select your condition number from below or enter your condition")
    Condition=input("Enter your condition's serial number or the name")
    if Condition==1:
       speak("Opening a site for Diabetes tips") 
       webbrowser.open_new_tab("https://www.mayoclinic.org/diseases-conditions/diabetes/in-depth/diabetes-management/art-20045803Mayo Clinic")
    if Condition==2:
        speak("Opening site for Blood Pressure tips")
        webbrowser.open_new_tab("https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/in-depth/high-blood-pressure/art-20046974")
    if Condition==3:
        speak("Opening site for Covid-19 tips")
        webbrowser.open_new_tab("https://kidshealth.org/en/parents/coronavirus-stop-spread.html")
    if Condition==4:
        speak("Opening site for Thyroid tips")
        webbrowser.open_new_tab("https://pharmeasy.in/blog/thyroid-problem-dos-and-donts-for-thyroid-patients/")
    if Condition==5:
        speak("Opening site for Arthritis tips")
        webbrowser.open_new_tab("https://www.bluecrossmn.com/wellbeing/preventive-care/how-prevent-arthritis-pain")
    if Condition!=range(1,6):
        speak("Opening site for"+Condition)
        webbrowser.open_new_tab("https://www.webmd.com/search/search_results/default.aspx?query="+Condition)
else:
    speak("")

speak("How many times in a day do you have to take your medication?")
frequency= int(input("Enter here:"))
for i in range(frequency):
   time=str(time)
   speak("at what time do you need to take you medicines?")
   alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
   def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"


while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()
now = datetime.now()
current_hour = now.strftime("%I")
current_min = now.strftime("%M")
current_sec = now.strftime("%S")
current_period = now.strftime("%p")
if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    speak("VISION REMINDER: It is time to take your medication")
                    playsound('D:/Library/Documents/Projects/Coding/Beginner Python Projects/Alarm Clock/alarm.wav')
                    notification.notify(
                    title = 'VISION:Medication Reminder',
                    message = 'Time to take your medications',
                    app_icon = None,
                    timeout = 10,
                    )



    





