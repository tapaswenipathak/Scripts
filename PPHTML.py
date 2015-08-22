from lxml import etree, html

input_html = raw_input()
document_root = html.fromstring(input_html)
print (etree.tostring(document_root, encoding='unicode', pretty_print=True))
