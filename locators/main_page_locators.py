from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    ORDER_FEED_BUTTON = (By.CSS_SELECTOR, "a[href='/feed']")
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_MODAL_NAME = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
    BUN_INGREDIENT = (By.XPATH, "//a[.//p[text()='Флюоресцентная булка R2-D3']]")
    CONSTRUCTOR_AREA = (By.CSS_SELECTOR, "section.BurgerConstructor_basket__29Cd7")
    ADDED_BUN_TOP = (By.CSS_SELECTOR, "img[alt='Флюоресцентная булка R2-D3 (верх)']")
    
    PERSONAL_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")   
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    LOADING_MODAL = (By.CSS_SELECTOR, "div.Modal_modal__P3_V5")