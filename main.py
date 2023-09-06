from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class trendsBot:
  def __init__(self, downloadPath):
    """
    Função para receber os dados
    :param downloadPath: string
    """
    #Configuração do Microsoft Edge
    self.edgeConfig = webdriver.EdgeOptions()
    self.prefs = {"download.default_directory" : downloadPath}
    self.edgeConfig.add_experimental_option("prefs", self.prefs)
    self.driver = webdriver.Edge(options=self.edgeConfig)
    self.driver.get('https://trends.google.com.br/trends/')
    sleep(2)
  def downloadCsv(self, movie):
    """
    Baixa o csv para o path
    :param movie: string
    """
    if(self.isValid(movie)):
      #Pesquisando filme
      searchInput = self.driver.find_element(By.ID, 'i9')
      searchInput.click()
      sleep(1)
      searchInput.clear()
      searchInput.send_keys(movie)
      sleep(0.5)
      searchInput.send_keys(Keys.ENTER)
      sleep(3)
      #Seleciona período
      periodoBtn = self.driver.find_element(By.ID, 'select_10')
      periodoBtn.click()
      periodo = self.driver.find_element(By.ID, 'select_option_21')
      periodo.click()
      #Baixa CSV para path
      csvButton = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]')
      csvButton.click()
      sleep(5)
    else:
      print("Nome inválido")
  

  def isValid(self, name):
    if(len(name)):
      return True
    return False

app = trendsBot("path aqui :)") #em caso de path inválido, o padrão será Downloads
try:
  app.downloadCsv("nome do filme")
except:
  print("Erro ao baixar csv!")