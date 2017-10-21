import requests
from bs4 import BeautifulSoup as bs
ph=raw_input("Enter the phone No ")
r=requests.post('http://site21.way2sms.com/LocateMobile/'+ph)
s=bs(r.content,'lxml')
st=s.find('div',attrs={"id":"info"})
for i in st.find_all('p'):
    print i.text
          
