#!/usr/bin/env python3
import requests
import argparse
import os
parser	=	argparse.ArgumentParser(description='Script para testear metodos')
parser.add_argument('-u', '--url', required=True, help='Fichero con URLs a testear')
parser.add_argument('-ct', '--content', required=True, help='Tipo de content type')
parser.add_argument('-a', '--authorization', help='Tipo de autorizacion')
parser.add_argument('-t', '--token', help='Token de autorizacion')
parser.add_argument('-o', '--output', help='Output file, en caso de querer la informacion en csv')
parser.add_argument('-v', '--verbosity', action='store_true', help='Muestra los resultados en pantalla mientras se guardan en el csv, solo funciona en modo outputfile')
# Paso los argimentos a variables mas faciles de manipular
args	=	parser.parse_args()
fileurl	=	open(args.url)
content	=	args.content
auth	=	args.authorization
token	=	args.token
# Chequeo si hay outputfile, en caso de que si creo los titulos y el archivo)
if args.output != None:
	output	=	open(args.output+'.csv', "w")
	output.write('URL,METODO,RESPONSE'+os.linesep)
# Chequeo de verbose
if args.output == None and args.verbosity:
	print('Falto el output file, en caso de no querer exportar a CSV borrar esta flag')
	exit()
# Creo header con flags entregadas por el user, manejo errores por entrega parciar de datos
if args.authorization and args.token == None:
	print("Falto ingresar token")
	exit()
elif args.authorization == None and args.token:
	print("Falto ingresar el tipo de autenticacion")
	exit()
elif args.authorization and args.token:
	header	=	{
		'Content-Type':content,
		'Authorization':auth+" "+token
	}
else:
	header  =       {
        	'Content-Type':content
        }
# Creo variables de request
rpost	= requests.post
rput	= requests.put
rhead	= requests.head
roptions= requests.options
rpatch	= requests.patch
rget	= requests.get
rdel	= requests.delete
# Ejecucion de request en relacion a lo solicitado por el usuario
# Sin outputfile
if args.output == None:
	for i in fileurl:
		i = i.rstrip('\n')
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print(i)
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print('GET	:'	+	str(rget(i,headers=header)))
		print('PUT	:'	+	str(rput(i,headers=header)))
		print('HEAD	:'	+	str(rhead(i,headers=header)))
		print('OPTIONS	:'	+	str(roptions(i,headers=header)))
		print('PATCH	:'	+	str(rpatch(i,headers=header)))
		print('DEL	:'	+	str(rdel(i,headers=header)))
		print('POST	:'	+	str(rpost(i,headers=header)))
# Con output y sin verbosity
elif args.output and args.verbosity == False:
	for i in fileurl:
		i = i.rstrip('\n')
		output.write(str(i)+','+'GET,'+str(rget(i,headers=header).status_code)+os.linesep)
		output.write(str(i)+','+'PUT,'+str(rput(i,headers=header).status_code)+os.linesep)
		output.write(str(i)+','+'HEAD,'+str(rhead(i,headers=header).status_code)+os.linesep)
		output.write(str(i)+','+'OPTIONS,'+str(roptions(i,headers=header).status_code)+os.linesep)
		output.write(str(i)+','+'PATCH,'+str(rpatch(i,headers=header).status_code)+os.linesep)
		output.write(str(i)+','+'DEL,'+str(rdel(i,headers=header).status_code)+os.linesep)
		output.write(str(i)+','+'POST,'+str(rpost(i,headers=header).status_code)+os.linesep)
# Con output y verbosity
elif args.output and args.verbosity == True:
	for i in fileurl:
		i = i.rstrip('\n')
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print(i)
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print('GET      :'      +       str(rget(i,headers=header)))
		output.write(str(i)+','+'GET,'+str(rget(i,headers=header).status_code)+os.linesep)
		print('PUT      :'      +       str(rput(i,headers=header)))
		output.write(str(i)+','+'PUT,'+str(rput(i,headers=header).status_code)+os.linesep)
		print('HEAD     :'      +       str(rhead(i,headers=header)))
		output.write(str(i)+','+'HEAD,'+str(rhead(i,headers=header).status_code)+os.linesep)
		print('OPTIONS  :'      +       str(roptions(i,headers=header)))
		output.write(str(i)+','+'OPTIONS,'+str(roptions(i,headers=header).status_code)+os.linesep)
		print('PATCH    :'      +       str(rpatch(i,headers=header)))
		output.write(str(i)+','+'PATCH,'+str(rpatch(i,headers=header).status_code)+os.linesep)
		print('DEL      :'      +       str(rdel(i,headers=header)))
		output.write(str(i)+','+'DEL,'+str(rdel(i,headers=header).status_code)+os.linesep)
		print('POST     :'      +       str(rpost(i,headers=header)))
		output.write(str(i)+','+'POST,'+str(rpost(i,headers=header).status_code)+os.linesep)
# Por cualquier error que no hay controlado
else:
	print('Ha ocurrido un error, revise las flags entregadas')
	if output != None:
		output.close
	exit()
# Cierro archivos
if args.output != None:
	output.close
fileurl.close
exit()
