import numpy as np
dice_nums = (2,4,6,8,10,12,20,100)

def func(phrase):
    if "d" not in phrase:
        return -1
    else:
        value_index = phrase.index("d")
        if (len(phrase) == value_index + 1): # checking to make sure there is something after "d"
            return -1
        for i in phrase[:value_index]:
            if i not in "0123456789": #ensures that we can validly typecast the number of dice into an int

                return -1
        # get the number of times the die needs to be rolled
        num_rolls_string = phrase[:value_index]
        num_rolls = int(num_rolls_string)
        if num_rolls < 1:
            return -1

        #find out if there is a number to be added to the roll
        modifier_index = len(phrase)
        modifier_value = 0
        if "+" in phrase or "-" in phrase:
            modifier_index = phrase.index("+")
            for i in phrase[modifier_index+1:]:
                if i not in "0123456789":
                    return -1 #ensure that after this, there is nothing but numbers to add as a modifier
            modifier_value += int(phrase[modifier_index + 1:]) * 1 if "+" in phrase else -1
        for i in phrase[value_index+1:modifier_index]:
            if i not in "0123456789":
                return -1
        dice_type = int(phrase[value_index+1:modifier_index])
        if dice_type not in dice_nums:
            return -1
        else:
            sum = 0
            for i in range(num_rolls):
                rolled = np.random.randint(1, dice_type + 1)
                yield rolled
                sum += rolled
            yield modifier_value
            sum += modifier_value
            yield sum
    return 0


