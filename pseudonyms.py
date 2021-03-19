### Import packages ###
import sys
import random
import time

# Main Screen
print("~~~ Welcome to My Hero Academia! ~~~")
print("Before you can start. You would need a Hero name using your quirk.")
print("Let's use this 'Hero Name Generator'")
print('\n\n'"~~~ PULL THE LEVER! ~~~")

time.sleep(4)


def progress_bar(secs, size=10):
    for i in range(size + 1):
        print('[{:<{}}]{}'.format('X' * i, size,
                                  '\b' * (size + 2)), end='', flush=True)
        time.sleep(secs)
    print()


print('Loading: ', end='', flush=True)
progress_bar(1.0)


# First Name List = Quirk 22
first = ('Brainwashing', 'Explosion', 'Erasure', 'Half Cold-Half Hot',
         'Acid', 'Pop Off', 'Metal Tail', 'Gravity Control',
         'Laser Eyes', 'All for One', 'One for All', 'Rewind',
         'Warp Gate', 'Overhaul', 'Decay', 'Manifest', 'Fierce Wings',
         'HellFlame', 'Healing', 'Search', 'Transform', 'Creation')

# Last Name List = Hero Name 22
last = ('SenNo', 'Baku', 'Shokyo', 'AttaKai',
        'San', 'Poppu', 'KinZokU', 'Juryoku', 'Reza',
        'Tsuyoi', 'AkuNo', 'Jikan', 'ToraBeru', 'Yami',
        'Hikari', 'Heiwa', 'Yuki', 'Ajiwau', 'Yoshi',
        'Masa', 'Haru', 'Iyashi')

# Randomize names
while True:
    quirk = random.choice(first)
    heroname = random.choice(last)

    print("\n\n")
    print("~~~ Quirk ={}" .format(quirk), file=sys.stderr)
    print("~~~ Hero Name = {}" .format(heroname), file=sys.stderr)
    print("\n\n")

    # Play again screen or exit
    user_choice = input("\n\nPick Another One? (Press ENTER else n to quit)")
    if user_choice == "n":
        sys.exit()
