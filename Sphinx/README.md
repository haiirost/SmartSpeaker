# Sphinx files read

//Запомнить пароль и логин github навсегда
git config credential.helper store


gcc -o hello_ps hello_ps.c     -DMODELDIR=\"`pkg-config --variable=modeldir pocketsphinx`\"     `pkg-config --cflags --libs pocketsphinx sphinxbase`

git add --all

git commit -m "new msg"

git push -u origin master

rec -r 16k -e signed-integer -b 16 -c 1 hello_ps.raw

./hello_ps



#Sphinx mic read continuous

pocketsphinx_continuous -inmic yes -lm /home/stas/Sphinx/j.lm -dict /home/stas/Sphinx/j.dic

gcc -o sphinx_mic sphinx_mic.c     -DMODELDIR=\"`pkg-config --variable=modeldir pocketsphinx`\"     `pkg-config --cflags --libs pocketsphinx sphinxbase`

git add --all && git commit -m "EDIT THIS MSG" && git push -u origin master

./sphinx_mic


#Для использования скрипта python

sudo apt-get install portaudio19-dev

sudo apt install python-pip

python -m pip install pyaudio

./sphinx_mic.py
