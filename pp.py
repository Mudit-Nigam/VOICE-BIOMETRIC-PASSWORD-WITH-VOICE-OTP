from voiceit2 import VoiceIt2


import random

import sounddevice as sd
import soundfile as sf


items = ['Zoos are filled with small and large animals']


rand_item = items[random.randrange(len(items))]
print("Your OTP is:")
print(rand_item)
my_voiceit = VoiceIt2('key_069d3c61a7ce4adf9d4136e6c46d0be7','tok_9dee93cae2e54688863186d14522da2e')



filename="C:\\Users\\Win10\\Desktop\\voiceit\\voiceit2\\4.wav"


print(my_voiceit.voice_verification("usr_c57ba85ee0cb466d8add6127b55835b9", "en-US", rand_item,filename ))
