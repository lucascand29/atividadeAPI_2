import requests
opcao = int(input('Digite a opção desejada para fazer a busca do endereço:\n 1-CEP\n 2-Logradouro\n '))

if opcao == 1:
    valorCep = input('Digite o número do seu cep:')
    URLCep = f'https://viacep.com.br/ws/{valorCep}/json/'
    buscaCep = requests.get(URLCep)
    endereco = buscaCep.json()['logradouro']
    bairro = buscaCep.json()['bairro']
    cidade = buscaCep.json()['localidade']
    uf = buscaCep.json()['uf']
    cep = '{}-{}'.format(valorCep[:5],valorCep[5:])
    print(f'Seu endereço: \nRua/AV: {endereco} - Bairro: {bairro}, Cidade: {cidade} - UF: {uf}, CEP: {cep}')
elif opcao == 2:
    valorUF = input('Digite a sigla do seu estado:')
    valorMunicipio = input('Digite o nome do seu municipio completo:')
    valorLogradouro = input('Digite o seu logradouro:')
    URLLogradouro = f'https://viacep.com.br/ws/{valorUF}/{valorMunicipio}/{valorLogradouro}/json/'
    buscaLogradouro = requests.get(URLLogradouro)
    bairro = buscaLogradouro.json()[0]['bairro']
    cep = buscaLogradouro.json()[0]['cep']
    print(f'Seu endereço: \nRua/AV: {valorLogradouro} - Bairro: {bairro}, Cidade: {valorMunicipio} - UF: {valorUF}, CEP: {cep}')
else:
    print('Opção invalida!')