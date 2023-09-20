from bs4 import BeautifulSoup

start_chapter = 0
end_chapter = 682

# 初始化一个空字符串来存储生成的XML代码
xml_code = ''

# 循环读取标题并生成章节代码
for chapter in range(start_chapter, end_chapter + 1):
    # 打开文件解析标题，逐行读取而不是readlnes
    with open(f'index-3_split_{chapter:03}.html', mode='r', encoding='utf-8') as f:
        content = f.read()

        # 使用Beautiful Soup解析HTML内容
        soup = BeautifulSoup(content, 'html.parser')
        chapter_title_element = soup.find(class_ = 'calibre4')
        
        # 提取章节标题文本
        if chapter_title_element:
            chapter_title = chapter_title_element.text.strip()
            xml_code += f'  <navPoint class="chapter" id="num_{chapter:03}" playOrder="{chapter + 1}">\n'
            xml_code += '    <navLabel>\n'
            xml_code += f'      <text>{chapter_title}</text>\n'
            xml_code += '    </navLabel>\n'
            xml_code += f'    <content src="index-3_split_{chapter:03}.html"/>\n'
            xml_code += '  </navPoint>\n'
            f.close()
        else:
            f.close()
            continue

# 写入文件
f = open('epub_bookmarks.txt', mode='w', encoding='utf-8')
f.write(xml_code)
f.close()

# 打印生成的XML代码
print(xml_code)
