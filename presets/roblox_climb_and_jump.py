delayAfterMouseMove = 0.5
delayAfterMouseClick = 0.5


# Run script as ADMIN, sometimes roblox doesn't react on click or react with big delay
def SlowClick(button, x=-1, y=-1):
    global delayAfterMouseMove, delayAfterMouseClick
    input_lib.MouseMove(x, y)
    input_lib.Sleep(delayAfterMouseMove)
    input_lib.MouseClick(button)
    input_lib.Sleep(delayAfterMouseClick)


def OpenSouvenirsTab():
    global SlowClick
    SlowClick('left', 1694, 314) # open inventory
    SlowClick('left', 307, 413) # open souvenirs tab


def UnequipAll():
    global SlowClick
    SlowClick('left', 727, 672)
    SlowClick('left', 733, 527)
    SlowClick('left', 727, 371)
    SlowClick('left', 549, 674)
    SlowClick('left', 550, 523)
    SlowClick('left', 548, 374)


def EquipFirstSixItems():
    global SlowClick
    for item in range(6):
        SlowClick('left', 934, 348)


def FilterSpeedItems():
    global SlowClick
    SlowClick('left', 964, 203) # filter menu
    SlowClick('left', 957, 330) # speed filter


def FilterGoldItems():
    global SlowClick
    SlowClick('left', 964, 203) # filter menu
    SlowClick('left', 957, 330) # gold filter


def CloseInventory():
    global SlowClick
    SlowClick('left', 1466, 200)


# Before run script:
# 1. Inventory should be closed
# 2. Souvenirs filter should be on "All"
# 3. You should stay opposite ladder and look at it
OpenSouvenirsTab()
UnequipAll()
FilterSpeedItems()
EquipFirstSixItems()
CloseInventory()

input_lib.KeyHold('w', 8) # climb for 8 seconds

OpenSouvenirsTab()
UnequipAll()
FilterGoldItems()
EquipFirstSixItems()
CloseInventory()

input_lib.KeyPress('space') # jump
input_lib.Sleep(10) # wait until lands
