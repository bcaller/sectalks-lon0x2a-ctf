git clone git@github.com:peteshadbolt/spectrogram.git
cd spectrogram
python spectrogram.py ../flag.jpg
cd ../

# optional
sox flag.jpg.wax -n spectrogram
xdg-open spectrogram.png
