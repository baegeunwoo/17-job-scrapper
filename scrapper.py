import requests
from bs4 import BeautifulSoup

def search_saramin(keyword):
    
    url=f"https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&searchword={keyword}&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage=1&recruitSort=relation&recruitPageCount=40&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting="
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    lis = soup.find_all("div",class_="item_recruit")
    
    jobs = []

    for li in lis:
        company =  li.find("div", class_="area_corp").find("a").text
        title = li.find("div", class_="area_job").find("a").text
        location = li.find("div", class_="job_condition").find_all("span")[0].text
        link = li.find("div",class_="area_job").find("a").get("href")
        link2 = "https://www.saramin.co.kr"+link
        
        job_data = {
            "company": company,
            "title": title,
            "location" : location,
            "link": link2
        }

        jobs.append(job_data)
    return jobs


def search_incruit(keyword, page=1):

    jobs = []

    for i in range(page):
        page = 30 * i 
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        lis = soup.find_all("li",class_="c_col")


        for li in lis:
            company = li.find("a", class_="cpname").text
            title = li.find("div",class_="cell_mid").find("div", class_="cl_top").find("a").text
            location = li.find("div",class_="cl_md").find_all("span")[0].text
            link = li.find("div",class_="cell_mid").find("div",class_="cl_top").find("a").get("href")

            job_data = {
                "company": company,
                "title": title,
                "location" : location,
                "link": link
            }
            jobs.append(job_data)
    return jobs
    
if __name__ == "__main__":
    result = search_incruit("간호사", 3)
    print(len(result))
