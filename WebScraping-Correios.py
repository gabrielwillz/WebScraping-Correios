import requests
from bs4 import BeautifulSoup

def main():
    print('\033[1;33m')
    print('###############################')
    print('#### RASTREAMENTO CORREIOS ####')
    print('###############################')
    print('\033[0;0m')
    
    codigo_rastreo = str(input('\033[1;32mColoque o número de rastreio ===>>> \033[0;0m'))


    req = requests.post(url='https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?',
                        data={'objetos': codigo_rastreo})
    soup = BeautifulSoup(req.text, 'html.parser')
    dados = soup.find_all(class_="listEvent sro")

    for i in dados:
        ult_atu = i.find(class_="sroLbEvent").text.split()
        ult_atu = ' '.join(map(str, ult_atu))
        data = i.find(class_="sroDtEvent").text.split()[0]
        print(f'\033[;1mStatus: {ult_atu} - Data: {data} - CODIGO: {codigo_rastreo}\033[0;0m')
        print()
        print('\033[1;91m-------------------------------------------------------------\033[0;0m')
        print()

    option = int(input('Quer fazer outro rastreamento?\n 1. SIM\n 2. NÃO\n'))
    print('====>>>>')

    if option == 1:
        main()
    else:
        print('Saindo.......')


if __name__ == '__main__':
    main()
