import requests
from bs4 import BeautifulSoup 
import math

login_data={
    'username': input("Enter the college id : "),'password': input("Enter the password : ")
}



headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
}

#login session
with requests.Session() as s:
    url="https://erp.skit.ac.in/signin/index"
    r=s.get(url,headers=headers)
    soup=BeautifulSoup(r.content,"html5lib")
    
    r=s.post(url,data=login_data,headers=headers)
    y=s.get("https://erp.skit.ac.in/reports/student_aggregate")

    soup=BeautifulSoup(y.content,"html.parser")

    containers=soup.tbody.find_all('tr')

    filename="attendance.csv"

    f=open(filename,'w')

    headers="S.no,Subject,Subject_code,Present,Absent,Total,Percentage,75_attendance,60%attendance"

    f.write(headers+"\n")


    for contain in containers:
        
        num=contain.find_all('td',{'data-title':'#'})
        Num=int(num[0].text.strip())
        
        
        subcode=contain.find_all('td',{'data-title':'Subject Code'})
        Subject_code=subcode[0].text.strip()

        sub=contain.find_all('td',{'data-title':'Subject'})
        Subject=sub[0].text.strip()

        pres=contain.find_all('td',{'data-title':'Present'})
        Present=int(pres[0].text.strip())

        ab=contain.find_all('td',{'data-title':'Absent'})
        Absent=int(ab[0].text.strip())
        
        Total=Present+Absent
        
        per=contain.find_all('td',{'data-title':'Percentage'})
        Percentage=float(per[0].text.strip())
        
        print("\nNum:",Num)
        print("Subject : ",Subject)
        print("Subject_code : ",Subject_code)
        print("Present : ",Present)
        print("Absent : ",Absent)
        print("Total : ",Total)
        print("Percentage : ",Percentage)
        
        if Percentage>=75.00:
        	x=math.ceil((0.75*Total-Present)/0.75)
        	print("for 75% attendence : ",x," days")
        else:
        	x=math.ceil((0.75*Total-Present)/0.25)
        	print("for 75% attendence : ",x," days")


        if Percentage>=60.00:
        	y=math.ceil((0.60*Total-Present)/0.60)
        	print("for 60% attendence : ",y," days")
        else:
        	y=math.ceil((0.60*Total-Present)/0.40)
        	print("for 60% attendence : ",y," days")
   
        

        f.write(str(Num)+","+Subject+","+Subject_code+","+str(Present)+","+str(Absent)+","+str(Total)+","+str(Percentage)+","+str(x)+","+str(y)+"\n")
    f.close()