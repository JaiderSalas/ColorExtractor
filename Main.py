from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from colorthief import ColorThief
import time


def capture_screenshot(url, output_path="screenshot.png"):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1280,1024")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(3)  # Esperar a que la página cargue completamente
    driver.save_screenshot(output_path)
    driver.quit()
    print(f"Screenshot guardado en {output_path}")

    # Reducir el tamaño de la imagen para mejorar la extracción de colores
    img = Image.open(output_path)
    img = img.resize((200, 200))
    img.save(output_path)

def get_main_colors(image_path, num_colors=5):
    color_thief = ColorThief(image_path)
    palette = color_thief.get_palette(color_count=num_colors, quality=1)
    
    filtered_colors = [
        color for color in palette
    ]

    return filtered_colors

if __name__ == "__main__":
    all_colors = {}
    url = input("Ingrese una url (Incluye el https://): ")
    
    image_path = "screenshot.png"
    
    capture_screenshot(url, image_path)
    main_colors = get_main_colors(image_path)
        
    


