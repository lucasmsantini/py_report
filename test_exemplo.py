from selenium import webdriver
import pytest
import autoit
from time import sleep
from locators import Locators
from selenium.common.exceptions import InvalidSelectorException


class Teste_User_PIN():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\GitHub\lucasmsantini\estudoAutomatizaRW\venv\geckodriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePageTitle(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        assert self.driver.title=='Releaser Web'

    def test_host_compatible(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        assert self.driver.find_element_by_id(Locators.input_username_id)
        #assert not self.driver.find_element_by_id('msg_host_incompativel_id')

    def test_host_autenticacao_configurada(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        assert self.driver.find_element_by_id(Locators.input_username_id)
        #self.driver.find_element_by_id(Locators.msg_auth_nao_configurada)

    def test_loginPIN_valid(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_class_name(Locators.login_altera_metodo).click()
        self.driver.find_element_by_id(Locators.input_pin_id).send_keys('0123')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        assert self.driver.find_element_by_xpath(Locators.botao_meusDocs)

    def test_loginPIN_INVALID(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_class_name(Locators.login_altera_metodo).click()
        self.driver.find_element_by_id(Locators.input_pin_id).send_keys('524523542')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        #self.driver.find_elementby_css_selector('#login-form-validation-message > span:nth-child(1)')
        assert self.driver.find_element_by_id(Locators.message_login_fail_id).text == 'Os dados informados estão incorretos. Tente novamente.'
        if self.driver.find_element_by_id(Locators.message_login_fail_id).text == 'Os dados informados estão incorretos. Tente novamente.':
            print('errooooouuu login')
        else:
            print('login correto')

    def test_upload_1_arquivo(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_class_name(Locators.login_altera_metodo).click()
        self.driver.find_element_by_id(Locators.input_pin_id).send_keys('0123')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        self.driver.find_element_by_xpath(Locators.botao_meusDocs).click()  # botão meusDocs
        numero_jobs = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print('1---', numero_jobs)
        self.driver.find_element_by_xpath(Locators.upload_botao_up_sem_dropdown).click()
        sleep(1)
        self.driver.find_element_by_xpath(
            Locators.upload_area_clicavel_para_selecionar_arquivo).click()  # clicar na área pra abrir a janela de escolha de arquiv
        sleep(1)
        path = "C:\\GitHub\\lucasmsantini\\estudoAutomatizaRW\\venv\\test.pdf"
        autoit.send(path)
        autoit.send("{ENTER}")
        sleep(1)
        self.driver.find_element_by_id(Locators.upload_botao_up_final_id).click()
        sleep(2)
        numero_jobs2 = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print('2---', numero_jobs2)
        assert numero_jobs != numero_jobs2

    def test_upload_1_arquivo_again(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_class_name(Locators.login_altera_metodo).click()
        self.driver.find_element_by_id(Locators.input_pin_id).send_keys('0123')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        self.driver.find_element_by_xpath(Locators.botao_meusDocs).click()  # botão meusDocs
        numero_jobs = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print('1---', numero_jobs)
        self.driver.find_element_by_xpath(Locators.upload_botao_up_sem_dropdown).click()
        sleep(1)
        self.driver.find_element_by_xpath(
            Locators.upload_area_clicavel_para_selecionar_arquivo).click()  # clicar na área pra abrir a janela de escolha de arquiv
        sleep(1)
        path = "C:\\GitHub\\lucasmsantini\\estudoAutomatizaRW\\venv\\test.pdf"
        autoit.send(path)
        autoit.send("{ENTER}")
        sleep(1)
        self.driver.find_element_by_id(Locators.upload_botao_up_final_id).click()
        sleep(2)
        numero_jobs2 = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print('2---', numero_jobs2)
        assert numero_jobs != numero_jobs2

    def test_meus_docs_seleciona_somente_um_e_deleta(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_class_name(Locators.login_altera_metodo).click()
        self.driver.find_element_by_id(Locators.input_pin_id).send_keys('0123')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        self.driver.find_element_by_xpath(Locators.botao_meusDocs).click()  # botão meusDocs
        sleep(1)
        numero_jobs = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print('1---', numero_jobs)
        self.driver.find_element_by_xpath(Locators.docs_seleciona_primeiro_item).click()  # botão seleciona o 1º item
        self.driver.find_element_by_id(Locators.docs_excluir_sem_dropdown_id).click()
        self.driver.find_element_by_xpath(Locators.pg_print_botao_Confirmar_sair_alteracoes).click()  #botao OK após Excluir
        sleep(3)
        numero_jobs2 = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print('2---', numero_jobs2)
        assert numero_jobs != numero_jobs2

    def test_meus_docs_seleciona_somente_um_e_manda_imprimir(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_class_name(Locators.login_altera_metodo).click()
        self.driver.find_element_by_id(Locators.input_pin_id).send_keys('0123')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        self.driver.find_element_by_xpath(Locators.botao_meusDocs).click()  # botão meusDocs
        self.driver.find_element_by_xpath(Locators.docs_seleciona_primeiro_item).click()  # botão seleciona o 1º item
        self.driver.find_element_by_xpath(Locators.docs_imprimir_sem_dropdown).click()  # imprimir sem dropdown
        sleep(1)
        self.driver.find_element_by_id(Locators.pg_print_botao_selec_imp_final_id).click()  # botão imprimir final
        try:
            self.driver.find_element_by_xpath(Locators.botao_ok_apos_imprimir).click()  #botao OK após imprimir
            assert Locators.string_sem_saldo_ptBR == 'Documentos selecionados excedem seu saldo'
        except InvalidSelectorException:
            print('---> Sem saldo ')




#  #################################################################################################
#  #################################################################################################
#  #################################################################################################
#  #################################################################################################



class Teste_User_User_Pass_com_tela_de_politica():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Firefox(
            executable_path=r'C:\GitHub\lucasmsantini\estudoAutomatizaRW\venv\geckodriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePageTitle(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        assert self.driver.title == 'Releaser Web'

    def test_host_compatible(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        assert self.driver.find_element_by_id(Locators.input_username_id)
        #assert not self.driver.find_element_by_id(Locators.msg_host_incompativel_id)

    def test_host_autenticacao_configurada(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        assert self.driver.find_element_by_id(Locators.input_username_id)
        #self.driver.find_element_by_id(Locators.msg_auth_nao_configurada)

    def login_user_pass_valid(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_id(Locators.input_username_id).send_keys('santini')
        self.driver.find_element_by_id(Locators.input_password_id).send_keys('321')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        assert self.driver.find_element_by_xpath(Locators.botao_meusDocs)

    def login_user_pass_INVALID(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_id(Locators.input_username_id).send_keys('santini')
        self.driver.find_element_by_id(Locators.input_password_id).send_keys('32132')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        assert self.driver.find_element_by_id(
            Locators.message_login_fail_id).text == 'Os dados informados estão incorretos. Tente novamente.'
        if self.driver.find_element_by_id(
                Locators.message_login_fail_id).text == 'Os dados informados estão incorretos. Tente novamente.':
            print('errooooouuu login')
        else:
            print('login correto')

    def test_upload_1_arquivo(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_id(Locators.input_username_id).send_keys('santini')
        self.driver.find_element_by_id(Locators.input_password_id).send_keys('321')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        self.driver.find_element_by_xpath(Locators.botao_meusDocs).click()  # botão meusDocs
        numero_jobs = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print(numero_jobs)
        self.driver.find_element_by_xpath(Locators.upload_botao_up_sem_dropdown).click()
        sleep(1)
        self.driver.find_element_by_xpath(
            Locators.upload_area_clicavel_para_selecionar_arquivo).click()  # clicar na área pra abrir a janela de escolha de arquiv
        sleep(1)
        path = "C:\\GitHub\\lucasmsantini\\estudoAutomatizaRW\\venv\\test.pdf"
        autoit.send(path)
        autoit.send("{ENTER}")
        sleep(1)
        self.driver.find_element_by_id(Locators.upload_botao_up_final_id).click()
        sleep(2)
        numero_jobs2 = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print(numero_jobs2)
        assert numero_jobs != numero_jobs2

    def test_upload_1_arquivo_again(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_id(Locators.input_username_id).send_keys('santini')
        self.driver.find_element_by_id(Locators.input_password_id).send_keys('321')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        self.driver.find_element_by_xpath(Locators.botao_meusDocs).click()  # botão meusDocs
        numero_jobs = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print(numero_jobs)
        self.driver.find_element_by_xpath(Locators.upload_botao_up_sem_dropdown).click()
        sleep(1)
        self.driver.find_element_by_xpath(
            Locators.upload_area_clicavel_para_selecionar_arquivo).click()  # clicar na área pra abrir a janela de escolha de arquiv
        sleep(1)
        path = "C:\\GitHub\\lucasmsantini\\estudoAutomatizaRW\\venv\\test.pdf"
        autoit.send(path)
        autoit.send("{ENTER}")
        sleep(1)
        self.driver.find_element_by_id(Locators.upload_botao_up_final_id).click()
        sleep(2)
        numero_jobs2 = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print(numero_jobs2)
        assert numero_jobs != numero_jobs2

    def test_meus_docs_seleciona_somente_um_e_deleta(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_id(Locators.input_username_id).send_keys('santini')
        self.driver.find_element_by_id(Locators.input_password_id).send_keys('321')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        self.driver.find_element_by_xpath(Locators.botao_meusDocs).click()  # botão meusDocs
        sleep(1)
        numero_jobs = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print('1---', numero_jobs)
        self.driver.find_element_by_xpath(Locators.docs_seleciona_primeiro_item).click()  # botão seleciona o 1º item
        self.driver.find_element_by_id(Locators.docs_excluir_sem_dropdown_id).click()
        self.driver.find_element_by_xpath(Locators.pg_print_botao_Confirmar_sair_alteracoes).click()  #botao OK após Excluir
        sleep(3)
        numero_jobs2 = (self.driver.find_element_by_xpath(Locators.docs_rodape_numero_docs_info).text)
        print('2---', numero_jobs2)
        assert numero_jobs != numero_jobs2

    def test_meus_docs_seleciona_somente_um_e_manda_imprimir(self, setup):
        self.driver.get('http://ndd-vm-tes4922:8082')
        self.driver.find_element_by_id(Locators.input_username_id).send_keys('santini')
        self.driver.find_element_by_id(Locators.input_password_id).send_keys('321')
        self.driver.find_element_by_id(Locators.login_botao_submit_id).click()
        sleep(3)
        self.driver.find_element_by_xpath(Locators.botao_meusDocs).click()  # botão meusDocs
        self.driver.find_element_by_xpath(Locators.docs_seleciona_primeiro_item).click()  # botão seleciona o 1º item
        self.driver.find_element_by_xpath(Locators.docs_imprimir_sem_dropdown).click()  # imprimir sem dropdown
        sleep(1)
        try:
            assert Locators.string_sem_saldo_ptBR == 'Documentos selecionados excedem seu saldo'
            self.driver.find_element_by_id(Locators.pg_print_botao_selec_imp_final_id).click()  # botão imprimir final
        except InvalidSelectorException:
            print('---> Sem saldo')
        #self.driver.find_element_by_xpath(Locators.botao_ok_apos_imprimir).click()  # botao OK após imprimir


#  pytest -v -s --html=report.html test_exemplo.py



'''
with open('locators.json', 'r') as j:
    json_data = json.load(j)
    print(json_data)

def teste_loginPIN_INVALID1():
    driver = webdriver.Firefox(executable_path=r'C:\GitHub\lucasmsantini\estudoAutomatizaRW\venv\geckodriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://ndd-vm-tes4922:8082')
    #driver.find_element_by_class_name(Locators.login_altera_metodo).click()
    driver.find_element_by_class_name(json.load(login_altera_metodo)).click()
    driver.find_element_by_id(Locators.input_pin_id).send_keys('6667647476')
    driver.find_element_by_id(Locators.login_botao_submit_id).click()
    #self.driver.find_elementby_css_selector('#login-form-validation-message > span:nth-child(1)')
    try:
        print('1:', driver.find_element_by_id(Locators.message_login_fail_id).text)
        print('2:', driver.find_element_by_id(Locators.message_login_fail_id).get_property('id'))
        print('3:', driver.find_element_by_xpath(Locators.message_login_fail).text)
    except NoSuchElementException:
        pass
    if driver.find_element_by_id(Locators.message_login_fail_id).text == 'Os dados informados estão incorretos. Tente novamente.':
        print('errooooouuu login')
    else:
        print('login correto')

teste_loginPIN_INVALID1()'''