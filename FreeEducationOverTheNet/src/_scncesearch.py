from _rlibs import *

__all__ = ["SCIENCENEWSSEARCH"]

class SCIENCENEWSSEARCH(object):
    def __init__(self):
        self.__u = "https://www.sciencenewsforstudents.org/page/"
        self.__q = "?s="
        self.__h = REQUESTHEADER()._PICK()
        self.__p = "html.parser"
    def __str__(self)->str:
        return "SCIENCE NEWS SEARCH - PROCESS"
    def __call__(self):
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[PICKLED - DENIED]")
    def __repr__(self)->str:
        return SCIENCENEWSSEARCH.__doc__
    def _BLOCKERRORS(self)->classmethod:
        requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    def _RETURNCONTENT(self,src:str,prg:str)->str:
        ct = RETURNCONTENTALL()._PICK(self.__u+str(prg)+self.__q+str(src))
        if ct != "None":
            return ct
        else:
            return "None"
    def _SEARCH(self,
                src:str,
                prg:str,
                spx:str="section",
                cpx:str="river-no-sidebar__wrapper___dY6V_",
                hpx:str="h3",
                apx:str="a",
                ppp:str="href")->list:
        ct = self._RETURNCONTENT(src,prg)
        if ct != None:
            bt = BeautifulSoup(ct,self.__p)
            sp = bt.find_all(spx,class_=cpx)
            for xs in sp:
                try:
                    h = xs.find_all(hpx)
                    for xh in h:
                        a = xh.find_all(apx)
                        for xa in a:
                            hf = xa.get(ppp)
                            yield hf
                except:
                    pass
        else:
            yield "None"
    def _LAUNCH(self,src:str,prg:str)->str:
        self._BLOCKERRORS()
        sr = list(self._SEARCH(src,prg))
        if isinstance(sr,list):
            if sr[0] != "None":
                if len(sr) == 1:
                    return sr[0]
                else:
                    rtr = ""
                    for _l in range(len(sr)):
                        rtr += str(sr[_l])+"\n"
                    return rtr  
        