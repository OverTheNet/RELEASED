__all__ = ["SAVERETURN"]

class SAVERETURN(object):
    def __init__(self,f:str):
        self.__f = f
        self.__d = None
    def __str__(self)->str:
        return "SAVE FROM RETURN - SUBPROCESS"
    def __call__(self):
        return
    def __getstate__(self)->classmethod:
        raise TypeError["[PICKLED - DENIED]"]
    def __repr__(self)->str:
        return SAVERETURN.__doc__
    def _TRANSFER(self,tx:str)->classmethod:
        self.__d.write(tx)
    def __enter__(self,er:str="replace")->classmethod:
        self.__d = open(self.__f,"wb",errors=er)
        return self
    def __exit__(self,
                 ety:classmethod,
                 evl:classmethod,
                 etb:classmethod)->classmethod:
        self.__d.close()