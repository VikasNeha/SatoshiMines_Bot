baseURL = 'https://satoshimines.com/newplayer.php'
webElementTimeOut = 20
betAmount = None
bot = None

totalGames = None
gamesWon = None
gamesLost = None

import sys
import os
import imp


def main_is_frozen():
    return (hasattr(sys, "frozen") or  # new py2exe
            hasattr(sys, "importers")  # old py2exe
            or imp.is_frozen("__main__"))  # tools/freeze


def get_main_dir():
    if main_is_frozen():
        return os.path.dirname(os.path.dirname(sys.executable))
    return os.path.dirname(sys.argv[0])