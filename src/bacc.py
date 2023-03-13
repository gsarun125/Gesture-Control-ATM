DAT_SEP = "-"

class BankAcc:
    def __init__(self):
        self.__dat=None
        self.acnum=0
        self.pnnum=0
        self.acbal=0
        self.__read()

    def update_bal(self, acc_bal):
        self.__dat = open("data/acde.dat", 'w')
        self.acnum=7689_2312_1245_2441
        self.pnnum=1234
        self.acbal=acc_bal
        self.__dat.write(str(self.acnum) + "-" + str(self.pnnum) + "-" + str(self.acbal))
        self.__dat.close()

    def __read(self):
        self.__dat = open("data/acde.dat", 'r')
        dat_line=self.__dat.readline()
        dat=dat_line.rsplit('-')
        if(len(dat) > 0):
            self.acnum=int(dat[0])
            self.pnnum=int(dat[1])
            self.acbal=int(dat[2])
        self.__dat.close()