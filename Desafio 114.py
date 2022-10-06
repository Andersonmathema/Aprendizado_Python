'''Exercício Python 114: Crie um código em Python que
teste se o site pudim (http://pudim.com.br) está acessível pelo computador usado.
(https://www.youtube.com/watch?v=8jAykqxIeqw)'''
import urllib
import urllib.request
#importado um verificador de url's
try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucessso')
    print(site.read()) #puxa o html inteiro do site