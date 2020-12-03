from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Z Robo"
        self.grupos =["Ygg"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang-pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        

        def EnviarMensagens(self):
            time.sleep(3)
            self.driver.get('https://www.web.whatsappweb.com')
            time.sleep(20)
        for grupo in self.grupos:
            time.sleep(5)
            self.driver.get('https://web.whatsapp.com')
            #self.driver.find_element_by_xpath(f"//span[@title='{grupo}']") _1Plpp
            time.sleep(5)
            grupo = self.driver.find_element_by_xpath(f"//span[@title='Ygg']")
            time.sleep(3)
            grupo.click()
            time.sleep(3)
            chat_box = self.driver.find_elements_by_class_name('_3F6QL _2WovP ')
            time.sleep(3)
            chat_box.self.mensagem
            time.sleep(3)
            self.driver.find_element_by_class_name("_3F6QL _2WovP ")
            time.sleep(3)
            self.driver.get('https://youtube.com')
            grupo.click()
            time.sleep(3)
            chat_box = self.driver.find_elements_by_class_name('_3pkkz V42si copyable-area ')
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_elements_by_class_name('_1Plpp ')
            time.sleep(3)
            grupo.click()
           
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_elements_by_class_name('_2S1VP copyable-text selectable-text ')
            time.sleep(3)
            chat_box.send_keys(self.mensagem)
            time.sleep(3)
            chat_box.send_keys(self.mensagem)
            chat_box.click()
            botao_enviar = self.driver.find_elements_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()