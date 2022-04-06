import requests

def pesq_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    print(response.status_code)
    dados_cep = response.json()
    logradoro = dados_cep['logradouro']
    complemento = dados_cep['complemento']
    bairro = dados_cep['bairro']
    localidade = dados_cep['localidade']
    uf = dados_cep['uf']
    ibge = dados_cep['ibge']
    ddd = dados_cep['ddd']
    return dados_cep



def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':

    dados_cep = pesq_cep(52070010)
    print(dados_cep)

    dados_pokemon = retorna_dados_pokemon('pikachu')
    print(dados_pokemon['sprites']['front_shiny'])

    response = retorna_response('https://globallabs.academy/')
    print(response)


