#!/bin/bash

echo -e "\n**************************"
echo -e "Bem-Vindo ao Moonlight v1.0"
echo -e "\n**************************"
echo -e "Escolha uma opção:"
echo -e " * 1: Parear Moonlight - Rafael "
echo -e " * 2: Conexão 1080p 60fps"
echo -e " * 3: Conexão 1080p 30fps"
echo -e " * 4: Conexão 720p 60fps"
echo -e " * 5: conexão 720p 30fps"

read NUM

case $NUM in

	1)
		echo -e "\nPareando Moonlight"
		echo -e "*******************"
		
		echo -e "IP do PC para parear com Moonlight.\n"
		#echo -e "IP: echo $'\n> '" ip
		#sudo -u pi moonlight pair $ip
		moonlight pair 192.168.0.107
		
		echo -e "\n**** Computador pareado com sucesso! ****"
		cd /home/pi
		./moon.sh
	;;
	
	2)
		echo -e "Conectando na config Ultra"
		moonlight stream -1080 -30fps -app mstsc 192.168.0.107
	;;
	
	3)
		echo -e "Conectando na config Alta"
		moonlight stream -1080 -30fps -app mstsc 192.168.0.107
	;;
	
	4)
		echo -e "Conectando na config Média"
		moonlight stream -720 -60fps -app mstsc 192.168.0.107
	;;

	5)
		echo -e "Conectando na config Baixa"
		moonlight stream -720 -30fps -app mstsc 192.168.0.107
	;;

	*) echo "Numero Invalido!";;

esac