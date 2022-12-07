import streamlit as st
from _doicrack import *
from _eoutput import *
from _scncesearch import *
from _libgnsearch import *
from _arxivsearch import *
from _citatsearch import *
from _halarsearch import *
from _htmlstyle import *

class FREEOVERTHENET(object):
    def __init__(self):
        self.__p = "OvRThNt"
        self.__l = "wide"
        self.__s = "expanded"
        self.__e = FROMERROR.PRT()
    def __str__(self)->str:
        return "OVERTHENET - STREAMLIT"
    def __call__(self):
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[PICKLED - DENIED]")
    def __repr__(self)->str:
        FREEOVERTHENET.__doc__
    def _CONF(self)->classmethod:
        st.set_page_config(page_title=self.__p,
                           layout=self.__l,
                           initial_sidebar_state=self.__s,
                           page_icon="^-^",
                           menu_items={"About":"# FREEDOM OF EDUCATION - OVERTHENET"})
    def _RETURNBANNER(self)->classmethod:
        st.subheader("FREEDOM IN MATRIX - OVERTHENET COMMUNITY")
        st.caption("> The instruments of darkness tell us truths")
        st.code(HTMLRETURN()._RETURNBANNER())
    def _PARAMETERCONTROL(self,tx:str)->bool:
        if tx != "" and tx != " " and tx != None:
            return True
        else:
            return False
    def _CHECKBOX(self)->classmethod:
        ml = st.selectbox("OPERATION TYPES",
                          ("DOI CRACKER",
                           "ALL SEARCH",
                           "LIBGEN SEARCH",
                           "ARXIV SEARCH",
                           "CITATIONSY SEARCH",
                           "HAL SEARCH",
                           "SCIENCE-NEWS SEARCH"))
        return ml
    def _PROCESS(self)->classmethod:
        st.subheader("OPERATIONS - LIBRARIES AND CRACKER")
        sx = self._CHECKBOX()
        if sx == "DOI CRACKER":
            tx = st.text_area("TYPE DOI-ARTICLE URL TO CRACK",
                              help="DOI CRACKER")
            fn = st.button("SEARCH")
            if fn:
                try:
                    ppt = self._PARAMETERCONTROL(tx)
                    if ppt:
                        with st.spinner("PLEASE WAIT"):
                            st.info("[SEARCHING] > PLEASE WAIT FOR SEARCHING")
                            sr = DOICRACKER()._LAUNCH(str(tx))
                            if sr != None and sr != "None" and sr != "" and sr != " ": 
                                st.success("[FOUND] > PLEASE SCROLL THE PAGE DOWN")
                                st.code(sr)
                            else:
                                st.code("COULD NOT FOUND - [MAYBE NEVER EXISTED] / TRY ANOTHER")
                    else:
                        st.warning("[WARNING] - EMPTY PARAMETER")
                        pass
                except:
                    st.code(str(self.__e._psearch()))
                    st.warning("IF YOU HAVE AN ERROR, YOU CAN TRY ANOTHER URL OR GENERAL SEARCH OPTIONS")
        elif sx == "ALL SEARCH":
            tx = st.text_area("TYPE TITLE TO SEARCH",
                              help="LIBGEN LIBRARY")
            cn = st.slider("SELECT POWER OF SEARCH",
                               1,24,1)
            fn = st.button("SEARCH")
            if fn:
                try:
                    ppt = self._PARAMETERCONTROL(tx)
                    if ppt:
                        with st.spinner("PLEASE WAIT"):
                            pp = ""
                            st.info("[SEARCHING] > PLEASE WAIT FOR SEARCHING")
                            for _l in range(int(cn)):
                                try:
                                    dt = LIBGENSEARCH()._LAUNCH(str(tx).lower(),str(int(_l)))
                                    if dt != "" and dt != " ":
                                        pp += dt+"\n"
                                    else:
                                        pass
                                except:
                                    pass
                                try:
                                    at = ARXIVSEARCH()._LAUNCH(str(tx).lower(),str(int(_l)))
                                    if at != "" and at != " ":
                                        pp += at+"\n"
                                    else:
                                        pass
                                except:
                                    pass
                                try:
                                    tt = CITATIONSYSEARCH()._LAUNCH(str(tx).lower(),str(int(_l)))
                                    if tt != "" and tt != " ":
                                        pp += tt+"\n"
                                    else:
                                        pass
                                except:
                                    pass
                                try:
                                    ht = HALARCHIVE()._LAUNCH(str(tx).lower(),str(int(_l)))
                                    if ht != "" and ht != " ":
                                        pp += ht+"\n"
                                    else:
                                        pass
                                except:
                                    pass
                                try:
                                    ss = SCIENCENEWSSEARCH()._LAUNCH(str(tx).lower(),str(int(_l)))
                                    if ss != "" and ss != " ":
                                        pp += ss+"\n"
                                    else:
                                        pass
                                except:
                                    pass
                            if pp != "":
                                st.success("[FOUND] > PLEASE SCROLL THE PAGE DOWN")
                                st.download_button("DOWNLOAD RESULT",pp)
                                st.code(pp)
                            else:
                                st.code("COULD NOT FOUND - [MAYBE NEVER EXISTED]")
                    else:
                        st.warning("[WARNING] - EMPTY PARAMETER")
                        pass
                except:
                    st.code(str(self.__e._psearch()))
                    st.warning("IF YOU HAVE AN ERROR, YOU CAN REDUCE THE SEARCH POWER - [JUST TRY AGAIN]")
        elif sx == "LIBGEN SEARCH":
            tx = st.text_area("TYPE TITLE TO SEARCH",
                              help="LIBGEN LIBRARY")
            cn = st.slider("SELECT POWER OF SEARCH",
                               1,24,1)
            fn = st.button("SEARCH")
            if fn:
                try:
                    ppt = self._PARAMETERCONTROL(tx)
                    if ppt:
                        with st.spinner("PLEASE WAIT"):
                            pp = ""
                            st.info("[SEARCHING] > PLEASE WAIT FOR SEARCHING")
                            for _l in range(int(cn)):
                                try:
                                    dt = LIBGENSEARCH()._LAUNCH(str(tx).lower(),str(int(_l)))
                                    if dt != "" and dt != " ":
                                        pp += dt+"\n"
                                    else:
                                        pass
                                except:
                                    pass
                            if pp != "":
                                st.success("[FOUND] > PLEASE SCROLL THE PAGE DOWN")
                                st.download_button("DOWNLOAD RESULT",pp)
                                st.code(pp)
                            else:
                                st.code("COULD NOT FOUND - [MAYBE NEVER EXISTED]")
                    else:
                        st.warning("[WARNING] - EMPTY PARAMETER")
                        pass
                except:
                    st.code(str(self.__e._psearch()))
                    st.warning("IF YOU HAVE AN ERROR, YOU CAN REDUCE THE SEARCH POWER - [JUST TRY AGAIN]")
        elif sx == "ARXIV SEARCH":
            tx = st.text_area("TYPE TITLE TO SEARCH",
                              help="ARXIV LIBRARY")
            cn = st.slider("SELECT POWER OF SEARCH",
                               1,24,1)
            fn = st.button("SEARCH")
            if fn:
                try:
                    ppt = self._PARAMETERCONTROL(tx)
                    if ppt:
                        with st.spinner("PLEASE WAIT"):
                            pp = ""
                            st.info("[SEARCHING] > PLEASE WAIT FOR SEARCHING")
                            for _l in range(int(cn)):
                                try:
                                    dt = ARXIVSEARCH()._LAUNCH(str(tx).lower(),str(int(_l)))
                                    if dt != "" and dt != " ":
                                        pp += dt+"\n"
                                    else:
                                        pass
                                except:
                                    pass
                            if pp != "":
                                st.success("[FOUND] > PLEASE SCROLL THE PAGE DOWN")
                                st.download_button("DOWNLOAD RESULT",pp)
                                st.code(pp)
                            else:
                                st.code("COULD NOT FOUND - [MAYBE NEVER EXISTED]")
                    else:
                        st.warning("[WARNING] - EMPTY PARAMETER")
                        pass
                except:
                    st.code(str(self.__e._psearch()))
                    st.warning("IF YOU HAVE AN ERROR, YOU CAN REDUCE THE SEARCH POWER - [JUST TRY AGAIN]")
        elif sx == "CITATIONSY SEARCH":
            tx = st.text_area("TYPE TITLE TO SEARCH",
                              help="CITATIONSY LIBRARY")
            cn = st.slider("SELECT POWER OF SEARCH",
                               2,24,1)
            fn = st.button("SEARCH")
            if fn:
                try:
                    ppt = self._PARAMETERCONTROL(tx)
                    if ppt:
                        with st.spinner("PLEASE WAIT"):
                            pp = ""
                            st.info("[SEARCHING] > PLEASE WAIT FOR SEARCHING")
                            for _l in range(int(cn)):
                                try:
                                    dt = CITATIONSYSEARCH()._LAUNCH(str(tx).lower(),str(int(_l)))
                                    if dt != "" and dt != " ":
                                        pp += dt+"\n"
                                    else:
                                        pass
                                except:
                                    pass
                            if pp != "":
                                print(pp)
                                st.success("[FOUND] > PLEASE SCROLL THE PAGE DOWN")
                                st.download_button("DOWNLOAD RESULT",pp)
                                st.code(pp)
                            else:
                                st.code("COULD NOT FOUND - [MAYBE NEVER EXISTED] / TRY [INCREASE] SEARCH POWER")
                    else:
                        st.warning("[WARNING] - EMPTY PARAMETER")
                        pass
                except:
                    st.code(str(self.__e._psearch()))
                    st.warning("IF YOU HAVE AN ERROR, YOU CAN REDUCE THE SEARCH POWER - [JUST TRY AGAIN]")
        elif sx == "HAL SEARCH":
            tx = st.text_area("TYPE TITLE TO SEARCH",
                              help="HAL LIBRARY")
            cn = st.slider("SELECT POWER OF SEARCH",
                               1,24,1)
            fn = st.button("SEARCH")
            if fn:
                try:
                    ppt = self._PARAMETERCONTROL(tx)
                    if ppt:
                        with st.spinner("PLEASE WAIT"):
                            pp = ""
                            st.info("[SEARCHING] > PLEASE WAIT FOR SEARCHING")
                            for _l in range(int(cn)):
                                try:
                                    dt = HALARCHIVE()._LAUNCH(str(tx).lower(),str(int(_l)))
                                    pp += dt+"\n"
                                except:
                                    pass
                            if pp != "":
                                st.success("[FOUND] > PLEASE SCROLL THE PAGE DOWN")
                                st.download_button("DOWNLOAD RESULT",pp)
                                st.code(pp)
                            else:
                                st.code("COULD NOT FOUND - [MAYBE NEVER EXISTED]")
                    else:
                        st.warning("[WARNING] - EMPTY PARAMETER")
                        pass
                except:
                    st.code(str(self.__e._psearch()))
                    st.warning("IF YOU HAVE AN ERROR, YOU CAN REDUCE THE SEARCH POWER - [JUST TRY AGAIN]")
        elif sx == "SCIENCE-NEWS SEARCH":
            tx = st.text_area("TYPE TITLE TO SEARCH",
                              help="SCIENCE-NEWS LIBRARY")
            ppt = self._PARAMETERCONTROL(tx)
            cn = st.slider("SELECT POWER OF SEARCH",
                           1,24,1)
            fn = st.button("SEARCH")
            if fn:
                try:
                    ppt = self._PARAMETERCONTROL(tx)
                    if ppt:
                        with st.spinner("PLEASE WAIT"):
                            pp = ""
                            st.info("[SEARCHING] > PLEASE WAIT FOR SEARCHING")
                            for _l in range(int(cn)):
                                try:
                                    dt = SCIENCENEWSSEARCH()._LAUNCH(str(tx).lower(),str(int(_l)))
                                    pp += dt+"\n"
                                except:
                                    pass
                            if pp != "":
                                st.success("[FOUND] > PLEASE SCROLL THE PAGE DOWN")
                                st.download_button("DOWNLOAD RESULT",pp)
                                st.code(pp)
                            else:
                                st.code("COULD NOT FOUND - [MAYBE NEVER EXISTED]")
                    else:
                        st.warning("[WARNING] - EMPTY PARAMETER")
                        pass
                except:
                    st.code(str(self.__e._psearch()))
                    st.warning("IF YOU HAVE AN ERROR, YOU CAN REDUCE THE SEARCH POWER - [JUST TRY AGAIN]")
        else:
            pass
        
        

if __name__ == "__main__":
    FREEOVERTHENET()._CONF()
    FREEOVERTHENET()._RETURNBANNER()
    FREEOVERTHENET()._PROCESS()