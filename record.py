# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 17:54:50 2020

@author: lisa_
"""
class CarRecord: 
    def __init__ (self): 
        self.VehicleID = "" 
        self.Registration= "" 
        self.DateOfRegistration = None 
        self.EngineSize = 0
        self.PurchasePrice = 0.00 
        
ThisCar = CarRecord()
ThisCar.EngineSize = 2500
NewCar = CarRecord()
Car = [NewCar for i in range(100)]
Car[1].EngineSize = 2500

# class CarRecord: 
#     def __init__ (self): 
#         self.__VehicleID = "" 
#         self.__Registration= "" 
#         self.__DateOfRegistration = None 
#         self.__EngineSize = 0
#         self.__PurchasePrice = 0.00 
        
#     def SetVehicleID(self, ID):
#         self.__VehicleID = ID
    
#     def SetRegistration(self, r):
#         self.__Registration = r
        
#     def SetDateOfRegistration(self, d):
#         self.__DateOfRegistration = d
        
#     def SetEngineSize(self, e):
#         self.__EngineSize = e
        
#     def SetPurchasePrice(self, p):
#         self.__PurchasePrice = p
        
#     def GetVehicleID(self):
#         return self.__VehicleID
    
#     def GetRegistration(self):
#         return self.__Registration
    
#     def GetDateOfRegistration(self):
#         return self.__DateOfRegistration
    
#     def GetEngineSize(self):
#         return self.__EngineSize
    
#     def GetPurchasePrice(self):
#         return self.__PurchasePrice
    
#     def PrintDetails(self):
#         print(" VehicleID: ", self.GetVehicleID(), "\n",
#               "Registration: ", self.GetRegistration(), "\n",
#               "Date Of Registration: ", self.GetDateOfRegistration(), "\n",
#               "Engine Size: ", self.GetEngineSize(), "\n",
#               "Purchase Price: ", self.GetPurchasePrice(), "\n")
    
# ThisCar = CarRecord() 
# ThisCar.SetEngineSize(2500)
# NewCar = CarRecord() 
# Car= [NewCar for i in range(100)] 
# Car[1].SetEngineSize(2500)
# Car[1].PrintDetails()