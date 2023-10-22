from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familiar with.')
unfamiliar_skills = list(map(str, input('>').split(',')))
print(f"Filtering out {', '.join(unfamiliar_skills)}")

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if all(skill.lower() not in skills.lower() for skill in unfamiliar_skills):
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company name: {company_name.strip()} \n')
                    f.write(f'Required skills: {skills.strip()} \n')
                    f.write(f'More info: {more_info} \n')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'Waiting {time_wait} minutes....')
        time.sleep(time_wait*60)
