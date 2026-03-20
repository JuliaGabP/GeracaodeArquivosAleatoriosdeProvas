import random

# Dados das provas. As chaves são os estados e os valores, suas capitais
capitals = {'Acre': 'Rio Branco', 'Alagoas': 'Maceió', 'Amapá': 'Macapá', 'Amazonas': 'Manaus', 'Bahia': 'Salvador', 'Ceará': 'Fortaleza', 'Distrito Federal': 'Brasília', 'Espírito Santo': 'Vitória', 'Goiás': 'Goiânia', 'Maranhão': 'São Luís', 'Mato Grosso': 'Cuiabá', 'Mato Grosso do Sul': 'Campo Grande', 'Minas Gerais': 'Belo Horizonte', 'Pará': 'Belém', 'Paraíba': 'João Pessoa', 'Paraná': 'Curitiba', 'Pernambuco': 'Recife', 'Piauí': 'Teresina', 'Rio de Janeiro': 'Rio de Janeiro', 'Rio Grande do Norte': 'Natal', 'Rio Grande do Sul': 'Porto Alegre', 'Rondônia': 'Porto Velho', 'Roraima': 'Boa Vista', 'Santa Catarina': 'Florianópolis', 'São Paulo': 'São Paulo', 'Sergipe': 'Aracaju', 'Tocantins': 'Palmas'}

# Gera 35 arquivos de prova
for quiz_num in range(35):
    # Cria os arquivos de prova e do gabarito
    quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w', encoding='UTF-8')
    answer_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w', encoding='UTF-8')
    
    # Grava o cabeçalho da prova
    quiz_file.write('Nome:\n\nData:\n\nPeríodo:\n\n')
    quiz_file.write((' ' * 20) + f'Quiz das Capitais (Form{quiz_num + 1})')
    quiz_file.write('\n\n')
    
    # Embaralha a ordem dos estados
    states = list(capitals.keys())
    random.shuffle(states)
    
    # Itera 10 estados, criando uma pergunta para cada
    for num in range(10):
        
        # Obtém a resposta correta e as incorretas
        correct_answer = capitals[states[num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)
        
        # Grava a pergunta e as opções de resposta no arquivo da prova
        quiz_file.write(f'{num + 1}. Capital de {states[num]}:\n')
        for i in range(4):
            quiz_file.write(f"  {'ABCD'[i]}. { answer_options[i]}\n")
        quiz_file.write('\n')
        
        # Grava o gabarito em um arquivo
        answer_file.write(f"{num + 1}.{'ABCD'[answer_options.index(correct_answer)]}")
    quiz_file.close()
    answer_file.close()
