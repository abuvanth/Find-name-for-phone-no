import requests
from bs4 import BeautifulSoup as bs
ph=raw_input("Enter the phone No ")
r=requests.post('http://site21.way2sms.com/LocateMobile/'+ph)
s=bs(r.content,'lxml')
st=s.find('div',attrs={"id":"info"})
data=st.find_all('p')
for details in data[:len(data)-1]:
    print ('\033[1;32;40m              '+details.text+'\n')
   
          
