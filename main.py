import random
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_names():
    name_list = ["Ali", "Ahmed", "Hassan", "Usman", "Bilal", "Imran", "Faisal", "Kamran", "Nadeem", "Rizwan",
                  "Abdullah", "Arif", "Tariq", "Irfan", "Aamir", "Kashif", "Majid", "Nasir", "Shahid", "Sohail",
                  "Qasim", "Tahir", "Asad", "Rafiq", "Yasin", "Riaz", "Mubashir", "Murtaza", "Farhan", "Muzammil",
                  "Saad", "Tanveer", "Zubair", "Waqar", "Salman", "Rashid", "Azhar", "Javed", "Junaid", "Moin",
                  "Nasir", "Yousaf", "Haroon", "Adnan", "Mehmood", "Akhtar", "Sultan", "Hamza", "Zahid", "Shabbir",
                  "Zia", "Fahad", "Jamil", "Sajid", "Adeel", "Raheel", "Noman", "Shakeel", "Rauf", "Iqbal", "Jawad",
                  "Arshad", "Amir", "Waheed", "Rameez", "Najeeb", "Sabir", "Zulfiqar", "Ijaz", "Saleem", "Atif",
                  "Aftab", "Zafar", "Fahim", "Hafeez", "Khurram", "Luqman", "Nawaz", "Adil", "Aurangzeb", "Tanweer",
                  "Ahsan", "Qaiser", "Ghulam", "Shoaib", "Pervez", "Ilyas", "Sharif", "Younis", "Sarwar", "Azam",
                  "Noman", "Shafiq", "Mudassir", "Rahim", "Babar", "Waseem", "Abid", "Tauseef", "Asif", "Nisar",
                  "Yaqoob", "Khalid", "Zaman","Aisha", "Sana", "Fatima", "Hira", "Nadia", "Samina", "Farida", "Naima", "Zainab", "Mehak",
                    "Saima", "Tahira", "Noreen", "Bushra", "Ambreen", "Tasneem", "Sadia", "Fauzia", "Gulnaz", "Shabnam",
                    "Nighat", "Nusrat", "Rukhsar", "Shazia", "Shahnaz", "Shamim", "Nida", "Nazia", "Hina", "Asma",
                    "Rabia", "Zeba", "Naila", "Nadia", "Iram", "Kausar", "Najma", "Sabiha", "Shaista", "Shehnaz",
                    "Sobia", "Tabassum", "Uzma", "Yasmin", "Fareeha", "Sarwat", "Shama", "Shazia", "Fozia", "Lubna",
                    "Samar", "Aneela", "Farkhanda", "Huma", "Kanwal", "Parveen", "Razia", "Roohi", "Tania", "Umaima",
                    "Yasmeen", "Nayab", "Rukhsana", "Zohra", "Fahmida", "Gulshan", "Iffat", "Javeria", "Kiran", "Madiha",
                    "Naheed", "Quratulain", "Roshan", "Shireen", "Zubaida", "Atiya", "Fariha", "Ishrat", "Laila", "Marina",
                    "Rehana", "Sajida", "Shakeela", "Tanzila", "Yumna", "Bisma", "Hooriya", "Maimoona", "Nabeela", "Rafia",
                    "Sabiya", "Tahira", "Ummara", "Zarish", "Farzana", "Jannat", "Kinza", "Naima", "Rukhsar", "Sarina",
                    "Tayyaba", "Uzma", "Wajiha", "Yasira", "Zainab"]

    return random.choice(name_list)

def join_meeting(driver):
    driver.get(input_url)
    base_uri = ""
    is_base_uri = False
    while is_base_uri == False:
        try:
            base_uri = driver.find_element(By.ID,'teamsLauncher').get_property("baseURI")
            if base_uri:
                is_base_uri = True
        except Exception as e:
            print(e)
        finally:
            continue

    driver.execute_script("window.open();")

    new_tab = driver.window_handles[-1]

    first_tab = driver.window_handles[0]
    driver.switch_to.window(first_tab)
    driver.close()

    driver.switch_to.window(new_tab)
    driver.get(base_uri)
    
    is_join_Btn = False
    joinBtn = ''

    while is_join_Btn ==False:
        try:
            joinBtn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,'button[aria-label="Join meeting from this browser"]'))
            )
            if joinBtn:
                is_join_Btn = True

        finally:
            continue

    joinBtn = driver.find_element(By.CSS_SELECTOR,'button[aria-label="Join meeting from this browser"]')
    joinBtn.click()

    is_loaded = False
    element_visible = ''
 
    while is_loaded ==False:
        try:
            element_visible = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "iframe"))
            )
            if element_visible:
                is_loaded = True
        finally:
            continue

    driver.switch_to.frame(element_visible)

    input_name = ''
    is_page_fully_loaded = False

    while is_page_fully_loaded == False:
        try:
            input_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,'input[placeholder="Type your name"]'))
            )
            if input_name:
                is_page_fully_loaded = True
        finally:
            continue

    if input_name:
        input_name.send_keys(get_names())

        disable_mic = driver.find_element(By.CSS_SELECTOR,'div[title="Microphone"]')
        disable_mic.click()

        disable_cam = driver.find_element(By.CSS_SELECTOR,'div[title="Camera"]')
        disable_cam.click()

        join_btn = driver.find_element(By.CSS_SELECTOR,'button[aria-label="Join now"]')
        join_btn.click()

    is_meeting_ended = False

    while is_meeting_ended == False:
        try:
            btn = driver.find_element(By.CSS_SELECTOR,'button[data-tid="anon-meeting-end-screen-rejoin-button"]')
            if btn:
                is_meeting_ended = True
        except:
            continue
    print("Meeting has been ended or you have been removed.")
    driver.close()


#start chrome webdriver
input_url = input("Enter URL of the meeting:")
number_of_instances = int(input("How many Users would you like to add:"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument('--headless')

chrome_drivers = []
for i in range(0,number_of_instances):
    driver = webdriver.Chrome(options=chrome_options)
    chrome_drivers.append(driver)


for driver in chrome_drivers:
    t = threading.Thread(target=join_meeting, args=[driver])
    t.start()

    