# Sphinx files read

//Запомнить пароль и логин github навсегда
git config credential.helper store


gcc -o ps_file ps_file.c     -DMODELDIR=\"`pkg-config --variable=modeldir pocketsphinx`\"     `pkg-config --cflags --libs pocketsphinx sphinxbase`

git add --all

git add .

git commit -m "new msg"

git push -u origin master

rec -r 16k -e signed-integer -b 16 -c 1 ps_file.raw

./ps_file



#Sphinx mic read continuous

pocketsphinx_continuous -inmic yes -lm /home/stas/Sphinx/j.lm -dict /home/stas/Sphinx/j.dic


#Для использования скрипта python

sudo apt-get install portaudio19-dev

sudo apt install python-pip

python -m pip install pyaudio

./sphinx_mic.py
