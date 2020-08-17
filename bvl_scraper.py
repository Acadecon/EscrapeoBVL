import requests
from bs4 import BeautifulSoup

# URL de información financiera
# r = requests.get(url_uf, verify=False)
# r.status_code
# print(r.ok)


def respuesta(url):
    r = requests.get(url)
    print(r.status_code)
    if not r.ok:
        print('El servidor respondió: ', r.status_code)
    else:
        sopa = BeautifulSoup(r.text, 'lxml')
    return sopa


def main():
    url_if = "https://www.bvl.com.pe/inf_financiera72620_Q1JFQ0FQQzE.html#"
    url_er = "https://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano=2020&Trimestre=2&Rpj=OE5132&RazoSoci=CREDICORP%20CAPITAL%20PERU%20%20S.A.A.&TipoEEFF=GYP&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0"
    respuesta(url_er)


if __name__ == '__main__':
    main()
