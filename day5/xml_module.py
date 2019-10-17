# Author:haha

import xml.etree.ElementTree as ET

tree=ET.parse('xml_file')
root=tree.getroot()
print(root.tag)
#输出：data

#遍历整个xml文档
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.attrib,i.text)
#输出：
'''
country {'name': 'Liechtenstein'}
rank {'updated': 'yes'} 2
year {} 2008
gdppc {} 141100
neighbor {'name': 'Austria', 'direction': 'E'} None
neighbor {'name': 'Switzerland', 'direction': 'W'} None
country {'name': 'Singapore'}
rank {'updated': 'yes'} 5
year {} 2011
gdppc {} 59900
neighbor {'name': 'Malaysia', 'direction': 'N'} None
country {'name': 'Panama'}
rank {'updated': 'yes'} 69
year {} 2011
gdppc {} 13600
neighbor {'name': 'Costa Rica', 'direction': 'W'} None
neighbor {'name': 'Colombia', 'direction': 'E'} None
'''
for child in root.iter('year'):#指定一个key值，查看text值
    print(child.tag,child.text)
#输出：
# year 2008
# year 2011
# year 2011

#修改和删除xml文档内容
for child in root.iter('year'):
    new_year=int(child.text)+2
    child.text=str(new_year)
    child.set('update','yes')
tree.write('xml_file')

for child in root.iter('year'):
    print(child.tag,child.text)
#输出：
# year 2010
# year 2013
# year 2013

for country in root.findall('country'):
    rank=int(country.find('rank').text)
    if rank>5:
        root.remove(country)

tree.write('xml_file')
