import subprocess
import time

def main():
    chrome_process = subprocess.Popen("pytest --browser=chrome", shell=True)
    edge_process = subprocess.Popen("pytest --browser=edge", shell=True)

    while True:
        chrome_status = chrome_process.poll()
        edge_status = edge_process.poll()

        if chrome_status is not None and edge_status is not None:
            break  

        time.sleep(2)  

if __name__ == "__main__":
    main()