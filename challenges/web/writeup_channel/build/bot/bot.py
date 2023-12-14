# Copyright 2022-2023 USTC-Hackergame
# Copyright 2021 PKU-GeekGame
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from selenium import webdriver
import time
import os
import urllib.parse

os.mkdir("/dev/shm/xss-data")
os.mkdir("/dev/shm/chromium-data")
FLAG = os.getenv("GZCTF_FLAG", "flag{test_flag}")
FLAG = urllib.parse.quote_plus(FLAG)

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")  # sandbox not working in docker
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--user-data-dir=/dev/shm/user-data")
os.environ["TMPDIR"] = "/dev/shm/chromium-data/"
options.add_experimental_option("excludeSwitches", ["enable-logging"])

while True:
    try:
        with webdriver.Chrome(options=options) as driver:
            ua = driver.execute_script("return navigator.userAgent")
            print("I am using", ua)

            print("Putting secret flag...")
            driver.get("http://localhost:5000")
            driver.execute_script(f'document.cookie="flag={FLAG}"')
            time.sleep(1)

            print("- Now browsing website...")
            driver.get("http://localhost:5000")
            time.sleep(4)

            print("Bye bye!")
    except Exception as e:
        print("ERROR", type(e), e)
        print("I'll not give you exception message this time.")

    time.sleep(60)
