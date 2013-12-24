from selenium.common.exceptions import ElementNotVisibleException
from webpageEvents import WebpageEvents
from Utilities.constants import IDMODE
import config
import random
import time


class SatoshiEvents(WebpageEvents):
    def __init__(self):
        super(SatoshiEvents, self).__init__()

    def destroy(self):
        super(SatoshiEvents, self).destroy()

    def enterBetAmount(self):
        self.enterText(IDMODE.ID, "bet", config.betAmount)

    def clickPlayButton(self):
        self.findElement(IDMODE.ID, "start_game").click()

    def play(self):
        self.enterBetAmount()
        # self.findElement(IDMODE.ID, "mines_5").click()
        self.clickPlayButton()

        board = self.findElement(IDMODE.CLASS, "board")
        tiles = board.find_elements_by_tag_name("li")
        time.sleep(2)
        tileRandomList = random.sample(range(0, 24), 2)

        bombFound = False
        for tileToClick in tileRandomList:
            print "----"
            print tileToClick
            while True:
                try:
                    tiles[tileToClick].click()
                    break
                except ElementNotVisibleException:
                    continue
            messages = self.findElement(IDMODE.CLASS, "messages")
            if 'Game over' in messages.text:
                bombFound = True
                break
        config.totalGames += 1
        if bombFound:
            print "Bomb Found"
            config.gamesLost += 1
            return 'LOST'
        else:
            self.findElement(IDMODE.CLASS, "cashout").click()
            print "cashout"
            config.gamesWon += 1
            return 'WIN'

