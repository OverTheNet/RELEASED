import json

__all__ = ["USERAGENTGATHERING"]

class USERAGENTGATHERING(object):
    def __init__(self):
        self.__ua = "../content/useragents.json"
    def __str__(self)->str:
        return "USERAGENT LIST - SUBPROCESS"
    def __call__(self):
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[PICKLED - DENIED]")
    def __repr__(self)->str:
        return USERAGENTGATHERING.__doc__
    def _SIMPLEREAD(self,er:str="replace")->classmethod:
        with open(self.__ua,"r",errors=er) as rd:
            dt = rd.read()
            return dt
    def _PICK(self)->list:
        u = []
        d = self._SIMPLEREAD()
        j = json.loads(d)
        a = j["user_agents"]
        for i1 in a:
            for i2 in a[i1]:
                for i3 in a[i1][i2]:
                    for i4 in a[i1][i2][i3]:
                        if i4 != "" and i4 != " ":
                            u.append(i4)
                        else:
                            pass
        return u