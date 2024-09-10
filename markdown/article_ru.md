# Michael Guidry

[dobbry vechur](https://t.me/good_evening), November 08, 2017

## Атаки нулевых..

В период с 1998 по 2000 гг. произошёл ряд DDoS-атак на сайты известных фирм и гос.организаций (например, eBay, CNN, Amazon, FBI, MSN, Yahoo). 

Софт, который использовался для этих атак, сейчас можно отыскать по запросам trinoo (Trin00), TFN (Tribe Flood Network), TFN2K (более продвинутая версия), Stacheldraht (нем. "колючая проволока").

Одним из организаторов атаки стал разработчик trinoo, 13-15-летний хакер Майкл Гайдри с псевдонимом phifli (ныне также пользуется mikeguidry, mikeg504, но phifli, похоже, остался с ним на всю жизнь).

## .. и их последствия

Атаки на столь серьёзные организации, конечно, не остались без внимания со стороны ФБР. Истории сильно путаются от рассказчика к рассказчику, что и не удивительно: какие-то материалы могут быть засекречены, у каждого субъективный взгляд, и т.д. 

Например, один из известных хакеров Mafiaboy (хотя репутация его сомнительна) выпустил [книгу](https://www.amazon.com/Mafiaboy-Portrait-Hacker-Young-Man/dp/0762770554) 

> Mafiaboy: A Portrait of the Hacker as a Young Man

В ней есть как минимум небольшой кусочек про Майкла:

> Phifli (AKA Mikey) - A serious coder, Phifli didn't bother with the battles; he was all about writing code. At my urging, he would go on to write Trinoo, a denial-of-service tool that was a key inspiration to me when I began working toward my series of major attacks. Although he didn't engage in battle, Phifli loved talking over channels. And he was kind enough to let his fellow TNT members test out his tools. That gave us a big advantage.

Перевод:

> Phifli (AKA Mikey) - Настоящий программист, Phifli не парился по поводу нападений и прочего, он всегда был занят кодом. Я думаю, он продолжил разрабатывать Trinoo (софт для DoS) который был для меня ключевым, когда я начал работать над моей серией крупных атак. Хотя он и не участвовал в самих атаках, Phifli любил разговаривать в каналах. И он был достаточно любезен, чтобы позволить своим коллегам из TNT тестировать свои разработки. Это дало нам большое преимущество.

Во время моих поисков я наткнулся на следующий комментарий (можно найти на [этой](https://webcache.googleusercontent.com/search?q=cache:mvJC71UWDtUJ:https://www.amazon.com/Mafiaboy-Cracked-Internet-Still-Broken/dp/0670067482+&cd=13&hl=ru&ct=clnk&gl=ru) странице, поискав, например, phifli) к этой книге:

> I was an actual member of `tnt/phorce` and I recall things VERY differently. MB asked others to help him packet the sites that were mentioned in the news, and most of them said F' off. Mafiaboy wrote no tools at all, most of any attack programs were written by phifli, sinkhole and a few select others. He did use a semi-public scanner to 'own' machines (solaris boxes, irix) and just either put bots on them, or used them with trinoo. Before trinoo, he simply logged into a bunch of machines and manually smurf'd or UDP flooded targets.

> I think he just wrote this because nobody wants to hire him, and he wanted to make money off of other people's accomplishments. What's sad is he made money off the following people:

> ShadowKnight, phifli, dreamwalk, sinkhole, CORE (group), conflict (group), madcrew (group), NoName (group), chrome (group)

> .. And countless others. By attacking all of those sites, he initially was the result of many people just giving it up (ie: phifli, dreamwalk, myself) because he attracted unwanted attention to the scene. I'm pretty sure Mshadow was the one who leaked the logs of him attacking the sites to the RCMP/FBI and that's what got him busted. There is much hatred towards him for this book, him attacking corporate companies. I showed this book to someone who was around at the same and his jaw dropped as the BS that is in this book.

> Also, the media portrays MB as some superhacker. HAH. Far from it, he's a victim of the public's stupidity.

Вольный перевод:

> Я в те времена участвовал в TNT/Phorce и я всё помню СОВЕРШЕННО иначе. Mafiaboy попросил помочь ему в сборе сайтов, засветившихся в новостях, и большинство просто послали его нахер. Он вообще ничего не разрабатывал, большинство инструментария было написано силами phifli, sinkhole и ещё некоторыми. Что он действительно делал - так это использовал полу-публичный сканер на "своих" машинах (solaris, irix), и просто либо устанавливал туда ботов, либо использовал их для мощностей trinoo. До появления trinoo он просто логинился на пачку машин и либо вручную проводил [smurf-атаку](https://en.wikipedia.org/wiki/Smurf_attack), либо просто флудил UDP-траффиком.

> Я думаю, он написал эту книгу только лишь потому, что никто не хочет брать его на работу, а он хотел поднять денег на чужих наработках. И самое печальное, что он так и поступил со следующими людьми:

> ShadowKnight, phifli, dreamwalk, sinkhole, CORE (group), conflict (group), madcrew (group), NoName (group), chrome (group)

> .. и ещё очень много с кем. Атакуя эти сайты, он добился только одного - многие просто съехали с этой темы (например, phifli, dreamwalk, да и я сам), потому что он привлёк к нам слишком много нежелательного внимания. Я почти уверен, что это Mshadow слил логи своей атаки на эти сайты в RCMP/FBI и именно поэтому его (Mafiaboy) посадили. На него валится куча дерьма и недовольства за эту книгу, за его атаки на эти корпорации. Я показывал её знакомому, который знает всё не понаслышке, так у него челюсть вывалилась прямо как всё дерьмо из этой книги.

> Ну и ещё кое-что. СМИ говорят о Mafiaboy как о каком-нибудь суперхацкере. Ха. Это уж точно не про него, он лишь жертва всеобщей глупости.

Статья, посвящённая атакам (2002): https://www.cnet.com/news/hacker-discloses-new-internet-attack-software/

[Некоторую](https://en.wikipedia.org/wiki/Trinoo) [информацию](https://en.wikipedia.org/wiki/Stacheldraht) можно [найти](https://en.wikipedia.org/wiki/Tribe_Flood_Network) и на википедии, да и просто во фринете.

А вот [тут](https://www-uxsup.csx.cam.ac.uk/pub/webmirrors/www.cert.org=/incident_notes/IN-99-04.html) и [тут](https://www.cert.org/historical/advisories/CA-1999-05.cfm?) можно чуть подробнее узнать, как проводилась атака технически.

Так или иначе, но все истории несколько различаются от источника к источнику, да и даже сам этот текст - всего лишь усреднение из найденного за пару дней.

## Начало

06.11.17 в 17:14 MSK на [FTP-канале бота-сканера в telegram](https://t.me/aiWeipeighah7vufoHa0ieToipooYe) появился пост следующего содержания:

![image1](img1.png)

Самыми интересными показались, конечно же:

- anti_mass_surveillance_proof_of_concept.tbz2
- bypassing_signal_intelligence_platforms.pdf
- congress_fax_9_22_17.pdf
- invisible_friends_9-16-17.pdf
- systembackup.tar.gz

Открыв первый попавшийся ([congress_fax](http://mikeguidry.net/releases/congress_complaint_april_2017.pdf)), я пробежался взглядом по тексту и с некоторым недоумением после прочитанного нажал на ссылку внизу страницы: http://mikeguidry.net/releases/

> documents released relating to human/civil rights violations in my life, and some vulnerabilities relating to mass surveillance, and a few other things..

## Раскопки

Позже выяснилось, что на этот же сервер ведут домены easystyle.org и  limittech.net 

Первый встречается только в pdf-файлах Майкла, второй Майкл использовал чаще всего для контактной почты (mike@easystyle.org, прежде phifli@yahoo.com). Последний очень мало где упомянут, но мне удалось найти информацию о заголовке страницы, из которого следует, что Майкл, по всей видимости, собирался продавать самописные эксплоиты. На момент составления поста, к сожалению, не удаётся найти пруфлинк.

В директории /releases/ на каждом из доменов доступен набор pdf-файлов, составленных Майклом в разное время за последние два года. Часть - размышления на тему киберсекьюрити, часть - параноидальные размышления о всеобщей слежке (например, [PRISM](http://mikeguidry.net/releases/dying_prism.pdf)) 

Вкратце пересказывая описанное самим Майклом - по его мнению, последние 20 лет его преследуют, насиловали (!) около 50 (!) раз, причём последний был в этом году. 

Кроме того, он постоянно говорит о том, что ему в напитки и еду подмешивают наркотики, где бы он ни был. Из-за этого ему сложно жить, каждый раз доза по его мнению повышается.

Ещё одна вещь, часто фигурирующая в его записях - похищение некими фирмами с миллиардными состояниями его интеллектуальной собственности. К сожалению, ничего конкретного выцепить не удалось, так что узнать, что это за софт и существует ли он на самом деле - довольно сложная задачка.

Кроме этого, я пробежался по серверу DirBuster-ом, что позволило мне узнать не только о неинтересных /link/ и /ks/, но ещё и о внезапно очень информативном письме Майкла своей семье. Его можно найти [тут](http://mikeguidry.net/a.txt).

Стоит прочесть это письмо, потому что в нём есть всё, чтобы понять, что происходит/происходило у Майкла в жизни и в каком положении он находится сейчас. Кроме того, достаточно подробный рассказ с описанием его путешествий можно найти в [одном](http://mikeguidry.net/releases/new_complaint.pdf) из PDF-файлов.

Самый последний документ, который доступен на сайте Майка - [bypassing_signal_intelligence_platforms.pdf](http://mikeguidry.net/releases/bypassing_signal_intelligence_platforms.pdf)

В нём содержатся размышления на тему современной слежки, как можно ей противостоять и т.п.

## Слежка, #AntiSurveillance

Мысль о глобальной слежке, очевидно, больше не покидает голову Майкла, о чём можно судить как из его заметок/писем, так и в его твиттере: https://twitter.com/phifli/

Последние записи оттуда:

> michael guidry‏ @phifli 24 hours ago

> For everyone who thought my attacks against surveillance platforms were theoretical or too hard.. I just accomplished it in a weekend

Перевод:

> Всем, кто считал, что мои атаки на системы слежки - лишь теория или что-то невозможное... Я только что осуществил это за неделю.

> michael guidry‏ @phifli Nov 6

> Wait till you guys get sight of what I plan on doing in the future w resources... LOL everything im doing now is a joke in comparison

Перевод:

> Подождите, ребята, вы потом поймёте, что я планирую делать с ресурсами... Лол, всё, что я делаю сейчас - это шутка в сравнении с тем, что впереди

В последнее время Майкл занимался разработкой эдакого "убийцы слежки" ([github](https://github.com/mikeguidry/clockwork/tree/antisurveillance)). Насколько я смог понять из всего, что за это время узнал, он хочет бороться как с тотальным контролем, так и с хакерами в интернете (?). Если верить его заявлениям, то он готов пустить свою разработку в бой. Времени разобраться в принципе работы или почитать код у меня, к сожалению, не было, а чтение чужого (хоть и бесспорно качественного) кода на C++ - достаточно сложное занятие.

Сайт и документы были лишь первой находкой (второй после нахождения того FTP-сервера, на котором больше ничего интересного и нету).

Тут несколько не сильно сортированных ссылок, которые я сохранял для себя по ходу поисков, это могут быть странички из блогов с упоминаниями или сообщениями самого phifli или что-нибудь ещё:

- https://myspace.com/phifli/
- http://prism.euwatch.eu/2437597877.html
- https://marc.info/?l=darklab&m=128924694300949&w=2
- https://gbatemp.net/threads/switch-hacking-homebrew-discussion.464282/page-9
- https://github.com/mikeguidry/
- http://infobot.sourceforge.net/snapshots/url/snapshot_19991218/url-is-final.txt
- https://publicdbhost.dmca.gripe/random/DigitalGangster.com%202016.txt
- ftp://d.easystyle.org/

А тут даже какие-то данные о Майкле. Впрочем, всё это и так можно запросто найти в интернете:

- Жил в штатах Теннесси, LA, Флорида, Техас, Луизиана, кроме этого в Дубаях, в Австралии, Германии, ОАЭ. В данный момент проживает в Майами (предположительный адрес: Miami 45 SW, 24th Rd, Miami, FL, 33129-1509)
- Достоверно известен только год рождения - 1985. Возможно, что полная дата - 31.07.1985

## чуть-чуть отдельно про FTP

Во время подготовки материала в FTP-канале появился ещё один сервер:

![image2](img2.png)

А позднее там же нашли нашли и другой:

![image3](img3.png)

Учитывая это и тот факт, что Майкл собирался действовать всеми возможными методами, возможно, таким образом он хочет рассказать всем о себе.

> The whole point is that since crimes continue to be committed against me I have decided to release information to cause entire different parts of this, and other governments to bat their eyebrows.  I am absolutely positive it has worked although I am still being drugged.  I will continue to exponentially increase the stakes while this continues to take place in my life.

Перевод:

> Все дело в том, что, поскольку [правительство] продолжает совершать преступления против меня, я решил опубликовать информацию, чтобы поднять повсюду шумиху, а другие правительства - остолбенеть. Я абсолютно уверен, что это сработало, хотя мне всё ещё подмешивают наркотики. И я продолжу экспоненциально увеличивать ставки, пока это является частью моей жизни.

Что касается самого первого - используя только открытые (вся файловая система практически!) данные, я выяснил, что там есть пользователь www (ftp://220.126.225.91/etc/passwd) и что у него пустой пароль. Это позволило подключиться к серверу удалённо, но ничего особо интересного я там не нашёл. А из-за legacy-состояния SSH-сервера на этой машинке мне пришлось повозиться и с подключением, в итоге команда выглядит как 

> ssh www@220.126.225.91 -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc

Да, кстати. Вместо сервера используется некое embedded-решение, это очевидно по наполненности каталогов. Я посмотрел на ftp://220.126.225.91/etc/hostname и забил его в [гугле](http://www.northstarmicro.com/undefined-category/miscellaneous4/at91sam9m10-ekes). 

Несмотря на то, что поиски в этом направлении ничего не дали (к тому же - что, если он действительно всё распространяет таким "вирусным" способом?), было довольно интересно.

## Итого

В общем-то, это всё, что мне удалось найти за один вечер.

Ещё раз список того, что можно почитать про всю эту историю:

- Письмо семье: http://mikeguidry.net/a.txt
- Письмо в посольства: http://mikeguidry.net/releases/new_complaint.pdf
- Твиттер: https://twitter.com/phifli/
- GitHub: https://github.com/mikeguidry/

подготовлено совместно с сообществом [@netstalking](https://t.me/netstalking)
