import os,sqlite3

rt = os.path.dirname(os.path.relpath((__file__)))

class DBSAVE(object):
    def __init__(self):
        self.__namedb = "MESSAGEFROMNET.db"
        self.__passdb = "backendpass.db"
        self.__block = "BLOCK_MESSAGE"
        self.__create = f"CREATE TABLE IF NOT EXISTS {self.__block} (keyword TEXT, chain TEXT, user TEXT)"
        self.__allselect = f"SELECT * FROM {self.__block}"
    def __str__(self)->str:
        return "DATABASE CONFIGURATION - SUBPROCESS"
    def __call__(self)->str:
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[DENIED - PICKLED]")
    def __repr__(self)->classmethod:
        return DBSAVE.__doc__
    def _CREATE(self)->classmethod:
        cn = sqlite3.connect(os.path.join(rt,self.__namedb))
        cr = cn.cursor()
        cr.execute(self.__create)
        cn.commit()
        cr.close()
    def _ADD(self,ms:str,bl:str,us:str)->classmethod:
        try:
            self._CREATE()
        except:
            pass
        cn = sqlite3.connect(os.path.join(rt,self.__namedb))
        cr = cn.cursor()
        cr.execute(f"INSERT INTO {self.__block} values (?,?,?)",(ms,bl,us))
        cn.commit()
        cr.close()
    def _REACH(self,bl:str)->classmethod:
        cn = sqlite3.connect(os.path.join(rt,self.__namedb))
        cr = cn.cursor()
        cr.execute(self.__allselect)
        dt = cr.fetchall()
        for i,cc in enumerate(dt):
            if str(bl) == str(dt[i][2]):
                cn.commit()
                cr.close()
                return dt[i][0],dt[i][1]
            else:
                cr.close()
    def _DELETE(self,bl:str)->classmethod:
        cn = sqlite3.connect(os.path.join(rt,self.__namedb))
        cr = cn.cursor()
        cr.execute(self.__allselect)
        dt = cr.fetchall()
        for i,cc in enumerate(dt):
            if str(bl) == str(dt[i][1]):
                cr.execute(f"DELETE FROM {self.__block} WHERE chain=?",(bl,))
                cn.commit()
                cr.close()
            else:
                cr.close()
    def _READ_DB(self)->classmethod:
        try:
            try:
                self._CREATE()
            except:
                pass
            cn = sqlite3.connect(os.path.join(rt,self.__namedb))
            cr = cn.cursor()
            cr.execute(self.__allselect)
            dt = cr.fetchall()
            cn.commit()
            cr.close()
            return dt
        except:
            pass
    def _READ_PASS(self)->classmethod:
        try:
            cn = sqlite3.connect(os.path.join(rt,self.__passdb))
            cr = cn.cursor()
            cr.execute(self.__allselect)
            dt = cr.fetchall()
            cn.commit()
            cr.close()
            return dt
        except:
            pass