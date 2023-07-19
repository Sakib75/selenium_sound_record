# Play audio file and Capture using recorder in Selenium

**Install FFMPEG**

`sudo apt install ffmpeg`

**Install PulseAudio**


`sudo apt-get remove --purge alsa-base pulseaudio`

`sudo apt-get install alsa-base pulseaudio`


**Create virtual output and input device**

`pactl load-module module-null-sink sink_name="virtual_speaker" sink_properties=device.description="virtual_speaker"`

`pactl load-module module-remap-source master="virtual_speaker.monitor" source_name="virtual_mic" source_properties=device.description="virtual_mic"`


**Run Python Script**

`python test.py`

