import zombiedice

class MyZombieBot:
    def __init__(self, name):
        self.name = name

    def turn(self, game_state):
        brains = 0
        shotguns = 0

        # Start rolling
        dice_roll_results = zombiedice.roll()
        
        # Keep rolling until 2 or more shotguns
        while dice_roll_results is not None:
            for die in dice_roll_results:
                if die['color'] and die['roll']:
                    if die['roll'] == 'brain':
                        brains += 1
                    elif die['roll'] == 'shotgun':
                        shotguns += 1
            
            if shotguns >= 2:
                break  # Stop and score

            dice_roll_results = zombiedice.roll()

# Add the bot to the game
zombies = [
    MyZombieBot(name='SafeBrainyBot'),
    zombiedice.examples.RandomCoinFlipZombie(name='RandomBot'),
]

# Start the game
zombiedice.runWebGui(zombies=zombies, numGames=1000)
