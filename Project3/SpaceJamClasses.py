from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task.Task import TaskManager
from typing import Callable
from direct.task import Task


#class MyApp(ShowBase):
    
class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Universe(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)



class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)


class Spaceship(ShowBase):
    def __init__(self, loader: Loader, taskMgr: TaskManager, accept: Callable[[str, Callable]], modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.taskMgr = taskMgr
        self.accept = accept
        self.render = render

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        self.SetKeyBindings()



    #errors aware of the camera moves in odd ways when you move the player around too much unsure of a easy fix possibly need to use Quaternions
    def SetKeyBindings(self):
        # All of our key binding for our spaceship's movement.
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])

        self.accept('a', self.LeftTurn, [1])
        self.accept('a-up', self.LeftTurn, [0])

        self.accept('d', self.RightTurn, [1])
        self.accept('d-up', self.RightTurn, [0])

        self.accept('w', self.PitchForward, [1])
        self.accept('w-up', self.PitchForward, [0])

        self.accept('s', self.PitchBack, [1])
        self.accept('s-up', self.PitchBack, [0])

        self.accept('q', self.RollLeft, [1])
        self.accept('q-up', self.RollLeft, [0])

        self.accept('e', self.RollRight, [1])
        self.accept('e-up', self.RollRight, [0])


    
    def Thrust(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.ApplyThrust, 'forward-thrust')
        else:
            self.taskMgr.remove('forward-thrust')

    def ApplyThrust(self, task):
        rate = 5
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont

    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.ApplyLeftTurn, 'left-turn')
        else:
            self.taskMgr.remove('left-turn')

    def ApplyLeftTurn(self, task):
        # Half a degree every frame.
        rate = 0.5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont


    def RightTurn(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.ApplyRightTurn, 'right-turn')
        else:
            self.taskMgr.remove('right-turn')

    def ApplyRightTurn(self, task):
        rate = 0.5
        self.modelNode.setH(self.modelNode.getH() - rate)
        return Task.cont


    def PitchForward(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.ApplyPitchForward, 'pitch-forward')
        else:
            self.taskMgr.remove('pitch-forward')

    def ApplyPitchForward(self, task):
        rate = 0.5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return Task.cont

    def PitchBack(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.ApplyPitchBackward, 'pitch-backward')
        else:
            self.taskMgr.remove('pitch-backward')

    def ApplyPitchBackward(self, task):
        rate = 0.5
        self.modelNode.setP(self.modelNode.getP() - rate)
        return Task.cont

    def RollLeft(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.ApplyRollLeft, 'roll-left')
        else:
            self.taskMgr.remove('roll-left')

    def ApplyRollLeft(self, task):
        rate = 0.5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont

    def RollRight(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.ApplyRollRight, 'roll-right')
        else:
            self.taskMgr.remove('roll-right')

    def ApplyRollRight(self, task):
        rate = 0.5
        self.modelNode.setR(self.modelNode.getR() - rate)
        return Task.cont
    




class Drone(ShowBase):
    # how many drones have been spawned.
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
