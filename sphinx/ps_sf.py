#!/usr/bin/python

from os import environ, path
import pyaudio

import speech_recognition as sr

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

MODELDIR = "/usr/local/share/pocketsphinx/model/"

config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', 'j.lm')
config.set_string('-dict', 'j.dic')
decoder = Decoder(config)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# write audio to a RAW file
with open("ps_sf.raw", "wb") as f:
    f.write(audio.get_raw_data()) 

decoder.start_utt()
stream = open('ps_sf.raw', 'rb')
decoder.start_utt()
stream = open('ps_sf.raw', 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print (decoder.hyp().hypstr)



