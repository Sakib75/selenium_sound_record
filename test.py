from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import subprocess

microphone_name = "virtual_mic"
command = f"pactl set-default-source {microphone_name}"

subprocess.run(command, shell=True)

# Set up Selenium webdriver (ensure you have the appropriate driver for your browser installed)

chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Grant permission automatically

driver = webdriver.Chrome(options=chrome_options)

# Navigate to the online recorder webpage
driver.get("https://online-voice-recorder.com/")


# Execute JavaScript to set the virtual microphone as the input device
# driver.execute_script("navigator.mediaDevices.getUserMedia({ audio: { deviceId: 'virtual_mic' } })")

# Find and click the record button (assuming it has an ID of 'record-button')
record_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//i[@class='icn-record']")))
record_button.click()


# Use ffmpeg to play the audio file to the virtual microphone (replace input.wav with your actual audio file)
import subprocess

# subprocess.call(["ffmpeg", "-i", "input.wav", "-f", "pulse", "-ac", "1", "virtual_mic"])
command = 'PULSE_SINK=virtual_speaker ffmpeg -i input.wav -f pulse "virtual_mic"'

# Execute the command
subprocess.run(command, shell=True)


# Find and click the stop button (assuming it has an ID of 'stop-button')
stop_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//i[@class='icn-record']")))
stop_button.click()


sleep(5)

save_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn-save']")))
save_button.click()

sleep(5)



# Close the web browser
driver.quit()
