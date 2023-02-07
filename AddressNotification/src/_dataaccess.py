import pandas as pd
import os

rt = os.path.dirname(os.path.relpath((__file__)))

class DATAGATHERING(object):
    def __init__(self):
        self.__dt = os.path.join(rt,"deprem_input.csv")
    def __str__(self):
        return "DATA GATHERING - SUBPROCESS"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[DENIED]")
    def __repr__(self):
        return DATAGATHERING.__doc__
    def _READFILE(self):
        return pd.read_csv(self.__dt)
    def _SPEC(self,nminit:str):
        return self._READFILE()[nminit]
