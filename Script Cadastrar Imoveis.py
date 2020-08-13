# Script Cadastrar Imoveis

# Desenvolvido Por Raffael Morais

# ## Importando Pandas e Outras Libs Importantes

import pandas as pd
import string
from slugify import slugify
import numpy
from psycopg2.extensions import register_adapter, AsIs


# ## Importando Libs Para Acessar DB

import psycopg2
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import update


# ## Importando Libs Para Acessar O Arquivo XML

from urllib.request import urlopen
from xml.etree.ElementTree import parse
import xml.etree.cElementTree as et



def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)


# ## Realizando Conexão Com O Banco De Dados E Deixando Pronto Para Realizar Comandos SQL

def main():

	POSTGRES_ADDRESS = 'Endereço do Banco de Dados' 
	POSTGRES_PORT = 'Porta do Banco de Dados'
	POSTGRES_USERNAME = 'Nome do Usuario' 
	POSTGRES_PASSWORD = 'Senha do Banco de Dados'  
	POSTGRES_DBNAME = 'Nome do Banco de Dados' 
	# Uma string com as informações necessárias para o login no postgres
	postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(username=POSTGRES_USERNAME,password=POSTGRES_PASSWORD,ipaddress=POSTGRES_ADDRESS,port=POSTGRES_PORT,dbname=POSTGRES_DBNAME))
	# Criando a conexão
	engine = db.create_engine(postgres_str)
	connection = engine.connect()
	metadata = db.MetaData()
	# Lendo a tabela dos imoveis e transformando em um data frame
	db_df =  pd.read_sql_query('''SELECT * FROM imoveis_imovel;''', engine)
	# Pegando as tabelas do DB
	imoveisDB = db.Table('imoveis_imovel', metadata, autoload=True, autoload_with=engine)
	galeriaurl = db.Table('imoveis_galeriaurl',metadata,autoload=True,autoload_with=engine)
	# Salvando o tamanho do data frame
	tam_db = int(db_df.shape[0])


	# ## Acessando o arquivo xml

	var_url = urlopen('Url do arquivo xml')
	xmldoc = parse(var_url)

	# Definindo as colunas do data frame onde vou armazenar informações dos imoveis
	df_cols = ["Url_Imagens","Titulo_Imovel", "Codigo_Imovel", "Tipo_Imovel","Finalidade", "Cidade",
	          "Bairro","Endereco","CondominioF", "Tipo_Locacao","PrecoLocacao","PrecoCondominio",
	           "Area_Util","Area_Total","Area_Privativa", "Observacao","QQUartos","QSuites",
	           "QBanheiro","QGaragem","QGCoberta","Finan","PrecoIptu",
	           "Varanda","Mobiliado","Depen_Empre",
	           "Area_Servico","Despensa"]
	rows = []
	pics = []
	tag ="<p>"
	# Armazenando na variavel o bloco onde vou estar percorrendo com for
	imoveis = xmldoc.findall('Imoveis/Imovel')
	for son in imoveis:
		# Pegando os valores nas tags que me interessavam e salvando nas variaveis
	    name = son.findtext("TituloImovel")
	    name2 = son.findtext("CodigoImovel")
	    name3 = son.findtext("TipoImovel")
	    name4 = son.findtext("Finalidade")
	    name5 = son.findtext("Cidade")
	    name6 = son.findtext("Bairro")
	    name7 = son.findtext("Endereco")
	    name8 = son.findtext("CondominioFechado")
	    if name8 == '1' or name8==1:
	        name8 = True
	    else:
	        name8=False
	    name9 = son.findtext("TipoLocacao")
	    if name9 == None:
	        name9 = son.findtext("TipoOferta")
	    name10 = son.findtext("PrecoLocacao")
	    if name10 == None:
	        name10 = son.findtext("PrecoVenda")
	    name11 = son.findtext("AreaUtil")
	    if name11=='':
	        name11= 0.0
	    else:
	        name11 = float(name11)
	    name12 = son.findtext("AreaTotal")
	    name13 = son.findtext("Observacao")
	    name14 = son.findtext("QtdDormitorios")
	    name14 = int(name14)
	    name15 = son.findtext("PrecoCondominio")
	    if name15 == None:
	        name15 = float(0.0)
	    else:
	        name15 = float(name15)
	    name16 = son.findtext("AceitaFinanciamento")
	    if name16==None:
	        name16=False
	    elif name16 == '1' or name16 == 1:
	        name16 = True
	    else:
	        name16=False
	    name17 = son.findtext("AreaPrivativa")
	    if name17==None:
	        name17=0
	    name18 = son.findtext("PrecoIptu")
	    if name18==None:
	        name18=0
	    name19 = son.findtext("QtdSuites")
	    if name19==None:
	        name19=0
	    name20 = son.findtext("QtdBanheiros")
	    if name20==None:
	        name20=0
	    name21 = son.findtext("QtdVagas")
	    if name21==None:
	        name21=0
	    name22 = son.findtext("QtdVagasCobertas")
	    if name22==None:
	        name22=0
	    name23 = son.findtext("Varanda")
	    if name23==None:
	        name23=False
	    elif name23 == '1' or name23 == 1:
	        name23 = True
	    else:
	        name23=False
	    name24 = son.findtext("Mobiliado")
	    if name24==None:
	        name24=False
	    elif name24 == '1' or name24 == 1:
	        name24 = True
	    else:
	        name24=False
	    name25 = son.findtext("DormitorioEmpregada")
	    if name25==None:
	        name25=False
	    elif name25 == '1' or name25 == 1:
	        name25 = True
	    else:
	        name25=False
	    name26 = son.findtext("AreaServico")
	    if name26==None:
	        name26=False
	    elif name26 == '1' or name26 == 1:
	        name26 = True
	    else:
	        name26=False
	    name27 = son.findtext("Despensa")
	    if name27==None:
	        name27=False
	    elif name27 == '1' or name27 == 1:
	        name27 = True
	    else:
	        name27=False

	    # Dentro do bloco de imoveis, existia outros blocos dentros onde ficavam fotos deles
	    # Então criei essa variavel para "salvar" esse bloco e percorrer ele dentro de outro for    
	    fotos = son.findall('Fotos/Foto')
	    
	    # Aqui ele pegava as urls e salvava em uma lista 
	    for url in fotos:
	        pics.append(url.findtext("URLArquivo"))
	        
	    
	    # Adicionando as informações as linhas do data frame
	    rows.append({"Titulo_Imovel": name,
	                 "Url_Imagens": pics,
	                 "Codigo_Imovel": name2, 
	                 "Tipo_Imovel": name3,
	                 "Finalidade": name4,
	                "Cidade": name5,
	                "Bairro": name6,
	                "Endereco": name7,
	                "PrecoCondominio": name15,
	                "CondominioF": name8,
	                "Tipo_Locacao": name9,
	                "PrecoLocacao": float(name10),
	                "Area_Util": name11,
	                "Area_Total": float(name12),
	                "Observacao": name13,
	                "QQUartos": int(name14),
	                "Finan": name16,
	                "Area_Privativa": float(name17),
	                "PrecoIptu": float(name18),
	                "QSuites": int(name19) ,
	                "QBanheiro": int(name20) ,
	                "QGaragem": int(name21) ,
	                "QGCoberta": int(name22),
	                "Varanda": name23,
	                "Mobiliado": name24,
	                "Depen_Empre":name25 ,
	                "Area_Servico": name26,
	                "Despensa": name27 })
	    # Reiniciando a lista
	    pics=[]
	    
	# Juntando as informações ao data frame novo e pegando o tamanho dele 
	xml_df = pd.DataFrame(rows, columns = df_cols)
	tam_xml = int(xml_df.shape[0])
	xml_df


	# ## Tratando Informações Do DataFrame XML


	#Adiciona o valor zero as celulas onde existiam valores none e NaN
	xml_df.fillna(0,inplace=True)

	# Trantando as informações, trocando o numero pelo nome correspondente  
	for i in range(0,tam_xml):
	    if xml_df['Tipo_Locacao'].iloc[i] == "3":
	        xml_df.ix[i,"Tipo_Locacao"] = "Aluga"
	    else:
	        xml_df.ix[i,"Tipo_Locacao"] = "Venda"
	        


	# ## Dando Get No Id Do Ultimo Imovel e galeria Cadastrada e somando +1 para que ele seja unico
	# Isso permite que o codigo se torne autonomo, sem a necessidade de eu ta criando um Id manualmente toda vez

	idIM = db_df["id"].iloc[-1]+1

	#Pegando o ultimo id da galeria
	gal_id = pd.read_sql_query('''SELECT * FROM imoveis_galeriaurl;''', engine)
	gal_id =gal_id["id"].iloc[-1]+1


	# In[19]:


	register_adapter(numpy.int64, addapt_numpy_int64)


	# ## Analisando e Verificando Se O Imovel Existe No Banco


	exist = False


	for i in range(0,tam_xml):
	    for y in range(0,tam_db):
	        if xml_df['Codigo_Imovel'].iloc[i] == db_df['codigo'].iloc[y]:
	            exist = True

	    # Caso ele não exista, ele então vai passar as informações do data frame que a gente criou 
	    # Para essas variaveis.
	    if exist != True:
	        idim = int(idIM+1)
	        tituloIm = xml_df['Titulo_Imovel'].iloc[i]
	        slugi= slugify(xml_df['Codigo_Imovel'].iloc[i])
	        codigoim= xml_df['Codigo_Imovel'].iloc[i]
	        situi = xml_df['Tipo_Locacao'].iloc[i]
	        tipoi = xml_df['Tipo_Imovel'].iloc[i]
	        tipoIm= xml_df['Finalidade'].iloc[i]
	        enderecoi= xml_df['Endereco'].iloc[i]
	        bairroi= xml_df['Bairro'].iloc[i]
	        cidadei= xml_df['Cidade'].iloc[i]
	        mapai= "Imovel"
	        brevedescrii= xml_df['Observacao'].iloc[i][:200]
	        descri= xml_df['Observacao'].iloc[i]
	        descri = tag+descri+tag
	        quartoi = xml_df['QQUartos'].iloc[i]
	        banho= xml_df['QBanheiro'].iloc[i]
	        suiti= xml_df['QSuites'].iloc[i]
	        garai = xml_df['QGaragem'].iloc[i] 
	        garac= xml_df['QGCoberta'].iloc[i] 
	        garad= xml_df['QGaragem'].iloc[i] 
	        areai= xml_df['Area_Total'].iloc[i]
	        areac= xml_df['Area_Util'].iloc[i]
	        areap= xml_df['Area_Privativa'].iloc[i]
	        iptui = xml_df['PrecoIptu'].iloc[i]
	        valori = xml_df['PrecoLocacao'].iloc[i]
	        condoni = xml_df['PrecoCondominio'].iloc[i]
	        condoFI= xml_df['CondominioF'].iloc[i]
	        finani = xml_df['Finan'].iloc[i]
	        lazeri = False
	        varanda = xml_df['Varanda'].iloc[i]
	        destaquei = False
	        mobiliadoi= xml_df['Mobiliado'].iloc[i]
	        emprei = xml_df['Depen_Empre'].iloc[i]
	        servii = xml_df['Area_Servico'].iloc[i]
	        dispei = xml_df['Despensa'].iloc[i]
	        peti =  False
	        created = db_df['created_at'].iloc[-1]
	    
	        # Cadastrando a imagem principal do imovel 
	        list_pic = xml_df['Url_Imagens'].iloc[i]
	        if len(list_pic)>0:
	            imgP = list_pic[0]
	        else:
	            imgP =""
	        
	        # Comando para cadastrar esse imovel no banco de dados do site
	        query = db.insert(imoveisDB).values(id=idim,imageurl = imgP,titulo=tituloIm,slug=slugi,codigo=codigoim,situ=situi,tipo=tipoi,tipoimo=tipoIm,endereco=enderecoi,bairro=bairroi,cidade=cidadei,mapa=mapai,brevedescri=brevedescrii,descricaocom=descri,quart=quartoi,banh=banho,suit=suiti,gara=garai,garaC=garac,garaD=garad,area=areai,areaP=areap,iptu=iptui,valor=valori,condon=condoni,condominiofechado=condoFI,finan=finani,lazer=lazeri,Varanda=varanda,destaque=destaquei,mobiliado=mobiliadoi,empre=emprei,servi=servii,dispe=dispei,pet=peti) 
	        result = connection.execute(query)
	        
	        # Depois do imovel estar criado
	        # Podemos estar cadastrando a lista das urls na galeria do imovel
	        tam_pic = len(list_pic)
	        if tam_pic>1:
	            for i in range(1,tam_pic):
	                querygal = db.insert(galeriaurl).values(id=gal_id,imagem=list_pic[i],imovel_id=idim)
	                resultgal = connection.execute(querygal)
	                gal_id+=1
	        elif tam_pic==1:
	            db.insert(galeriaurl).values(id=gal_id,imagem=list_pic[0],imovel_id=idim)
	            gal_id+=1
	            
	        print("Imovel cadastrado")
	        idIM+=1
	        
	    exist=False
     
    
    
   






