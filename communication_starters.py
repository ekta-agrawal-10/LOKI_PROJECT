#this is communication starter shinae
import time
import datetime
import pyttsx3
import os
from googletrans import Translator

translator = Translator()


engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme ():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else :
        speak("good evening!")




#program structure

if __name__ == "__main__":
        wishme()
        speak(" i Shenai welcome you to our project LOKI . i am a Language helper who will provide you tips and tricks along with fun questions to start converstaion .")
        print(" i Shenai welcome you to our project LOKI . i am a Language helper who will provide you tips and tricks along with fun questions to start converstaion  .")
        print("""
TIPS :
1) Give a compliment
Complimenting someone whom you have met for the first time can lead to an ongoing and pleasant conversation. You can pick anything about the person you like and say something nice about them.
2)Talk about an event or situation
Identify something interesting in your surroundings and talk about it. For instance, if you are at a business conference, you can share your views on the conference with the person sitting next to you. If you are in a coffee shop, you can talk about your favourite coffee to the person next to you in line.
3)Ask an opinion
To start a conversation with someone you do not know, you can ask someone's opinion on a particular topic. When you give importance to the opinions of others, you can showcase your willingness to talk to that person.
4)Offer help
If you have an option to help someone you want to talk to, offer them your help. When you provide assistance without asking, you can earn the other person's trust because you show genuine concern for their needs.
5)Ask for help
Asking and requesting help from someone is a great way to start a conversation. Before asking for help, you can make sure your request is convenient and easy to perform.
6)Share an interesting fact
Sharing an exciting fact with someone you want to talk to can be an effective way to establish a meaningful conversation. This is because it can connect two people through exploring a common interest or learning something new.
7)Make a useful comment
Another effective strategy to start a conversation is making a useful or insightful comment based on the situation you find yourself. This way of conversing works best when there is something common to talk about.
8)Make an observation
The environment in which you live or work can provide ample opportunities to start a conversation. For example, you can comment on the building, artwork or temperature.
9)Seek advice
You can start a conversation by seeking advice from a stranger. When doing so, try to keep your advice relevant to the environment.
10)Discuss common interests
In many circumstances, you may share an obvious interest with the other person. For example, if you both watch a cricket match sitting in a coffee shop, cricket is the common interest for both parties.


SOME GREAT QUESTIONS:

1. Tell me about yourself.

2. Have you done anything exciting lately?

3. What made you smile today?

4. How did you meet the host?

5. What’s your favorite form of social media?

6. What was the last good book you read?

7. Do you listen to any podcasts? Which is your favorite?

8. What do you think is the best show on Netflix right now?

9, Have you been on any interesting trips lately?

10. What do you think has been the best movie of the year so far?

11. What song do you wish you could put on right now?

12. Are you a cat person or a dog person?

13. Do you think you’re an introvert or an extrovert?

14. If you didn’t have the job you have now, what would you be?

15. What’s your strangest hidden talent?

16. What is something people are always surprised to learn about you?

17. What is the most rewarding part of your career?

18. Where do you want to be in five years?

19. What superpower do you wish you could have?

20. Where would you go on vacation if you had no budget?

21. If you could travel back in time, what decade would you choose to live in?

22. What’s the best thing you’ve ever bought off Amazon?

23. What’s the last concert you went to?

24. What is one thing you can’t live without?

25. What’s the strangest dream you’ve had recently?

26. What is your favorite book of all time?

27. How many countries have you been to?

28. What’s your favorite city you’ve visited?

29. Would you rather travel via plane or boat?

30. Would you rather be really hot or really cold?

31. What are your thoughts on the British royal family?

32. Do you like documentaries? Have you watched any good ones recently?

33. Who is your favorite celebrity couple ever?

34. Which celebrity couple do you wish would get back together?

35. If you could host a talk show, who would you have on first?

36. What’s your favorite sport?

37. What sport do you wish you were really good at?

38. What’s the best holiday?

39. How did you spend your last birthday?

40. Do you believe men and women can ever just be friends?
""")
        

       

time.sleep(5)
