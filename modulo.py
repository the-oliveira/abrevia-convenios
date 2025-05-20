def abrevia_nome_split():
    conselhos = {}
    while True:
        sigla_conselho = ''
        conselho = str(input('Nome completo do conselho: '))
        nome_lista = conselho.upper().split(' ')
        for p in nome_lista:
            if p not in ['DA', 'DE', 'DO', 'DAS', 'DOS']:
                sigla_conselho += p[0]
        
        conselhos[conselho] = sigla_conselho
        continuar = str(input('Adicionar mais conselhos? [S/N]')).upper()[0]
        if continuar != 'S':
            break
        
    return conselhos


def abrevia_nome():
    conselhos = {}
    while True:
        sigla_conselho = ''
        palavra = ''
        conselho = str(input('Nome completo do conselho: ')).upper()
        for l in conselho:
            if l != ' ':
                palavra += l
            elif l == ' ':
                if palavra not in ['DA','DE', 'DO', 'DOS', 'DAS', 'E']:
                    sigla_conselho += palavra[0]
                    palavra = ''
                else:
                    palavra = ''

        if palavra and palavra not in ['DA','DE', 'DO', 'DOS', 'DAS', 'E']:
            sigla_conselho += palavra[0]
                
        conselhos[conselho] = sigla_conselho
        continuar = str(input('Adicionar mais conselhos? [S/N]')).upper()[0]
        if continuar != 'S':
            break
        
    return conselhos
            

