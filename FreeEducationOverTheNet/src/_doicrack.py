from _rlibs import *

__all__ = ["DOICRACKER"]

class DOICRACKER(object):
    def __init__(self):
        self.__u = "https://sci-hub.ee/"
        self.__h = REQUESTHEADER()._PICK()
        self.__p = "html.parser"
        self.__t = 7.2
    def __str__(self)->str:
        return "DOI SEARCH AND CRACK - PROCESS"
    def __call__(self):
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[PICKLED - DENIED]")
    def __repr__(self)->str:
        return DOICRACKER.__doc__
    def _BLOCKERRORS(self)->classmethod:
        requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    def _RETURNCONTENT(self,t:str)->str:
        ct = RETURNCONTENTALL()._PICK(self.__u+t)
        if ct != "None":
            return ct
        else:
            return "None"
    def _SEARCH(self,
                trg:str,
                fc:str="div",
                tid:str="article",
                emb:str="iframe",
                lsr:str="src")->list:
        ct = self._RETURNCONTENT(trg)
        if ct != "None":
            bt = BeautifulSoup(ct,self.__p)
            dv = bt.find_all(fc,id=tid)
            for xp in dv:
                eid = xp.find_all(emb)
                for sp in eid:
                    fop = sp.get(lsr)
                    yield fop
        else:
            yield "None"
    def _LAUNCH(self,trg:str)->str:
        self._BLOCKERRORS()
        src = list(self._SEARCH(trg))
        if isinstance(src,list):
            if src[0] != "None":
                if len(src) == 1:
                    return src[0]
                else:
                    rtr = ""
                    for xl in range(len(src)):
                        rtr += str(src[xl])+"\n"
                    return rtr
            else:
                return "None"
        else:
            return "None"