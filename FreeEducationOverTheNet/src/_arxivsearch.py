from _rlibs import *

__all__ = ["ARXIVSEARCH"]

class ARXIVSEARCH(object):
    def __init__(self):
        self.__u = "https://arxiv.org/search/?query="
        self.__q = "&searchtype=all&start="
        self.__h = REQUESTHEADER()._PICK()
        self.__p = "html.parser"
    def __str__(self)->str:
        return "ARXIV SEARCH - PROCESS"
    def __call__(self):
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[PICKLED - DENIED]")
    def __repr__(self)->str:
        return ARXIVSEARCH.__doc__
    def _BLOCKERRORS(self)->classmethod:
        requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    def _RETURNCONTENT(self,src:str,prg:str):
        ct = RETURNCONTENTALL()._PICK(self.__u+str(src)+self.__q+str(prg))
        if ct != "None":
            return ct
        else:
            return "None"
    def _SEARCH(self,
                src:str,
                prg:str,
                spx:str="ol",
                clp:str="breathe-horizontal",
                plx:str="li",
                arx:str="arxiv-result",
                apx:str="a",
                ppx:str="p",
                tpx:str="title is-5 mathjax",
                ppp:str="href")->list:
        ct = self._RETURNCONTENT(src,prg)
        if ct != "None":
            bt = BeautifulSoup(ct,self.__p)
            olx = bt.find_all(spx,class_=clp)
            for ox in olx:
                try:
                    li = ox.find_all(plx,class_=arx)
                    for ix in li:
                        a = ix.find_all(apx)
                        for ax in a:
                            hr = ax.get(ppp)
                            if hr != None:
                                if "https://" in hr or "http://" in hr:
                                    if "pdf" in hr:
                                        yield hr
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                except:
                    pass
        else:
            yield "None"     
    def _LAUNCH(self,src:str,prg:str)->str:
        sr = list(self._SEARCH(src,prg))
        if isinstance(sr,list):
            if sr[0] != "None":
                if len(sr) == 1:
                    return sr[0]
                else:
                    rtr = ""
                    for xl in range(len(sr)):
                        rtr += str(sr[xl])+"\n"
                    return rtr  