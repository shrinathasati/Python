class Train:
    
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
        self.lst=[i for i in range(1,self.seats+1)]
    def getinfo(self):
        print(f"The train name is {self.name}")
        print(f"The fare of the train is Rs. {self.fare}")
    def bookticket(self):
        
        if(self.seats>0):
            print(f"your ticket is successfully booked and your seat no. is {self.lst[-1]}.")
            self.lst.pop(-1)
            self.seats-=1
        else:
            print("Seats are not available kindly try in tatkal mode.")
    def cancel(self,seat_no):
        self.lst.append(seat_no)
        print("your ticket has successfully cancelled.")
        self.seats+=1
    def getstatus(self):
        print(f"The no. of seats available are {self.seats}")
RajyaRani=Train("Rajyarani Express: 22161",105,600)
RajyaRani.getinfo()
RajyaRani.getstatus()
RajyaRani.bookticket()
RajyaRani.getstatus()
RajyaRani.cancel(600)
RajyaRani.getstatus()
RajyaRani.bookticket()
RajyaRani.getstatus()