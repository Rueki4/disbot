import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
import requests
import random

def crear_randomizador(tag : str) -> str:
    def nueva_funcion():
        
        last_soup_str = ":("
        error_code = 0
        try:
            url = "https://rule34.xxx/index.php?page=post&s=list&tags=" + tag + "+&pid=0"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }

            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, "html.parser")

            soup_str = str(soup).split("\n")
            error_code = 1
            
            for i in range(len(soup_str)):
                if ";pid=" in soup_str[i]:
                    error_code = 2
                    last_pid = soup_str[i].split('pid=')[-1].split('"')[0]
                    if int(last_pid) > 200000:
                        last_pid = "200000"
                    pid = random.randint(0, int(last_pid))
                    url = f"{url[0:-1]}{pid}"

                    print(f"{last_pid} -> {pid}")
                    
                    
                    resp = requests.get(url, headers=headers)
                    soup = BeautifulSoup(resp.text, "html.parser")
                    error_code = 3

                    new_soup_str = str(soup).split("\n")
                    error_code = 4
                    for j in range(len(new_soup_str)):
                        if "score" in new_soup_str[j]:
                            code = new_soup_str[j].split("?")[1].split('"')[0]
                            break
                    # print(code)
                    error_code = 5
                    url = f"https://rule34.xxx/index.php?page=post&s=view&id={code}"
                    error_code = 6
                    resp = requests.get(url, headers=headers)
                    error_code = 7
                    soup = BeautifulSoup(resp.text, "html.parser")
                    error_code = 8

                    last_soup_str = "https://wimg." + str(soup).split("https://wimg.")[1].split('"')[0]
        except:
            last_soup_str = error_code
        return last_soup_str
    return nueva_funcion

def random_de(tag : str, canal : str) -> str:
    try:
        url = "https://rule34.xxx/index.php?page=post&s=list&tags=" + tag + "+&pid=0"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")

        soup_str = str(soup).split("\n")
        indice_pass = 0
        for i in range(len(soup_str)):
            if ";pid=" in soup_str[i]:
                last_pid = soup_str[i].split('pid=')[-1].split('"')[0]
                pid = random.randint(0, int(last_pid))
                url = f"{url[0:-1]}{pid}"
                
                resp = requests.get(url, headers=headers)
                soup = BeautifulSoup(resp.text, "html.parser")

                new_soup_str = str(soup).split("\n")
                for j in range(len(new_soup_str)):
                    if "score" in new_soup_str[j]:
                        if int(new_soup_str[j].split("score:")[1].split(" ")[0]) > score:
                            code = new_soup_str[j].split("?")[1].split('"')[0]
                            break
                url = f"https://rule34.xxx/index.php?page=post&s=view&id={code}"
                resp = requests.get(url, headers=headers)
                soup = BeautifulSoup(resp.text, "html.parser")

                last_soup_str = "https://wimg." + str(soup).split("https://wimg.")[1].split('"')[0]
    except:
        last_soup_str = "Enjoying the goon sesion?"
    return last_soup_str



funcion = crear_randomizador('-ai_generated+boobs')

print(funcion())
print(funcion())
print(funcion())
print(funcion())
print(funcion())