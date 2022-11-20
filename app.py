from flask import Flask,render_template
import re
import ibm_db

app = Flask(__name__)
app.secret_key="ayan"


conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30426;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=qtg16997;PWD=cMD8dkRCO5kH4gzu",'','')


@app.route('/')
def hello():
   return render_template('home.html')

@app.route('/test')
def test():
       sql="SELECT * FROM Users"
       stmt = ibm_db.exec_immediate(conn,sql)
       dictionary=ibm_db.fetch_both(stmt)
       print(dictionary)



if __name__ == '__main__':
      app.run()
