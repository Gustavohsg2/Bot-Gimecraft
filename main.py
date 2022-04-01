from ast import Await
import discord
import random
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('g!oi'):
        await message.channel.send('Oi tudo bem? Seja Bem-Vindo!')
        
    if message.content.startswith('g!link'):
        await message.channel.send('Links: \n\n Youtube: https://www.youtube.com/channel/UC014Q9AuEzn-ncArNGdQhZA\nProjeto Fnaf: https://www.youtube.com/channel/UCWZ0xPHFdbh2N6Ibb5n5fVQ\nTwich: https://www.twitch.tv/gustavohsg6craft\nDiscord Age SMP: https://discord.gg/JHacVRqWd5\nDiscord Projeto Fnaf: https://discord.gg/8rVFAsdkqg')
    if message.content.startswith('g!inspire'):
        inspire = ['“Só é lutador quem sabe lutar consigo mesmo” - Carlos Drummond de Andrade', 
'“A vida é igual andar de bicicleta. Para manter o equilíbrio é preciso se manter em movimento” - Einstein', 
'“No caminho entre as pedras o espinho protege a flor” - Osmar Sampaio', 
'“Daqui a vinte anos você estará mais decepcionado pelas coisas que não fez do que pelas que fez” - Mark Twain', 
'“Até cortar os próprios defeitos pode ser perigoso. Nunca se sabe qual é o defeito que sustenta nosso edifício inteiro” - Clarice Lispector', 
'“Você deve pensar grande e começar pequeno” - Carlos Martins Wizard', 
'“Antes que diga que não consegue fazer alguma coisa, experimente” - Sakichi Toyoda', 
'“Todos os nossos sonhos podem virar realidade, se tivermos a coragem de persegui-los” - Walt Disney', 
'“Eu nunca sonhei com o sucesso, eu trabalhei por ele” - Estée Lauder', 
'“Nós somos o que fazemos repetidamente. A excelência, então, não é um ato, mas um hábito” - Aristóteles', 
'“Você não pode ensinar nada a ninguém, mas pode ajudar as pessoas a descobrirem por si mesmas” - Galileu', 
'“Mire na lua. Mesmo que você erre, você vai acertar as estrelas” - Les Brown']
        await message.channel.send(random.choice(inspire))
    if message.content.startswith('g!help'):
        await message.channel.send('```diff\n+ Comandos do bot GIMECRAFT!\n\n+ g!inspire\n+ O bot manda uma frase de inspiração.\n\n+ g!link\n+ O bot manda os links de canais e discords de projetos do Gustavo\n```')
    if message.content.startswith('g!fnaf')


client.run('OTU1NTc4NzY3MTY4OTI1NzU2.YjjuEw.CHF25NLKCciMwRAKSozkYcFr0bo')
