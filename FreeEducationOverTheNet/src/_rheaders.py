from _uagents import *
import random,os

__all__ = ["REQUESTHEADER"]

class REQUESTHEADER(object):
    def __init__(self):
        self.__u = random.choice(USERAGENTGATHERING()._PICK())
        self.__f = "/refererrequests.txt"
        self.__w = random.choice(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
        self.__m = random.choice(["Jan","Feb","Mar","Apr","Aug","Sep","Oct","Nov","Dec"])
        self.__a = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        self.__h = {}
    def __str__(self)->str:
        return "REQUEST HEADER - SUBPROCESS"
    def __call__(self):
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[PICKLED - DENIED]")
    def __repr__(self)->str:
        return REQUESTHEADER.__doc__
    def _REFERERREAD(self,er:str="replace")->str:
        r = []
        dr = os.path.dirname(__file__)
        mfl = dr+self.__f
        with open(mfl,"r",errors=er) as rd:
            for ir in rd:
                try:
                    x = ir.strip()
                    r.append(x)
                except:
                    pass
        if len(r) != 0 :
            return random.choice(r)
        else:
            return "None"
    def _RANDOMVALUES(self)->list:
        rl = [random.randint(1,30),
              random.randint(2000,2022),
              random.randint(10,23),
              random.randint(10,50),
              random.randint(10,55),
              random.randint(100,155)]
        for _l in rl:
            yield _l
    def _PICK(self)->dict:
        vl = list(self._RANDOMVALUES())
        rf = self._REFERERREAD()
        self.__h["User-Agent"] = str(self.__u)
        self.__h["Accept"] = str(self.__a)
        self.__h["Connection"] = "Keep-Alive"
        self.__h["Keep-Alive"] = str(vl[-1])
        if vl != "None":
            self.__h["Referer"] = str(rf)
        else:
            self.__h["Referer"] = "https://google.com"
        self.__h["Date"] = f"{self.__w}, {vl[0]} {self.__m} {vl[1]} {vl[2]}:{vl[3]}:{vl[4]} GMT"
        return self.__h
        
