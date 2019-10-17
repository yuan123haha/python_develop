# Author:haha
import xml.etree.ElementTree as ET

new_xml = ET.Element("personlist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name=ET.SubElement(personinfo,'name')
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
name.text='haha'
age.text = '33'
personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name2=ET.SubElement(personinfo2,'name2')
age = ET.SubElement(name2, "age")
age.text = '19'
name2.text='enen'
et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式