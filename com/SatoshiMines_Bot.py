from PageEvents.satoshiEvents import SatoshiEvents
from PageEvents import inputContent
import config
from Utilities.myLogger import logger
import sys
import time


def playSatoshiMines():
    try:
        if config.bot is None:
            config.bot = SatoshiEvents()
            config.bot.navigate(config.baseURL)
        print config.bot.driver.current_url
        ret_value = config.bot.play()
        # config.bot.destroy()
        inputContent.writeStats()
        return ret_value
    except:
        logger.exception(sys.exc_info())
