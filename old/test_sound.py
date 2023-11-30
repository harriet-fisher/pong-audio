import pygame
pygame.mixer.init()

instructions_audio_event = False
instructions = pygame.mixer.Sound('instructions.wav')

def instructions_audio():
    global instructions_audio_event
    if instructions_audio_event:
        instructions.play()
    else:
        instructions.stop()

val = None

while val != 'q':
    val = input("True or False? (t/f)")
    if val == 't':
        instructions_audio_event = True
    if val == 'f':
        instructions_audio_event = False
    print(instructions_audio_event)
    instructions_audio()