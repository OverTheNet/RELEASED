import streamlit as st
from _errorsoutput import *
from _htmlformat import*
from _usermessageconf import *
from _databaseconf import *

__all__ = ["STOVERTHENET"]
__author__ = "OverTheNet / ^-^"
__copyright__ = "Fuck CopyRights"
__version__ = "1.0"
__status__ = "RELEASE - OPERATION"
__description__  = "Free Message To The World"

class STOVERTHENET(object):
    def __init__(self):
        self.__pt = "OvRThNt"
        self.__ly = "wide"
        self.__ss = "expanded"
        self.__tl = "^-^"
        self.__sidebartitle = "OvRThNt"
        self.__messageall = {"main_feed":{}}
    def __str__(self)->str:
        return "STREAMING - PROCESS"
    def __call__(self)->str:
        return
    def __getstate__(self)->classmethod:
        raise TypeError("[DENIED - PICKLED]")
    def __repr__(self)->classmethod:
        return STOVERTHENET.__doc__
    def _CONF(self)->classmethod:
        st.set_page_config(page_title=self.__pt,
                           layout=self.__ly,
                           initial_sidebar_state=self.__ss)
        try:
            DBSAVE()._CREATE()
        except:
            pass
    def _PRINTBANNER(self)->classmethod:
        st.code(HTMLFORMATTYPES()._BANNER())
    def _SIDEBARINFORMATION(self)->classmethod:
        sb = st.sidebar.selectbox("SELECT PROCESS",
                                  ("JOIN THE FEED",
                                   "ACCESS THE MESSAGE",
                                   "CURRENT COMMUNITY FEED",
                                   "PAST-TIME SPEECHES",
                                   "MESSAGE TO DATABASE",
                                   "IMAGE TO DATABASE"))
        return sb
    def _SELECTIONPROCESS(self)->classmethod:
        sb = self._SIDEBARINFORMATION()
        if sb == "JOIN THE FEED":
            st.markdown(HTMLFORMATTYPES()._HEAD("JOIN THE FEED"),
                        unsafe_allow_html=True)
            ms = st.text_area("WHAT IS YOUR MESSAGE",
                              help="> TYPE YOUR MESSAGE TO TRANSMIT").replace("\n","|")
            rb = st.button("LAUNCH")
            if rb:
                msxt,cdxt,usxt = USERMESSAGECONF()._SAVE(str(ms))
                st.info("SUCCESS - TRANSFERRED AND SAVED")
                self.__messageall["main_feed"] = msxt[-1]
                self.__messageall["main_feed"]["MESSAGE-PROOF"] = str(cdxt[-1])
                DBSAVE()._ADD(str(ms),str(msxt[-1]),str(usxt[-1]))
                dt = DBSAVE()._READ_DB()
                for xc,xd in enumerate(dt):
                    st.text("---"*7)
                    st.markdown(HTMLFORMATTYPES()._TXTNORMAL(dt[xc-1][1]),
                                unsafe_allow_html=True)
                st.json(self.__messageall)
            else:
                pass
        elif sb == "ACCESS THE MESSAGE":
            st.markdown(HTMLFORMATTYPES()._HEAD_SUB("ACCESS THE MESSAGE"),
                        unsafe_allow_html=True)
            ms = st.text_area("TYPE USER-PROOF PARAMETER",
                              help="> TYPE USER-PROOF TO ACCESS THE MESSAGE").replace(" ", "")
            rb = st.button("FIND")
            if rb:
                st.info("SUCCESS - FOUND")
                st.text("MESSAGE")
                msusr,allusr = DBSAVE()._REACH(str(ms))
                if msusr != None:
                    st.markdown(HTMLFORMATTYPES()._TXTNORMAL(msusr),
                                unsafe_allow_html=True)
                    st.json(allusr)
                else:
                    st.markdown(HTMLFORMATTYPES()._TXTNORMAL("NO-MESSAGE / DELETED OR NEVER EXISTED"),
                                unsafe_allow_html=True)
            else:
                pass
        elif sb == "CURRENT COMMUNITY FEED":
            dt = DBSAVE()._READ_DB()
            c_1,c_2,c_3 = st.columns(3)
            c_1.metric("USER",str(len(dt)),str(len(dt)))
            c_2.metric("MESSAGE",str(len(dt)),str(len(dt)))
            c_3.text("EXPIRATION:\n5'TH DAY OF EVERY MONTH")
            st.markdown(HTMLFORMATTYPES()._HEAD_SUB_II("CURRENT COMMUNITY FEED"),
                        unsafe_allow_html=True)
            st.json(dt)
        elif sb == "PAST-TIME SPEECHES":
            dt = DBSAVE()._READ_PASS()
            st.markdown(HTMLFORMATTYPES()._HEAD_SUB_III("PAST-TIME SPEECHES"),
                        unsafe_allow_html=True)
            st.json(dt)
        elif sb == "MESSAGE TO DATABASE":
            st.markdown(HTMLFORMATTYPES()._HEAD_SUB_IV("MESSAGE TO DATABASE"),
                        unsafe_allow_html=True)
            st.markdown(HTMLFORMATTYPES()._MAILSEND(),
                        unsafe_allow_html=True)
        elif sb == "IMAGE TO DATABASE":
            st.markdown(HTMLFORMATTYPES()._HEAD_SUB_V("IMAGE TO DATABASE"),
                        unsafe_allow_html=True)
            st.markdown(HTMLFORMATTYPES()._FILESEND(),
                        unsafe_allow_html=True)
        else:
            pass
            
        
        
if __name__ == "__main__":
    STOVERTHENET()._CONF()
    STOVERTHENET()._PRINTBANNER()
    STOVERTHENET()._SELECTIONPROCESS()