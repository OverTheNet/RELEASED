class SYSTEMERROR(object):
    nm = " [ SYSTEM ERROR - FATAL / CHECK PROCESS ]"
    def print_sys(self):
        return "[ERROR: %s]"%self.nm
class FORMATERROR(object):
    nm = "[ FORMAT ERROR - GENERAL / CHECK PARAMETER ]"
    def print_frm(self):
        return "[ERROR: %s]"%self.nm
class CONNECTIONERROR(object):
    nm = "[ CONNECTION ERROR - IMPORTANT / CHECK CONNECTION ]"
    def print_con(self):
        return "[ERROR: %s]"%self.nm
class FILEERROR(object):
    nm = "[ FILE ERROR - GENERAL / CHECK FILE OR DIRECTORY ]"
    def print_fln(self):
        return "[ERROR: %s]"%self.nm
class E_SYSTEM(SYSTEMERROR):
    nm = "[SYSTEM ERROR - FATAL / CHECK PROCESS]"
class E_FORMAT(FORMATERROR):
    nm = "[FORMAT ERROR - GENERAL / CHECK PARAMETER]"
class E_CONNECTION(CONNECTIONERROR):
    nm = "[CONNECTION ERROR - IMPORTANT / CHECK CONNECTION]"
class E_FILE(FILEERROR):
    nm = "[FILE ERROR - GENERAL / CHECK FILE OR DIRECTORY]"    
class ERRORSLIST:
    def OUT():
        typ = type("ERROR TYPES",
                   (SYSTEMERROR,
                    FORMATERROR,
                    CONNECTIONERROR,
                    FILEERROR),
                   {})
        t = typ()
        return t