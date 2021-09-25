#!/usr/bin/env python
# coding: utf-8

# # Text to Speech & Speech To Text by `Mr. Harshit Dawar!`
# 
# * Libraries Needed for this practical:
#     * ffmpeg
#     * pyaudio
#     * pydub
#     * SpeechRecognition
#     * pyttsx3

# In[8]:


# Importing the required Libraries
import speech_recognition as SR
from pydub import AudioSegment as ADS
import pyttsx3


# ## Creating Microphone & Audio Recognizer objects

# In[9]:


voice_recognizer = SR.Recognizer()
Mic = SR.Microphone()


# ## Capturing Audio & Saving Files

# In[10]:


wav_file_path = "/Users/harshitdawar/GitHub/Natural-Language-Processing/Speech-To-Text-And-Text-To-Speech/audio-captured.wav"
mp3_file_path = "/Users/harshitdawar/GitHub/Natural-Language-Processing/Speech-To-Text-And-Text-To-Speech/audio-captured.mp3"

try:
    with Mic as source:
        print("wait for the microphone to calibrate\n")
        voice_recognizer.adjust_for_ambient_noise(source = source, duration = 3)
        print("Set minimum energy threshold to {}".format(voice_recognizer.energy_threshold))

    # Capturing the audio & writing it to a file!
    while True:
        with Mic as source:
            print("Please Say Something!")
            audio_captured = voice_recognizer.listen(source)
            print("Captured It, Wait for a while, audio file Generation is in progress!")
            
        # Generating the Audio File to store the Audio
        with open(wav_file_path, "wb") as file:
            file.write(audio_captured.get_wav_data())
        
        # Converting WAV File to MP3 File
        WAV_File = ADS.from_file(wav_file_path, format = "wav")
        MP3_File = WAV_File.export(mp3_file_path, format = "mp3", bitrate = "320")
        break
        
        
except KeyboardInterrupt:
    pass


# ## Displaying the Audio Captured

# In[11]:


def display_speech(library_to_use, audio):
    if library_to_use == "Google":
        speech = voice_recognizer.recognize_google(audio)
    else:
        pass
    
    try:
        print("{0} thinks you said '{1}'" .format(library_to_use, speech))
    except SR.UnknownValueError:
        print("%s could not understand audio"%library_to_use)
    except SR.RequestError as e:
        print("{0} error; {1}".format(library_to_use, e))
        


# In[12]:


display_speech("Google", audio_captured)


# ## Text To Speech

# In[13]:


# Saving the text recognized by Google Library from the Speech
with open("Google_recognized_text.txt", "w") as file:
    file.write(voice_recognizer.recognize_google(audio_captured))


# In[14]:


def text_to_speech(text_file_path):
    with open(text_file_path, "r") as file:
        text = file.read()
        
    
    # Initializing the Text to Speech Engine
    audio_engine = pyttsx3.init()
    
    # Adding the work in the queue
    audio_engine.say(text)
    
    # Running the work added in the queue
    audio_engine.runAndWait()
    
    
def tts_save(text_file_path, file_path_to_save_audio_to):
    with open(text_file_path, "r") as file:
        text = file.read()
    
    # Initializing the Text to Speech Engine
    audio_engine = pyttsx3.init()
    
    # Saving the Text To Speech Audio File
    audio_engine.save_to_file(text, file_path_to_save_audio_to)
    audio_engine.runAndWait()


# ### Calling Functions to convert Text To Speech as well as Saving the generated Audio to MP3 File as well!

# In[15]:


text_to_speech("Google_recognized_text.txt")


# In[16]:


tts_save("Google_recognized_text.txt", "google_tts_audio.mp3")


# # Congratulations, you have learned how to convert Text to Speech & Vice Versa simaltaneously with saving files for them
