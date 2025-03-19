#
#     **             **                  
#    ****    ****** //                   
#   **//**  /**///** **  ******  ******* 
#  **  //** /**  /**/** **////**//**///**
# **********/****** /**/**   /** /**  /**
#/**//////**/**///  /**/**   /** /**  /**
#/**     /**/**     /**//******  ***  /**
#//      // //      //  //////  ///   //


#          Author: APION🔌

import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, init 
import pyfiglet
from urllib.parse import urlparse
import sys
import signal
import os
#from undetected_chromedriver import ChromeOptions

proxies = [ 
    ""
    ]

# Initialize colorama 
init(autoreset=True)

def signal_handler(sig, frame): 
    print("\nCtrl + C pressed. Exiting the script...") 
    #sys.exit(0) # Register the signal handler for SIGINT 
    main_menu()
signal.signal(signal.SIGINT, signal_handler)

def is_url(input_text): 
    try: 
        result = urlparse(input_text) 
        return all([result.scheme, result.netloc]) 
    except ValueError: 
        return False
    
def loading_animation(duration): 
    animation = "|/-\\" 
    idx = 0 
    start_time = time.time() 
    while time.time() - start_time < duration: 
        sys.stdout.write("\r" + animation[idx % len(animation)] + " 🎶 Playing ") 
        sys.stdout.flush() 
        idx += 1 
        time.sleep(0.1) 
    sys.stdout.write("\r🎵 Done Playing! ⏏️ \n")

def wait_animation(duration): 
    animation = "|/-\\" 
    idx = 0 
    start_time = time.time() 
    while time.time() - start_time < duration: 
        sys.stdout.write("\r" + animation[idx % len(animation)] + " ⏱️ Waiting ") 
        sys.stdout.flush() 
        idx += 1 
        time.sleep(0.1) 
    sys.stdout.write("\r⏰ Done Waiting! \n")

def read_file_to_list(file_path): 
    with open(file_path, 'r') as file: items = [line.strip() for line in file] 
    return items

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    letters = string.ascii_lowercase
    email_user = ''.join(random.choice(letters) for i in range(10))
    domain = random.choice(domains)
    random_email = f"{email_user}@{domain}"
    return random_email

def generate_random_month():
    months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
    letters = string.ascii_lowercase
    random_month = ''.join(random.choice(letters) for i in range(10))
    months = random.choice(months)
    random_month = f"{months}"
    return random_month

def generate_random_day():
    return random.randint(1, 30)

def generate_random_year():
    return random.randint(1990, 2006)

def generate_random_username(): 
    letters = string.ascii_lowercase 
    username = ''.join(random.choice(letters) for i in range(8))
    return username

def generate_random_headers():
     user_agents = [ "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15A372 Safari/604.1" ]
     accept_languages = [ 'en-US,en;q=0.9', 'en-GB,en;q=0.8', 'fr-FR,fr;q=0.9', 'es-ES,es;q=0.9' ] 
     headers = { 'User-Agent': random.choice(user_agents), 
                'Accept-Language': random.choice(accept_languages), 
                'X-Custom-Header': ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(200)) } 
     return headers

def random_sleep(min_time=2, max_time=5): 
    time.sleep(random.uniform(min_time, max_time))

def random_sleep2(min_seconds, max_seconds): 
    return random.uniform(min_seconds, max_seconds)

def save_emails_to_list(num_emails):
    email_list = [generate_random_email() for _ in range(num_emails)]
    with open("spotify_emails.txt", "w") as file:
        for email in email_list:
            file.write(email + "\n")
    return email_list

def get_random_proxy(): 
    return random.choice(proxies)

