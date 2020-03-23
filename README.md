# wikikey_rss

<h3>Steps:</h3>
  Step 1: GO TO THE FOLDER and OPEN TERMINAL
  
  <br>Optionl step: Create Virtual Environment
  
  ```bash
    python3 -m virtualenv venv
  ```
  ```bash
    source venv/bin/activate
  ```
  <br>Step 2: Install Packages
  
  ```bash
  pip3 install -r requirement.txt
  ```
  <br>Step 3: Run main.py
  ```bash
  python3 main.py -o soup
  ```
  OR
  ```bash
  python3 main.py -o regex
   ```
  Data will be saved in data folder in .txt format
  
  ## Additional
  <h3>Setting Up Cron Job For Continous Extraction</h3>
  
  ```bash
  vim /etc/crontab
  (append following command)
  0 0 * * * root /usr/bin/env python3 PATH_TO_FOLDER/main.py -o soup
  ```
  Save your cron file
