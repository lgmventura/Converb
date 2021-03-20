# Convolve MP3 audio with wav or mp3 stereo impulse signals.

#!/bin/bash
cd "$(dirname "$0")"

printf "$2"

ffmpeg -i "$1" metaAudio.wav
#if [$# = 4]; then
python3 converb.py metaAudio.wav "$2" "$3" metaAudio.wav
#elif [$# = 3]; then
#python3 converb.py metaAudio.wav "$2" metaAudio.wav
#fi
fname=`echo "$1" | cut -d'.' -f1`
ffmpeg -i metaAudio.wav -vn -ar 44100 -ac 2 -b:a 192k "$fname [convolved].mp3"
rm metaAudio.wav
