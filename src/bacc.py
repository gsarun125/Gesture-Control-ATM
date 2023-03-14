from pytz import timezone
from datetime import datetime

DAT_SEP = "-"

class BankAcc:
    def __init__(self):
        self.acnum=0
        self.pnnum=0
        self.acbal=0
        self.__read()

    def update_bal(self, acc_bal):
        file=open("data/acde.dat", 'w')
        self.acnum=7689_2312_1245_2441
        self.pnnum=1234
        self.acbal=acc_bal
        file.write(str(self.acnum) + "-" + str(self.pnnum) + "-" + str(self.acbal))
        file.close()

    def __read(self):
        file=open("data/acde.dat", 'r')
        dat_line=file.readline()
        dat=dat_line.rsplit('-')
        if(len(dat) > 0):
            self.acnum=int(dat[0])
            self.pnnum=int(dat[1])
            self.acbal=int(dat[2])
        file.close()

class TranDetails:
    def __read(self):
        file=open("data/trns.dat", 'r', encoding='utf-8')
        d=file.readlines()
        max=len(d)
        strt= 0 if max-5 < 0 else max-5
        dat=[]
        for i in range(strt, max):
            dat.append(d[i].strip())
        
        file.close()
        return dat
    
    def __write(self, dat):
        file=open("data/trns.dat", 'a', encoding='utf-8')
        file.write(dat)
        file.close()

    def transact(self, type, amt):
        self.__dt = datetime.now(timezone("Asia/Kolkata")).strftime('%d-%m-%Y [%I:%M:%S %p]')
        self.__ty = type
        self.__amt = amt

        data = self.__dt + ": " + self.__ty + " ₹" + str(self.__amt) + '\n'
        self.__write(data)

    def get_details(self):
        details = self.__read()
        return details
