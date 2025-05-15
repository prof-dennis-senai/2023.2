from django.urls import reverse
from app_home.models import PizzaModel

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Ative se quiser rodar sem interface
    options.add_argument('--disable-gpu')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


@pytest.mark.django_db
def test_colaborador_nome_opcao_registrar_acao(live_server, browser):
    PizzaModel.objects.create(
        pizza="Mussarela",
        ingredientes="Mussarela, tomate, cebola",
        preco=30.00
    )

    url = live_server.url + reverse('home')
    browser.get(url)

    # Espera o botão com o texto "Adicionar no carrinho" ficar clicável
    wait = WebDriverWait(browser, 10)
    botao = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div/a"))
    )
    botao.click()

    carrinho_botao = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/header/nav/ul/li[3]/a"))
    )
    carrinho_botao.click()

    comprar_botao = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/main/span/a[2]"))
    )
    comprar_botao.click()

    # Valida que o texto "Mussarela" está presente na página após o clique
    assert "Seu Pedido chegou no balcão" in browser.page_source
