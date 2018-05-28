#!/usr/bin/python

from os import environ, path
import pyaudio

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

MODELDIR = "/usr/local/share/pocketsphinx/model/"

config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', 'j.lm')
config.set_string('-dict', 'j.dic')
decoder = Decoder(config)

#p = pyaudio.PyAudio()
#stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
#stream.start_stream() 

#in_speech_bf = False
#decoder.start_utt()
#while True:
#    buf = stream.read(1024)
#    if buf:
 #       decoder.process_raw(buf, False, False)
  #      if decoder.get_in_speech() != in_speech_bf:
   #         in_speech_bf = decoder.get_in_speech()
    #        if not in_speech_bf:
     #           decoder.end_utt()
      #          if decoder.hyp().hypstr == 'JARVICE':
       #             print (1)
        #        else:
         #           print (decoder.hyp().hypstr)
          #      decoder.start_utt()
    #else:
     #   break    
#decoder.end_utt()



decoder.start_utt()
stream = open('ps_sf.raw', 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])







