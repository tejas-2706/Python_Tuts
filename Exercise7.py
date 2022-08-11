# --------------------------------------Healthy Programmer--------------------------------------------------------------

# active time of this program 9am to 5pm
# Water - Water.mp3 (3.5 litres) - "Drank" - [log in a file all the data with time] - every 30 min [200 ml glases ]
# Eyes - Eyes.mp3  -- "EyDone" - [log in a file all the data with time] - every 30 min
# Physical activity - Physical.mp3 - every 45 min - he should write "ExDone" - log
# Time should not clash

# Rules : pygame module to play audio
import time
# def water_drinking_time():
# print(datetime.time())




# from pygame import mixer
# # Starting the mixer
# mixer.init()
#
# # Loading the song
# mixer.music.load("F:\\023 AA GALE LAG JA = WADA KARO.mp3")
#
# # Setting the volume
# mixer.music.set_volume(0.7)
#
# # Start playing the song
# mixer.music.play()

# infinite loop
# while True:
#
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input(" ")
#
#     if query == 'p':
#
#         # Pausing the music
#         mixer.music.pause()
#     elif query == 'r':
#
#         # Resuming the music
#         mixer.music.unpause()
#     elif query == 'e':
#
#         # Stop the mixer
#         mixer.music.stop()
#         break

from time import time
from datetime import datetime
from pygame import mixer

def music(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    l_o_g = open("imp-log.text", "a")
    l_o_g.write(f"{msg} ||{datetime.now()}||\n")
    l_o_g.close()

if __name__ == '__main__':
    # music("F:\\wave.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_in_seconds = 5
    eyes_in_seconds = 15
    exercise_in_seconds = 10


    while True:
        if time() - init_water > water_in_seconds:
            print("Time to drink some Water Buddy......Enter 'drank' after drinking water")
            music("F:\\wave.mp3", "drank")
            init_water = time()
            log_now("Drank Water at:-- ")

        if time() - init_eyes > eyes_in_seconds:
            print("Time to relax your Eyes Buddy......Enter 'eyes relaxed' after relaxation of your eyes")
            music("F:\\wave.mp3", "eyes relaxed")
            init_eyes = time()
            log_now("Eyes relaxed at:-- ")

        if time() - init_exercise > exercise_in_seconds:
            print("Time to do some physical Exercise Buddy......Enter 'ex done' after drinking water")
            music("F:\\wave.mp3", "ex done")
            init_exercise = time()
            log_now("Physical Exercise Done at:-- ")







