# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:45:04 2022

@author: julio
"""
import nltk
from functions import removestopwords, aplicastemmer, buscapalavras, buscafrequencia, buscapalavrasunicas, extratorpalavras

basetreinamento = [('você e abominável','desgosto'),
('abomino a maneira como você age','desgosto'),
('estou adoentado','desgosto'),
('meu pai esta adoentado','desgosto'),
('estamos todos doentes','desgosto'),
('essa situação e muito amarga','desgosto'),
('disse adeus amargamente','desgosto'),
('tenho antipatia por aquela pessoa','desgosto'),
('como pode ser tão antipática!','desgosto'),
('que horrível seu asqueroso','desgosto'),
('tenho aversão agente como você','desgosto'),
('isso tudo e só chateação','desgosto'),
('estou muito chateada com suas mentiras','desgosto'),
('tão desagradável','desgosto'),
('isso me desagrada completamente','desgosto'),
('te desagrada isso','desgosto'),
('estou com enjôos terríveis','desgosto'),
('todos estão enfermos','desgosto'),
('foi uma enfermidade terrível','desgosto'),
('isso e muito grave','desgosto'),
('não seja tão grosseiro','desgosto'),
('você fez uma manobra ilegal','desgosto'),
('sua indecente, não tem vergonha?','desgosto'),
('você e malvado com as crianças','desgosto'),
('que comentário maldoso','desgosto'),
('sem escrúpulos você manipula a tudo','desgosto'),
('sinto repulsa por você','desgosto'),
('e repulsivo a maneira como olha para as pessoas','desgosto'),
('estou indisposta','desgosto'),
('a indisposição me atacou hoje','desgosto'),
('acho que vou vomitar','desgosto'),
('tem muito vomito lá','desgosto'),
('que incomodo essa dor','desgosto'),
('não me incomode nunca mais','desgosto'),
('suas bobagens estão nos incomodando','desgosto'),
('que nojo olha toda essa sujeira','desgosto'),
('como isso está sujo','desgosto'),
('tenho náuseas só de lembrar','desgosto'),
('me sinto nauseada com o cheiro desta comida','desgosto'),
('você esta obstruindo a passagem de ar','desgosto'),
('você esta terrivelmente doente','desgosto'),
('olhe que feia esta roupa','desgosto'),
('que atitude deplorável','desgosto'),
('nossa como você e feio','desgosto'),
('muito mau tudo isso','desgosto'),
('estou desgostoso com você','desgosto'),
('você cortou o meu assunto','desgosto'),
('para que tanta chateação?','desgosto'),
('esse perfume e enjoativo','desgosto'),
('ser perigoso não nada bom','desgosto'),
('você e perigoso demais para minha filhas','desgosto'),
('que fetido este esgoto','desgosto'),
('que fedido você esta','desgosto'),
('que cachorro malcheiroso','desgosto'),
('hora que ultraje','desgosto'),
('e ultrajante da sua parte','desgosto'),
('situação desagradável essa','desgosto'),
('você só me da desgosto','desgosto'),
('tenho aversão a pessoas assim','desgosto'),
('antipatia e um mal da sociedade','desgosto'),
('que criatura abominável','desgosto'),
('e depressiva a maneira como você vê o mundo','desgosto'),
('me desagrada sua presença na festa','desgosto'),
('sinto asco dessa coisa','desgosto'),
('que hediondo!','desgosto'),
('vou golfar o cafe fora','desgosto'),
('hora que garota detestável!','desgosto'),
('estou nauseada','desgosto'),
('isso que você disse foi muito grave','desgosto'),
('não seja obsceno na frente das crianças','desgosto'),
('não seja rude com as visitas','desgosto'),
('esse assunto me da repulsa','desgosto'),
('que criança terrivelmente travessa','desgosto'),
('que criança mal educada','desgosto'),
('estou indisposta te dar o divorcio','desgosto'),
('tão patetico, não tem nada mais rude para dizer?','desgosto'),
('por motivo torpe, com emprego de meio cruel e com impossibilidade de defesa para a vítima','desgosto'),
('a inveja e tão vil e vergonhosa que ninguem se atreve a confessá-la','desgosto'),
('o miserável receio de ser sentimental e o mais vil de todos os receios modernos','desgosto'),
('travesso gato quando fica com saudades do dono mija no sapato','desgosto'),
('isso e um ato detestável e covarde','desgosto'),
('revelam apenas o que e destrutivo e detestável para o povo','desgosto'),
('não sei como e a vida de um patife, mais a de um homem honesto e abominável','desgosto'),
('há coisas que temos que suportar para não acharmos a vida insuportável','desgosto'),
('as injurias do tempo e as injustiças do homem','desgosto'),
('odioso e desumano','desgosto'),
('você não publicará conteúdo odiento, pornográfico ou ameaçador','desgosto'),
('rancoroso e reprimido','desgosto'),
('não há animal mais degradante, estúpido, covarde, lamentável, egoísta, rancoroso e invejoso do que o homem','desgosto'),
('o virulento debate ente políticos','desgosto'),

('por favor não me abandone','tristeza'),
('não quero ficar sozinha','tristeza'),
('não me deixe sozinha','tristeza'),
('estou abatida','tristeza'),
('ele esta todo abatido','tristeza'),
('tão triste suas palavras','tristeza'),
('seu amor não e mais meu','tristeza'),
('estou aborrecida','tristeza'),
('isso vai me aborrecer','tristeza'),
('estou com muita aflição','tristeza'),
('me aflige o modo como fala','tristeza'),
('estou em agonia com meu intimo','tristeza'),
('não quero fazer nada','tristeza'),
('me sinto ansiosa e tensa','tristeza'),
('não consigo parar de chorar','tristeza'),
('não consigo segurar as lagrimas','tristeza'),
('e muita dor perder um ente querido','tristeza'),
('estou realmente arrependida','tristeza'),
('acho que o carma volta, pois agora sou eu quem sofro','tristeza'),
('você não cumpriu suas promessas','tristeza'),
('me sinto amargurada','tristeza'),
('coitado esta tão triste','tristeza'),
('já e tarde de mais','tristeza'),
('nosso amor acabou','tristeza'),
('essa noite machuca só para mim','tristeza'),
('eu não estou mais no seu coração','tristeza'),
('você mudou comigo','tristeza'),
('quando eu penso em você realmente dói','tristeza'),
('como se fosse nada você vê minhas lagrimas','tristeza'),
('você disse cruelmente que não se arrependeu','tristeza'),
('eu nunca mais vou te ver','tristeza'),
('ela esta com depressão','tristeza'),
('a depressão aflige as pessoas','tristeza'),
('estar depressivo e muito ruim','tristeza'),
('estou derrotada e deprimida depois deste dia','tristeza'),
('e comovente te ver dessa maneira','tristeza'),
('e comovente ver o que os filhos do brasil passam','tristeza'),
('como me sinto culpada','tristeza'),
('estou abatida','tristeza'),
('a ansiedade tomou conta de mim','tristeza'),
('as pessoas não gostam do meu jeito','tristeza'),
('adeus passamos bons momentos juntos','tristeza'),
('sinto sua falta','tristeza'),
('ele não gostou da minha comida','tristeza'),
('estou sem dinheiro para a comida','tristeza'),
('queria que fosse o ultimo dia da minha vida','tristeza'),
('você está com vergonha de mim','tristeza'),
('ela não aceitou a minha proposta','tristeza'),
('era o meu ultimo centavo','tristeza'),
('reprovei de ano na faculdade','tristeza'),
('afinal você só sabe me desfazer','tristeza'),
('eu falhei em tudo nessa vida','tristeza'),
('eu fui muito humilhado','tristeza'),
('e uma história muito triste','tristeza'),
('ninguem acredita em mim','tristeza'),
('eu não sirvo para nada mesmo','tristeza'),
('droga, não faço nada direito','tristeza'),
('sofrimento em dobro na minha vida','tristeza'),
('fui demitida essa semana','tristeza'),
('as crianças sofrem ainda mais que os adultos','tristeza'),
('pra mim um dia e ruim, o outro e pior','tristeza'),
('de repente perdi o apetite','tristeza'),
('oh que dia infeliz','tristeza'),
('estamos afundados em contas','tristeza'),
('nem um milagre pode nos salvar','tristeza'),
('só me resta a esperança','tristeza'),
('pior que isso não pode ficar','tristeza'),
('meu salário e baixo','tristeza'),
('não passei no vestibular','tristeza'),
('ninguem se importa comigo','tristeza'),
('ninguem lembrou do meu aniversário','tristeza'),
('tenho tanto azar','tristeza'),
('o gosto da vingança e amargo','tristeza'),
('sou uma mulher amargurada depois de que você me deixou','tristeza'),
('estou desanimada com a vida','tristeza'),
('e um desanimo só coitadinha','tristeza'),
('a derrota e depressiva','tristeza'),
('discriminar e desumano','tristeza'),
('que desanimo','tristeza'),
('e uma desonra para o pais','tristeza'),
('a preocupação deveria nos levar a ação não a depressão','tristeza'),
('passamos ao desalento e a loucura','tristeza'),
('aquele que nunca viu a tristeza nunca reconhecerá a alegria','tristeza'),
('cuidado com a tristeza ela e um vicio','tristeza')]

baseteste =[('o mundo e feio como o pecado','desgosto'),
('a coisa mais difícil de esconder e aquilo que não existe','desgosto'),
('você errou feio aquele gol','desgosto'),
('nunca vou me casar sou muito feia','desgosto'),
('os golpes da adversidade são terrivelmente amargos','desgosto'),
('os homem ficam terrivelmente chatos','desgosto'),
('abominavelmente convencido','desgosto'),
('terrivelmente irritado','desgosto'),
('as instituições publicas estão terrivelmente decadentes','desgosto'),
('a população viveu em isolamento por muito tempo','desgosto'),
('estou terrivelmente preocupada','desgosto'),
('o nacionalismo e uma doença infantil','desgosto'),
('se me es antipático a minha negação esta pronta','desgosto'),
('muitos documentários sobre esse casal antipático','desgosto'),
('sua beleza não desfaça sua antipatia','desgosto'),
('esta e uma experiência desagradável','desgosto'),
('desagradável estrago nos banheiros','desgosto'),
('o mais irritante no amor e que se trata de um crime que precisa de um cúmplice','desgosto'),
('a situação nos causa grande incomodo','desgosto'),
('estou preocupado com o incomodo na garganta','desgosto'),
('simplesmente não quero amolação da policia','desgosto'),
('você e uma criaturinha muito impertinente','desgosto'),
('o peso e a dor da vida','desgosto'),
('me arrependo amargamente de minhas ações','desgosto'),
('o destino e cruel e os homens não são dignos de compaixão','desgosto'),
('o ódio conduz ao isolamento cruel e ao desespero','desgosto'),
('encerrou com o massacre mais repudiável e asqueroso que se conhece','desgosto'),
('de mal gosto e asqueroso','desgosto'),
('tudo e inserto neste mundo hediondo','desgosto'),
('o crime de corrupção e um crime hediondo','desgosto'),
('o rio esta fetido e de cor escura','desgosto'),
('muito lixo no rio o deixa malcheiroso','desgosto'),
('existe uma laranja podre no grupo e já desconfiamos quem e','desgosto'),
('foi de repente estou machucado e me sentindo enjoado','desgosto'),
('eu fiquei enojado','desgosto'),
('daqui alguns meses vou embora deste pais que já estou nauseado','desgosto'),

('isso tudo e um erro','tristeza'),
('eu sou errada eu sou errante','tristeza'),
('tenho muito dó do cachorro','tristeza'),
('e dolorida a perda de um filho','tristeza'),
('essa tragedia vai nos abalar para sempre','tristeza'),
('perdi meus filhos','tristeza'),
('perdi meu curso','tristeza'),
('sou só uma chorona','tristeza'),
('você e um chorão','tristeza'),
('se arrependimento matasse','tristeza'),
('me sinto deslocado em sala de aula','tristeza'),
('foi uma passagem fúnebre','tristeza'),
('nossa condolências e tristeza a sua perda','tristeza'),
('desanimo, raiva, solidão ou vazies, depressão','tristeza'),
('vivo te desanimando','tristeza'),
('estou desanimado','tristeza'),
('imperador sanguinário, depravado e temeroso','tristeza'),
('meu ser esta em agonia','tristeza'),
('este atrito entre nos tem que acabar','tristeza'),
('a escuridão desola meu ser','tristeza'),
('sua falsa preocupação','tristeza'),
('sua falsidade me entristece','tristeza'),
('quem esta descontente com os outros esta descontente consigo próprio','tristeza'),
('a torcida esta descontente com a demissão do tecnico','tristeza'),
('estou bastante aborrecido com o jornal','tristeza'),
('me sinto solitário e entediado','tristeza'),
('a vida e solitária para aqueles que não são falsos','tristeza'),
('como com compulsão depois da depressão','tristeza'),
('estou me desencorajando a viver','tristeza'),
('ele desencoraja minhas vontades','tristeza'),
('isso vai deprimindo por dentro','tristeza'),
('acho que isso e defeituoso','tristeza'),
('os remedios me derrubam na cama','tristeza'),
('a depressão vai me derrubar','tristeza'),
('suas desculpas são falsas','tristeza'),
('não magoe as pessoas','tristeza')]

#Remoção das Stopwords e extração do radical 
frasescomstemmingtreinamento = aplicastemmer(basetreinamento)
frasescomstemmingteste = aplicastemmer(baseteste)

#Lista todas as palavraas da base de treinamento e teste
palavrastreinamento = buscapalavras(frasescomstemmingtreinamento)
palavrasteste = buscapalavras(frasescomstemmingteste)

#Frequencia com que as palavras se repetem
frequenciatreinamento = buscafrequencia(palavrastreinamento)
frequenciateste = buscafrequencia(palavrasteste)

#Palavras unicas
palavrasunicastreinamento = buscapalavrasunicas(frequenciatreinamento)
palavrasunicasteste = buscapalavrasunicas(frequenciateste)

#Extração das palavras de todas as frases
basecompletapalavrastrain = nltk.classify.apply_features(extratorpalavras, frasescomstemmingtreinamento)
basecompletapalavrasteste = nltk.classify.apply_features(extratorpalavras, frasescomstemmingteste)

#Construção da tabela de propabilidade
classificador = nltk.NaiveBayesClassifier.train(basecompletapalavrastrain)
#print(classificador.labels())
print(nltk.classify.accuracy(classificador, basecompletapalavrasteste))

#Matriz de confusão
from nltk.metrics import ConfusionMatrix
esperado = []
previsto = []

for (frase, classe) in basecompletapalavrasteste:
    resultado = classificador.classify(frase)
    previsto.append(resultado)
    esperado.append(classe)
    
matriz = ConfusionMatrix(esperado, previsto)
print(matriz)