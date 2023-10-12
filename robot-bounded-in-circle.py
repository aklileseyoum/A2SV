class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0, 0]
        add = True
        y = True
        for i in range(4):
            for each in instructions:
                if each == "G":
                    if add:
                        if y:
                            position[1] += 1
                        else:
                            position[0] += 1
                    else:
                        if y:
                            position[1] -= 1
                        else:
                            position[0] -= 1
                elif each == "L":
                    if add and y:
                        y = False
                    elif add and not y:
                        add = False
                        y = True
                    elif not add and y:
                        y = False
                    elif not add and not y:
                        add = True
                        y = True
                elif each == "R":
                    if add and y:
                        add = False
                        y = False
                    elif add and not y:
                        y = True
                    elif not add and y:
                        add = True
                        y = False
                    elif not add and not y:
                        add = False
                        y = True
        
        return position == [0,0]