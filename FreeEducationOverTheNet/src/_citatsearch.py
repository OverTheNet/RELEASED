from _rlibs import *
import json

__all__ = ["CITATIONSYSEARCH"]

class CITATIONSYSEARCH(object):
    def __init__(self):
        self.__u = "https://api.crossref.org/works?query.bibliographic="
        self.__q = "&sort=score&rows="
        self.__h = REQUESTHEADER()._PICK()
        self.__p = "html.parser"
    def __str__(self)->list:
        return "CITATIONSY SEARCH - PROCESS"
    def __call__(self):
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[PICKLED - DENIED]")
    def __repr__(self):
        return CITATIONSYSEARCH.__doc__
    def _RETURNCONTENT(self,src:str,prg:str)->str:
        ct = RETURNCONTENTALL()._PICK(self.__u+str(src)+self.__q+str(prg))
        if ct != None:
            return ct
        else:
            return "None"
    def _LAUNCH(self,src:str,prg:str)->str:
        j = self._RETURNCONTENT(src,prg)
        exp = ""
        if j != "None":
            jsp = json.loads(j)
            msp = jsp["message"]["items"]
            if len(msp) == 1:
                exp += msp[0]["resource"]["primary"]["URL"]
            else:
                for xl in range(len(msp)):
                    try:
                        exp += msp[xl]["resource"]["primary"]["URL"]
                    except:
                        pass
            return exp
        else:
            return "None"