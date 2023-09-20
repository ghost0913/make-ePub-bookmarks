from bs4 import BeautifulSoup

# 打开xml文件
with open('toc.ncx', 'r', encoding='utf-8') as f:
    xml_content = f.read()

# 创建Beautiful Soup 对象
soup = BeautifulSoup(xml_content, 'xml')

# 找到content元素
contents = soup.find_all('content')

# 修改content src属性
for content in contents:
    src = content.get('src')
    if src.startswith('index_split_'):
        new_src=  src.replace('index_split_', 'index-1_split_')
        content['src'] = new_src

print(str(soup))

# with open('new_toc.txt', 'w', encoding='utf-8') as f:
#     f.write(str(soup))
#     print('success!')

f = open('new_toc.ncx', mode='w', encoding='utf-8')
f.write(str(soup))
f.close()
    

