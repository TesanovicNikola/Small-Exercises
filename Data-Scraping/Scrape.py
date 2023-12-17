from bs4 import BeautifulSoup
import pandas as pd

with open('test.html', 'r') as html_fajl:

    test = html_fajl.read()
    soup = BeautifulSoup(test, 'lxml')

    glavno = soup.find('div', class_='master-wrapper-main')
    Opis = glavno.find('div', class_ ='full-description').text.replace('•', '\n')
    Kategorija = glavno.find('h1', itemprop='name').text
    Model = glavno.find('span', class_='value').text
    URL_Slike = glavno.find('img', alt='BEAKERS, PTFE, HEATABLE')['src']

    with open('Opisi.txt', 'w') as f:

        f.write(f'Kategorija: {Kategorija}')
        f.write(f'Model: \n{Model}\n')
        f.write(f'Opis proizvoda: {Opis}')
        f.write(f'URL slike: \n{URL_Slike}\n')


    Item_Number1 = glavno.find('span', id="sku-113941").string
    Item_Number2 = glavno.find('span', id="sku-113942").string
    Item_Number3 = glavno.find('span', id="sku-113943").string
    Item_Number = pd.Series([Item_Number1,Item_Number2,Item_Number3])

    Item_Descript1 = glavno.find('tr', id="product-CG-1109H-01").find('div', class_="variant-description").text.replace('\n','')
    Item_Descript2 = glavno.find('tr', id="product-CG-1109H-02").find('div', class_="variant-description").text.replace('\n','')
    Item_Descript3 = glavno.find('tr', id="product-CG-1109H-03").find('div', class_="variant-description").text.replace('\n','')
    Item_Descript = pd.Series([Item_Descript1, Item_Descript2, Item_Descript3])

    PQ1 = glavno.find('tr', id="product-CG-1109H-01").find('div', class_="variant-pq").text.replace('\n','')
    PQ2 = glavno.find('tr', id="product-CG-1109H-02").find('div', class_="variant-pq").text.replace('\n','')
    PQ3 = glavno.find('tr', id="product-CG-1109H-03").find('div', class_="variant-pq").text.replace('\n','')
    PQ = pd.Series([PQ1, PQ2, PQ3])

    PRICE1 = glavno.find('tr', id="product-CG-1109H-01").find('span', itemprop="price").string.replace('\n','')
    PRICE2 = glavno.find('tr', id="product-CG-1109H-02").find('span', itemprop="price").string.replace('\n','')
    PRICE3 = glavno.find('tr', id="product-CG-1109H-03").find('span', itemprop="price").string.replace('\n','')
    PRICE = pd.Series([PRICE1, PRICE2, PRICE3])

    Qty_Avail1 = glavno.find('tr', id="product-CG-1109H-01").find('div', class_="variant-availablequantity").text.replace('\n','')
    Qty_Avail2 = glavno.find('tr', id="product-CG-1109H-02").find('div', class_="variant-availablequantity").text.replace('\n','')
    Qty_Avail3 = glavno.find('tr', id="product-CG-1109H-03").find('div', class_="variant-availablequantity").text.replace('\n','')
    Qty_Avail = pd.Series([Qty_Avail1, Qty_Avail2, Qty_Avail3])

    d = {'Item_Number':Item_Number, 'Item_Descript':Item_Descript, 'PQ':PQ, 'PRICE':PRICE, 'Qty_Avail': Qty_Avail }
    df = pd.DataFrame(data=d)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df.to_csv('TabelaSaPodacima.csv')

    print(f'Kategorija: {Kategorija}')
    print(f'Model: \n{Model}\n')
    print(f'Opis proizvoda: {Opis}')
    print(f'URL slike: \n{URL_Slike}\n')
    print(df)



