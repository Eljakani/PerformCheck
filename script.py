import threading
import requests
import time
import json
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored, cprint
from tqdm import tqdm
import random
import string

def send_request(url, username, password, results, index, progress_bar, success_counter):
    try:
        start_time = time.time()
        response = requests.post(url, data={'username': username, 'password': password}, allow_redirects=True)
        end_time = time.time()
        response_time = end_time - start_time
        results[index] = response_time
        if response.status_code == 200 or response.status_code == 302: 
            success_counter['count'] += 1
    except requests.RequestException as e:
        results[index] = 'Error'
        cprint(f"Erreur lors de l'envoi de la requête {index+1}: {str(e)}", 'red')
    finally:
        progress_bar.update(1)

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))
def banner():
    print('''
     __   ___  __   ___  __   __                   __   ___     __        ___  __       
    |__) |__  |__) |__  /  \ |__)  |\/|  /\  |\ | /  ` |__     /  ` |__| |__  /  ` |__/ 
    |    |___ |  \ |    \__/ |  \  |  | /~~\ | \| \__, |___    \__, |  | |___ \__, |  \ 
                                                                                        
    ''')
    print(colored('[+] By : MrPatcher', 'red', attrs=['bold']))
    print("------------------------------------------------")
def main():
    url = input(colored('URL de la requête : ', 'blue', attrs=['bold']))
    num_threads = int(input(colored('Nombre de threads (requêtes simultanées) : ', 'blue', attrs=['bold'])))
    num_requests = int(input(colored('Nombre de requêtes à envoyer : ', 'blue', attrs=['bold'])))

    results = [None] * num_requests
    success_counter = {'count': 0}

    threads = []
    cprint('Envoi des requêtes HTTP...', 'green')

    progress_bar = tqdm(total=num_requests, unit='request')

    for i in range(num_requests):
        username = generate_random_string(8)
        password = generate_random_string(10)
        thread = threading.Thread(target=send_request, args=(url, username, password, results, i, progress_bar, success_counter))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    progress_bar.close()

    cprint('Toutes les requêtes ont été envoyées.', 'green')

    total_requests = num_requests
    success_requests = success_counter['count']
    error_requests = total_requests - success_requests
    print(colored('\nStatistiques des requêtes :\n', 'blue', attrs=['bold']))
    print(f"Total de requêtes : {total_requests}")
    print(f"Requêtes réussies (code de statut 200 ou 302) : {success_requests}")
    print(f"Requêtes en erreur : {error_requests}")

    print(colored('\nGénération du graphique...', 'blue', attrs=['bold']))
    fig, ax = plt.subplots()
    response_times = [rt if rt != 'Error' else 0 for rt in results]
    bar_colors = ['green' if rt != 'Error' else 'red' for rt in results]
    ax.bar(range(1, num_requests + 1), response_times, color=bar_colors)
    ax.set_xlabel('Numéro de requête')
    ax.set_ylabel('Temps de réponse (secondes)')
    ax.set_title('Temps de réponse des requêtes HTTP')
    plt.show()
    print(colored('Statistiques', 'blue', attrs=['bold']))


    export_path = input(colored("Chemin d'exportation du fichier JSON : ", 'blue', attrs=['bold']))
    data = {
        'results': results,
        'total_requests': total_requests,
        'success_requests': success_requests,
        'error_requests': error_requests
    }
    with open(export_path, 'w') as fichier:
        json.dump(data, fichier)

    cprint(f'\nLes résultats ont été enregistrés dans le fichier "{export_path}".', 'green')

if __name__ == '__main__':
    banner()
    main()
