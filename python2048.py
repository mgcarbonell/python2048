import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://play2048.co/')

htmlElem = browser.find_element_by_tag_name('body')
# linkElem = browser.find_element_by_link_text('Try again')

moves = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

time.sleep(1)

# while True:
#   htmlElem.send_keys(random.choice(moves))

def the_moves(moves):
  # game = browser.find_element_by_xpath("//div[contains(text(), 'game-message')]")
  # if game == True:
  if browser.find_elements_by_class_name('game-message') != 'Game over!':
    htmlElem.send_keys(random.choice(moves))
    time.sleep(0.25)
    the_moves(moves)
  else:
    browser.quit()
  

the_moves(moves)

  # if browser.find_element_by_xpath('//div[contains(text(), 'Game over!')]') == False
  # elif browser.find_element_by_class_name('game-message') == browser.find_element_by_class_name('game-message game-over'):
  # elif browser.find_element_by_class_name('game-message') == 'Game over!':
    # time.sleep(3)
    # browser.find_element_by_class_name('keep-playing-button').click()
    # linkElem.click()
    # browser.switchTo().activeElement()
    # browser.find_element_by_link_text('Try again').click()
    # browser.find_element_by_css_selector('a.retry-button').click()

# htmlElem.send_keys(random.choice(moves))
# htmlElem.send_keys(Keys.DOWN)
# htmlElem.send_keys(Keys.LEFT)
# htmlElem.send_keys(Keys.RIGHT)


# <div class="game-container">
# <div class="grid-container">
# <div class="grid-cell"></div>
# <div class="tile-inner">2</div>
# <div class="tile-inner">4</div>
# <div class="tile tile-16 tile-position-4-4"><div class="tile-inner">16</div></div>

# <div class="game-message game-over"><p>Game over!</p><div class="lower"><a class="keep-playing-button">Keep going</a>
# <a class="retry-button">Try again</a></div></div>

# Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
# <div class="game-message game-over">
# <p>Game over!</p><div class="lower">
# <a class="keep-playing-button">Keep going</a>
# browser.find_element_by_class_name('retry-button').click()
# <a class="retry-button">Try again</a></div></div>