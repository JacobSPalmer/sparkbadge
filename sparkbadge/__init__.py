import jinja2
from xml.dom import minidom
from sparkbadge import plot_normalizer as norm

_JINJA2_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.PackageLoader('sparkbadge')
)

def _remove_blanks(node):
    for x in node.childNodes:
        if x.nodeType == minidom.Node.TEXT_NODE:
            if x.nodeValue:
                x.nodeValue = x.nodeValue.strip()
        elif x.nodeType == minidom.Node.ELEMENT_NODE:
            _remove_blanks(x)

def badge(data) -> str:
    template = _JINJA2_ENVIRONMENT.get_template('sparkbadge_template.svg')

    svg = template.render(sparklinestr = norm.sparkline_str(data))
    xml = minidom.parseString(svg)
    _remove_blanks(xml)
    xml.normalize()
    return xml.documentElement.toxml()

