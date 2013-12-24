from Utilities.myLogger import logger
import config


def readStats():
    fileName = "Resources\\stats"
    f = open(config.get_main_dir() + "\\" + fileName)
    config.totalGames = int(f.readline())
    config.gamesWon = int(f.readline())
    config.gamesLost = int(f.readline())
    f.close()


def writeStats():
    fileName = "Resources\\stats"
    f = open(config.get_main_dir() + "\\" + fileName, "wb")
    print>>f, str(config.totalGames)
    print>>f, str(config.gamesWon)
    print>>f, str(config.gamesLost)
    f.close()