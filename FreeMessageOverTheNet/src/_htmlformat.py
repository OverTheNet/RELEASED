__all__ = ["HTMLFORMATTYPES"]

class HTMLFORMATTYPES(object):
    def __init__(self):
        self.__banner = """
      

░█████╗░██╗░░░██╗███████╗██████╗░|  ████████╗██╗░░██╗███████╗███╗░░██╗███████╗████████╗
██╔══██╗██║░░░██║██╔════╝██╔══██╗|  ╚══██╔══╝██║░░██║██╔════╝████╗░██║██╔════╝╚══██╔══╝
██║░░██║╚██╗░██╔╝█████╗░░██████╔╝|  ░░░██║░░░███████║█████╗░░██╔██╗██║█████╗░░░░░██║░░░
██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗|  ░░░██║░░░██╔══██║██╔══╝░░██║╚████║██╔══╝░░░░░██║░░░
╚█████╔╝░░╚██╔╝░░███████╗██║░░██║|  ░░░██║░░░██║░░██║███████╗██║░╚███║███████╗░░░██║░░░
░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝|  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░
    
    ^₋^
        """
    def __str__(self):
        return "HTML FORMAT TYPES - SUBPROCESS"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("[DENIED - PICKLED]")
    def __repr__(self):
        return HTMLFORMATTYPES.__doc__
    def _BANNER(self):
        return self.__banner
    def _HEAD(self,t:str)->str:
        return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta name="viewport" content="width=device-width">
    <style>
    h1 {
    background-color: white;
    text-align: center;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    color: #000000;
    font-size: 24px;
    }
    </style>
    <title>OvRThNt</title>
    </head>
    <body>
    <h1>%s</h1>
    <p style="text-align: center; font-size:13px; color:#ffffff; background-color: black">CREATE YOUR MESSAGE TO TRANSMIT</p>
    </body>
    </html>"""%(str(t))
    def _HEAD_SUB(self,t:str)->str:
        return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta name="viewport" content="width=device-width">
    <style>
    h1 {
    background-color: white;
    text-align: center;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    color: #000000;
    font-size: 24px;
    }
    </style>
    <title>OvRThNt</title>
    </head>
    <body>
    <h1>%s</h1>
    <p style="text-align: center; font-size:13px; color:#ffffff; background-color: black">ACCESS USER MESSAGE</p>
    </body>
    </html>"""%(str(t))
    def _HEAD_SUB_II(self,t:str)->str:
        return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta name="viewport" content="width=device-width">
    <style>
    h1 {
    background-color: white;
    text-align: center;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    color: #000000;
    font-size: 24px;
    }
    </style>
    <title>OvRThNt</title>
    </head>
    <body>
    <h1>%s</h1>
    <p style="text-align: center; font-size:13px; color:#ffffff; background-color: black">READ COMMUNITY FEED</p>
    </body>
    </html>"""%(str(t))
    def _HEAD_SUB_III(self,t:str)->str:
        return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta name="viewport" content="width=device-width">
    <style>
    h1 {
    background-color: white;
    text-align: center;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    color: #000000;
    font-size: 24px;
    }
    </style>
    <title>OvRThNt</title>
    </head>
    <body>
    <h1>%s</h1>
    <p style="text-align: center; font-size:13px; color:#ffffff; background-color: black">READ PAST SPEECHES</p>
    </body>
    </html>"""%(str(t))
    def _HEAD_SUB_IV(self,t:str)->str:
        return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta name="viewport" content="width=device-width">
    <style>
    h1 {
    background-color: white;
    text-align: center;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    color: #000000;
    font-size: 24px;
    }
    </style>
    <title>OvRThNt</title>
    </head>
    <body>
    <h1>%s</h1>
    <p style="text-align: center; font-size:13px; color:#ffffff; background-color: black">SEND MESSAGE TO DATABASE</p>
    </body>
    </html>"""%(str(t))
    def _HEAD_SUB_V(self,t:str)->str:
        return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta name="viewport" content="width=device-width">
    <style>
    h1 {
    background-color: white;
    text-align: center;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    color: #000000;
    font-size: 24px;
    }
    </style>
    <title>OvRThNt</title>
    </head>
    <body>
    <h1>%s</h1>
    <p style="text-align: center; font-size:13px; color:#ffffff; background-color: black">SEND IMAGE TO DATABASE</p>
    </body>
    </html>"""%(str(t))
    def _TXTNORMAL(self,t:str)->str:
        return """
    <style>
    .gen {
    background-color: black;
    font-size: 12px;
    color: white;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    font-weight: bold;
    }
    </style>
    <body>
    <p style="color:#ffffff; background-color: black; font-size: 15px; padding: 12px 12px 12px">%s</p>
    </body>"""%(str(t))
    def _TXTMESSAGE(self,b:str,l:str,i:str)->str:
        return """
    <style>
    .gen {
    background-color: black;
    font-size: 12px;
    color: white;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    font-weight: bold;
    }
    </style>
    <body>
    <p style="color:#ffffff; background-color: black; font-size: 12px; padding: 12px 12px 12px">USER[BLOCK]: %s </p>
    <p class="gen">USER[MESSAGE]: %s </p>
    <p class="gen">USER[ID]: %s </p>
    </body>"""%(str(l),str(b),str(i))
    def _MAILSEND(self):
        return """
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
        .danger {background-color: #990000;} 
        .danger:hover {background: #ff1a1a;}
        </style>
        <form action="https://formsubmit.co/f32952229552d0aaa5a5a39a2adbf870" method="POST">
          <table>
          <fieldset>
          <label for="in_name">USERNAME</label><br>
          <input type="text" id="in_name" name="username" placeholder="Username"><br>
          </fieldset>
          <fieldset>
          <label>MESSAGE</label><br>
          <textarea rows="15" cols="60" name="message" placeholder="Message">
          </textarea>
          </fieldset>
          <fieldset>
          <label for="in_loc">NOTE</label><br>
          <input type="text" id="in_loc" name="note" placeholder="Note"><br>
          </fieldset>
          <input type="hidden" name="_subject" value="New Message">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="box">
          <input type="hidden" name="_autoresponse" value="Your message has been forwarded to database">
          <button class="btn danger" type="submit">SEND</button>
          </table>
        </form>"""
    def _FILESEND(self):
        return """
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
        <form action="https://formsubmit.co/f32952229552d0aaa5a5a39a2adbf870" method="POST" enctype="multipart/form-data">
          <table>
          <fieldset>
          <label for="in_name">USERNAME</label><br>
          <input type="text" id="in_name" name="username" placeholder="Username"><br>
          </fieldset>
          <fieldset>
          <label for="in_loc">NOTE</label><br>
          <input type="text" id="in_loc" name="note" placeholder="Note"><br>
          </fieldset>
          <fieldset>
          <label for="in_loc">UPLOAD IMAGE</label><br>
          <input class="btn_plus" type="file" name="attachment" accept="image/png, image/jpeg">
          </fieldset>
          <input type="hidden" name="_subject" value="New Image">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="box">
          <button class="btn danger" type="submit">SEND</button>
          </table>
        </form>"""