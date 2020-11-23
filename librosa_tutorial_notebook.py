#!/usr/bin/env python
# coding: utf-8

# In[5]:


import librosa

audio_file = 'bensound-moose.mp3'

y, sr = librosa.load(audio_file)


# In[8]:


print(f'Estimated tempo: {tempo:.2f} beats per min')


# In[6]:


tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print(f'Estimated tempo: {tempo} beats per min')

beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print(beat_times)

