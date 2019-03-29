import m1lib
import config

#This script intends to show the m1lib.py file in use.

if (m1lib.login(config.username, config.password) == True):
    m1lib.DebugCommand("I successfully ran the login function.")
    m1lib.tickerSearch(aum_min='0',aum_max='',pe_min='1',pe_max='',div_min='3',div_max='5',sector='Basic Materials',industry='Coal')
    #m1lib.selectAccount("Roth")
    #and your magic here... 😄

    #Some examples:
    #m1lib.orderPie(50, "Q1BTOjVRTjQyODE1LDYwODE5MCw2MDk5MTc%3D") #Purchases $50 from the listed pie
    #m1lib.orderPie(-50, "Q1BTOjVRTjM4MDYzLDU4MDEyNiw0NDQ2NDI%3D") #Sells $50 from the listed pie
    #m1lib.orderPV(50, config.accountType) #Purchases $50 from config.accountType
    #m1lib.orderPV(-50, "Individual") #Sells $50 from "Individual" account

    #dayReturn = m1lib.checkReturnsPV(config.accountType, "week") #day/week/month/year/all
    #print (dayReturn) #Returns float value
    #dayReturn = m1lib.checkReturnsPie(m1lib.getPID(config.accountType), "week")
    #print (dayReturn) #Returns same float value


    #AAPL = m1lib.searchTicker("aapl")
    #m1lib.initiateDeposit(50, "Roth", 2019)
    #m1lib.changeAutoInvest("Roth", option="off", amount='')
    #m1lib.changeAutoInvest("Individual", "all")
    #m1lib.changeAutoInvest("Roth", option="set", amount='10')
#End your file with...
#m1lib.closeSession()
