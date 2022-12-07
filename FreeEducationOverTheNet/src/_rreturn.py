import requests
from _rheaders import *
from _eoutput import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning

__all__ = ["RETURNCONTENTALL"]

class RETURNCONTENTALL(object):
    def __init__(self):
        self.__h = REQUESTHEADER()._PICK()
        self.__t = 17.2
        self.__e = FROMERROR.PRT()
    def __str__(self)->str:
        return "RETURN CONTENT - SUBPROCESS"
    def __call__(self):
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[PICKLED - DENIED]")
    def __repr__(self)->str:
        return RETURNCONTENTALL.__doc__
    def _BLOCKERRORS(self)->classmethod:
        requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    def _PICK(self,t:str)->str:
        self._BLOCKERRORS()
        rq = requests.Session()
        if rq:
            try:
                ct = rq.get(t,
                            verify=False,
                            stream=True,
                            allow_redirects=True,
                            timeout=self.__t,
                            headers=self.__h)
                if ct.status_code == 200:
                    if len(ct.text) != 0 and ct.text != "" and ct.text != " ":
                        rq.close()
                        return ct.text
                    else:
                        return "None"
                else:
                    return "None"
            except requests.exceptions.ConnectTimeout as rqec:
                pass
            except requests.exceptions.ConnectionError as rqee:
                pass
            except requests.exceptions.HTTPError as rqeh:
                pass
            except requests.exceptions.Timeout as rqet:
                pass
        else:
            return self.__e._pconnect()