#!/bin/bash

# Convolve MP3 audio with wav or mp3 stereo impulse signals.

cd "$(dirname "$0")"

printf "$1"

#fname=`echo "$1" | cut -d'.' -f1`
#fname=`echo "$1 | -f1`
fullfile="$1"
fpath=${fullfile%/*}
xbase=${fullfile##*/}
xfext=${xbase##*.}
xpref=${xbase%.*}

ffmpeg -i "$1" metaAudio.wav

#if [$# = 4]; then
python3 converb.py metaAudio.wav "$2" "$3" metaAudio.wav
#elif [$# = 3]; then
#python3 converb.py metaAudio.wav "$2" metaAudio.wav
#fi
if [ $xfext == "wav" ]; then
	cp metaAudio.wav "$fpath/$xpref [convolved].wav"
elif [ $xfext == "mp3" ]; then
	ffmpeg -i metaAudio.wav -vn -ar 44100 -ac 2 -b:a 192k "$fpath/$xpref [convolved].mp3"
fi

rm metaAudio.wav
