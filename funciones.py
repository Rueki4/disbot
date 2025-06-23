import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
import requests
import random

def crear_randomizador(tag : str, canal : str) -> str:
    def nueva_funcion():
        
        last_soup_str = ":("
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
                        code = new_soup_str[j].split("?")[1].split('"')[0]
                        print( new_soup_str[j].split("score:")[1].split(" ")[0] )
                        break
                    url = f"https://rule34.xxx/index.php?page=post&s=view&id={code}"
                    resp = requests.get(url, headers=headers)
                    soup = BeautifulSoup(resp.text, "html.parser")

                    last_soup_str = "https://wimg." + str(soup).split("https://wimg.")[1].split('"')[0]
        except:
            last_soup_str = ":("
        return last_soup_str, canal
    print("De momento todo bien")
    return nueva_funcion

def random_de(tag : str, canal : str, score : int = 0) -> str:
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



# print(random_de("bulma_briefs+-ai_generated"))