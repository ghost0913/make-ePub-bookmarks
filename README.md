# make-ePub-bookmarks
use python scripts to make .epub ebooks bookmarks for EthFans's posts.

## 用途
为EthFans上的历史文章资源制作epub版本书签

## 使用方式
1. 解压epub文件，将bookmarksMaker.py放入同级目录下
2. 根据epub内的html页面数、html名称、标题所在的class('calibre4' or 'calibre1')，修改代码内的end_chapter，"index*_split_" ,soup.find(class_ = ''),运行文件
3. 将生成的epub_bookmarks.txt内的内容复制
4. 用Sigil等epub电子书制作器打开epub文件，将上述复制内容粘贴到noc.ncx的相应位置里，生成目录
5. 保存epub文件。
   
## 技术点
- 使用BeautifulSoup库解析HTML内容，按class提取文章标题，按属性src修改XML内容。
- python文件读写

## 文件描述
bookmarkMaker.py:解析HTML文件，提取标题信息，生成XML作为epub目录内容
xmlEdit.py:修改已有的XML文件内容

# English Version
## Purpose
Make .epub bookmarks for EthFans.org's historical articles.
## How to use
1. Unzip the epub file and put bookmarksMaker.py into the same level directory.
2. According to the number of html pages in epub, the html name format, the class of title ('calibre4' or 'calibre1'), modify end_chapter, "index*_split_" ,soup.find(class_ = '') in the code. Run bookmarksMaker.py.
3. Copy the contents of epub_bookmarks.txt 
4. Use Sigil and other epub e-book sotfware to open the epub file, paste the above copied contents into the corresponding location of noc.ncx 
5. Save the epub file.
## Technical Points
- Use BeautifulSoup library to parse HTML contents
- Python file I/O
## File description
bookmarkMaker.py: parse HTML files, extract title information, generate XML as epub directory content.
xmlEdit.py: modify the content of XML file
