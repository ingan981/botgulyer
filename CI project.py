import datetime
import discord


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("실행중...")
    game = discord.Game("관리")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):

    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith('!라이선스'):
        await message.channel.send('`http://ko.scp-wiki.net/chaos-insurgency-hub 를 기반으로 만들어진 디코입니다.`')
        await message.channel.send('`혼돈의반란 허브(scp사이트): http://ko.scp-wiki.net/chaos-insurgency-hub`')
        await message.channel.send('`라이센스 관련은 http://ko.scp-wiki.net/licensing-guide`')
        await message.channel.send('`CC BY AS 3.0`')

    if message.content.startswith("!커맨드"):
        embed = discord.Embed(title="커맨드", description="접두사=!", color=0x000000)  # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="사진(!사진 ~)", value="`SCP재단로고`, `CI로고`", inline=True)
        embed.add_field(name="유용한것(!~)", value="`정보`, `라이선스`", inline=False)
        embed.add_field(name="공식문서(!공식문서 ~)", value="`SCP재단`, `SCP리스트`, `SCP리스트KO`, `카논`, `카논KO`, `MTF`, `MTF-KO`", inline=False)
        await message.channel.send(embed=embed)  # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith("!사진 CI로고"):
        await message.channel.send("http://www.scp-wiki.net/local--files/chaos-insurgency-hub/CI%20Main.png")

    if message.content.startswith("!공식문서 SCP재단"):
        await message.channel.send("http://www.scp-wiki.net/")

    if message.content.startswith("!공식문서 SCP리스트"):
        await message.channel.send("http://www.scp-wiki.net/scp-series")

    if message.content.startswith("!공식문서 SCP리스트KO"):
        await message.channel.send("http://www.scp-wiki.net/scp-series-ko")

    if message.content.startswith("!공식문서 카논"):
        await message.channel.send("http://www.scp-wiki.net/canon-hub")

    if message.content.startswith("!공식문서 카논KO"):
        await message.channel.send("http://www.scp-wiki.net/canon-hub-ko")

    if message.content.startswith("!공식문서 MTF"):
        await message.channel.send("http://www.scp-wiki.net/task-forces")

    if message.content.startswith("!공식문서 MTF-KO"):
        await message.channel.send("http://www.scp-wiki.net/task-forces-ko")

    if message.content.startswith("!사진 SCP재단로고"):
        await message.channel.send("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/SCP_Foundation_%28emblem%29.svg/480px-SCP_Foundation_%28emblem%29.svg.png")

    if message.content.startswith("!카운트 다운"):
        await message.channel.send("10")
        await message.channel.send("9")
        await message.channel.send("8")
        await message.channel.send("7")
        await message.channel.send("6")
        await message.channel.send("5")
        await message.channel.send("4")
        await message.channel.send("3")
        await message.channel.send("2")
        await message.channel.send("1")
        await message.channel.send("떙")






client.run("NzE5ODU3MTU5MTg1MzY3MTcx.Xt9q0A.7A2eo0fsEcZC4wJb8e7vpiQchnQ")