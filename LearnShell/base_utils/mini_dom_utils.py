# coding=utf-8

__author__ = 'sinlov'

# === minidom操作XML代码示例

import xml
from xml.dom import minidom
import codecs


def fixed_writexml(self, writer, indent="", addindent="", newl=""):
    """
     S.fixed_writexml(self, writer, indent, addindent)
     由于minidom默认的writexml()函数在读取一个xml文件后，修改后重新写入如果加了newl='\n',会将原有的xml中写入多余的行
     indent = current indentation
     addindent = indentation to add to higher levels
     newl = newline string
    """
    writer.write(indent + "<" + self.tagName)

    attrs = self._get_attributes()
    a_names = attrs.keys()
    a_names.sort()

    for a_name in a_names:
        writer.write(" %s=\"" % a_name)
        minidom._write_data(writer, attrs[a_name].value)
        writer.write("\"")
    if self.childNodes:
        if len(self.childNodes) == 1 \
                and self.childNodes[0].nodeType == minidom.Node.TEXT_NODE:
            writer.write(">")
            self.childNodes[0].writexml(writer, "", "", "")
            writer.write("</%s>%s" % (self.tagName, newl))
            return
        writer.write(">%s" % (newl))
        for node in self.childNodes:
            if node.nodeType is not minidom.Node.TEXT_NODE:
                node.writexml(writer, indent + addindent, addindent, newl)
        writer.write("%s</%s>%s" % (indent, self.tagName, newl))
    else:
        writer.write("/>%s" % (newl))


minidom.Element.writexml = fixed_writexml


def opXml():
    # =====从一个空xml文档开始
    impl = xml.dom.getDOMImplementation()
    dom = impl.createDocument(None, 'All_Students', None)
    root = dom.documentElement
    # --创建一个节点，并添加到root下
    student = dom.createElement('student')
    root.appendChild(student)
    # --创建一个子节点，并设置属性
    nameE = dom.createElement('name')
    value = u'测试角色'
    nameE.setAttribute("attr", value)
    nameN = dom.createTextNode(value)
    nameE.appendChild(nameN)
    student.appendChild(nameE)

    # -- 写进文件,如果出现了unicode，指定文件的编码
    f = codecs.open('1.xml', 'w', 'utf-8')
    dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
    f.close()

    # =====处理一个已经存在的xml文档
    dom = xml.dom.minidom.parse("1.xml")
    root = dom.documentElement
    #  -- 重新设置属性
    # --- 返回所有node name为student的节点
    allnodes = dom.getElementsByTagName('student')
    value = u'王力宏'
    for node in allnodes:
        node.setAttribute('name', value)
        # --删除节点属性
    for node in allnodes:
        node.removeAttribute('name')
        # --每个节点有 nodeType,nodeName,和nodeVaulue 等属性
        # --对于textNode，想得到它的文本内容可以使用: .data属性
        print node.nodeType, node.nodeValue
        # --也可以删除节点
        root.removeChild(node)
    f = codecs.open('1.xml', 'w', 'utf-8')
    dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
    f.close()


if __name__ == '__main__':
    opXml()
