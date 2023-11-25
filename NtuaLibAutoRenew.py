"""
MY AUTO RENEW APPLICATION (LINUX VERSION) only changes in the final step
"""
import time
from datetime import date, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import gui
import subprocess
import os


def book_to_renew_row(books_sum_):
    books_rows = []
    for book_row in range(2, books_sum_ + 2):
        r_date_str = driver.find_element(By.XPATH,
                                         f"/html/body/div[1]/div[3]/div[2]/div/div[4]/form/table/tbody/tr[{book_row}]/td[3]").text
        # r_date_str = " DUE 06-02-23 " and has to become 2023-02-06.
        dates_list = r_date_str.strip()[4:12].split('-')
        r_date = date(int('20' + dates_list[2]), int(dates_list[1]), int(dates_list[0]))
        three_days_before_return_date = [r_date - timedelta(days=i) for i in range(4)]
        if date.today() in three_days_before_return_date:
            books_rows.append(book_row)
    return books_rows


gui.set_credentials()
with open('credentials', 'r') as f:
    credentials = [s.replace('\n', '') for s in f.readlines()]
libID = credentials[0]
password = credentials[1]

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver.set_window_position(-2000, 0)  # move the driver off the screen.
time.sleep(2)

driver.get(
    f'https://opac.seab.gr/iii/cas/login?service=https%3A%2F%2Fopac.seab.gr'
    f'%3A443%2Fpatroninfo~S7*gre%2FIIITICKET&lang=gre&scope=7')

time.sleep(4)
driver.find_element("id", 'code').send_keys(libID)
time.sleep(4)

driver.find_element("id", 'pin').send_keys(password)
driver.find_element("xpath", '//*[@id="login"]/fieldset/input').submit()

time.sleep(4)

# navigate to borrowed
driver.find_element("xpath", '//*[@id="patButChkouts"]/div/a').click()

# Book is in the first row of borrowed so books_sum = 1
checkout_table = driver.find_element("xpath", '//*[@id="checkout_form"]/table')
books_sum = len(checkout_table.find_elements(By.TAG_NAME, 'tr')) - 1

books = book_to_renew_row(books_sum)
if books:
    for book in books:
        driver.find_element("xpath",  # click all the books to be renewed
                            f'/html/body/div[1]/div[3]/div[2]/div/div[4]/form/table/tbody/tr[{book}]/td[1]/input').click()

    driver.find_element("xpath",  # renew selected button
                        '/html/body/div[1]/div[3]/div[2]/div/div[4]/form/a[6]/div/div/span/span').click()
    driver.find_element("xpath",  # click yes button (to renew them)
                        '/html/body/div[1]/div[3]/div[2]/div/form/span[1]/a[1]/div/div/span/span').click()
    time.sleep(5)

driver.quit()


def build_exe_and_send_in_startup():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    setup_py_path = os.path.join(script_dir, 'setup.py')
    # Run the build command
    print('reached here')
    subprocess.call(["python", setup_py_path, "build"])
    executable_path = os.path.join(script_dir, 'build/exe.linux-x86_64-3.10/NtuaLibAutoRenew')
    autostart_dir = os.path.expanduser('~/.config/autostart')
    os.makedirs(autostart_dir, exist_ok=True)
    # Create .desktop file content
    desktop_entry = f"""[Desktop Entry]
Type=Application
Exec={executable_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=NtuaLibAutoRenew
Comment=Auto renew library books
"""
    # Write .desktop file
    desktop_file_path = os.path.join(autostart_dir, 'NtuaLibAutoRenew.desktop')
    with open(desktop_file_path, 'w') as desktop_file:
        desktop_file.write(desktop_entry)
    os.chmod(executable_path, 0o775)  # Adjust permissions as needed
    print("Setup complete, executable added to startup.")


build_exe_and_send_in_startup()
# %%
