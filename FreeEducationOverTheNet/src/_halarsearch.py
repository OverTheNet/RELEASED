from _rlibs import *

__all__ = ["HALARCHIVE"]

class HALARCHIVE(object):
    def __init__(self):
        self.__m = "https://hal.archives-ouvertes.fr"
        self.__u = "https://hal.archives-ouvertes.fr/search/index/?q="
        self.__q = "&docType_s=ART+OR+COMM+OR+OUV+OR+COUV+OR+DOUV+OR+OTHER+OR+UNDEFINED+OR+REPORT+OR+THESE+OR+HDR+OR+LECTURE&page="
        self.__h = REQUESTHEADER()._PICK()
        self.__p = "html.parser"
    def __str__(self)->str:
        return "HAL-ARCHIVE SEARCH - PROCESS"
    def __call__(self)->classmethod:
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[PICKLED - DENIED]")
    def __repr__(self)->str:
        return HALARCHIVE.__doc__
    def _BLOCKERRORS(self)->classmethod:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
    def _RETURNCONTENT(self,src:str,prg:str)->str:
        ct = RETURNCONTENTALL()._PICK(self.__u+str(src)+self.__q+str(prg))
        if ct != "None":
            return ct
        else:
            return "None"
    def _SEARCH(self,
                src:str,
                prg:str,
                spc:str="tr",
                sub:str="td",
                dpe:str="div",
                lpe:str="a",
                ppp:str="href")->list:
        ct = self._RETURNCONTENT(src,prg)
        if ct != "None":
            bt = BeautifulSoup(ct,self.__p)
            tr = bt.find_all(spc)
            for x in tr:
                try:
                    td = x.find_all(sub)
                    for d in td:
                        v = d.find_all(dpe)
                        for y in v:
                            a = y.find_all(lpe)
                            for h in a:
                                if "/h" in h.get(ppp):
                                    yield self.__m+str(h.get(ppp))
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