                                       # ####### #
import requests
import bs4
import DatabaseFunctions
import DataFile
import pymssql

print("Welcom To C# Jobs APP from Wuzzuf  ")
print("Last Seen for The Website We Found   ")

DatabaseFunctions.print_data()

ans = input("Do you need To Updata Data ? .. To update Enter any Key .. To Skip Enter n   ...   ")
if (ans !="n"):
    print("Please Wait We update data ")
    DatabaseFunctions.Delete_all()
    # 1 get Url For Page  2 take content of this page 3 make obj from it and make parser
    respon = requests.get("https://wuzzuf.net/search/jobs/?q=c%23&a=navbg")
    pagecontent = respon.content

    # create obj >
    soup = bs4.BeautifulSoup(pagecontent, "html.parser")

    # ----------------------------------------------------
    # collect data
    Job_Title = soup.find_all('h2', {'class': 'css-m604qf'})
    Job_location = soup.find_all('span', {'class': 'css-5wys0k'})
    Company = soup.find_all('a', {'class': 'css-17s97q8'})
    Since = soup.find_all('div', {'class': 'css-d7j1kk'})
    Job_Type = soup.find_all('span', {'class': 'css-1ve4b75'})
    links = soup.find_all('a', {'class': 'css-o171kl', "target": "_blank"})
    # --------------------------------------------------------

    # Some Data operation
    # ------------------------------------------------------
    # in this loop we need to find Type (full time  or part time ) we
    # cut extra data like freelance work from Home because the take the same tag

    le = len(Job_Type)
    for i in range(le):
        if Job_Type[i].text != "Work From Home" and Job_Type[i].text != "Freelance / Project":
            DataFile.Type.append(Job_Type[i].text)
    # push data in the Lists
    value = "https://wuzzuf.net"
    for i in range(len(Job_Title)):
        DataFile.Titles.append(Job_Title[i].text)
        DataFile.Locations.append(Job_location[i].text)
        DataFile.Companys.append(Company[i].text)
        DataFile.Sinces.append(Since[i].text.replace(DataFile.Companys[i], "").replace(DataFile.Locations[i], ""))
        DataFile.Jobbs_links.append(value + links[i].get("href"))

    DatabaseFunctions.insert_all()
    print("The Data After Update : ")
    DatabaseFunctions.print_data()
else:
    print("OK Think You ...")





