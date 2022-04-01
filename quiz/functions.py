# functions file
correct = 0
wrong = 0

import random

# -----------------------------------------------------------------------------------------------

def random_generator():
    rand = random.randrange(1, 10)
    return rand

# -----------------------------------------------------------------------------------------------

def random_question_generator(question):
    global song
    
    if question == 1:
        print("WHAT SONG? 'Sometimes I just feel like, quitting I still might / Why do I put up this fight, why do I still write / Sometimes it’s hard enough just dealing with real life'")
        song = '8 mile'
        
    elif question == 2:
        print("WHAT SONG? 'Goin’ through public housing systems, victim of Munchausen’s Syndrome / My whole life I was made to believe I was sick when I wasn’t'")
        song = 'cleaning out my closet'
        
    elif question == 3:
        print("WHAT SONG? 'It’s been six months and still no word, I don’t deserve it? / I know you got my last two letters, I wrote the addresses on ‘em perfect'")
        song = 'stan'
        
    elif question == 4:
        print("WHAT SONG? 'Sit me here next to Britney Spears / Shit, Christina Aguilera better switch me chairs / So I can sit next to Carson Daly and Fred Durst / And hear ‘em argue over who she gave head to first'")
        song = 'the real slim shady'
        
    elif question == 5:
        print("WHAT SONG? 'If you was really selling coke, well then what the fuck / You stop for, dummy? If you slew some crack, you’d make a lot more money than you do from rap'")
        song = 'nail in the coffin'
        
    elif question == 6:
        print("WHAT SONG? 'At least have the decency in you / To leave me alone, when you freaks see me out / In the streets when I’m eating or feeding my daughter'")
        song = 'the way i am'
        
    elif question == 7:
        print("WHAT SONG? 'Maybe it’s beautiful music I made for you to just cherish / But I’m debated, disputed, hated, and viewed in America / As a motherfuckin’ drug addict, like you didn’t experiment'")
        song = 'renegade'
        
    elif question == 8:
        print("WHAT SONG? 'You dealing with a few true villains who stand inside of a booth, truth spilling / And spit true feelings until our tooth fillings come flying up outta of our mouths / Now rewind it'")
        song = 'forever'
        
    elif question == 9:
        print("WHAT SONG? 'By the way, when you see my dad / Tell him that I slit his throat in this dream I had'")
        song = 'my name is'
        
    elif question == 10:
        print("WHAT SONG? 'And when the cops came through / Me and Dre stood next to a burnt down house / With a can full of gas and a hand full of matches / And still weren’t found out'")
        song = 'forgot about dre'
    return song

# -----------------------------------------------------------------------------------------------

def response_func(song_chosen):
    global song
    global correct
    global wrong
    print()
    response = input('What is the song name?\n')

    if response == song:
        print('congratulations! You got it right!')
        correct += 1
    else:
        print('WRONG! Try again!')
        wrong += 1

# -----------------------------------------------------------------------------------------------
    
def results():
    if correct == 1:
        print(f'You got {correct} question right!')
    else:
        print(f'You got {correct} questions right!')
        
    if wrong == 1:
        print(f'You got {wrong} question wrong!')
    else:
        print(f'You got {wrong} questions wrong!')

# -----------------------------------------------------------------------------------------------

def help_button():
    global song

    print()
    print('Press "h" for help!')
    helpInput = input()

    if helpInput == 'h':
        if song == '8 mile':
            print('The song was written for his famous movie!')
            
        elif song == 'cleaning out my closet':
            print('The song is written mostly about his mother...')
            
        elif song == 'stan':
            print('One of the best story-written songs of all time.')
            
        elif song == 'the real slim shady':
            print('The last written and most famous song off his Marshall Mathers LP.')
            
        elif song == 'nail in the coffin':
            print('Famous Benzino diss!')
            
        elif song == 'the way i am':
            print('Very angry track off his Marshall Mathers LP.')
            
        elif song == 'renegade':
            print('Featured with Jay-Z. Also demolishes him...')
            
        elif song == 'forever':
            print('Song with Kanye, Wayne, and Drake!')
            
        elif song == 'my name is':
            print('First famous song off Slim Shady LP.')
            
        elif song == 'forgot about dre':
            print('Dre song off 2001?')
    else:
        print('ERROR. TRY AGAIN.')
