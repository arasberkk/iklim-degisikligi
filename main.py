import discord
import os
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def iklim(ctx):
    await ctx.send("İklim, bir bölgenin uzun yıllar boyunca gözlenen ortalama hava koşullarıdır.")

@bot.command()
async def  ısınma (ctx):
    await ctx.send("Küresel ısınma, atmosferdeki sera gazlarının artışıyla Dünya'nın sıcaklığının yükselmesidir.")

@bot.command()
async def sera(ctx):
    await ctx.send("Sera gazları, atmosferde ısıyı tutarak gezegeni ısıtan gazlardır.")

@bot.command()
async def karbon (ctx):
    await ctx.send("Karbon ayak izi, bir kişinin veya kurumun atmosfere saldığı sera gazı miktarıdır.")
    
@bot.command()
async def orman(ctx):
    await ctx.send("Ormanlar karbonu emer, kesildiklerinde iklim değişikliği hızlanır.")

@bot.command()
async def su(ctx):
    await ctx.send("İklim değişikliği, su kıtlığına ve kuraklığa yol açar.")
    
@bot.command()
async def buzul(ctx):
    await ctx.send("Kutuplardaki buzullar iklim değişikliği nedeniyle hızla eriyor ve su seviyesi giderek artıyor.")

@bot.command()
async def gelecek(ctx):
    await ctx.send("Bilim insanları 2100 yılına kadar sıcaklığın 3°C artabileceğini öngörüyor,  önlem alınmazsa dereceler artmaya devam edicek.")

@bot.command()
async def ulaşım(ctx):
    await ctx.send("Bisiklet kullanımı arttırılmalı, bisiklet yolları yapılmalı, toplu taşıma araçları elektrikli olmalı" \
                    " egzozlu arabalar kaldırılmalı, elektrikli araba üretimi artmalı ve alım için fiyat düşürülmeli kampanyalar yapılmalıdır.")

@bot.command()
async def arttıran(ctx):
    await ctx.send("fosil yakıtların kullanımı, egzozlu arabaların egzozundan duman çıkması, ve araba sayısının artmasıdır.")

@bot.command()
async def önlem(ctx):
    await ctx.send("ağaçlandırma yeşillendirme çalışmaları yapılmalı, fosil yakıtları azalmalı, geri dönüşüme teşvik edilmeli ve yenilenebilir enerji kaynaklarının kullanımı arttırılmalıdır.")

@bot.command()
async def bilinçlenme(ctx):
    await ctx.send("okullarda ders niteliğinde anlatılmalı, her zaman gündemde tutulmalı ki önlemler alınsın.")

@bot.command()
async def geri_dönüşüm (ctx):
    await ctx.send("Geri dönüşüm, atıkları azaltır ve yeni üretimde enerji tasarrufu sağlar.")

@bot.command()
async def yenilenebilir_enerji(ctx):
    await ctx.send("Yenilenebilir enerji kaynakları: güneş, rüzgar, hidroelektrik ve jeotermaldir.")

@bot.command()
async def anlaşma(ctx):
    await ctx.send("Paris Anlaşması'nın hedefi: küresel sıcaklık artışını 1.5°C’nin altında tutmak.")

@bot.command()
async def hayvanlar(ctx):
    await ctx.send("Birçok hayvan türü yaşam alanı kaybı nedeniyle yok olma tehlikesinde ve iklim değişikliği sebebiyle nesilleride tehlike altındadır.")

@bot.command()
async def tarım(ctx):
    await ctx.send("İklim değişikliği ürün verimliliğini azaltıyor, gıda güvenliğini tehdit ediyor ayrıca tarım ürünlerinin neslinide tehlike altında bırakıyor.")

@bot.command()
async def sonuçları(ctx):
    await ctx.send("Kuraklık, sel, fırtına, buzulların erimesi ve deniz seviyesinin yükselmesi.")

@bot.command()
async def sağlık(ctx):
    await ctx.send("Kuraklık, sel, fırtına, buzulların erimesi ve deniz seviyesinin yükselmesi.")

@bot.command()
async def göç(ctx):
    await ctx.send("Su ve gıda kıtlığı yaşayan bölgelerden milyonlarca insan başka yerlere göç etmek zorunda kalıyor.")
   
@bot.command()
async def adalet(ctx):
    await ctx.send("İklim adaleti, iklim krizinden en az sorumlu olan fakir ülkelerin en çok zarar görmesini önlemek için adil çözümler üretmeyi savunur.")

@bot.command()
async def ekonomi (ctx):
    await ctx.send("Tarım verimliliğinin düşmesi, altyapı hasarları ve enerji maliyetlerinin artması ekonomiye büyük zarar verir.")

@bot.command()
async def güvenlik (ctx):
    await ctx.send("Kaynak kıtlığı, göçler ve afetler ülkeler arası çatışmaları artırabilir. Bu yüzden iklim değişikliği bir güvenlik tehdidi sayılır.")

@bot.command()
async def okyanuslar(ctx):
    await ctx.send("Artan sıcaklıklar okyanuslarda ısınmaya ve asitlenmeye yol açıyor; mercan resifleri yok oluyor, balık popülasyonları azalıyor.")

@bot.command()
async def biyoçeşitlilik(ctx):
    await ctx.send("Habitat kaybı, sıcaklık değişimleri ve besin zincirindeki bozulmalar yüzünden birçok tür yok olma tehlikesinde.")
@bot.command()
async def çocuklar (ctx):
    await ctx.send("Çocukların bağışıklık sistemi zayıf olduğu için sıcak hava dalgaları, hastalıklar ve besin yetersizliğinden daha çok etkileniyorlar.")

@bot.command()
async def dönüş(ctx):
    await ctx.send("Bazı etkiler yavaşlatılabilir (sera gazı azaltımıyla), ancak eriyen buzullar ve yok olan türler geri getirilemez.")


bot.run("token")
