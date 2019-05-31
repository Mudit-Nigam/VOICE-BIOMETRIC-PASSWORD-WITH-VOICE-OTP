from voiceit2 import VoiceIt2


import random

import sounddevice as sd
import soundfile as sf
import re



my_voiceit = VoiceIt2('key_069d3c61a7ce4adf9d4136e6c46d0be7','tok_9dee93cae2e54688863186d14522da2e')
user1 = my_voiceit.create_user()
print(user1['userId'])
