from direct.showbase.ShowBase import ShowBase
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses
import math, random
from panda3d.core import *





class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setScene()

        self.SetCamera()

        fullCycle = 60

        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)

            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseballSeams(self.SpaceStation1, nickName, j, fullCycle, 2)

        
        #the following code is subject to change
        self.parent = self.loader.loadModel("./Assets/DroneDefender/DroneDefender.obj")

        radius = 200.0

        for i in range(25):
            theta = i * (2 * math.pi / 25)

            self.circleX = self.render.attachNewNode("circleX")
            self.circleX.setPos(radius * math.cos(theta), radius * math.sin(theta), 0)
            self.circleX.setColorScale(1.0, 0.0, 0.0, 1.0)
            self.parent.instanceTo(self.circleX)

            self.circleZ = self.render.attachNewNode("circleZ")
            self.circleZ.setPos(radius * math.cos(theta), 0, radius * math.sin(theta))
            self.circleZ.setColorScale(0.0, 1.0, 0.0, 1.0)
            self.parent.instanceTo(self.circleZ)

            self.circleY = self.render.attachNewNode("circleY")
            self.circleY.setPos(0, radius * math.cos(theta), radius * math.sin(theta))
            self.circleY.setColorScale(0.0, 0.0, 1.0, 1.0)
            self.parent.instanceTo(self.circleY)
        #the up above code is subject to change

    def setScene(self):
        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', "./Assets/Universe/Universe.jpg", (0, 0, 0), 10000)
        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet1', "./Assets/Planets/Planet1.jpg", (-6000, -3000, -800), 250)
        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet2', "./Assets/Planets/Planet2.jpg", (0, 6000, 0), 300)
        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet3', "./Assets/Planets/Planet3.jpg", (500, -5000, 200), 500)
        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet4', "./Assets/Planets/Planet4.jpg", (300, 6000, 500), 150)
        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet5', "./Assets/Planets/Planet5.jpg", (700, -2000, 100), 500)
        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet6', "./Assets/Planets/Planet6.jpg", (0, -900, -1400), 700)
        self.SpaceStation1 = spaceJamClasses.SpaceStation(self.loader, "./Assets/Space Station/spaceStation.egg", self.render, 'Space Station', "./Assets/Space Station/SpaceStation1_Dif2.png", (1500, 1000, -100), 40)
        self.Hero = spaceJamClasses.Spaceship(self.loader, self.taskMgr, self.accept,  "./Assets/Spaceships/Dumbledore.egg", self.render, 'Hero', "./Assets/Spaceships/spacejet_C.png", Vec3(1000, 1200, -50), 50)

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)

    def SetCamera(self):
        self.disableMouse()
        self.camera.reparentTo(self.Hero.modelNode)
        self.camera.setFluidPos(0, 1, 0)


app = MyApp()
app.run()