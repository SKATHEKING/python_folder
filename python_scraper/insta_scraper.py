import re
from datetime import datetime
from itertools import takewhile, dropwhile

import instaloader


#começar a melhorar esse script e meter erros e exceções no código

def vamoPegarTudo(username):
    bot = instaloader.Instaloader()

    # Loading the profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, username)
    print("Usuario: ", profile.username)
    print("User ID: ", profile.userid)
    print("Numero of Posts: ", profile.mediacount)
    print("Numero de Followers: ", profile.followers)
    print("Numoro De seguidores: ", profile.followees)
    print("Bio: ", profile.biography)
    print("URL Externa: ", profile.external_url)
    emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
    print("Emails extraidos da bio:")
    print(emails)

def download_foto_de_perfil( username):
    L = instaloader.Instaloader()
    L.download_profile(username, profile_pic_only=True)

hashtags = []
usuarios_trending = []

def vamoPegarOTrending(topico= 'Anonymous'):

    bot = instaloader.Instaloader()

    search_results = instaloader.TopSearchResults(bot.context, topico)

    for username in search_results.get_prefixed_usernames():
        usuarios_trending.append(username)

    for username in search_results.get_profiles():
        print(username)

    for hashtag in search_results.get_hashtags():
        print(hashtag)
        hashtags.append(hashtag)

def download_de_posts_do_usuario(username, ano=2020,mes=3, dia=20):
        L = instaloader.Instaloader()
        posts = instaloader.Profile.from_username(L.context, username).get_posts()
        DESDE = datetime(ano, mes, dia)
        ATE = datetime.today()
        for post in takewhile(lambda p: p.date > DESDE, dropwhile(lambda p: p.date > ATE, posts)):
            L.download_post(post, username)




def main():

    username = input('Digite qual username vc gostaria de persquisar no instagram:')


    vamoPegarTudo(username)
    download_foto_de_perfil(username)

    dia = int(input('Qual dia voce deseja fazer download:'))
    mes = int(input('Qual mes voce deseja fazer download:'))
    ano =int(input('Qual o ano voce deseja fazer download:'))

    download_de_posts_do_usuario(username, ano, mes, dia)

    topico = input('Qual topico vc gostaria de pesquisar:')
    vamoPegarOTrending(topico)

    for usuario in usuarios_trending:
        vamoPegarTudo(usuario)
        download_foto_de_perfil(usuario)

main()