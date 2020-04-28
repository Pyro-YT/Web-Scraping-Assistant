from bs4 import BeautifulSoup
import requests

url = input('input url to scrape:')
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

try:
    with open('site_markup.txt', 'w+', encoding  ='utf-8') as f:
        f.write(str(soup.prettify))
except Exception as e:
    f = open('site_markup.txt', 'w+', encoding = 'utf-8')
    f.write(str(soup.prettify))
    f.close()

stats = open('site_stats.txt', 'w+', encoding = 'utf-8')
tags = ['a', 'abbr', 'acronym', 'address', 'applet', 'area', 'article', 'aside', 'aside', 'audio', 'b', 'base', 'basefront', 'bb', 'bdo', 'big', 'blockquote', 'br /', 'body', 'button', 'canvas', 'caption', 'center', 'cite', 'code', 'col', 'colgroup', 'command', 'datagrid', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog', 'dir', 'div', 'dl', 'dt', 'em','embed', 'eventsource', 'fieldset', 'figcaptioin', 'figure', 'font', 'footer', 'form', 'frame', 'frameset', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'head', 'header', 'hgroup', 'hb /', 'html', 'i', 'iframe', 'img', 'input', 'ins', 'isindex', 'kbd', 'keygen', 'label', 'legend', 'li', 'link', 'map', 'mark', 'menu', 'meta', 'meter', 'nav', 'noframes', 'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 'p', 'param', 'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source', 'span', 'strike', 'strong', 'style', 'sub', 'sup', 'table', 'tbody', 'td', 'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'track', 'tt', 'u', 'ul', 'var', 'video', 'wbr']
component_dict = {}

for i in tags:
    try:
        total_tags = soup.find_all(i)
        tag_num = len(total_tags)
        if tag_num != 0:
            component_dict.update({i:tag_num})
    except Exception as e:
        print(e)
        pass

stats.truncate()
stats.close()

for i in component_dict.keys():
    full_tag_list = soup.find_all(i)
    for item in full_tag_list:
        item_string = item.string
        item_attr = item.attrs
        with open('site_stats.txt', 'a+') as stats:
            if item_string != None and len(item_attr) >= 1:
                stats.write(f'tag name = {i}\n')
                stats.write(f'tag content = {item_string}\n')
                for key in item_attr.keys():
                    stats.write(f'attribute = {key}, value = {item_attr.get(key)}\n')
                stats.write('\n\n')
            
        


