import secrets
from selenium import webdriver
driver = webdriver.PhantomJS("""D:/Programme/phantomjs-2.1.1-windows/bin/phantomjs.exe""")
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

def get_job_posting_from_stepstone(url):
  """
  docstring
  """
  jobplatform_provider="StepStone"
  driver.get("https://duckduckgo.com/")
  driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
  driver.find_element_by_id("search_button_homepage").click()
  print(driver.current_url)
  driver.quit()


if __name__ == "__main__":
  print(secrets.LINKEDIN_USERNAME)
  counter = 10
  get_job_posting_from_stepstone('')

  for counter in range(0,counter):
    pass

