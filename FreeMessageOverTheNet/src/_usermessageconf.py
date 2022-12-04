import time,string,random,hashlib
from datetime import date

__all__ = ["USERMESSAGECONF"]

class USERMESSAGECONF(object):
    def __init__(self):
        self.__db = "USER_DATABASE"
        self.__chainlist = []
        self.__messagelist = []
        self.__mainlist = []
    def __str__(self)->str:
        return "USER MESSAGE CONFIGURATION - SUBPROCESS"
    def __call__(self)->str:
        return
    def __getstate__(self):
        raise TypeError("[DENIED - PICKLED]")
    def __repr__(self)->classmethod:
        USERMESSAGECONF.__doc__
    def _CREATEUSERID(self)->str:
        rl = random.choices(string.ascii_lowercase,k=3)
        dl = random.choices(string.digits,k=5)
        ll = random.choices(string.ascii_lowercase,k=2)
        return "".join(str(x) for x in rl) + "".join(str(x) for x in dl) + "".join(str(x) for x in ll)
    def _SAVE(self,msx:str)->classmethod:
        us = self._CREATEUSERID()
        tm = time.time()
        dtt = date.today().strftime("%d/%m/%Y")
        cx = str(us)+str(tm)
        mp = hashlib.sha256(cx.encode()).hexdigest()
        self.__chainlist.append(mp)
        ms = {"USER-PROOF":self.__chainlist[-1],
              "USER":str(us),
              "MESSAGE":str(msx),
              "DATE":str(dtt)}
        self.__mainlist.append(hashlib.sha256(str(ms).encode()).hexdigest())
        self.__messagelist.append(ms)
        return self.__messagelist,self.__mainlist,self.__chainlist