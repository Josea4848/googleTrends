from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

class trendsBot:
  def __init__(self, downloadPath):
    """
    Função para receber os dados
    :param downloadPath: string
    """
    #Configuração do Microsoft Edge
    self.verificado = 0
    self.service = Service("/usr/bin/chromedriver")
    self.chromeConfig = webdriver.ChromeOptions()
    self.prefs = {"download.default_directory" : downloadPath}
    self.chromeConfig.add_experimental_option("prefs", self.prefs)
    self.chromeConfig.add_extension("extension_0_145_0_0.crx")
    self.chromeConfig.add_extension("extension_1_52_0_0.crx")
    self.driver = webdriver.Chrome(service=self.service, options=self.chromeConfig)
    try:
      self.geraConta()
    except:
      print("erro ao criar conta! :(")

  def downloadCsv(self, movie):
    """
    Baixa o csv para o path
    :param movie: string
    """
    self.driver.get('https://trends.google.com/trends/?')
    if(self.isValid(movie)):      
      #Pesquisando filme
      sleep(1)
      searchInput = self.driver.find_element(By.ID, 'keyword')
      searchInput.click()
      sleep(1)
      searchInput.clear()
      searchInput.send_keys(movie)
      sleep(2)
      searchInput.send_keys(Keys.ENTER)
      sleep(2)
      
      self.removeMsg()

      try:
        self.removeMensage()
      except:
        print("Sem mensagem ou overflow")
      sleep(0.5)
      if(not self.verificado):
        try:
          self.DesativaBotao()
          sleep(0.5)
          self.ativaBotao()
          self.verificado = 1
        except:
          print("Erro ao verificar")

      sleep(3000)
      #Seleciona período 
      periodoBtn = self.driver.find_element(By.ID, 'select_value_label_9')
      periodoBtn.click()
      sleep(1)
      periodo = self.driver.find_element(By.ID, 'select_option_17')
      periodo.click()
      sleep(2)
      periodoBtn = self.driver.find_element(By.ID, 'select_value_label_9')
      periodoBtn.click()
      sleep(1)
      periodo = self.driver.find_element(By.ID, 'select_option_21')
      sleep(2)
      periodo.click()
      sleep(15)
      #Baixa CSV para path
      svgOption = self.driver.find_element(By.XPATH, "//div[@class='fe-atoms-generic-header-container fe-line-chart-header-container fe-atoms-generic-separator']//span[@class='glimpse-actions-toggle']//*[name()='svg']")
      svgOption.click()
      sleep(1)
      csvBtn = self.driver.find_element(By.XPATH, "//button[@title='Download CSV']//i[@class='material-icons-extended gray relative -bottom-px'][normalize-space()='file_download']")
      csvBtn.click()
      sleep(2)
      csvBtn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Download CSV']")
      csvBtn.click()
      sleep(1)
    else:
      print("Nome inválido")

  def isValid(self, name):
    if(len(name)):
      return True
    return False
  
  def removeMensage(self):
    self.driver.execute_script("""
    let box = document.getElementsByClassName('fixed z-[1000] grid justify-items-center items-center inset-0 font-google')[0];
    box.parentNode.removeChild(box);
    """)
  def ativaBotao(self):
    self.driver.execute_script("""let botao = document.getElementsByClassName("w-[26px] h-3.5 flex border box-border transition-opacity duration-[0.25s] p-0.5 rounded-[99rem] border-solid border-[#e4e9ed] bg-white")[0];
    botao.click();""")


  def DesativaBotao(self):
    self.driver.execute_script("""let botao = document.getElementsByClassName("w-[26px] h-3.5 flex border box-border transition-opacity duration-[0.25s] p-0.5 rounded-[99rem] border-solid border-[--glimpse-color-primary] bg-[--glimpse-color-primary]")[0];
    botao.click();""")

    

  def geraConta(self):
    #Gera email aleatório
    self.window_Gen = self.driver.window_handles[0]
    self.driver.get("https://generator.email/")
    self.driver.find_element(By.ID, "copbtn").click()
    sleep(2)
    #Muda para janela de login
    self.window_Login = self.driver.window_handles[1]
    self.driver.switch_to.window(self.window_Login)
    self.driver.get("https://meetglimpse.com/sign-up")
    sleep(1)
    #Inseri email
    inputEmail = self.driver.find_element(By.ID, "email")
    inputEmail.click()
    inputEmail.send_keys(Keys.CONTROL, 'v')
    inputEmail.send_keys(Keys.ENTER)
    #Confirma email
    self.driver.switch_to.window(self.window_Gen)
    sleep(3)
    self.driver.find_element(By.ID, "refresh").click()
    sleep(2)
    self.driver.find_element(By.ID, "refresh").click()
    sleep(30)
    self.driver.find_element(By.XPATH, "//a[@class='hover-bg-brand-600']").click()
    #Realiza procedimentos necessários para usar o glimpse
    self.driver.switch_to.window(self.window_Login)
    sleep(3)
    self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(3)
    self.driver.find_element(By.XPATH, "//div[normalize-space()='Other']").click()
    sleep(3)
    self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/button[1]").click()
    sleep(3)
    self.driver.find_element(By.ID, "viewSource").send_keys("Qualquer coisa")
    sleep(1)
    self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    self.driver.get("https://trends.google.com/trends/?")
    sleep(3)
    #Ativa extensão
    self.ativaBotao()

  def removeMsg(self):
    try:
      self.driver.execute_script("""
      let l = document.getElementsByClassName("button button--primary button--lg")[0];
      l.click();                           
      """)
    except:
      print("Sem mensagem")

  def closeBrowser(self):
    self.driver.quit()

path = "/home/jose/Downloads/CSVACTORS"

#Armazenando filmes em lista
arquivo = open("actors1.txt")
linhas = arquivo.readlines()
filmes = list()
for linha in linhas:
  filmes.append(linha[0:len(linha)-1].replace(',',' '))

while(len(filmes)):
  app = trendsBot(path)
  while(True):
    try:
      app.downloadCsv(filmes[0])
      filmes.pop(0)
    except:
      print("Erro")
      app.closeBrowser()
      break