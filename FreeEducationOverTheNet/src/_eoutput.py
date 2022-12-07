class SYSTEMERROR(object):
    __n = "[SYSTEM ERROR] - FATAL"
    def _psystem(self)->str:
        return "ERROR TYPE: %s"%self.__n
class FORMATERROR(object):
    __n = "[FORMAT ERROR] - GENERAL"
    def _pformat(self)->str:
        return "ERROR TYPE: %s"%self.__n
class CONNECTIONERROR(object):
    __n = "[CONNECTION ERROR] - IMPORTANT"
    def _pconnect(self)->str:
        return "ERROR TYPE: %s"%self.__n
class FILEERROR(object):
    __n = "[FILE ERROR] - GENERAL"
    def _pfile(self)->str:
        return "ERROR TYPE: %s"%self.__n
class SEARCHERROR(object):
    __n = "[SEARCH ERROR] - GENERAL"
    def _psearch(self)->str:
        return "ERROR TYPE: %s"%self.__n
class ESYSTEM(SYSTEMERROR):
    __n = "[SYSTEM ERROR] - FATAL"
class EFORMAT(FORMATERROR):
    __n = "[FORMAT ERROR] - GENERAL"
class ECONNECTION(CONNECTIONERROR):
    __n = "[CONNECTION ERROR] - IMPORTANT"
class EFILE(FILEERROR):
    __n = "[FILE ERROR] - GENERAL"
class ESEARCH(SEARCHERROR):
    __n = "[SEARCH ERROR] - GENERAL"
class FROMERROR:
    def PRT()->classmethod:
        t = type("ERROR TYPES",
                 (SYSTEMERROR,
                 FORMATERROR,
                 CONNECTIONERROR,
                 FILEERROR,
                 SEARCHERROR),
                 {})
        p = t()
        return p