import tkinter as tk
from breezypythongui import EasyFrame, EasyCanvas

class GUI(EasyFrame):
  
    def __init__(self):


        self.flavorPrice = -1000 #Declaring default variables to set up the error message
        self.fillingPrice = -2000
        self.frostingPrice = -3000
        self.toppingPrice = -4000
        EasyFrame.__init__(self)
        self.flavorBox = self.addListbox(row = 0, column = 1, rowspan = 2) #Creating the area and the list selection for the flavors of the cake
        self.flavorBox.insert(0, "Chocolate")
        self.flavorBox.insert(1, "Yellow")
        self.flavorBox.insert(2, "Pineapple")
        self.flavorBox.insert(3, "Fudge")
        self.flavorBox.insert(4, "Lemon")
        self.flavorBox.insert(5, "Red Velvet")
        self.flavorBox.insert(6, "Pumpkin")
        self.addLabel(text = "Select a Flavor", row = 0, column = 0) #Selection button
        self.addButton(text = "Select Flavor", row = 2, column = 1, command = self.flavorCommand) #Command to add the assigned selection price to the total
    
        self.fillingBox = self.addListbox(row = 3, column = 1, rowspan = 2) #Building box to choose whether or not you want a filling
        self.fillingBox.insert(0, "Yes")
        self.fillingBox.insert(1, "No")
        self.addLabel(text = "Select Filling", row = 3, column = 0)
        self.addButton(text = "Select Filling", row = 5, column = 1, command = self.fillingCommand)#command to add either nothing or the filling price to the total

        self.frostingBox = self.addListbox(row = 6, column = 1, rowspan = 2) #Frosting choice list
        self.frostingBox.insert(0, "Buttercream")
        self.frostingBox.insert(1, "Chocolate Glaze")
        self.frostingBox.insert(2, "Meringue Buttercream")
        self.addLabel(text = "Select Icing", row = 6, column = 0) #button to select the frosting
        self.addButton(text = "Select Icing", row = 8, column = 1, command = self.frostingCommand) #command that adds the frosting selection total to the final total

        self.toppingBox = self.addListbox(row = 9, column = 1, rowspan = 2) #list for toppings options
        self.toppingBox.insert(0, "None")
        self.toppingBox.insert(1, "Rainbow Sprinkles")
        self.toppingBox.insert(2, "Glitter")
        self.toppingBox.insert(3, "Oreo Crumbs")
        self.addLabel(text = "Select Topping", row = 9, column = 0) #button for the topping selection
        self.addButton(text = "Select Topping", row = 11, column = 1, command = self.toppingCommand) #command to add the topping selection or none to the final total
        
        self.addButton(text = "Get Total", row = 13, column = 0, command = self.computeTotal)  #Get total button to be used after all other buttons are clicked
        self.outputField = self.addFloatField("", row = 13, column = 1)  #entry field for the total
        self.outputField.setPrecision(precision = 2) #two decimal places because it's in dollars

        python_image = tk.PhotoImage(file='./Untitled.gif')

        self.shapeCanvas = EasyCanvas(self)
        self.addCanvas(self.shapeCanvas, row = 14, column = 0, width = 300, height = 150, columnspan=2)
        self.shapeCanvas.drawImage(python_image,150,75)
        

    def computeTotal(self):
        if self.flavorPrice == -1000: #value defined at the beginning of the program.  Set to -1000 for an easy callback to the default
            self.messageBox(message = "You must click the Select Flavor button")  #These and the following three are error messages to be displayed
        else:                                                                     #if any of the buttons do not get selected
            self.outputField.setNumber(number = self.flavorPrice + self.fillingPrice + self.frostingPrice + self.toppingPrice) #if all of the buttons are selected then the calculation of price runs
        if self.fillingPrice == -2000:
            self.messageBox(message = "You must click the Select Filling button")  
        if self.frostingPrice == -3000:
            self.messageBox(message = "You must click the Select Icing button")
        if self.toppingPrice == -4000:
            self.messageBox(message = "You must click the Select Topping button")

    def flavorCommand(self):
        myCustomMessage = self.flavorBox.getSelectedItem()  #Assinging prices to all of the options
        if myCustomMessage == "Chocolate":
            self.flavorPrice = 1.0
        elif myCustomMessage == "Yellow":
            self.flavorPrice = 1.0
        elif myCustomMessage == "Pineapple":
            self.flavorPrice = 1.5
        elif myCustomMessage == "Fudge":
            self.flavorPrice = 1.5
        elif myCustomMessage == "Lemon":
            self.flavorPrice = 1.5
        elif myCustomMessage == "Red Velvet":
            self.flavorPrice = 2.0
        elif myCustomMessage == "Pumpkin":
            self.flavorPrice = 2.0
        else:
            self.messageBox(message = "You must select a flavor") #Error message if nothing is selected
    
    
    def fillingCommand(self):
        myCustomMessage = self.fillingBox.getSelectedItem() #assinging prices to the filling options 
        if myCustomMessage == "Yes":
            self.fillingPrice = 1.0
        elif myCustomMessage == "No":
            self.fillingPrice = 0.0
        else:
            self.messageBox(message = "You must select a filling")  #error message displayed if nothing is selected
        
    
    def frostingCommand(self):
        myCustomMessage = self.frostingBox.getSelectedItem() #assigning prices to the icings
        if myCustomMessage == "Buttercream":
            self.frostingPrice = 1.0
        elif myCustomMessage == "Chocolate Glaze":
            self.frostingPrice = 1.5
        elif myCustomMessage == "Meringue Buttercream":
            self.frostingPrice = 2.0
        else:
            self.messageBox(message = "You must select an icing")   #message displayed if nothing is selected

    def toppingCommand(self):
        myCustomMessage = self.toppingBox.getSelectedItem()  #assinging values to the toppings, or zero for none
        if myCustomMessage == "None":
            self.toppingPrice = 0.0
        if myCustomMessage == "Rainbow Sprinkles":
            self.toppingPrice = .50
        if myCustomMessage == "Oreo Crumbs":
            self.toppingPrice = .50
        if myCustomMessage == "Glitter":
            self.toppingPrice = .50
        else:
            self.messageBox(message = "You must select a topping")  #message displayed if nothing is selected
        
        
    

    

def main():
    GUIinstance = GUI()
    GUIinstance.mainloop()

if __name__ == "__main__":
    main()