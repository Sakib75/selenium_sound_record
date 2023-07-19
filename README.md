# Play audio file and Capture using recorder in Selenium

**Install PulseAudio**


`sudo apt-get remove --purge alsa-base pulseaudio`

`sudo apt-get install alsa-base pulseaudio`


**Create virtual output and input device**

`pactl load-module module-null-sink sink_name="virtual_speaker" sink_properties=device.description="virtual_speaker"`

`pactl load-module module-remap-source master="virtual_speaker.monitor" source_name="virtual_mic" source_properties=device.description="virtual_mic"`

Download a sample file

`wget -O input.wav https://file-examples.com/wp-content/storage/2017/11/file_example_WAV_1MG.wav`

**Run Python Script**

`python test.py`

