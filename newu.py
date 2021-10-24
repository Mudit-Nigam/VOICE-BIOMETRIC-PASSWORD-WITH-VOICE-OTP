from voiceit2 import VoiceIt2


import random

import sounddevice as sd
import soundfile as sf
import re

key='key_069d3c61a7ce4adf9d4136e6c46d0be7'
tokenId='tok_9dee93cae2e54688863186d14522da2e'

my_voiceit = VoiceIt2(key,tokenId)
user1 = my_voiceit.create_user()
#print((user1))
print(user1['userId'])
user = user1['userId']
#user = "usr_c57ba85ee0cb466d8add6127b55835b9"
ph1 = my_voiceit.get_phrases("en-US")

phrases = []
for i in range(len(ph1['phrases'])):
          phrases.append(ph1['phrases'][i]['text'])
print(phrases)

print("Please enroll your voice for the following phrases: ")
print(phrases[0])
count = 0
while count<3:
    samplerate = 42100  # More Synchronous Hertz
    duration = 3  # seconds
    filename = 'try1.wav'
    print("Speak Now")
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                    channels=2, blocking=True)
    sf.write(filename, mydata, samplerate)
    print("Stop")

    enroll = my_voiceit.create_voice_enrollment(user, "en-US", phrases[0], "try1.wav")
    print(enroll["responseCode"])
    if enroll["responseCode"] == "SUCC":
        count = count+1
        print("attempt successful")
    else:
        print("attempt fail,try again")


'''



//filename="C:\\Users\\Win10\\Desktop\\voiceit\\output.wav"


//print(my_voiceit.voice_verification("usr_c57ba85ee0cb466d8add6127b55835b9", "en-US", "my face and voice identify me",filename ))
'''
