import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


#header to make request as it is comming from a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# final data frame to store the data of all pages
final_dataframe =pd.DataFrame()

for j in range(1,1001):
  webpage=requests.get('https://www.ambitionbox.com/list-of-companies?page={}'.format(j)).text
  soup=BeautifulSoup(webpage,'lxml')
  company=soup.find_all('div',class_='company-content-wrapper')
  name=[]
  rating=[]
  reviews=[]
  company_type=[]
  head_quaters=[]
  how_old=[]
  no_of_employee=[]

  for i in company:

    try:
       name.append(i.find('h2').text.strip())
    except:
       name.append(np.nan)

    try:
       rating.append(i.find('p',class_='rating').text.strip())
    except:
       rating.append(np.nan)
   
    try:

      reviews.append(i.find('a' , class_='review-count').text.strip())
    except:
      reviews.append(np.nan)

    try:

      company_type.append(i.find_all('p',class_='infoEntity')[0].text.strip())
    except:
      company_type.append(np.nan)
    try:

      head_quaters.append(i.find_all('p',class_='infoEntity')[1].text.strip())
    except:
      head_quaters.append(np.nan)
    
    try:

      how_old.append(i.find_all('p',class_='infoEntity')[2].text.strip())
    except:
      how_old.append(np.nan)
    try:
      no_of_employee.append(i.find_all('p',class_='infoEntity')[3].text.strip())
    except:
      no_of_employee.append(np.nan)
    

  df=pd.DataFrame({'name':name,
    'rating':rating,
    'reviews':reviews,
    'company_type':company_type,
    'Head_Quarters':head_quaters,
    'Company_Age':how_old,
    'No_of_Employee':no_of_employee,
    })
  
  final_dataframe=final_dataframe.append(df,ignore_index=True)

