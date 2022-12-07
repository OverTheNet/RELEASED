from _rlibs import *

__all__ = ["LIBGENSEARCH"]

class LIBGENSEARCH(object):
    def __init__(self):
        self.__u = "https://libgen.is/scimag/?q="
        self.__q = "&page="
        self.__h = REQUESTHEADER()._PICK()
        self.__p = "html.parser"
    def __str__(self)->str:
        return "LIBGEN SEARCH - PROCESS"
    def __call__(self)->classmethod:
        return
    def __getstate__(self):
        raise TypeError("[PICKLED - DENIED]")
    def __repr__(self)->str:
        return LIBGENSEARCH.__doc__
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
                tbl:str="table",
                clp:str="catalog",
                spc:str="a",
                ppp:str="href")->list:
        ct = self._RETURNCONTENT(src,prg)
        if ct != "None":
            bt = BeautifulSoup(ct,self.__p)
            t = bt.find_all(tbl,class_=clp)
            for xt in t:
                try:
                    a = xt.find_all(spc)
                    for xa in a:
                        if "https://" in xa.get(ppp) or "http://" in xa.get(ppp):
                            yield xa.get(ppp)
                except:
                    pass
        else:
            return "None"
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