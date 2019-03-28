def read_NIF(lines):
    elements=[]
    temp=""
    for line in lines.split('\n'):
        l=line.strip()
        if len(l)==0:
            continue
        if l[0]=="@":
            continue
        elif l[0]=="<":
            if temp!="":
                elements.append(temp)
                temp=""
                temp+='\n'+l
            else:
                temp+='\n'+l
        else:
            temp+='\n'+l
    if temp!="":
        elements.append(temp)
        
    texts=[]
    URI=""  
    for element in elements:
        element=element.strip()
        if element[0]=='<':
            URI=element[element.index('<')+1:element.index('>')]
        if 'nif:Context' in element:
            for line in element.split('\n'):
                if len(line)==0:
                    continue
                elif 'nif:isString' in line:
                    texts.append([line[line.index('"')+1:line.rindex('"')].replace('"',''),URI])
    return texts[0]


def generate_NIF_entity(question,context,entity,entity_URL):
    #print(entity_URL)
    try:
        index=question.index(entity)
    except:
        index=-1
        return -1
    #print(question)
    output='\t\t<'+context[:context.index('#')]+'''#char='''+str(index)+''','''+str(index+len(entity))+'''>
            a nif:RFC5147String ;
            nif:anchorOf """'''+entity+'''"""^^xsd:string ;
            nif:beginIndex "'''+str(index)+'''"^^xsd:nonNegativeInteger ;
            nif:endIndex "'''+str(index+len(entity))+'''"^^xsd:nonNegativeInteger ;
            nif:referenceContext <'''+context+'''> ;
            itsrdf:taIdentRef <'''+entity_URL+'''> .
    '''
    return output        
def NIF_output(URI,text,entities):
    output=""
    for entity in entities:
        entity_string=entity[1]
        entity_URL=entity[0]
        temp=generate_NIF_entity(text,URI,entity_string,entity_URL)
        if temp==-1:
            continue
        output+=temp
    return output
        