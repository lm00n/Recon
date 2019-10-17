# Recon Scrips

Los scrips en este repo fueron realizados en el día a día para tareas de recon e information gathering. No tienen mucha ciencia pero de eso de trata, de mantener simple algunas tareas básicas en la búsqueda de recolección de datos antes de un pentest.


## Curl.sh

Un script simple para corroborar el size en el response de varias paginas web, el fin de este script es descartar y/o encontrar default web page.
> Las URLs deben tener el formato:  https://WEB:PUERTO
> > El uso es simple -> curl.sh ARCHIVO


## Metodos.py

Este script fue creado para testear endpoints probando todos los metodos posibles. Su uso generalmente esta apuntado a APIs.
>usage: metodos.py -u URL -ct CONTENT [-a AUTHORIZATION] [-t TOKEN] [-o OUTPUT] [-v]
> >Solo trabaja con archivo de entrada
> >El content type es obligatorio
> >El output file es en csv, con indicar nobre del archivo es suficiente
> 
>Ejemplo de uso 
>>python3 metodos.py -u urls.txt -ct application/json -a basic -t MTIzOjEyMw== -o result -v


**Trato de mantener lo mas updateado posible este repo**

_**Salu2**_
