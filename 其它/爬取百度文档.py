import re
import requests

session=requests.session()
def fetch_url(url):
    print(session.get(url).content.decode('UTF-8'))
    return session.get(url).content.decode('UTF-8')
def get_doc_id(url):
    return re.findall('view/(.*).html',url)[0]
#地址：https://wenku.baidu.com/view/8a38640b5af5f61fb7360b4c2e3f5727a4e924ce.html
#https://wenku.baidu.com/browse/interface/getdocpacklist?docId=7eb0e17e81c758f5f61f67ff
#https://wenku.baidu.com/view/7eb0e17e81c758f5f61f67ff.html
Request Method: GET
def pqrser_type(content):
    return re.findall(r"docType.*?\:.*?\'(.*?)\'\,",content)[0]
def parser_title(content):
    return re.findall(r"title.*?\:.*?\'(.*?)\'\,",content)[0]
def parser_txt(doc_id):
    content_url='#https://wenku.baidu.com/browse/interface/getdocpacklist?docId='
def main():
    url=input('请输入要下载的文库Url地址')
    content=fetch_url(url)
    doc_id=get_doc_id(url)
  #  print(doc_id)
    type=pqrser_type(content)
    print(type)
    title=parser_title(content)
main()