import gui
import os
import sys
import config
from Utilities.myLogger import logger
import SatoshiMines_Bot
from PageEvents import inputContent


# --- here goes your event handlers ---

def updateStats():
    mywin['txtTotalGames'].value = str(config.totalGames)
    mywin['txtGamesWon'].value = str(config.gamesWon)
    mywin['txtGamesLost'].value = str(config.gamesLost)
    winRate = round(float(config.gamesWon) * 100 / float(config.totalGames), 2)
    lostRate = round(float(config.gamesLost) * 100 / float(config.totalGames), 2)
    mywin['txtWinRate'].value = str(winRate) + " %"
    mywin['txtLostRate'].value = str(lostRate) + " %"


def load(evt):
    inputContent.readStats()
    mywin['statusbar'].text = 'Satoshi Mines Auto Play Bot. Powered by K Team !!!'
    updateStats()


def playSatoshiMines(evt):
    if not mywin['txtBetAmount'].value:
        gui.alert("Please enter Bet Amount")
        return
    try:
        float(mywin['txtBetAmount'].value)
    except ValueError:
        gui.alert("Please enter a valid Bet Amount")
        return
    config.betAmount = mywin['txtBetAmount'].value

    try:
        # gui.alert("Playing Satoshi Mines. \nPlease do not touch your keyboard or mouse.")
        mywin.minimized = True

        ret_value = SatoshiMines_Bot.playSatoshiMines()
        mywin.minimized = False
        updateStats()
        if ret_value == 'LOST':
            gui.alert("You Lost !!!")
        elif ret_value == 'WIN':
            gui.alert("Hurray !!! You Won !!!")
        else:
            gui.alert("There were some problems with the bot. Please report to developer.")
    except:
        logger.exception(sys.exc_info())
    finally:
        mywin.minimized = False

# --- gui2py designer generated code starts ---

#======== MAIN WINDOW ========#
gui.Window(name=u'SatoshiMines_Bot',
           title=u'Fiverr Order Scraping Tool',
           maximize_box=False, resizable=False, height='400px', left='173',
           top='58', width='550px', bgcolor=u'#E0E0E0', fgcolor=u'#000000',
           image=config.get_main_dir()+'/Resources/tile.bmp', tiled=True, )

#======== HEADER LABELS ========#
gui.Label(id=281, name='label_211_281', height='17', left='50', top='40',
          width='254', transparent=True,
          font={'size': 9, 'family': 'sans serif', 'face': u'Arial'},
          parent=u'SatoshiMines_Bot',
          text=u'Welcome to Satoshi Mines Auto Play Bot', )

gui.Label(id=1001, name='label_1001', height='17', left='50', top='80',
          width='131', parent=u'SatoshiMines_Bot',
          text=u'Bet Amount:', transparent=True, )

gui.TextBox(id=1003, name=u'txtBetAmount', height='23', left='170',
            sizer_align='center', top='80', width='150', bgcolor=u'#FFFFFF',
            editable=True, enabled=True, fgcolor=u'#000000',
            parent=u'SatoshiMines_Bot', transparent=True, value=u'0.5')

gui.Label(id=1002, name='label_1002', height='17', left='50', top='120',
          width='131', parent=u'SatoshiMines_Bot',
          text=u'Total Games Played:', transparent=True, )

gui.TextBox(id=1004, name=u'txtTotalGames', height='23', left='170',
            sizer_align='center', top='120', width='150', bgcolor=u'#FFFFFF',
            editable=False, enabled=False, fgcolor=u'#000000',
            parent=u'SatoshiMines_Bot', transparent=True,)

gui.Label(id=1005, name='label_1005', height='17', left='50', top='150',
          width='131', parent=u'SatoshiMines_Bot',
          text=u'Total Games Won:', transparent=True, )

gui.TextBox(id=1006, name=u'txtGamesWon', height='23', left='170',
            sizer_align='center', top='150', width='150', bgcolor=u'#FFFFFF',
            editable=False, enabled=False, fgcolor=u'#000000',
            parent=u'SatoshiMines_Bot', transparent=True,)

gui.Label(id=1007, name='label_1007', height='17', left='50', top='180',
          width='131', parent=u'SatoshiMines_Bot',
          text=u'Total Games Lost:', transparent=True, )

gui.TextBox(id=1008, name=u'txtGamesLost', height='23', left='170',
            sizer_align='center', top='180', width='150', bgcolor=u'#FFFFFF',
            editable=False, enabled=False, fgcolor=u'#000000',
            parent=u'SatoshiMines_Bot', transparent=True,)

gui.Label(id=1009, name='label_1009', height='17', left='50', top='210',
          width='131', parent=u'SatoshiMines_Bot',
          text=u'Win Rate:', transparent=True, )

gui.TextBox(id=1010, name=u'txtWinRate', height='23', left='170',
            sizer_align='center', top='210', width='150', bgcolor=u'#FFFFFF',
            editable=False, enabled=False, fgcolor=u'#000000',
            parent=u'SatoshiMines_Bot', transparent=True,)

gui.Label(id=1011, name='label_1011', height='17', left='50', top='240',
          width='131', parent=u'SatoshiMines_Bot',
          text=u'Lost Rate:', transparent=True, )

gui.TextBox(id=1012, name=u'txtLostRate', height='23', left='170',
            sizer_align='center', top='240', width='150', bgcolor=u'#FFFFFF',
            editable=False, enabled=False, fgcolor=u'#000000',
            parent=u'SatoshiMines_Bot', transparent=True,)

#======== DO ORDER SCRAPE BUTTON ========#
gui.Button(label=u'Play Satoshi Mines', name=u'btnPlaySatoshiMines', height='39',
           left='185', top='327', width='292', fgcolor=u'#000000',
           font={'size': 11, 'family': 'sans serif', 'face': u'Tahoma'},
           parent=u'SatoshiMines_Bot', transparent=True, )

gui.StatusBar(name='statusbar', parent=u'SatoshiMines_Bot', )

gui.Image(name='image_148', height='40', left='440', top='5', width='100',
          fgcolor=u'#000000',
          filename=config.get_main_dir()+'/Resources/python-powered.bmp',
          parent=u'SatoshiMines_Bot', stretch=False, transparent=False, border='static')

# --- gui2py designer generated code ends ---

# get a reference to the Top Level Window:
mywin = gui.get("SatoshiMines_Bot")

# assign your event handlers:
mywin.onload = load
# mywin['btnOutputDefault'].onclick = setDefaultOutputPaths
# mywin['btnBrowseOutputPath'].onclick = browseOutputPath
mywin['btnPlaySatoshiMines'].onclick = playSatoshiMines
#mywin['btnOpenOutput'].onclick = openOutputXLS

if __name__ == "__main__":
    # myLogger.setupLogging()
    mywin.show()
    gui.main_loop()