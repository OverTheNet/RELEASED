import streamlit as st
from PIL import Image
from _dataaccess import *

rt = os.path.dirname(os.path.relpath((__file__)))

class STAPP(object):
    def __init__(self):
        self.__pt = "ADDRESS GATHERING SYSTEM - EMERGENCY"
        self.__ly = "wide"
        self.__ss = "expanded"
        self.__adiyaman = None
        self.__maras = None
        self.__hatay = None
        self.__antep = None
    def __str__(self):
        return "ADDRESS GATHERING WEB APPLOCATION - PROCESS"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[DENIED]")
    def __repr__(self):
        return STAPP.__doc__
    def _CONVERT_DF(self,dtinit):
        return dtinit.to_csv().encode("utf-8")
    def _CONF(self):
        st.set_page_config(page_title=self.__pt,
                           layout=self.__ly,
                           initial_sidebar_state=self.__ss,
                           menu_items={"About":"ADDRESS GATHERING SYSTEM - EMERGENCY"})
    def _PRINTBANNER(self):
        st.header("ADRES BİLGİLENDİRME VE TESPİT SİSTEMİ")
        st.caption("Bu platform kazazedelere erişimi kolaylaştırmak ve adres bilgilendirmesi için oluşturulmuştur")
        ct1,ct2 = st.columns(2)
        with ct1:
            st.image(Image.open(os.path.join(rt,"AKUT.png")).resize((250,100)))
        with ct2:
            st.image(Image.open(os.path.join(rt,"AFAD.png")).resize((340,150)))
    def _SIDEBAR(self):
        _infoex = """
        
**ADRES BİLGİLENDİRME VE TESPİT SİSTEMİ**\n\n\r

AFAD KOORDİNASYON VE İLETİŞİM BİLGİLERİ\n\n\r

:signal_strength: [Diyarbakır](https://diyarbakir.afad.gov.tr/) : 0412 326 1156\n\n
:signal_strength: [Hatay](https://hatay.afad.gov.tr/) : 0326 112 0000\n\n
:signal_strength: [Maraş](https://kahramanmaras.afad.gov.tr/): 0344 221 4991\n\n
:signal_strength: [Antep](https://gaziantep.afad.gov.tr/) : 0342 428 1118\n\n
:signal_strength: [Adana](https://adana.afad.gov.tr/) : 0322 227 2854\n\n
:signal_strength: [Adıyaman](https://adiyaman.afad.gov.tr/) : 0416 216 1231\n\n
:signal_strength: [Urfa](https://sanliurfa.afad.gov.tr/) : 0414 313 7290\n\n
:signal_strength: [Malatya](https://malatya.afad.gov.tr/) : 0422 212 8432\n\n
:signal_strength: [Mardin](https://mardin.afad.gov.tr/) : 0482 212 3740\n\n

        """
        st.sidebar.markdown(_infoex,unsafe_allow_html=True)
    def _DATAACCESS(self):
        func = DATAGATHERING()
        fileinit = func._READFILE()
        self.__adiyaman = fileinit[fileinit["SEHIR"] == "Adıyaman"].reset_index(drop=True)
        self.__maras = fileinit[fileinit["SEHIR"] == "Maraş"].reset_index(drop=True)
        self.__hatay = fileinit[fileinit["SEHIR"] == "Hatay"].reset_index(drop=True)
        self.__antep = fileinit[fileinit["SEHIR"] == "Antep"].reset_index(drop=True)
        self.__adiyaman["ADRES"] = self.__adiyaman["ADRES"].str.capitalize()
        self.__maras["ADRES"] = self.__maras["ADRES"].str.capitalize()
        self.__hatay["ADRES"] = self.__hatay["ADRES"].str.capitalize()
        self.__antep["ADRES"] = self.__antep["ADRES"].str.capitalize()
        self.__adiyaman["ISIM"] = self.__adiyaman["ISIM"].str.capitalize()
        self.__maras["ISIM"] = self.__maras["ISIM"].str.capitalize()
        self.__hatay["ISIM"] = self.__hatay["ISIM"].str.capitalize()
        self.__antep["ISIM"] = self.__antep["ISIM"].str.capitalize()
    def _TABS(self):
        self._DATAACCESS()
        md1,md2,md3 = st.tabs(["SORGU PANELİ",
                           "BÜTÜN ADRESLER",
                           "ADRES BİLDİRİMİ"])
        with md1:
            smc = 0
            st.caption("Cümle sonunda boşluk bırakmayınız ve aramak istediğiniz adresi doğru girmeye çalışınız")
            ms = st.text_area("ARAMAK İSTEDİĞİNİZ ADRESİ GİRİNİZ",
                              help="Erişmek veya sorgulamak için adres giriniz")
            rb = st.button("ARA")
            if rb:
                if len(ms) > 7:
                    for xc,xv in enumerate(self.__adiyaman["ADRES"].values):
                        if (ms.lower() in xv.lower()) or (ms.lower() == xv.lower()):
                            st.info("KAYIT BULUNDU")
                            st.text(f'İSİM: {self.__adiyaman["ISIM"][xc]}')
                            st.text(f'ŞEHİR: {self.__adiyaman["SEHIR"][xc]}')
                            st.text(f'ADRES: {self.__adiyaman["ADRES"][xc]}')
                            smc += 1
                        else:
                            pass
                    for xc,xv in enumerate(self.__maras["ADRES"].values):
                        if (ms.lower() in xv.lower()) or (ms.lower() == xv.lower()):
                            st.info("KAYIT BULUNDU")
                            st.text(f'İSİM: {self.__maras["ISIM"][xc]}')
                            st.text(f'ŞEHİR: {self.__maras["SEHIR"][xc]}')
                            st.text(f'ADRES: {self.__maras["ADRES"][xc]}')
                            smc += 1
                        else:
                            pass
                    for xc,xv in enumerate(self.__hatay["ADRES"].values):
                        if (ms.lower() in xv.lower()) or (ms.lower() == xv.lower()):
                            st.info("KAYIT BULUNDU")
                            st.text(f'İSİM: {self.__hatay["ISIM"][xc]}')
                            st.text(f'ŞEHİR: {self.__hatay["SEHIR"][xc]}')
                            st.text(f'ADRES: {self.__hatay["ADRES"][xc]}')
                            smc += 1
                        else:
                            pass
                    for xc,xv in enumerate(self.__antep["ADRES"].values):
                        if (ms.lower() in xv.lower()) or (ms.lower() == xv.lower()):
                            st.info("KAYIT BULUNDU")
                            st.text(f'İSİM: {self.__antep["ISIM"][xc]}')
                            st.text(f'ŞEHİR: {self.__antep["SEHIR"][xc]}')
                            st.text(f'ADRES: {self.__antep["ADRES"][xc]}')
                            smc += 1
                        else:
                            pass
                    if smc == 0:
                        st.warning("Kayıt bulunamadı")
                    else:
                        pass
                else:
                    st.error("Geçerli bir adres girdiğinizden emin olunuz")
                    
        with md2:
            hd1,hd2,hd3,hd4 = st.tabs(["ADIYAMAN",
                                       "MARAŞ",
                                       "HATAY",
                                       "ANTEP"])
            with hd1:
                st.subheader("ADIYAMAN - BİLGİLENDİRME VE ERİŞİM")
                if len(self.__adiyaman["ADRES"]) != 0:
                    st.dataframe(self.__adiyaman)
                    md = self._CONVERT_DF(self.__adiyaman)
                    st.download_button("Veriyi İndir",
                                       data=md,
                                       file_name="adiyaman.csv",
                                       mime="text/csv")
                else:
                    st.text("Henüz veri bulunmamaktadır")
            with hd2:
                st.subheader("MARAŞ - BİLGİLENDİRME VE ERİŞİM")
                if len(self.__maras["ADRES"]) != 0:
                    st.dataframe(self.__maras)
                    md = self._CONVERT_DF(self.__maras)
                    st.download_button("Veriyi İndir",
                                       data=md,
                                       file_name="maras.csv",
                                       mime="text/csv")
                else:
                    st.text("Henüz veri bulunmamaktadır")
            with hd3:
                st.subheader("HATAY - BİLGİLENDİRME VE ERİŞİM")
                if len(self.__hatay["ADRES"]) != 0:
                    st.dataframe(self.__hatay)
                    md = self._CONVERT_DF(self.__hatay)
                    st.download_button("Veriyi İndir",
                                       data=md,
                                       file_name="hatay.csv",
                                       mime="text/csv")
                else:
                    st.text("Henüz veri bulunmamaktadır")
            with hd4:
                st.subheader("ANTEP - BİLGİLENDİRME VE ERİŞİM")
                if len(self.__antep["ADRES"]) != 0:
                    st.dataframe(self.__antep)
                    md = self._CONVERT_DF(self.__antep)
                    st.download_button("Veriyi İndir",
                                       data=md,
                                       file_name="antep.csv",
                                       mime="text/csv")
                else:
                    st.text("Henüz veri bulunmamaktadır")
        with md3:
            st.caption("Lütfen iletmek istediğiniz adres bilgilerini doğru girdiğinizden emin olunuz")
            CONTACT_US_FORM = """
        <style>
        .btn {
          border: none;
          color: white;
          padding: 10px 32px;
          padding-top: 10px;
          border-spacing: 10px;
          margin: 7px 0 0 0;
          font-size: 15px;
          cursor: pointer;
        }
        .btn_plus {
          border: none;
          color: 990000;
          margin: 7px 0 0 0;
          font-size: 17px;
          cursor: pointer;
        }
        .danger {background-color: #990000;} 
        .danger:hover {background: #ff1a1a;}
        </style>
        <form action="https://formsubmit.co/68eac7a9af3210d2d1df02d4aa3ef059" method="POST" enctype="multipart/form-data">
          <table>
          <fieldset>
          <label for="in_name">İSİM-SOYİSİM</label><br>
          <input type="text" id="in_name" name="ISIM" placeholder="isim" required><br>
          </fieldset>
          <fieldset>
          <label for="in_loc">ŞEHİR</label><br>
          <input type="text" id="in_loc" name="SEHIR" placeholder="şehir" required><br>
          </fieldset>
          <fieldset>
          <label for="in_loc">ADRES</label><br>
          <textarea rows="15" cols="60" name="ADRES" required>
          </textarea>
          </fieldset>
          <input type="hidden" name="_subject" value="Yeni Adres Bildirimi">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="box">
          <input type="hidden" name="_autoresponse" value="Bildiriminiz başarıyla iletilmiştir, kontrollerden sonra listeye eklenecektir.">
          <button class="btn danger" type="submit">GÖNDER</button>
          </table>
        </form>
        """
            st.markdown(CONTACT_US_FORM,
                        unsafe_allow_html=True)

if __name__ == "__main__":
    STAPP()._CONF()
    STAPP()._SIDEBAR()
    STAPP()._PRINTBANNER()
    try:
        STAPP()._TABS()
    except:
        st.warning("İNTERNET BAĞLANTINIZI KONTROL EDİN VEYA TEKRAR DENEYİN")
