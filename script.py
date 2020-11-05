import secrets
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# driver = webdriver.PhantomJS("""D:/Programme/phantomjs-2.1.1-windows/bin/phantomjs.exe""")

driver = webdriver.Chrome("D:/Programme/chromedriver.exe")
delay = 10
driver.set_window_size(1120, 550)

def write_resume(data):
  """
  docstring
  """
  pass

def write_cover_letter(data):
  """
  docstring
  """
  pass

def write_job_posting_summary(data):
  """
  docstring
  """
  pass

def get_job_posting_from_linkedin(url):
  """
  docstring
  """
  jobplatform_provider="LinkedIn"
  pass

def get_job_postings_from_stepstone(url):
  """
  docstring
  """
  jobplatform_provider="StepStone"
  jobposition = "react"

  # This url does all the filtering for us, the one thing what does change is the job position
  driver.get('https://www.stepstone.de/5/job-search-simple.html?stf=freeText&ns=1&companyid=0&sourceofthesearchfield=resultlistpage%3Ageneral&qs=%5B%5D&cityid=0&ke='+ jobposition +'&ws=12159%20Berlin&radius=30&suid=b3958f38-4979-4f03-a203-ba3a9f5f6a5c&wt=80001&wt=80005&ex=90001&action=facet_selected%3BdetectedLanguages%3Bde&fdl=de')
  all_job_postings = driver.find_elements_by_css_selector('.gvBCse h2')

  get_job_posting_data_from_stepstone()



  sleep(10)


  driver.quit()

if __name__ == "__main__":
  print(secrets.LINKEDIN_USERNAME)
  counter = 10
  get_job_postings_from_stepstone('')

  for counter in range(0,counter):
    pass

