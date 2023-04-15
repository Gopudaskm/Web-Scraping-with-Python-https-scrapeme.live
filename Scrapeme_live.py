import requests as res
import json
from lxml import html
z=1
pokemon_dict={}
pokemon_list=[]
def Extract_data(url):
    response=res.get(url)
    tree=html.fromstring(html=response.text)
    title=tree.xpath('/html/body/div[1]/div[2]/div/div[2]/main/div/div[2]/h1/text()')[0]
    price=('£'+str(tree.xpath('/html/body/div[1]/div[2]/div/div[2]/main/div/div[2]/p[1]/span/text()')[0]))
    stock=tree.xpath('/html/body/div[1]/div[2]/div/div[2]/main/div/div[2]/p[2]/text()')[0].split(" ")[0]
    description=tree.xpath('/html/body/div[1]/div[2]/div/div[2]/main/div/div[3]/div[1]/p/text()')[0]
    sku=tree.xpath('/html/body/div[1]/div[2]/div/div[2]/main/div/div[2]/div[2]/span[1]/span/text()')[0]
    category_count=len(tree.xpath('/html/body/div[1]/div[2]/div/div[2]/main/div/div[2]/div[2]/span[2]')[0])
    category_list=[]
    for i in range(1,category_count+1):
        xp='/html/body/div[1]/div[2]/div/div[2]/main/div/div[2]/div[2]/span[2]/a['+str(i)+']/text()'
        xp2=tree.xpath(xp)[0]
        category_list.append(xp2)
    tag_count=len(tree.xpath('/html/body/div[1]/div[2]/div/div[2]/main/div/div[2]/div[2]/span[3]')[0])
    tag_list=[]
    for j in range(1,tag_count+1):
        xp3='/html/body/div[1]/div[2]/div/div[2]/main/div/div[2]/div[2]/span[3]/a['+str(j)+']/text()'
        xp4=tree.xpath(xp3)[0]
        tag_list.append(xp4)
    pokemon={}
    pokemon_dtls={}

    pokemon['Price']=str(price)
    pokemon['Stock']=stock
    pokemon['SKU']=sku
    pokemon['Description']=str(description)
    pokemon['Categories']=category_list
    pokemon['Tags']=tag_list
    pokemon_dtls[title]=pokemon
    pokemon_list.append(pokemon_dtls)


response1=res.get('https://scrapeme.live/shop/')
tree=html.fromstring(html=response1.text) 
main=tree.xpath('//*[@id="main"]/ul')[0]
itr_no=(len(main))
for i in range(1,itr_no+1):
    url='//*[@id="main"]/ul/li['+str(i)+']/a[1]'
    main2=tree.xpath(url)[0]
    Extract_data(str(html.tostring(main2)).split(" ")[1].replace("href=","").replace("\"",""))
for j in range(2,49):
    temp_url='https://scrapeme.live/shop/page/'+str(j)
    response1=res.get(temp_url)
    tree=html.fromstring(html=response1.text) 
    main=tree.xpath('//*[@id="main"]/ul')[0]
    itr_no=(len(main))
    for i in range(1,itr_no+1):
        url='//*[@id="main"]/ul/li['+str(i)+']/a[1]'
        main2=tree.xpath(url)[0]
        Extract_data(str(html.tostring(main2)).split(" ")[1].replace("href=","").replace("\"",""))
    print(str(z),'/',str(775))
    z+=1
pokemon_dict['Pokemon']=pokemon_list
# print(pokemon_dict)

with open ('pokemon_1.json','w',encoding='utf-8') as write_file:
    json.dump(pokemon_dict,write_file,indent=2,ensure_ascii=False)
