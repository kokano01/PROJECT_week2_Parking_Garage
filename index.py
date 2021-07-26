class ParkingGarage():
    def __init__(self):
        self.tickets = [0,0,0,0,0,0]
        # self.parking_space = []
        # self.current_ticket = {}
    

    def availTix(self):
        print("Parking spots:", self.tickets)
        try:
            ticket = int(input("\nINDICATORS: 0 = open; 1 = occupied; 2 = paid. \nPlease enter an available ticket number: (1 - 6)     "))
            if self.tickets[ticket-1] == 0:
                    self.tickets[ticket-1] = 1
                    print(self.tickets)
                
            elif self.tickets[ticket-1] == 1 or 2:
                print(f"Ticket number {ticket} is already taken. Please choose an available ticket number.")
        except (SyntaxError, ValueError, IndexError):
                print("You didn't enter a valid number")
        
       

    def payTix(self):
    # ------- How to add "paid" to an index in the ticket list--------
        pymtNum = int(input("\nPlease enter ticket number to pay for:     "))
        if self.tickets[pymtNum-1] == 1:
            try:
                pymt2 = int(input("Enter payment amount:    "))                
                self.tickets[pymtNum-1] = 2
                print(" Your ticket has been paid. You have 15 minutes to depart. Thank You!")
            except (SyntaxError, ValueError, IndexError):
                print("You didn't enter a valid number")
        elif self.tickets[pymtNum-1] == 0 or 2:
            print("Either you have already paid for it, or this is not your number. Please try again.")


    def leavePG(self):
        print(self.tickets)
        try:
            reticket = int(input("\nPlease enter your ticket number to leave: (1 - 6)    "))
            # ----CHECK ---- if ticket is paid, then change the value to 0.        
            if self.tickets[reticket-1] == 0:
                print(f"Parking number {reticket} is already vacant. Please enter the correct ticket number.")
            elif self.tickets[reticket-1] == 1:
                x = input("You have not paid yet. Would you like to pay right now? (yes/no)  ")
                if x.lower() == "yes":
                    self.payTix()
                elif x.lower() == "no":
                    self.quitTix()
                elif x.lower() not in ("yes", "no"):
                    print("invalid input")
            elif self.tickets[reticket-1] == 2:
                print("\nHave a nice day!")
                self.tickets[reticket-1] = 0
                print(self.tickets)
        except (SyntaxError, ValueError, IndexError):
                print("You didn't enter a valid number")

    def quitTix(self):
        print(self.tickets)
        print("\nCome back soon!")
    

    def run(self):
        while True:
            task = input("\nWelcome! (take/pay/leave/quit)   ")
            if task.lower() == "take":
                self.availTix()
            elif task.lower() == "quit":
                self.quitTix()
            elif task.lower() == "pay":
                self.payTix()
            elif task.lower() == "leave":
                self.leavePG()
            elif task.lower() not in ("take", "quit", "pay", "leave"):
                print("===========INVALID INPUT============")
                print("Please enter one of the options.")

tix = ParkingGarage()
tix.run()