def register(email):
    # Set up the Chrome WebDriver
    username = generate_random_username()
    random_month = generate_random_month()
    random_day = generate_random_day()
    random_year = generate_random_year()
    proxy = get_random_proxy() 
    options = webdriver.ChromeOptions()
    #options.add_argument('--disable-web-security') 
    #options.add_argument('--headless')
    #options.add_argument('--allow-running-insecure-content') 
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-data-dir=C:/Users/aosha/AppData/Local/Google/Chrome/User Data/Profile 1")
    options.add_argument("--profile-directory=Profile 1")
    options.add_argument(f"--proxy-server={proxy}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    headers = generate_random_headers() 
    driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': headers})

    try:
        # Open Spotify registration page
        driver.get("https://www.spotify.com/signup/")
        random_sleep(1, 3)
        print("💉 email = " + email)
        # Fill in the registration form
        driver.find_element(By.XPATH, "//*[@id='username']").send_keys(email)
        random_sleep()
        driver.find_element(By.XPATH, "/html/body/div[1]/main/main/section/div/form/button").click()
        random_sleep()
        print("💉 password = **********")
        driver.find_element(By.XPATH, "//*[@id='new-password']").send_keys("hitler301998")
        random_sleep()
        driver.find_element(By.XPATH, "/html/body/div[1]/main/main/section/div/form/div[2]/button").click()
        random_sleep()
        driver.find_element(By.XPATH, "//*[@id='displayName']").send_keys(username)
        print("💉 Username = " + username)
        random_sleep()
        driver.find_element(By.XPATH, "//*[@id='day']").send_keys(random_day)
        print("💉 Day = " + str(random_day))
        random_sleep()
        driver.find_element(By.XPATH, "//*[@id='month']").send_keys(random_month)
        print("💉 Month = " + str(random_month))
        random_sleep()
        driver.find_element(By.XPATH, "//*[@id='year']").send_keys(random_year)
        print("💉 Year = " + str(random_year))
        random_sleep()
        driver.find_element(By.XPATH, "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[4]/label").click()
        random_sleep()
        driver.find_element(By.XPATH, "/html/body/div[1]/main/main/section/div/form/div[2]/button").click()
        random_sleep()
        driver.find_element(By.XPATH, "/html/body/div[1]/main/main/section/div/form/div[2]/button").click()
        print("💉 🌐web")
        random_sleep()
        
        try:
            #WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div[1]")) )
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div[1]")
            #WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div[1]")) )
            print("reCAPTCHA found!")
            if driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div[1]") :
                 rule = input("Completed Captcha Y/N: ")
                 if rule == "y" or rule == "Y" and WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div[1]")) ):
                    print("captcha completed")
                    driver.find_element(By.XPATH, '//*[@id="encore-web-main-content"]/div/div/div/div/div/div/button').click()
                    with open("spotreg_emails.txt", "a") as file:
                        file.write(email + "\n")
                    print(email + " Written to file")
                    time_sleep = random_sleep2(180, 300)
                    wait_animation(time_sleep)
                    return
                    #random_sleep()
            else:
            #driver.execute_script("arguments[0].setAttribute('type', 'none');", driver.find_element(By.XPATH, '//*[@id="recaptcha-token"]))
            #driver.find_element(By.XPATH, "/html/body/input").click()
            #time.sleep(10)
            #driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/button").click()
            #time.sleep(86400)
                print("captcha fail")
                return
        except NoSuchElementException: 
            print("No reCAPTCHA found.") # Handle the absence of reCAPTCHA as needed
            print(" 💾 " + email)
            with open("spotreg_emails.txt", "a") as file:
                    file.write(email + "\n")
            #random_sleep(180, 300)
            time_sleep = random_sleep2(180, 300)
            wait_animation(time_sleep)
            return

        driver.delete_all_cookies()
        # Clear cache using JavaScript 
        driver.execute_script("window.localStorage.clear();") 
        driver.execute_script("window.sessionStorage.clear();")
    finally:
        driver.quit()


def stream(email, url):
    if is_url(url):
        # Set up the Chrome WebDriver
        proxy = get_random_proxy() 
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-data-dir=C:/Users/aosha/AppData/Local/Google/Chrome/User Data/Profile 1")
        options.add_argument("--profile-directory=Profile 1")
        options.add_argument(f"--proxy-server={proxy}")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        headers = generate_random_headers() 
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': headers})
        try:
            # Log in to Spotify
            driver.get("https://accounts.spotify.com/login")
            random_sleep(1, 3)
            driver.find_element(By.XPATH, "//*[@id='login-username']").send_keys(email)
            random_sleep()
            print("💉 email = " + email)
            #your password goes here
            driver.find_element(By.XPATH, "//*[@id='login-password']").send_keys("Yourpassword")
            print("💉 password = **********")
            random_sleep()
            driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
            # Wait for login to complete
            random_sleep()

            # Navigate to a music stream page
            driver.get(url)
            print("💉 🌐web")
            random_sleep()

            # Play the music
            WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[3]/div[2]/div/div/div/button")) )
            driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[3]/div[2]/div/div/div/button").click()
            random_sleep()
            #element_view = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[1]/div[3]/div[3]/div/span[8]")
            #element_text_view = element_view.text
            #print("🎵 plays: "+ element_text_view)
            #element = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[1]/div[3]/div[3]/span[2]/h1")
            #element_text = element.text
            #print(" 💉 Song: "+ element_text)

            #time.sleep(15)  # Adjust the sleep time as needed
            time_sleep = random_sleep2(35, 45)
            loading_animation(time_sleep)
            print(email +" 💊 "+" + "+" 🎵 ")
            print(Fore.GREEN + "----------------------------------------")

            #driver.get("https://accounts.spotify.com/en/status")
            random_sleep()
            #driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/p/button").click()
            driver.delete_all_cookies()
            # Clear cache using JavaScript 
            driver.execute_script("window.localStorage.clear();") 
            driver.execute_script("window.sessionStorage.clear();")
        finally:
            driver.quit()
            #driver.delete_all_cookies()
    elif url.lower() == "q":
        print("")
        main_menu()
    else:
        print("Invalid input. Please enter a Url.") 
        print("")

def main_menu():
     # Generate random emails and save them to a list
    header = pyfiglet.figlet_format("SpotiBot", font="slant")
    # Print the header with colors 
    while True:
        os.system('cls')
        print("")
        print(Fore.CYAN + header) 
        print(Fore.GREEN + "----------------------------------------")
        print(Fore.GREEN + "     💉🌐 Register / 💉💿 Stream      ")
        print(Fore.GREEN + "----------------------------------------")
        print(Fore.GREEN + "           Author: APION🔌              ") 
        print(Fore.GREEN + "            Version: 1.0🛠️              ") 
        print(Fore.YELLOW + "========================================")
        print(Fore.YELLOW + "💊 Manual Captcha completion until we find a way")
        print(Fore.YELLOW + "🔐 All Accounts are created With Password set in file!!")
        print(Fore.YELLOW + "- ctrl + c = menu")
        print(Fore.YELLOW + "- q = quit (Only Main Menu)")
        print(Fore.YELLOW + "- Register = R")
        print(Fore.YELLOW + "- Stream = S")
        print("")
        print("")
        rule = input("Spotibot 💉🦠 => ")
        print("")
        if rule.lower() == "r":
            email_count = input("Number Of Accounts (eg 1) 💉 🖥️  => ")
            try:
                num_emails = int(email_count)  # Number of random emails to generate
                email_list = save_emails_to_list(num_emails)
                print(f"Generated {num_emails} random emails:")
                print("\n".join(email_list))
            except ValueError:
                print("Spotibot 'Can't Read?' ")
                print("Bye! ")
                break
            # Use the first email to register and stream music on Spotify
            if email_list:
                for i in email_list:
                    register(i)

        elif rule.lower() == "s":
            file_path = 'spotreg_emails.txt'
            items = read_file_to_list(file_path)
            url = input("Spotify Music/Audio Link 💉🌐web => ")
            # Use the first email to register and stream music on Spotify
            for i in items:
                stream(i, url)
        elif rule.lower() == "q":
            sys.exit()
        else:
            print("Invalid input. Please enter 'R' to register or 'S' to stream.") 
            continue

if __name__ == "__main__":
    main_menu()
