import pygame
import random
import sys
try:
    #####PARA TODOS XD NO SÉ USAR CLASES AYUDA ESTO NO ES UN MEME#########
    def pastoParaTodos(pantalla, pasto, pasto2):
    	#Pasto img#
    	pantalla.blit(pasto, [0, 0])
    	pantalla.blit(pasto2, [0, 280])
    	pantalla.blit(pasto2, [0, 230])
    	pantalla.blit(pasto2, [0, 180])
    	pantalla.blit(pasto2, [0, 160])

    	#área chica#
    	pastoarea = pygame.transform.scale(pasto2, [530,120])
    	#pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(0, 155, 600, 500))

    	pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(20, 210, 550, 120))
    	#pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(30, 200, 530, 120))
    	pantalla.blit(pastoarea, [30,200])
    	pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(0, 210, 600, 10))

    def arbustoParaTodos(pantalla, arbustoImg):
    	#EL ARBUSTO PARA TODOS XD#
    	pantalla.blit(arbustoImg, [0, 115])
    	pantalla.blit(arbustoImg, [47, 115])
    	pantalla.blit(arbustoImg, [94, 115])
    	pantalla.blit(arbustoImg, [141, 115])
    	pantalla.blit(arbustoImg, [188, 115])
    	pantalla.blit(arbustoImg, [235, 115])
    	pantalla.blit(arbustoImg, [282, 115])
    	pantalla.blit(arbustoImg, [329, 115])
    	pantalla.blit(arbustoImg, [376, 115])
    	pantalla.blit(arbustoImg, [423, 115])
    	pantalla.blit(arbustoImg, [470, 115])
    	pantalla.blit(arbustoImg, [517, 115])
    	pantalla.blit(arbustoImg, [564, 115])
    	pantalla.blit(arbustoImg, [611, 115])

    def todoslosequipos():
    	######Equipos######
    	global chivas,atlas,america,toluca,pumas,monterrey,tigres,cruzazul
    	global americaImg,chivasImg,cruzazulImg,monterreyImg,pumasImg,tigresImg,tolucaImg,atlasImg

    	chivasImg = pygame.image.load('menu\\equipos\\chivas.png')
    	chivasImg = pygame.transform.scale(chivasImg, [200,200])
    	chivas = pygame.sprite.Sprite()
    	chivas.image = chivasImg
    	chivas.rect = chivasImg.get_rect()
    	chivas.rect.left = 220
    	chivas.rect.top = 150
    	colorElegirChivas = (225, 3, 3)
    	elegirChivas = pygame.Rect(263, 450, 120, 40)

    	americaImg = pygame.image.load('menu\\equipos\\america.png')
    	americaImg = pygame.transform.scale(americaImg, [200,200])
    	america = pygame.sprite.Sprite()
    	america.image = americaImg
    	america.rect = americaImg.get_rect()
    	america.rect.left = 220
    	america.rect.top = 150
    	colorElegirAmerica = (237, 221, 21)
    	elegirAmerica = pygame.Rect(263, 450, 120, 40)

    	atlasImg = pygame.image.load('menu\\equipos\\atlas.png')
    	atlasImg = pygame.transform.scale(atlasImg, [200,200])
    	atlas = pygame.sprite.Sprite()
    	atlas.image = atlasImg
    	atlas.rect = atlasImg.get_rect()
    	atlas.rect.left = 220
    	atlas.rect.top = 150
    	colorElegirAtlas = (149, 12, 12)
    	elegirAtlas = pygame.Rect(263, 450, 120, 40)

    	tolucaImg = pygame.image.load('menu\\equipos\\toluca.png')
    	tolucaImg = pygame.transform.scale(tolucaImg, [200,200])
    	toluca = pygame.sprite.Sprite()
    	toluca.image = tolucaImg
    	toluca.rect = tolucaImg.get_rect()
    	toluca.rect.left = 220
    	toluca.rect.top = 150
    	colorElegirToluca = (255, 0, 0)
    	elegirToluca = pygame.Rect(263, 450, 120, 40)

    	tigresImg = pygame.image.load('menu\\equipos\\tigres.png')
    	tigresImg = pygame.transform.scale(tigresImg, [200,200])
    	tigres = pygame.sprite.Sprite()
    	tigres.image = tigresImg
    	tigres.rect = tigresImg.get_rect()
    	tigres.rect.left = 220
    	tigres.rect.top = 150
    	colorElegirTigres = (236, 140, 0)
    	elegirTigres = pygame.Rect(263, 450, 120, 40)

    	cruzazulImg = pygame.image.load('menu\\equipos\\cruzazul.png')
    	cruzazulImg = pygame.transform.scale(cruzazulImg, [200,200])
    	cruzazul = pygame.sprite.Sprite()
    	cruzazul.image = cruzazulImg
    	cruzazul.rect = cruzazulImg.get_rect()
    	cruzazul.rect.left = 220
    	cruzazul.rect.top = 150
    	colorElegirCruzAzul = (16, 49, 234)
    	elegirCruzAzul = pygame.Rect(263, 450, 120, 40)

    	monterreyImg = pygame.image.load('menu\\equipos\\monterrey.png')
    	monterreyImg = pygame.transform.scale(monterreyImg, [200,200])
    	monterrey = pygame.sprite.Sprite()
    	monterrey.image = monterreyImg
    	monterrey.rect = monterreyImg.get_rect()
    	monterrey.rect.left = 220
    	monterrey.rect.top = 150
    	colorElegirMonterrey = (9, 30, 149)
    	elegirMonterrey = pygame.Rect(263, 450, 120, 40)

    	pumasImg = pygame.image.load('menu\\equipos\\pumas.png')
    	pumasImg = pygame.transform.scale(pumasImg, [200,200])
    	pumas = pygame.sprite.Sprite()
    	pumas.image = pumasImg
    	pumas.rect = pumasImg.get_rect()
    	pumas.rect.left = 220
    	pumas.rect.top = 150
    	colorElegirPumas = (141, 122, 29)
    	elegirPumas = pygame.Rect(263, 450, 120, 40)

    #############################################################################

    def ganador(miEquipo):
    	#Agregando un título más dependiendo el equipo campeón#

    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	fps = pygame.time.Clock()
    	salir = False
    	copa = pygame.image.load('trofeo.png')
    	copa = pygame.transform.scale(copa, [70, 120])
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 20)
    	fuenteVolver = pygame.font.Font('menu\\letrasmenu.ttf', 14)
    	cursor = pygame.Rect(50,50,0,0)

    	colorAmerica = [240, 235, 82]
    	colorAtlas = [155, 16, 16]
    	colorChivas = [226, 5, 5]
    	colorCruzAzul = [43, 94, 254]
    	colorMonterrey = [26, 60, 165]
    	colorPumas = [196, 129, 13]
    	colorTigres = [248, 163, 13]
    	colorToluca = [255, 0, 0]

    	todoslosequipos()

    	botonMenu = pygame.Rect(5,5,150,30)
    	colorBotonMenu = [113, 210, 223]

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(botonMenu):
    					menu()
    		fps.tick(60)
    		if miEquipo == 'America':
    			pantalla.fill(colorAmerica)
    			pantalla.blit(americaImg, [210, 210])
    		elif miEquipo == 'Atlas':
    			pantalla.fill(colorAtlas)
    			pantalla.blit(atlasImg, [210, 210])
    		elif miEquipo == 'Chivas':
    			pantalla.fill(colorChivas)
    			pantalla.blit(chivasImg, [210, 210])
    		elif miEquipo == 'Cruz Azul':
    			pantalla.fill(colorCruzAzul)
    			pantalla.blit(cruzazulImg, [210, 210])
    		elif miEquipo == 'Monterrey':
    			pantalla.fill(colorMonterrey)
    			pantalla.blit(monterreyImg, [210, 210])
    		elif miEquipo == 'Pumas':
    			pantalla.fill(colorPumas)
    			pantalla.blit(pumasImg, [210, 210])
    		elif miEquipo == 'Tigres':
    			pantalla.fill(colorTigres)
    			pantalla.blit(tigresImg, [210, 210])
    		elif miEquipo == 'Toluca':
    			pantalla.fill(colorToluca)
    			pantalla.blit(tolucaImg, [210, 210])

    		pantalla.blit(copa, [270, 50])
    		sonidoGanar = pygame.mixer.Sound("sonidos\\ganador.wav")
    		ganaste = fuente.render("ERES CAMPEÓN DEL FUTBOL MEXICANO",4,[255,255,255])
    		felicidades = fuente.render("¡FELICIDADES!",4,[255,255,255])
    		pantalla.blit(ganaste, [110, 450])
    		pantalla.blit(felicidades, [222, 10])

    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		pygame.draw.rect(pantalla, [255,255,255], cursor)

    		pygame.draw.rect(pantalla, colorBotonMenu, botonMenu)
    		txtVolver = fuenteVolver.render("Volver al menú",4,[255,255,255])
    		pantalla.blit(txtVolver, [16,10])
    		pygame.display.update()

    def resultadoFinal(misGoles, goles, miEquipo, randomA, randomB, equipoContrario):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	fps = pygame.time.Clock()
    	salir = False
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 20)
    	fondoRol = pygame.image.load('menu\\fondoMenu.jpg')
    	cursor = pygame.Rect(50, 50, 1, 1)


    ####Auxiliares#####
    	moverMiEquipoY = 0
    	moverMiEquipoX = 0
    	colorMiEquipo = [225, 225, 225]

    	def contrarioEnFinalArriba():
    		moverContrarioX = 4
    		moverContrarioY = 0

    		if cruzazul.rect.x == 400 or monterrey.rect.x == 400 or tigres.rect.x == 400 or chivas.rect.x == 400:
    			moverContrarioY = 0
    			moverContrarioX = 0

    		if randomA == "1":
    			if randomB > 5:
    				cruzazul.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(cruzazul.image, cruzazul.rect)
    			elif randomB <= 5:
    				monterrey.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(monterrey.image, monterrey.rect)

    		if randomA == "2":
    			if randomB > 5:
    				tigres.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(tigres.image, tigres.rect)
    			elif randomB <= 5:
    				chivas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(chivas.image, chivas.rect)

    	def contrarioEnFinalAbajo():
    		moverContrarioX = 4
    		moverContrarioY = 0

    		if atlas.rect.x == 400 or america.rect.x == 400 or toluca.rect.x == 400 or pumas.rect.x == 400:
    			moverContrarioY = 0
    			moverContrarioX = 0

    		if randomA == "1":
    			if randomB > 5:
    				pumas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(pumas.image, pumas.rect)
    			elif randomB <= 5:
    				america.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(america.image, america.rect)
    		elif randomA == "2":
    			if randomB > 5:
    				atlas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(atlas.image, atlas.rect)
    			elif randomB <= 5:
    				toluca.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(toluca.image, toluca.rect)

    	while salir != True:
    		fps.tick(60)
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				salir = True
    				pygame.quit()

    		pantalla.fill([255,255,255])
    		pantalla.blit(fondoRol, [0,0])

    		if miEquipo == "Chivas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if chivas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [232, 22, 22]
    			chivas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(chivas.image, chivas.rect)
    		####Equipo contrario#####
    			contrarioEnFinalAbajo()

    		elif miEquipo == "America":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if america.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [225, 200, 18]
    			america.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(america.image, america.rect)
    		####Equipo contrario#####
    			contrarioEnFinalArriba()

    		elif miEquipo == "Atlas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if atlas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [153, 9, 9]
    			atlas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(atlas.image, atlas.rect)

    			####Equipo contrario#####
    			contrarioEnFinalArriba()

    		elif miEquipo == "Toluca":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if toluca.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [255, 19, 19]
    			toluca.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(toluca.image, toluca.rect)

    			####Equipo contrario#####
    			contrarioEnFinalArriba()

    		elif miEquipo == "Tigres":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if tigres.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [241, 161, 10]
    			tigres.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(tigres.image, tigres.rect)

    			####Equipo contrario#####
    			contrarioEnFinalAbajo()

    		elif miEquipo == "Cruz Azul":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if cruzazul.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 158, 255]
    			cruzazul.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(cruzazul.image, cruzazul.rect)

    			####Equipo contrario#####
    			contrarioEnFinalAbajo()

    		elif miEquipo == "Pumas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if pumas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [184, 153, 31]
    			pumas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(pumas.image, pumas.rect)
    			####Equipo contrario#####
    			contrarioEnFinalArriba()

    		elif miEquipo == "Monterrey":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if monterrey.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 49, 153]
    			monterrey.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(monterrey.image, monterrey.rect)
    			####Equipo contrario#####
    			contrarioEnFinalAbajo()

    		continuarFuente = pygame.font.Font('menu\\letrasmenu.ttf', 15)
    		botonContinuar = pygame.Rect(250, 450, 130, 30)
    		textoContinuar = continuarFuente.render("Continuar", 4, [255,255,255])
    		fuentevs = pygame.font.Font('menu\\letrasmenu.ttf', 30)
    		vs = fuentevs.render("vs", 4, [0,0,0])
    		textoMisGoles = fuente.render("Goles: {}".format(misGoles), 4, colorMiEquipo)
    		textoGolesContrario = fuente.render("Goles {}".format(goles), 4, [0,0,0])
    		pantalla.blit(textoGolesContrario, [450, 400])
    		pantalla.blit(textoMisGoles, [20,400])
    		pantalla.blit(vs, [280, 280])
    		####Si quedan en empate######
    		if goles == misGoles:
    			textoEmpate = fuente.render("EMPATE. Continuan los penales.",4, [6, 139, 199])
    			pantalla.blit(textoEmpate, [100, 10])
    			continuarEmpate = pygame.Rect(250,450, 120, 30)
    			pygame.draw.rect(pantalla, [26, 139, 199], continuarEmpate)
    			textoContinuar = fuente.render("Continuar", 4, [0,0,0])
    			pantalla.blit(textoContinuar, [255, 453])
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuarEmpate):
    						#Registrar partido empatado#
    					if miEquipo == "Toluca":
    						archivoE = open('sts\\toluca\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Pumas":
    						archivoE = open('sts\\pumas\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Monterrey":
    						archivoE = open('sts\\monterrey\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Tigres":
    						archivoE = open('sts\\tigres\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Cruz Azul":
    						archivoE = open('sts\\cruzazul\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Atlas":
    						archivoG = open("sts\\atlas\\e.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "America":
    						archivoG = open("sts\\america\\e.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Chivas":
    						archivoG = open("sts\\e.csv", "a")
    						archivoG.write("1")
    						archivoG.close()
    					final(miEquipo, equipoContrario, randomA, randomB)
    ######Si ganaste######
    		if misGoles > goles:
    			textoGanaste = fuente.render("GANASTE. Pasas a la siguiente ronda.",4, [26, 199, 29])
    			pantalla.blit(textoGanaste, [100, 10])
    			continuarGanaste = pygame.Rect(250,450, 120, 30)
    			pygame.draw.rect(pantalla, [26, 199, 29], continuarGanaste)
    			textoContinuar = fuente.render("Continuar", 4, [0,0,0])
    			pantalla.blit(textoContinuar, [255, 453])
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuarGanaste):
    					#Registrar partido ganado#
    					if miEquipo == "Toluca":
    						archivoG = open('sts\\toluca\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    						#Registrar título#
    						archivoTituloToluca = open('sts\\toluca\\t.csv', 'a')
    						archivoTituloToluca.write("1")
    						archivoTituloToluca.close()

    					if miEquipo == "Pumas":
    						archivoG = open('sts\\pumas\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    						#Registrar título#
    						archivoTituloPumas = open('sts\\pumas\\t.csv', 'a')
    						archivoTituloPumas.write("1")
    						archivoTituloPumas.close()

    					if miEquipo == "Monterrey":
    						archivoG = open('sts\\monterrey\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    						#Registrar título#
    						archivoTituloMonterrey = open('sts\\monterrey\\t.csv', 'a')
    						archivoTituloMonterrey.write("1")
    						archivoTituloMonterrey.close()

    					if miEquipo == "Tigres":
    						archivoG = open('sts\\tigres\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    						#Registrar título#
    						archivoTituloTigres = open('sts\\tigres\\t.csv', 'a')
    						archivoTituloTigres.write("1")
    						archivoTituloTigres.close()

    					if miEquipo == "Cruz Azul":
    						archivoG = open('sts\\cruzazul\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    						#Registrar título#
    						archivoTituloCruzAzul = open('sts\\cruzazul\\t.csv', 'a')
    						archivoTituloCruzAzul.write("1")
    						archivoTituloCruzAzul.close()

    					if miEquipo == "Atlas":
    						archivoG = open("sts\\atlas\\g.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    						#Registrar título#
    						archivoTituloAtlas = open('sts\\atlas\\t.csv', 'a')
    						archivoTituloAtlas.write("1")
    						archivoTituloAtlas.close()

    					if miEquipo == "America":
    						archivoG = open("sts\\america\\g.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    						#Registrar título#
    						archivoTituloAmerica = open('sts\\america\\t.csv', 'a')
    						archivoTituloAmerica.write("1")
    						archivoTituloAmerica.close()

    					if miEquipo == "Chivas":
    						archivoG = open("sts\\g.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    						#Registrar título#
    						archivoTitulo = open('sts\\t.csv', 'a')
    						archivoTitulo.write("1")
    						archivoTitulo.close()
    					ganador(miEquipo)
    ######Si perdiste#######
    		if  goles > misGoles:
    			textoPerdiste = fuente.render("PERDISTE. Quedas fuera del torneo.", 4, [199, 26, 26])
    			pantalla.blit(textoPerdiste, [100, 10])
    			continuarPerdiste = pygame.Rect(250,450, 120, 30)
    			pygame.draw.rect(pantalla, [199, 26, 26], continuarPerdiste)
    			textoContinuar = fuente.render("Continuar", 4, [0,0,0])
    			pantalla.blit(textoContinuar, [255, 453])

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuarPerdiste):
    					#Registrar partido perdido#
    					if miEquipo == "Toluca":
    						archivoP = open('sts\\toluca\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Pumas":
    						archivoP = open('sts\\pumas\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Monterrey":
    						archivoP = open('sts\\monterrey\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Tigres":
    						archivoP = open('sts\\tigres\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Cruz Azul":
    						archivoP = open('sts\\cruzazul\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Atlas":
    						archivoP = open("sts\\atlas\\p.csv", "a")
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "America":
    						archivoP = open("sts\\america\\p.csv", "a")
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Chivas":
    						archivoP = open("sts\\p.csv", "a")
    						archivoP.write("1")
    						archivoP.close()
    					menu()
    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		pygame.display.update()


    def penalesContrarioFinal(misGoles, miEquipo, randomA, randomB, equipoContrario):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	fps = pygame.time.Clock()
    	salir = False
    	cursor = pygame.Rect(50, 50, 1, 1)
    ####Balón######

    	balonPosXInicial = 280
    	balonPosYInicial = 400

    	imgBalonContrario = pygame.image.load('balonC.png')
    	imgBalonContrario = pygame.transform.scale(imgBalonContrario, (30,30))
    	balonContrario = pygame.sprite.Sprite()
    	balonContrario.image = imgBalonContrario
    	balonContrario.rect = imgBalonContrario.get_rect()
    	balonContrario.rect.left = balonPosXInicial
    	balonContrario.rect.top = balonPosYInicial

    	balonesRestantes = pygame.transform.scale(imgBalonContrario, (20, 20))

    	####portero1######
    	#Inicial#
    	imgportero1 = pygame.image.load('portero\\portero1.png')
    	imgportero1 = pygame.transform.scale(imgportero1, (125,140))
    	imgportero2 = pygame.image.load('portero\\portero2.png')
    	imgportero2 = pygame.transform.scale(imgportero2, (150,110))
    	imgportero3 = pygame.image.load('portero\\portero3.png')
    	imgportero3 = pygame.transform.scale(imgportero3, (140,100))
    	imgportero4 = pygame.image.load('portero\\portero4.png')
    	imgportero4 = pygame.transform.scale(imgportero4, (150,110))
    	imgportero5 = pygame.image.load('portero\\portero5.png')
    	imgportero5 = pygame.transform.scale(imgportero5, (150,110))
    	imgportero6 = pygame.image.load('portero\\portero6.png')
    	imgportero6 = pygame.transform.scale(imgportero6, (125,140))
    	imgportero7 = pygame.image.load('portero\\portero7.png')
    	imgportero7 = pygame.transform.scale(imgportero7, (150,110))
    	imgportero8 = pygame.image.load('portero\\portero8.png')
    	imgportero8 = pygame.transform.scale(imgportero8, (150,110))

    	portero1 = pygame.sprite.Sprite()
    	portero1.image = imgportero1
    	portero1.rect = imgportero1.get_rect()
    	porteroPosXInicial = 80
    	porteroPosYInicial = 245
    	portero1.rect.top = porteroPosXInicial
    	portero1.rect.left = porteroPosYInicial

    	portero2 = pygame.sprite.Sprite()
    	portero2.image = imgportero2
    	portero2.rect = imgportero2.get_rect()
    	portero2.rect.top = 80
    	portero2.rect.left = 200

    	portero3 = pygame.sprite.Sprite()
    	portero3.image = imgportero3
    	portero3.rect = imgportero3.get_rect()
    	portero3.rect.top = 0
    	portero3.rect.left = 0

    	portero4 = pygame.sprite.Sprite()
    	portero4.image = imgportero4
    	portero4.rect = imgportero4.get_rect()
    	portero4.rect.top = 80
    	portero4.rect.left = 200

    	portero5 = pygame.sprite.Sprite()
    	portero5.image = imgportero5
    	portero5.rect = imgportero5.get_rect()
    	portero5.rect.top = 80
    	portero5.rect.left = 270

    	portero6 = pygame.sprite.Sprite()
    	portero6.image = imgportero6
    	portero6.rect = imgportero6.get_rect()
    	portero6.rect.top = portero6.rect.top
    	portero6.rect.left = portero6.rect.left

    	portero7 = pygame.sprite.Sprite()
    	portero7.image = imgportero7
    	portero7.rect = imgportero6.get_rect()
    	portero7.rect.top = 130
    	portero7.rect.left = 200

    	portero8 = pygame.sprite.Sprite()
    	portero8.image = imgportero8
    	portero8.rect = imgportero8.get_rect()
    	portero8.rect.top = 80
    	portero8.rect.left = 290

    	xposGuante = 0
    	yposGuante = 0
    	xposGuante2 = 0
    	yposGuante2 = 0
    	guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    	guante2 = pygame.Rect(xposGuante2, yposGuante2, 6, 6)

    #####Cancha######
    	colorPasto = (43, 171, 23)
    	arbustoImg = pygame.image.load('extra\\arbusto.png')
    	arbustoImg = pygame.transform.scale(arbustoImg, [50,50])
    	#pastos XD#

    	pasto = pygame.image.load('extra\\pasto.png')
    	pasto = pygame.transform.scale(pasto, [600,500])
    	pasto2 = pygame.image.load('extra\\pasto2.jpg')

    	#Postes#
    	colorPostes = (255,255,255)
    	iz = pygame.Rect(100, 50, 10, 160)
    	arr = pygame.Rect(100, 50, 380, 10)
    	ab = pygame.Rect(480, 50, 10, 160)
    	#red#
    	imagenRed = pygame.image.load('portero\\redporteria.png')
    	imagenRed = pygame.transform.scale(imagenRed, [395, 245])

    ####Tiros###
    	numTiros = 5
    	fuente = pygame.font.Font('fuentes/letras.otf', 20)

    	textoMarcador = fuente.render("Marcador:", 4, [0,0,0])
    	####Marcador####
    	#Goles#
    	goles = 0
    	#Fallados#
    	fallados = 0
    	#Imagenes#
    	gol = pygame.image.load('marcador\\gol.jpg')
    	fallado = pygame.image.load('marcador\\fallado.jpg')

    	marcador = pygame.Rect(295, 6, 130, 20)
    	tirosMarcador = 0

    ####Aficion####
    	#borde#
    	colorBordeAficion = (136, 11, 11)

    	bordeAficion = pygame.Rect(0,0,600,150)
    	finalBordeAficion = pygame.Rect(0, 120, 600, 40)
    	fila1 = pygame.Rect(0, 30, 600, 5)
    	fila2 = pygame.Rect(0, 60, 600, 5)
    	fila3 = pygame.Rect(0, 90, 600, 5)

    #####Blancos########
    	imgBlanco = pygame.image.load('blanco.png')
    	imgBlanco = pygame.transform.scale(imgBlanco, (30,30))
    	blanco1 = pygame.sprite.Sprite()
    	blanco2 = pygame.sprite.Sprite()
    	blanco3= pygame.sprite.Sprite()
    	blanco4 = pygame.sprite.Sprite()
    	blanco5 = pygame.sprite.Sprite()

    	blanco1.image = imgBlanco
    	blanco1.rect = imgBlanco.get_rect()
    	blanco1.rect.left = 110
    	blanco1.rect.top = 60

    	blanco2.image = imgBlanco
    	blanco2.rect = imgBlanco.get_rect()
    	blanco2.rect.left = 110
    	blanco2.rect.top = 180

    	blanco3.image = imgBlanco
    	blanco3.rect = imgBlanco.get_rect()
    	blanco3.rect.left = 440
    	blanco3.rect.top = 65

    	blanco4.image = imgBlanco
    	blanco4.rect = imgBlanco.get_rect()
    	blanco4.rect.left = 440
    	blanco4.rect.top = 175

    	blanco5.image = imgBlanco
    	blanco5.rect = imgBlanco.get_rect()
    	blanco5.rect.left = 290
    	blanco5.rect.top = 60

    ####Sonidos####

    	sonidoGol = pygame.mixer.Sound("sonidos\\gol.wav")
    	sonidoGol.set_volume(0.3)
    	sonidoTirar = pygame.mixer.Sound("sonidos\\futboltirar.wav")
    	sonidoTirar.set_volume(0.5)

    #####Auxiliares#####
    	ha_tirado = False
    	porteroX = 0
    	porteroY = 0
    	posiciones = ""
    	colorGuante = [0,0,0]
    	listaTiros = ["1", "2", "3", "4", "5"]
    	tiroRandom = random.choice(listaTiros)
    	fallados = 0
    	golFallado = False
    	fallo = False
    	goles = 0
    	golAnotado = False
    	tirosMarcador = 0
    	golFalladoMarcador1 = False
    	golAnotadoMarcador1 = False
    	golFalladoMarcador2 = False
    	golAnotadoMarcador2 = False
    	golFalladoMarcador3 = False
    	golAnotadoMarcador3 = False
    	golFalladoMarcador4 = False
    	golAnotadoMarcador4 = False
    	golFalladoMarcador5 = False
    	golAnotadoMarcador5 = False

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(blanco1.rect):
    					posiciones = "7"
    				elif cursor.colliderect(blanco2.rect):
    					posiciones = "2"
    				elif cursor.colliderect(blanco3.rect):
    					posiciones = "5"
    				elif cursor.colliderect(blanco4.rect):
    					posiciones = "3"
    				elif cursor.colliderect(blanco5.rect):
    					posiciones = "6"
    				if cursor.colliderect(blanco1.rect) or cursor.colliderect(blanco2.rect) or cursor.colliderect(blanco3.rect) or cursor.colliderect(blanco4.rect) or cursor.colliderect(blanco5.rect):
    					ha_tirado = True
    					tirosMarcador += 1
    					sonidoTirar.play()

    		fps.tick(60)
    		pantalla.fill(colorPasto)

    		pygame.draw.rect(pantalla, colorBordeAficion, bordeAficion)
    		pygame.draw.rect(pantalla, [22, 160, 13], finalBordeAficion)
    		#área chica#
    		pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(0, 155, 600, 500))
    		pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(20, 210, 550, 120))
    		pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(30, 200, 530, 120))
    		pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(0, 210, 600, 10))

    		#Pasto img#
    		pastoParaTodos(pantalla, pasto, pasto2)

    		#puntoPenal#
    		pygame.draw.circle(pantalla, (255,255,255), (295, 415), 15)

    		pygame.draw.rect(pantalla, [211, 211, 211], fila1)
    		pygame.draw.rect(pantalla, [211, 211, 211], fila2)
    		pygame.draw.rect(pantalla, [211, 211, 211], fila3)
    		pygame.draw.rect(pantalla, [255,255,255], marcador)

    		#Arbusto#
    		arbustoParaTodos(pantalla, arbustoImg)

    		#pintar red#
    		pantalla.blit(imagenRed, [95, 10])

    		pygame.draw.rect(pantalla, colorPostes, iz)
    		pygame.draw.rect(pantalla, colorPostes, arr)
    		pygame.draw.rect(pantalla, colorPostes, ab)

    		pantalla.blit(blanco1.image, blanco1.rect)
    		pantalla.blit(blanco2.image, blanco2.rect)
    		pantalla.blit(blanco3.image, blanco3.rect)
    		pantalla.blit(blanco4.image, blanco4.rect)
    		pantalla.blit(blanco5.image, blanco5.rect)
    		pantalla.blit(balonContrario.image, balonContrario.rect)

    		if ha_tirado == False:
    			pantalla.blit(portero1.image, portero1.rect)
    			balonContrario.rect.left = balonPosXInicial
    			balonContrario.rect.top = balonPosYInicial
    			velocidadXContrario = 0
    			velocidadYContrario = 0
    			porteroX = 0
    			porteroY = 0
    			tiroRandom = random.choice(listaTiros)
    			portero2.rect.left = 200
    			portero2.rect.top = 80
    			portero3.rect.left = 245
    			portero3.rect.top = 80
    			portero4.rect.left = 200
    			portero4.rect.top = 80
    			portero5.rect.left = 270
    			portero5.rect.top = 80
    			portero6.rect.left = 245
    			portero6.rect.top = 80
    			portero7.rect.left = 200
    			portero7.rect.top = 130
    			portero8.rect.left = 200
    			portero8.rect.top = 130
    			fallo = False
    			golAnotado = False

    		if ha_tirado == True:
    			if numTiros > 0:
    				if posiciones == "2":
    					pantalla.blit(portero2.image, portero2.rect)
    					xposGuante = portero2.rect.left+11
    					yposGuante = portero2.rect.top+100
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -2
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero2.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "3":

    					pantalla.blit(portero3.image, portero3.rect)
    					xposGuante = portero3.rect.left+122
    					yposGuante = portero3.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 3
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero3.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "4":
    					pantalla.blit(portero4.image, portero4.rect)
    					xposGuante = portero4.rect.left+10
    					yposGuante = portero4.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -3
    					porteroY = 0
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero4.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "5":
    					pantalla.blit(portero5.image, portero5.rect)
    					xposGuante = portero5.rect.left+110
    					yposGuante = portero5.rect.top+10
    					xposGuante2 = portero5.rect.left+130
    					yposGuante2 = portero5.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					guante2 = pygame.Rect(xposGuante2, yposGuante2, 8, 8)
    					porteroX = 1
    					porteroY = 2
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					pygame.draw.rect(pantalla, colorGuante, guante2)
    					portero5.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "6":
    					xposGuante = portero5.rect.left+30
    					yposGuante = portero5.rect.top+6
    					guante = pygame.Rect(xposGuante, yposGuante, 12, 6)
    					portero6.rect.left = 245
    					portero6.rect.top = 80
    					pantalla.blit(portero6.image, portero6.rect)
    					pygame.draw.rect(pantalla, (0,0,0), guante)

    				elif posiciones == "7":
    					pantalla.blit(portero7.image, portero7.rect)
    					xposGuante = portero7.rect.left+9
    					yposGuante = portero7.rect.top+5
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -1
    					porteroY = -1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero7.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "8":
    					pantalla.blit(portero8.image, portero8.rect)
    					xposGuante = portero8.rect.left+135
    					yposGuante = portero8.rect.top+8
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 5
    					porteroY = -2
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero8.rect.move_ip(porteroX, porteroY)

    				####Para el contrario#####

    				if tiroRandom == "1":
    					#Arriba izquierda#
    					velocidadXContrario = -4
    					velocidadYContrario = -9
    				elif tiroRandom == "2":
    						#Abajo izquierda#
    					velocidadXContrario = -5
    					velocidadYContrario = -7
    				elif tiroRandom == "3":
    					#Arriba derecha#
    					velocidadXContrario = 5
    					velocidadYContrario = -10
    				elif tiroRandom == "4":
    					#Abajo izquierda#
    					velocidadXContrario = 5
    					velocidadYContrario = -10
    				elif tiroRandom == "5":
    					#centro#
    					velocidadXContrario = 0
    					velocidadYContrario = -10

    				balonContrario.rect.move_ip(velocidadXContrario, velocidadYContrario)

    		if guante.colliderect(balonContrario.rect) or guante2.colliderect(balonContrario.rect):
    			fallados += 1
    			ha_tirado = False
    			golFallado = True
    			fallo = True
    		if balonContrario.rect.colliderect(blanco1.rect) or balonContrario.rect.colliderect(blanco2.rect) or balonContrario.rect.colliderect(blanco3.rect) or balonContrario.rect.colliderect(blanco4.rect) or balonContrario.rect.colliderect(blanco5.rect):
    			if fallo != True:
    				goles += 1
    				golAnotado = True
    			ha_tirado = False

    		if balonContrario.rect.colliderect(guante) or balonContrario.rect.colliderect(blanco1.rect) or balonContrario.rect.colliderect(blanco2.rect) or balonContrario.rect.colliderect(blanco3.rect) or balonContrario.rect.colliderect(blanco4.rect) or balonContrario.rect.colliderect(blanco5.rect):
    			numTiros-=1

    		if numTiros == 0:
    			resultadoFinal(misGoles, goles, miEquipo, randomA, randomB, equipoContrario)

    ##############################################################

    		if tirosMarcador == 1:
    			#RESULTADO1#
    			if golAnotado == True:
    				golAnotadoMarcador1 = True

    			if fallo == True:
    				golFalladoMarcador1 = True

    		if tirosMarcador == 2:
    			#RESULTADO2#
    			if golAnotado == True:
    				golAnotadoMarcador2 = True

    			if fallo == True:
    				golFalladoMarcador2 = True

    		if tirosMarcador == 3:
    			#RESULTADO3#
    			if golAnotado == True:
    				golAnotadoMarcador3 = True

    			if fallo == True:
    				golFalladoMarcador3 = True

    		if tirosMarcador == 4:
    			#RESULTADO4#
    			if golAnotado == True:
    				golAnotadoMarcador4 = True

    			if fallo == True:
    				golFalladoMarcador4 = True

    		if tirosMarcador == 5:
    			#RESULTADO5#
    			if golAnotado == True:
    				golAnotadoMarcador5 = True

    			if fallo == True:
    				golFalladoMarcador5 = True

    ###################################################################

    		if golAnotadoMarcador1 == True:
    			pantalla.blit(gol, [300, 7])

    		elif golFalladoMarcador1 == True:
    			pantalla.blit(fallado, [300, 7])

    		if golAnotadoMarcador2 == True:
    			pantalla.blit(gol, [325, 7])
    		elif golFalladoMarcador2 == True:
    			pantalla.blit(fallado, [325, 7])

    		if golAnotadoMarcador3 == True:
    			pantalla.blit(gol, [350, 7])
    		elif golFalladoMarcador3 == True:
    			pantalla.blit(fallado, [350, 7])

    		if golAnotadoMarcador4 == True:
    			pantalla.blit(gol, [375, 7])
    		elif golFalladoMarcador4 == True:
    			pantalla.blit(fallado, [375, 7])

    		if golAnotadoMarcador5 == True:
    			pantalla.blit(gol, [400, 7])
    		elif golFalladoMarcador5 == True:
    			pantalla.blit(fallado, [400, 7])


    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		tiros = str(numTiros)
    		tirosRestantes = fuente.render("X {}".format(tiros), 4, [255,255,255])
    		pantalla.blit(tirosRestantes, [30, 10])
    		pantalla.blit(balonesRestantes, [0,10])
    		pantalla.blit(textoMarcador, [200, 5])

    		pygame.display.update()

    def cambioDeRolFinal(misGoles, miEquipo, equipoContrario, randomA, randomB):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	fps = pygame.time.Clock()
    	salir = False
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 30)
    	fondoRol = pygame.image.load('menu\\fondoMenu.jpg')
    	cursor = pygame.Rect(50, 50, 1, 1)
    ####Equipos#####
    	todoslosequipos()

    ####Auxiliares#####
    	moverMiEquipoY = 0
    	moverMiEquipoX = 0
    	colorMiEquipo = [225, 225, 225]

    	def contrarioEnFinalArriba():
    		moverContrarioX = 4
    		moverContrarioY = 0

    		if cruzazul.rect.x == 400 or monterrey.rect.x == 400 or tigres.rect.x == 400 or chivas.rect.x == 400:
    			moverContrarioY = 0
    			moverContrarioX = 0

    		if randomA == "1":
    			if randomB > 5:
    				cruzazul.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(cruzazul.image, cruzazul.rect)
    			elif randomB <= 5:
    				monterrey.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(monterrey.image, monterrey.rect)

    		if randomA == "2":
    			if randomB > 5:
    				tigres.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(tigres.image, tigres.rect)
    			elif randomB <= 5:
    				chivas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(chivas.image, chivas.rect)

    	def contrarioEnFinalAbajo():
    		moverContrarioX = 4
    		moverContrarioY = 0

    		if atlas.rect.x == 400 or america.rect.x == 400 or toluca.rect.x == 400 or pumas.rect.x == 400:
    			moverContrarioY = 0
    			moverContrarioX = 0

    		if randomA == "1":
    			if randomB > 5:
    				pumas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(pumas.image, pumas.rect)
    			elif randomB <= 5:
    				america.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(america.image, america.rect)
    		elif randomA == "2":
    			if randomB > 5:
    				atlas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(atlas.image, atlas.rect)
    			elif randomB <= 5:
    				toluca.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(toluca.image, toluca.rect)

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				salir = True
    				pygame.quit()
    		fps.tick(60)
    		pantalla.fill([255,255,255])
    		pantalla.blit(fondoRol, [0,0])

    		if miEquipo == "Chivas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if chivas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [232, 22, 22]
    			chivas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(chivas.image, chivas.rect)
    		####Equipo contrario#####
    			contrarioEnFinalAbajo()

    		elif miEquipo == "America":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if america.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [225, 200, 18]
    			america.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(america.image, america.rect)
    		####Equipo contrario#####
    			contrarioEnFinalArriba()

    		elif miEquipo == "Atlas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if atlas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [153, 9, 9]
    			atlas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(atlas.image, atlas.rect)

    			####Equipo contrario#####
    			contrarioEnFinalArriba()

    		elif miEquipo == "Toluca":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if toluca.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [255, 19, 19]
    			toluca.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(toluca.image, toluca.rect)

    			####Equipo contrario#####
    			contrarioEnFinalArriba()

    		elif miEquipo == "Tigres":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if tigres.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [241, 161, 10]
    			tigres.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(tigres.image, tigres.rect)

    			####Equipo contrario#####
    			contrarioEnFinalAbajo()

    		elif miEquipo == "Cruz Azul":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if cruzazul.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 158, 255]
    			cruzazul.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(cruzazul.image, cruzazul.rect)

    			####Equipo contrario#####
    			contrarioEnFinalAbajo()

    		elif miEquipo == "Pumas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if pumas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [184, 153, 31]
    			pumas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(pumas.image, pumas.rect)
    			####Equipo contrario#####
    			contrarioEnFinalArriba()

    		elif miEquipo == "Monterrey":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if monterrey.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 49, 153]
    			monterrey.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(monterrey.image, monterrey.rect)
    			####Equipo contrario#####
    			contrarioEnFinalAbajo()

    		continuarFuente = pygame.font.Font('menu\\letrasmenu.ttf', 20)
    		botonContinuar = pygame.Rect(250, 450, 130, 30)
    		textoContinuar = continuarFuente.render("Continuar", 4, [255,255,255])
    		fuentevs = pygame.font.Font('menu\\letrasmenu.ttf', 30)
    		vs = fuentevs.render("vs", 4, [0,0,0])
    		textoMisGoles = fuente.render("Goles: {}".format(misGoles), 4, colorMiEquipo)
    		pantalla.blit(textoMisGoles, [20,400])
    		pantalla.blit(vs, [280, 280])
    		pygame.draw.rect(pantalla, [0,0,0], botonContinuar)
    		pantalla.blit(textoContinuar, [260, 455])
    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()

    		if evento.type == pygame.MOUSEBUTTONDOWN:
    			if cursor.colliderect(botonContinuar):
    				penalesContrarioFinal(misGoles, miEquipo, randomA, randomB, equipoContrario)

    		pygame.display.update()

    def final(miEquipo, equipoContrario, randomA, randomB):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600, 500])
    	fps = pygame.time.Clock()
    	salir = False
    	cursor = pygame.Rect(50,50,1,1)
    ###Registrar partido###

    	if miEquipo == "Toluca":
    		archivoPJ = open('sts\\toluca\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Pumas":
    		archivoPJ = open('sts\\pumas\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Monterrey":
    		archivoPJ = open('sts\\monterrey\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Tigres":
    		archivoPJ = open('sts\\tigres\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Cruz Azul":
    		archivoPJ = open('sts\\cruzazul\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Atlas":
    		archivoPJ = open('sts\\atlas\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "America":
    		archivoPJ = open('sts\\america\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Chivas":
    		archivoPJ = open('sts\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    ####Sonidos####

    	sonidoGol = pygame.mixer.Sound("sonidos\\gol.wav")
    	sonidoGol.set_volume(0.3)
    	sonidoTirar = pygame.mixer.Sound("sonidos\\futboltirar.wav")
    	sonidoTirar.set_volume(0.5)

    ####Puntero#####

    	puntero = pygame.Rect(50,50,1,1)
    	rolJugador = True

    ####Balón####
    	imgBalon = pygame.image.load('balonC.png')
    	imgBalon = pygame.transform.scale(imgBalon, (30,30))
    	tirosBalon = pygame.transform.scale(imgBalon, (15, 15))
    	balon = pygame.sprite.Sprite()
    	balon.image = imgBalon
    	balon.rect = imgBalon.get_rect()
    	balonPosXInicial = 280
    	balonPosYInicial = 400
    	balon.rect.left = balonPosXInicial
    	balon.rect.top = balonPosYInicial

    ####portero1######
    	#Inicial#
    	imgportero1 = pygame.image.load('portero\\portero1.png')
    	imgportero1 = pygame.transform.scale(imgportero1, (125,140))
    	imgportero2 = pygame.image.load('portero\\portero2.png')
    	imgportero2 = pygame.transform.scale(imgportero2, (150,110))
    	imgportero3 = pygame.image.load('portero\\portero3.png')
    	imgportero3 = pygame.transform.scale(imgportero3, (140,100))
    	imgportero4 = pygame.image.load('portero\\portero4.png')
    	imgportero4 = pygame.transform.scale(imgportero4, (150,110))
    	imgportero5 = pygame.image.load('portero\\portero5.png')
    	imgportero5 = pygame.transform.scale(imgportero5, (150,110))
    	imgportero6 = pygame.image.load('portero\\portero6.png')
    	imgportero6 = pygame.transform.scale(imgportero6, (125,140))
    	imgportero7 = pygame.image.load('portero\\portero7.png')
    	imgportero7 = pygame.transform.scale(imgportero7, (150,110))
    	imgportero8 = pygame.image.load('portero\\portero8.png')
    	imgportero8 = pygame.transform.scale(imgportero8, (150,110))


    	portero1 = pygame.sprite.Sprite()
    	portero1.image = imgportero1
    	portero1.rect = imgportero1.get_rect()
    	porteroPosXInicial = 80
    	porteroPosYInicial = 245
    	portero1.rect.top = porteroPosXInicial
    	portero1.rect.left = porteroPosYInicial

    	portero2 = pygame.sprite.Sprite()
    	portero2.image = imgportero2
    	portero2.rect = imgportero2.get_rect()
    	portero2.rect.top = 80
    	portero2.rect.left = 200

    	portero3 = pygame.sprite.Sprite()
    	portero3.image = imgportero3
    	portero3.rect = imgportero3.get_rect()
    	portero3.rect.top = 0
    	portero3.rect.left = 0

    	portero4 = pygame.sprite.Sprite()
    	portero4.image = imgportero4
    	portero4.rect = imgportero4.get_rect()
    	portero4.rect.top = 80
    	portero4.rect.left = 200

    	portero5 = pygame.sprite.Sprite()
    	portero5.image = imgportero5
    	portero5.rect = imgportero5.get_rect()
    	portero5.rect.top = 80
    	portero5.rect.left = 270

    	portero6 = pygame.sprite.Sprite()
    	portero6.image = imgportero6
    	portero6.rect = imgportero6.get_rect()
    	portero6.rect.top = portero6.rect.top
    	portero6.rect.left = portero6.rect.left

    	portero7 = pygame.sprite.Sprite()
    	portero7.image = imgportero7
    	portero7.rect = imgportero6.get_rect()
    	portero7.rect.top = 130
    	portero7.rect.left = 200

    	portero8 = pygame.sprite.Sprite()
    	portero8.image = imgportero8
    	portero8.rect = imgportero8.get_rect()
    	portero8.rect.top = 80
    	portero8.rect.left = 290

    	"""NO PONGAS EL 1 PORQUE NO HAY"""
    	posicionesLista = ["2","3","4","5","6","7","8"]
    	if rolJugador == True:
    		posiciones = random.choice(posicionesLista)
    ####Variables de la cancha#####
    	colorPasto = (43, 171, 23)
    	arbustoImg = pygame.image.load('extra\\arbusto.png')
    	arbustoImg = pygame.transform.scale(arbustoImg, [50,50])
    	#pastos XD#

    	pasto = pygame.image.load('extra\\pasto.png')
    	pasto = pygame.transform.scale(pasto, [600,500])
    	pasto2 = pygame.image.load('extra\\pasto2.jpg')

    ####Variables portería#######
    	#Postes#
    	colorPostes = (255,255,255)
    	iz = pygame.Rect(100, 50, 10, 160)
    	arr = pygame.Rect(100, 50, 380, 10)
    	ab = pygame.Rect(480, 50, 10, 160)
    	#red#
    	imagenRed = pygame.image.load('portero\\redporteria.png')
    	imagenRed = pygame.transform.scale(imagenRed, [395, 245])

    ####Aficion####
    	#borde#
    	colorBordeAficion = (136, 11, 11)
    	"""if randomA == "1":
    		colorBordeAficion = (12, 58, 205)
    	elif randomA == "2":
    		colorBordeAficion = (215, 140, 0)
    	"""
    	bordeAficion = pygame.Rect(0,0,600,150)
    	finalBordeAficion = pygame.Rect(0, 120, 600, 40)
    	fila1 = pygame.Rect(0, 30, 600, 5)
    	fila2 = pygame.Rect(0, 60, 600, 5)
    	fila3 = pygame.Rect(0, 90, 600, 5)

    ####Tiros###
    	numTiros = 5

    	fuente = pygame.font.Font('fuentes/letras.otf', 20)

    	imgBlanco = pygame.image.load('blanco.png')
    	imgBlanco = pygame.transform.scale(imgBlanco, (30,30))
    	blanco1 = pygame.sprite.Sprite()
    	blanco2 = pygame.sprite.Sprite()
    	blanco3= pygame.sprite.Sprite()
    	blanco4 = pygame.sprite.Sprite()
    	blanco5 = pygame.sprite.Sprite()

    	blanco1.image = imgBlanco
    	blanco1.rect = imgBlanco.get_rect()
    	blanco1.rect.left = 110
    	blanco1.rect.top = 60

    	blanco2.image = imgBlanco
    	blanco2.rect = imgBlanco.get_rect()
    	blanco2.rect.left = 110
    	blanco2.rect.top = 180

    	blanco3.image = imgBlanco
    	blanco3.rect = imgBlanco.get_rect()
    	blanco3.rect.left = 440
    	blanco3.rect.top = 65

    	blanco4.image = imgBlanco
    	blanco4.rect = imgBlanco.get_rect()
    	blanco4.rect.left = 440
    	blanco4.rect.top = 175

    	blanco5.image = imgBlanco
    	blanco5.rect = imgBlanco.get_rect()
    	blanco5.rect.left = 290
    	blanco5.rect.top = 60

    ####Marcador####
    	#Goles#
    	goles = 0
    	#Fallados#
    	fallados = 0
    	#Imagenes#
    	gol = pygame.image.load('marcador\\gol.jpg')
    	fallado = pygame.image.load('marcador\\fallado.jpg')
    	marcador = pygame.Rect(295, 6, 130, 20)
    	tirosMarcador = 0

    ####Cambiar rol######
    	#cambiarRol = fuente.render("Ahora tú eres el portero, adivina los tiros.", 4, [21, 246, 246])

    ####Variables auxiliares#######
    	ha_tirado = False
    	velocidadX = 0
    	velocidadY = 0
    	segundosInt = 0
    	porteroY = 0
    	porteroX = 0
    	xposGuante = 0
    	yposGuante = 0
    	xposGuante2 = 0
    	yposGuante2 = 0
    	colorGuante = (245, 184, 222)
    	guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    	guante2 = pygame.Rect(xposGuante2, yposGuante2, 6, 6)
    	fallo = False
    	golAnotado = False
    	golFallado = False
    	golFalladoMarcador1 = False
    	golAnotadoMarcador1 = False
    	golFalladoMarcador2 = False
    	golAnotadoMarcador2 = False
    	golFalladoMarcador3 = False
    	golAnotadoMarcador3 = False
    	golFalladoMarcador4 = False
    	golAnotadoMarcador4 = False
    	golFalladoMarcador5 = False
    	golAnotadoMarcador5 = False

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()

    			if numTiros > 0:
    				rolJugador = True
    				if evento.type == pygame.MOUSEBUTTONDOWN:
    					if puntero.colliderect(blanco1.rect):
    						#Arriba izquierda#
    						velocidadX = -4
    						velocidadY = -8

    					elif puntero.colliderect(blanco2.rect):
    						#Abajo izquierda#
    						velocidadX = -5
    						velocidadY = -6

    					elif puntero.colliderect(blanco3.rect):
    						#Arriba derecha#
    						velocidadX = 5
    						velocidadY = -10
    					elif puntero.colliderect(blanco4.rect):
    						#Abajo derecha#
    						velocidadX = 4
    						velocidadY = -6
    					elif puntero.colliderect(blanco5.rect):
    						#centro#

    						velocidadX = 0
    						velocidadY = -8

    					if puntero.colliderect(blanco1.rect) or puntero.colliderect(blanco2.rect) or puntero.colliderect(blanco3.rect) or puntero.colliderect(blanco4.rect) or puntero.colliderect(blanco5.rect):
    						ha_tirado = True
    						tirosMarcador += 1
    						sonidoTirar.play()

    			if numTiros == 0:
    				cambioDeRolFinal(goles, miEquipo, equipoContrario, randomA, randomB)

    		fps.tick(60)
    		pantalla.fill(colorPasto)
    		tiros = str(numTiros)

    		mostrarTiros = fuente.render("X {}".format(tiros), 2, [255,255,255])


    		pygame.draw.rect(pantalla, colorBordeAficion, bordeAficion)
    		pygame.draw.rect(pantalla, (11, 156, 13), finalBordeAficion)

    		#área chica#
    		pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(0, 155, 600, 500))
    		pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(20, 210, 550, 120))
    		pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(30, 200, 530, 120))
    		pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(0, 210, 600, 10))

    		pygame.draw.rect(pantalla, (215,215,215), fila1)
    		pygame.draw.rect(pantalla, (215,215,215), fila2)
    		pygame.draw.rect(pantalla, (215,215,215), fila3)

    		#Pasto img#
    		pastoParaTodos(pantalla, pasto, pasto2)

    		#Arbusto#
    		arbustoParaTodos(pantalla, arbustoImg)

    		pantalla.blit(imagenRed, [95, 10])
    		pygame.draw.rect(pantalla, colorPostes, iz)
    		pygame.draw.rect(pantalla, colorPostes, arr)
    		pygame.draw.rect(pantalla, colorPostes, ab)
    		#puntoPenal#
    		pygame.draw.circle(pantalla, (255,255,255), (295, 415), 15)

    		pantalla.blit(blanco1.image, blanco1.rect)
    		pantalla.blit(blanco2.image, blanco2.rect)
    		pantalla.blit(blanco3.image, blanco3.rect)
    		pantalla.blit(blanco4.image, blanco4.rect)
    		pantalla.blit(blanco5.image, blanco5.rect)

    		if ha_tirado == False:
    			pantalla.blit(portero1.image, portero1.rect)
    			balon.rect.left = balonPosXInicial
    			balon.rect.top = balonPosYInicial
    			velocidadX = 0
    			velocidadY = 0
    			posiciones = random.choice(posicionesLista)
    			portero2.rect.left = 200
    			portero2.rect.top = 80
    			portero3.rect.left = 245
    			portero3.rect.top = 80
    			portero4.rect.left = 200
    			portero4.rect.top = 80
    			portero5.rect.left = 270
    			portero5.rect.top = 80
    			portero6.rect.left = 245
    			portero6.rect.top = 80
    			portero7.rect.left = 200
    			portero7.rect.top = 130
    			portero8.rect.left = 200
    			portero8.rect.top = 130
    			fallo = False
    			golAnotado = False


    		if ha_tirado == True:
    			if numTiros > 0:
    				if posiciones == "2":
    					pantalla.blit(portero2.image, portero2.rect)
    					xposGuante = portero2.rect.left+11
    					yposGuante = portero2.rect.top+100
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -3
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero2.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "3":

    					pantalla.blit(portero3.image, portero3.rect)
    					xposGuante = portero3.rect.left+122
    					yposGuante = portero3.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 2
    					porteroY = 2
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero3.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "4":
    					pantalla.blit(portero4.image, portero4.rect)
    					xposGuante = portero4.rect.left+10
    					yposGuante = portero4.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -1
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero4.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "5":
    					pantalla.blit(portero5.image, portero5.rect)
    					xposGuante = portero5.rect.left+110
    					yposGuante = portero5.rect.top+10
    					xposGuante2 = portero5.rect.left+130
    					yposGuante2 = portero5.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					guante2 = pygame.Rect(xposGuante2, yposGuante2, 8, 8)
    					porteroX = 2
    					porteroY = 0
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					pygame.draw.rect(pantalla, colorGuante, guante2)
    					portero5.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "6":
    					xposGuante = portero5.rect.left+30
    					yposGuante = portero5.rect.top+6
    					guante = pygame.Rect(xposGuante, yposGuante, 12, 6)
    					portero6.rect.left = 245
    					portero6.rect.top = 80
    					pantalla.blit(portero6.image, portero6.rect)
    					pygame.draw.rect(pantalla, (0,0,0), guante)

    				elif posiciones == "7":
    					pantalla.blit(portero7.image, portero7.rect)
    					xposGuante = portero7.rect.left+9
    					yposGuante = portero7.rect.top+5
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -2
    					porteroY = -1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero7.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "8":
    					pantalla.blit(portero8.image, portero8.rect)
    					xposGuante = portero8.rect.left+135
    					yposGuante = portero8.rect.top+8
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 4
    					porteroY = -1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero8.rect.move_ip(porteroX, porteroY)

    		if guante.colliderect(balon.rect) or guante2.colliderect(balon.rect):
    			fallados += 1
    			ha_tirado = False
    			golFallado = True
    			fallo = True
    		if balon.rect.colliderect(blanco1.rect) or balon.rect.colliderect(blanco2.rect) or balon.rect.colliderect(blanco3.rect) or balon.rect.colliderect(blanco4.rect) or balon.rect.colliderect(blanco5.rect):
    			if fallo != True:
    				goles += 1
    				golAnotado = True
    			ha_tirado = False

    		if balon.rect.colliderect(guante) or balon.rect.colliderect(blanco1.rect) or balon.rect.colliderect(blanco2.rect) or balon.rect.colliderect(blanco3.rect) or balon.rect.colliderect(blanco4.rect) or balon.rect.colliderect(blanco5.rect):
    			numTiros-=1

    		balon.rect.move_ip(velocidadX, velocidadY)
    		pantalla.blit(balon.image, balon.rect)

    		pantalla.blit(mostrarTiros, [50, 10])
    		pantalla.blit(tirosBalon, [20,10])

    		pygame.draw.rect(pantalla, (0,0,0), puntero)
    		(puntero.x, puntero.y) = pygame.mouse.get_pos()

    		pygame.draw.rect(pantalla, (255,255,255), marcador)
    		mensajeMarcador = fuente.render("Marcador: ", 2, (0,0,0))
    		pantalla.blit(mensajeMarcador, [205, 7])

    ##############################################################

    		if tirosMarcador == 1:
    			#RESULTADO1#
    			if golAnotado == True:
    				golAnotadoMarcador1 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador1 = True

    		if tirosMarcador == 2:
    			#RESULTADO2#
    			if golAnotado == True:
    				golAnotadoMarcador2 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador2 = True

    		if tirosMarcador == 3:
    			#RESULTADO3#
    			if golAnotado == True:
    				golAnotadoMarcador3 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador3 = True

    		if tirosMarcador == 4:
    			#RESULTADO4#
    			if golAnotado == True:
    				golAnotadoMarcador4 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador4 = True

    		if tirosMarcador == 5:
    			#RESULTADO5#
    			if golAnotado == True:
    				golAnotadoMarcador5 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador5 = True

    ###################################################################

    		if golAnotadoMarcador1 == True:
    			pantalla.blit(gol, [300, 7])

    		elif golFalladoMarcador1 == True:
    			pantalla.blit(fallado, [300, 7])

    		if golAnotadoMarcador2 == True:
    			pantalla.blit(gol, [325, 7])
    		elif golFalladoMarcador2 == True:
    			pantalla.blit(fallado, [325, 7])

    		if golAnotadoMarcador3 == True:
    			pantalla.blit(gol, [350, 7])
    		elif golFalladoMarcador3 == True:
    			pantalla.blit(fallado, [350, 7])

    		if golAnotadoMarcador4 == True:
    			pantalla.blit(gol, [375, 7])
    		elif golFalladoMarcador4 == True:
    			pantalla.blit(fallado, [375, 7])

    		if golAnotadoMarcador5 == True:
    			pantalla.blit(gol, [400, 7])
    		elif golFalladoMarcador5 == True:
    			pantalla.blit(fallado, [400, 7])

    		pygame.display.update()


    def resultadosAFinal(miEquipo, randomA):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	fps = pygame.time.Clock()
    	salir = False
    	cursor = pygame.Rect(50,50,1,1)
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 15)
    	#elegirFinal = ["2", "1"]
    	randomB = random.randrange(0, 10)

    ####Torneo equipos######
    	chivasImg = pygame.image.load('menu\\equipos\\chivas.png')
    	americaImg = pygame.image.load('menu\\equipos\\america.png')
    	atlasImg = pygame.image.load('menu\\equipos\\atlas.png')
    	tolucaImg = pygame.image.load('menu\\equipos\\toluca.png')
    	tigresImg = pygame.image.load('menu\\equipos\\tigres.png')
    	cruzazulImg = pygame.image.load('menu\\equipos\\cruzazul.png')
    	monterreyImg = pygame.image.load('menu\\equipos\\monterrey.png')
    	pumasImg = pygame.image.load('menu\\equipos\\pumas.png')

    	chivasImg = pygame.transform.scale(chivasImg, [30,30])
    	americaImg = pygame.transform.scale(americaImg, [30,30])
    	atlasImg = pygame.transform.scale(atlasImg, [30,30])
    	tolucaImg = pygame.transform.scale(tolucaImg, [30,30])
    	tigresImg = pygame.transform.scale(tigresImg, [30,30])
    	cruzazulImg = pygame.transform.scale(cruzazulImg, [30,30])
    	pumasImg = pygame.transform.scale(pumasImg, [30,30])
    	monterreyImg = pygame.transform.scale(monterreyImg, [30,30])

    	chivas = pygame.sprite.Sprite()
    	chivas.image = chivasImg
    	chivas.rect = chivasImg.get_rect()
    	chivas.rect.left = 30
    	chivas.rect.top = 255
    	if miEquipo == "Chivas" or randomA == "2":
    		chivas.rect.left = 180
    		chivas.rect.top = 265

    	monterrey = pygame.sprite.Sprite()
    	monterrey.image = monterreyImg
    	monterrey.rect = monterreyImg.get_rect()
    	monterrey.rect.left = 30
    	monterrey.rect.top = 300
    	if miEquipo == "Monterrey" or randomA == "1":
    		monterrey.rect.left = 180
    		monterrey.rect.top = 265

    	tigres = pygame.sprite.Sprite()
    	tigres.image = tigresImg
    	tigres.rect = tigresImg.get_rect()
    	tigres.rect.left = 30
    	tigres.rect.top = 355

    	if miEquipo == "Tigres" or randomA == "2":
    		tigres.rect.left = 180
    		tigres.rect.top = 365

    	cruzazul = pygame.sprite.Sprite()
    	cruzazul.image = cruzazulImg
    	cruzazul.rect = cruzazulImg.get_rect()
    	cruzazul.rect.left = 30
    	cruzazul.rect.top = 405
    	if miEquipo == "Cruz Azul" or randomA == "1":
    		cruzazul.rect.left = 180
    		cruzazul.rect.top = 365

    	atlas = pygame.sprite.Sprite()
    	atlas.image = atlasImg
    	atlas.rect = atlasImg.get_rect()
    	atlas.rect.left = 30
    	atlas.rect.top = 20
    	if miEquipo == "Atlas" or randomA == "2":
    		atlas.rect.left = 180
    		atlas.rect.top = 45

    	america = pygame.sprite.Sprite()
    	america.image = americaImg
    	america.rect = americaImg.get_rect()
    	america.rect.left = 30
    	america.rect.top = 70
    	if miEquipo == "America" or randomA == "1":
    		america.rect.left = 180
    		america.rect.top = 45

    	toluca = pygame.sprite.Sprite()
    	toluca.image = tolucaImg
    	toluca.rect = tolucaImg.get_rect()
    	toluca.rect.left = 30
    	toluca.rect.top = 160
    	if miEquipo == "Toluca" or randomA == "2":
    		toluca.rect.left = 180
    		toluca.rect.top = 160

    	pumas = pygame.sprite.Sprite()
    	pumas.image = pumasImg
    	pumas.rect = pumasImg.get_rect()
    	pumas.rect.left = 30
    	pumas.rect.top = 190
    	if miEquipo == "Pumas" or randomA == "1":
    		pumas.rect.left = 180
    		pumas.rect.top = 160


    ####Texto#######
    	equipoEnPantalla = fuente.render("Tu equipo:", 4, [0,0,0])
    	contrarioEnPantalla = fuente.render("Contrario:", 4, [0,0,0])
    ####Torneo posiciones#####
    	torneo = pygame.image.load('posiciones\\posiciones.jpg')

    ####Botón continuar####
    	continuar = pygame.Rect(400, 460, 100, 30)
    	colorContinuar = [0,0,0]
    	fuenteContinuar = pygame.font.Font('menu\\letrasmenu.ttf', 15)
    	textoContinuar = fuenteContinuar.render("Continuar", 4, [255,255,255])

    ####Auxiliares####
    	velX = 0
    	velY = 0
    	equipoContrario = ""

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()

    		fps.tick(60)
    		pantalla.fill([255,255,255])
    		pantalla.blit(torneo, [70,30])
    		pantalla.fill([255,255,255])

    		pantalla.blit(torneo, [70,30])
    		#Grupo1#
    		pantalla.blit(atlas.image, atlas.rect)
    		pantalla.blit(america.image, america.rect)
    		#Grupo2#
    		pantalla.blit(toluca.image, toluca.rect)
    		pantalla.blit(pumas.image, pumas.rect)
    		#Grupo3#
    		pantalla.blit(chivas.image, chivas.rect)
    		pantalla.blit(monterrey.image, monterrey.rect)
    		#Grupo4#
    		pantalla.blit(tigres.image, tigres.rect)
    		pantalla.blit(cruzazul.image, cruzazul.rect)
    		#Mi equipo#
    		pantalla.blit(equipoEnPantalla, [0, 475])
    		pantalla.blit(contrarioEnPantalla, [150, 475])

    		pygame.draw.rect(pantalla, colorContinuar, continuar)
    		pantalla.blit(textoContinuar, [406, 465])

    		def contrarioEquiposArriba():
    			if randomA == "1":
    				if randomB > 5:
    					pantalla.blit(cruzazulImg, [240, 470])
    					equipoContrario = "Cruz Azul"
    				elif randomB <= 5:
    					pantalla.blit(monterreyImg, [240, 470])
    					equipoContrario = "Monterrey"
    			elif randomA == "2":
    				if randomB > 5:
    					pantalla.blit(tigresImg, [240, 470])
    					equipoContrario = "Tigres"
    				elif randomB <= 5:
    					pantalla.blit(chivasImg, [240, 470])
    					equipoContrario = "Chivas"
    		def contrarioEquiposAbajo():
    			if randomA == "1":
    				if randomB > 5:
    					pantalla.blit(pumasImg, [240, 470])
    					equipoContrario = "Pumas"
    				elif randomB <= 5:
    					pantalla.blit(americaImg, [240, 470])
    					equipoContrario = "America"
    			elif randomA == "2":
    				if randomB > 5:
    					pantalla.blit(atlasImg, [240, 470])
    					equipoContrario = "Atlas"
    				elif randomB <= 5:
    					pantalla.blit(tolucaImg, [240, 470])
    					equipoContrario = "Toluca"

    		if miEquipo == "Chivas":
    			pantalla.blit(chivasImg, [90, 470])
    			#Contrario en primer juego#
    			#EL 1 SON LOS QUE SE ACOMODAN  PARA ARRIBA WN
    			contrarioEquiposAbajo()


    		elif miEquipo == "America":
    			pantalla.blit(americaImg, [90, 470])
    			#Contrario en primer juego#
    			contrarioEquiposArriba()

    		elif miEquipo == "Atlas":
    			pantalla.blit(atlasImg, [90, 470])
    			#Contrario#
    			contrarioEquiposArriba()

    		elif miEquipo == "Toluca":
    			pantalla.blit(tolucaImg, [90, 470])
    			#Contrario en primer juego#
    			contrarioEquiposArriba()

    		elif miEquipo == "Tigres":
    			pantalla.blit(tigresImg, [90, 470])
    			#Contrario en primer juego#
    			contrarioEquiposAbajo()

    		elif miEquipo == "Cruz Azul":
    			pantalla.blit(cruzazulImg, [90, 470])
    			#Contrario en primer juego#
    			contrarioEquiposAbajo()

    		elif miEquipo == "Pumas":
    			pantalla.blit(pumasImg, [90, 470])
    			contrarioEquiposArriba()

    		elif miEquipo == "Monterrey":
    			pantalla.blit(monterreyImg, [90, 470])
    			#Contrario en primer juego#
    			contrarioEquiposAbajo()

    ####Si tu equipo está en el grupo A#
    		def finalistaA():

    			if randomA == "2":
    				if randomB > 5:
    					velXContrario = 0
    					velYContrario = -1
    					if tigres.rect.top == 340:
    						velXContrario = 1
    						velYContrario = 0
    						if tigres.rect.left == 370:
    							velXContrario = 0
    							velYContrario = 0
    					tigres.rect.move_ip(velXContrario, velYContrario)

    				elif randomB <= 5:
    					velXContrario = 0
    					velYContrario = 1
    					if chivas.rect.top == 350:
    						velXContrario = 1
    						velYContrario = 0
    						if chivas.rect.left == 370:
    							velXContrario = 0
    							velYContrario = 0
    					chivas.rect.move_ip(velXContrario, velYContrario)

    			elif randomA == "1":
    				if randomB > 5:
    					velXContrario = 0
    					velYContrario = -1
    					if cruzazul.rect.top == 350:
    						velXContrario = 1
    						velYContrario = 0
    						if cruzazul.rect.left == 370:
    							velXContrario = 0
    							velYContrario = 0
    					cruzazul.rect.move_ip(velXContrario, velYContrario)

    				elif randomB <= 5:
    					velXContrario = 0
    					velYContrario = 1
    					if monterrey.rect.top == 350:
    						velXContrario = 1
    						velYContrario = 0
    						if monterrey.rect.left == 370:
    							velXContrario = 0
    							velYContrario = 0
    					monterrey.rect.move_ip(velXContrario, velYContrario)
    ############################################################################

    		def finalistaB():

    			if randomA == "2":
    				if randomB > 5:
    					velXContrario = 0
    					velYContrario = 1
    					if atlas.rect.top == 100:
    						velXContrario = 1
    						velYContrario = 0
    						if atlas.rect.left == 370:
    							velXContrario = 0
    							velYContrario = 0
    					atlas.rect.move_ip(velXContrario, velYContrario)

    				elif randomB <= 5:
    					velXContrario = 0
    					velYContrario = -1
    					if toluca.rect.top == 100:
    						velXContrario = 1
    						velYContrario = 0
    						if toluca.rect.left == 370:
    							velXContrario = 0
    							velYContrario = 0
    					toluca.rect.move_ip(velXContrario, velYContrario)

    			elif randomA == "1":
    				if randomB > 5:
    					velXContrario = 0
    					velYContrario = -1
    					if pumas.rect.top == 100:
    						velXContrario = 1
    						velYContrario = 0
    						if pumas.rect.left == 370:
    							velXContrario = 0
    							velYContrario = 0
    					pumas.rect.move_ip(velXContrario, velYContrario)

    				elif randomB <= 5:
    					velXContrario = 0
    					velYContrario = 1
    					if america.rect.top == 100:
    						velXContrario = 1
    						velYContrario = 0
    						if america.rect.left == 370:
    							velXContrario = 0
    							velYContrario = 0
    					america.rect.move_ip(velXContrario, velYContrario)


    		if miEquipo == "Atlas":
    			velX = 0
    			velY = 1

    			if atlas.rect.top == 100:
    				velX = 1
    				velY = 0
    				if atlas.rect.left == 370:
    					velX = 0
    					velY = 0
    			atlas.rect.move_ip(velX, velY)

    			if randomA == "1":
    				pumas.rect.left = 180
    				pumas.rect.top = 160
    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				toluca.rect.left = 180
    				toluca.rect.top = 160
    			finalistaA()

    		elif miEquipo == "America":
    			velX = 0
    			velY = 1

    			if america.rect.top == 100:
    				velX = 1
    				velY = 0
    				if america.rect.left == 370:
    					velX = 0
    					velY = 0
    			america.rect.move_ip(velX, velY)

    			if randomA == "1":
    				pumas.rect.left = 180
    				pumas.rect.top = 160
    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				toluca.rect.left = 180
    				toluca.rect.top = 160
    			finalistaA()

    		elif miEquipo == "Toluca":
    			velX = 0
    			velY = -1
    			if toluca.rect.top == 100:
    				velX = 1
    				velY = 0
    				if toluca.rect.left == 370:
    					velX = 0
    					velY = 0
    			toluca.rect.move_ip(velX, velY)

    			if randomA == "1":
    				america.rect.left = 180
    				america.rect.top = 50
    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				atlas.rect.left = 180
    				atlas.rect.top = 50
    			finalistaA()

    		elif miEquipo == "Pumas":
    			velX = 0
    			velY = -1
    			if pumas.rect.top == 100:
    				velX = 1
    				velY = 0
    				if pumas.rect.left == 370:
    					velX = 0
    					velY = 0
    			pumas.rect.move_ip(velX, velY)

    			if randomA == "1":
    				america.rect.left = 180
    				america.rect.top = 50
    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				atlas.rect.left = 180
    				atlas.rect.top = 50
    			finalistaA()
    ################################################################################

    		elif miEquipo == "Chivas":
    			velX = 0
    			velY = 1
    			if chivas.rect.top == 350:
    				velX = 1
    				velY = 0
    				if chivas.rect.left == 370:
    					velX = 0
    					velY = 0
    			chivas.rect.move_ip(velX, velY)
    			monterrey.rect.left = 30
    			monterrey.rect.top = 300

    			if randomA == "2":
    				tigres.rect.left = 180
    				tigres.rect.top = 365
    			elif randomA == "1":
    				###Otro grupo de 4 equipos###
    				cruzazul.rect.left = 180
    				cruzazul.rect.top = 365
    			finalistaB()

    		elif miEquipo == "Monterrey":
    			velX = 0
    			velY = 1
    			if monterrey.rect.top == 350:
    				velX = 1
    				velY = 0
    				if monterrey.rect.left == 370:
    					velX = 0
    					velY = 0
    			monterrey.rect.move_ip(velX, velY)
    			chivas.rect.left = 30
    			chivas.rect.top = 255

    			if randomA == "2":
    				tigres.rect.left = 180
    				tigres.rect.top = 365
    			elif randomA == "1":
    				###Otro grupo de 4 equipos###
    				cruzazul.rect.left = 180
    				cruzazul.rect.top = 365
    			finalistaB()

    		elif miEquipo == "Tigres":
    			velX = 0
    			velY = -1
    			if tigres.rect.top == 350:
    				velX = 1
    				velY = 0
    				if tigres.rect.left == 370:
    					velX = 0
    					velY = 0
    			tigres.rect.move_ip(velX, velY)
    			cruzazul.rect.left = 30
    			cruzazul.rect.top = 355

    			if randomA == "2":
    				chivas.rect.left = 180
    				chivas.rect.top = 265
    			elif randomA == "1":
    				###Otro grupo de 4 equipos###
    				monterrey.rect.left = 180
    				monterrey.rect.top = 265
    			finalistaB()

    		elif miEquipo == "Cruz Azul":
    			velX = 0
    			velY = -1
    			if cruzazul.rect.top == 350:
    				velX = 1
    				velY = 0
    				if cruzazul.rect.left == 370:
    					velX = 0
    					velY = 0
    			cruzazul.rect.move_ip(velX, velY)
    			tigres.rect.left = 30
    			tigres.rect.top = 355

    			if randomA == "2":
    				chivas.rect.left = 180
    				chivas.rect.top = 265
    			elif randomA == "1":
    				###Otro grupo de 4 equipos###
    				monterrey.rect.left = 180
    				monterrey.rect.top = 265
    			finalistaB()

    	#######Si mi equipo está en el grupo B#####
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuar):
    					final(miEquipo, equipoContrario, randomA, randomB)

    		pygame.display.update()

    def resultadoSemifinal(misGoles, goles, miEquipo, randomA):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600, 500])
    	fps = pygame.time.Clock()
    	salir = False
    	cursor = pygame.Rect(50, 50, 1, 1)
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 20)

    #####Fondo#####
    	fondo = pygame.image.load('menu\\fondoMenu.jpg')

    ####Equipos####
    	todoslosequipos()

    	####Auxiliares#####
    	moverMiEquipoY = 0
    	moverMiEquipoX = 0
    	colorMiEquipo = [225, 225, 225]
    	equipoContrario = ""

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()

    		fps.tick(60)
    		pantalla.fill([255,255,255])
    		pantalla.blit(fondo, [0,0])

    		if miEquipo == "Chivas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if chivas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [232, 22, 22]
    			chivas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(chivas.image, chivas.rect)
    		####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if cruzazul.rect.x == 400 or tigres.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			if randomA == "1":
    					cruzazul.rect.move_ip(moverContrarioX, moverContrarioY)
    					pantalla.blit(cruzazul.image, cruzazul.rect)
    					equipoContrario = "Cruz Azul"
    			if randomA == "2":
    				tigres.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(tigres.image, tigres.rect)
    				equipoContrario = "Tigres"

    		elif miEquipo == "America":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if america.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [225, 200, 18]
    			america.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(america.image, america.rect)
    		####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if pumas.rect.x == 400 or toluca.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			if randomA == "1":
    				pumas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(pumas.image, pumas.rect)
    				equipoContrario = "Pumas"
    			if randomA == "2":
    				toluca.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(toluca.image, toluca.rect)
    				equipoContrario = "Toluca"

    		elif miEquipo == "Atlas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if atlas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [153, 9, 9]
    			atlas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(atlas.image, atlas.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if pumas.rect.x == 400 or toluca.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			if randomA == "1":
    				pumas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(pumas.image, pumas.rect)
    				equipoContrario = "Pumas"
    			if randomA == "2":
    				toluca.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(toluca.image, toluca.rect)
    				equipoContrario = "Toluca"

    		elif miEquipo == "Toluca":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if toluca.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [255, 19, 19]
    			toluca.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(toluca.image, toluca.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if america.rect.x == 400 or atlas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			if randomA == "1":
    				america.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(america.image, america.rect)
    				equipoContrario = "America"
    			if randomA == "2":
    				atlas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(atlas.image, atlas.rect)
    				equipoContrario = "Atlas"

    		elif miEquipo == "Tigres":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if tigres.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [241, 161, 10]
    			tigres.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(tigres.image, tigres.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if monterrey.rect.x == 400 or chivas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			if randomA == "1":
    				monterrey.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(monterrey.image, monterrey.rect)
    				equipoContrario = "Monterrey"
    			if randomA == "2":
    				chivas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(chivas.image, chivas.rect)
    				equipoContrario = "Chivas"

    		elif miEquipo == "Cruz Azul":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if cruzazul.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 158, 255]
    			cruzazul.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(cruzazul.image, cruzazul.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if monterrey.rect.x == 400 or chivas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			if randomA == "1":
    				monterrey.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(monterrey.image, monterrey.rect)
    				equipoContrario = "Monterrey"
    			if randomA == "2":
    				chivas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(chivas.image, chivas.rect)
    				equipoContrario = "Chivas"

    		elif miEquipo == "Pumas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if pumas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [184, 153, 31]
    			pumas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(pumas.image, pumas.rect)
    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if america.rect.x == 400 or atlas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			if randomA == "1":
    				america.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(america.image, america.rect)
    				equipoContrario = "America"
    			if randomA == "2":
    				atlas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(atlas.image, atlas.rect)
    				equipoContrario = "Atlas"

    		elif miEquipo == "Monterrey":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if monterrey.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 49, 153]
    			monterrey.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(monterrey.image, monterrey.rect)
    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if cruzazul.rect.x == 400 or tigres.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			if randomA == "1":
    					cruzazul.rect.move_ip(moverContrarioX, moverContrarioY)
    					pantalla.blit(cruzazul.image, cruzazul.rect)
    					equipoContrario = "Cruz Azul"
    			if randomA == "2":
    				tigres.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(tigres.image, tigres.rect)
    				equipoContrario = "Tigres"

    		textoMisGoles = fuente.render("Goles {}".format(misGoles), 4, colorMiEquipo)
    		textoGolesContrario = fuente.render("Goles {}".format(goles), 4, [0,0,0])
    		textovs = fuente.render("vs", 4, [0,0,0])
    		pantalla.blit(textoMisGoles, [50, 400])
    		pantalla.blit(textoGolesContrario, [450, 400])
    		pantalla.blit(textovs, [300, 250])
    ####Si quedan en empate######
    		if goles == misGoles:
    			textoEmpate = fuente.render("EMPATE. Continuan los penales.",4, [6, 139, 199])
    			pantalla.blit(textoEmpate, [100, 10])
    			continuarEmpate = pygame.Rect(250,450, 120, 30)
    			pygame.draw.rect(pantalla, [26, 139, 199], continuarEmpate)
    			textoContinuar = fuente.render("Continuar", 4, [0,0,0])
    			pantalla.blit(textoContinuar, [255, 453])
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuarEmpate):
    						#Registrar partido empatado#
    					if miEquipo == "Toluca":
    						archivoE = open('sts\\toluca\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Pumas":
    						archivoE = open('sts\\pumas\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Monterrey":
    						archivoE = open('sts\\monterrey\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Tigres":
    						archivoE = open('sts\\tigres\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Cruz Azul":
    						archivoE = open('sts\\cruzazul\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Atlas":
    						archivoG = open("sts\\atlas\\e.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "America":
    						archivoG = open("sts\\america\\e.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Chivas":
    						archivoG = open("sts\\e.csv", "a")
    						archivoG.write("1")
    						archivoG.close()
    					semifinal(miEquipo, equipoContrario, randomA)
    ######Si ganaste######
    		if misGoles > goles:
    			textoGanaste = fuente.render("GANASTE. Pasas a la siguiente ronda.",4, [26, 199, 29])
    			pantalla.blit(textoGanaste, [100, 10])
    			continuarGanaste = pygame.Rect(250,450, 120, 30)
    			pygame.draw.rect(pantalla, [26, 199, 29], continuarGanaste)
    			textoContinuar = fuente.render("Continuar", 4, [0,0,0])
    			pantalla.blit(textoContinuar, [255, 453])
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuarGanaste):
    					#Registrar partido ganado#
    					if miEquipo == "Toluca":
    						archivoG = open('sts\\toluca\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Pumas":
    						archivoG = open('sts\\pumas\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Monterrey":
    						archivoG = open('sts\\monterrey\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Tigres":
    						archivoG = open('sts\\tigres\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Cruz Azul":
    						archivoG = open('sts\\cruzazul\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Atlas":
    						archivoG = open("sts\\atlas\\g.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "America":
    						archivoG = open("sts\\america\\g.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Chivas":
    						archivoG = open("sts\\g.csv", "a")
    						archivoG.write("1")
    						archivoG.close()
    					resultadosAFinal(miEquipo, randomA)
    ######Si perdiste#######
    		if  goles > misGoles:
    			textoPerdiste = fuente.render("PERDISTE. Quedas fuera del torneo.", 4, [199, 26, 26])
    			pantalla.blit(textoPerdiste, [100, 10])
    			continuarPerdiste = pygame.Rect(250,450, 120, 30)
    			pygame.draw.rect(pantalla, [199, 26, 26], continuarPerdiste)
    			textoContinuar = fuente.render("Continuar", 4, [0,0,0])
    			pantalla.blit(textoContinuar, [255, 453])

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuarPerdiste):
    					#Registrar partido perdido#
    					if miEquipo == "Toluca":
    						archivoP = open('sts\\toluca\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Pumas":
    						archivoP = open('sts\\pumas\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Monterrey":
    						archivoP = open('sts\\monterrey\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Tigres":
    						archivoP = open('sts\\tigres\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Cruz Azul":
    						archivoP = open('sts\\cruzazul\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Atlas":
    						archivoP = open("sts\\atlas\\p.csv", "a")
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "America":
    						archivoP = open("sts\\america\\p.csv", "a")
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Chivas":
    						archivoP = open("sts\\p.csv", "a")
    						archivoP.write("1")
    						archivoP.close()
    					menu()
    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		pygame.display.update()


    def penalesContrarioSemifinal(misGoles, miEquipo, randomA):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	fps = pygame.time.Clock()
    	salir = False
    	cursor = pygame.Rect(50, 50, 1, 1)
    ####Balón######

    	balonPosXInicial = 280
    	balonPosYInicial = 400

    	imgBalonContrario = pygame.image.load('balonC.png')
    	imgBalonContrario = pygame.transform.scale(imgBalonContrario, (30,30))
    	balonContrario = pygame.sprite.Sprite()
    	balonContrario.image = imgBalonContrario
    	balonContrario.rect = imgBalonContrario.get_rect()
    	balonContrario.rect.left = balonPosXInicial
    	balonContrario.rect.top = balonPosYInicial

    	balonesRestantes = pygame.transform.scale(imgBalonContrario, (20, 20))

    	####portero1######
    	#Inicial#
    	imgportero1 = pygame.image.load('portero\\portero1.png')
    	imgportero1 = pygame.transform.scale(imgportero1, (125,140))
    	imgportero2 = pygame.image.load('portero\\portero2.png')
    	imgportero2 = pygame.transform.scale(imgportero2, (150,110))
    	imgportero3 = pygame.image.load('portero\\portero3.png')
    	imgportero3 = pygame.transform.scale(imgportero3, (140,100))
    	imgportero4 = pygame.image.load('portero\\portero4.png')
    	imgportero4 = pygame.transform.scale(imgportero4, (150,110))
    	imgportero5 = pygame.image.load('portero\\portero5.png')
    	imgportero5 = pygame.transform.scale(imgportero5, (150,110))
    	imgportero6 = pygame.image.load('portero\\portero6.png')
    	imgportero6 = pygame.transform.scale(imgportero6, (125,140))
    	imgportero7 = pygame.image.load('portero\\portero7.png')
    	imgportero7 = pygame.transform.scale(imgportero7, (150,110))
    	imgportero8 = pygame.image.load('portero\\portero8.png')
    	imgportero8 = pygame.transform.scale(imgportero8, (150,110))

    	portero1 = pygame.sprite.Sprite()
    	portero1.image = imgportero1
    	portero1.rect = imgportero1.get_rect()
    	porteroPosXInicial = 80
    	porteroPosYInicial = 245
    	portero1.rect.top = porteroPosXInicial
    	portero1.rect.left = porteroPosYInicial

    	portero2 = pygame.sprite.Sprite()
    	portero2.image = imgportero2
    	portero2.rect = imgportero2.get_rect()
    	portero2.rect.top = 80
    	portero2.rect.left = 200

    	portero3 = pygame.sprite.Sprite()
    	portero3.image = imgportero3
    	portero3.rect = imgportero3.get_rect()
    	portero3.rect.top = 0
    	portero3.rect.left = 0

    	portero4 = pygame.sprite.Sprite()
    	portero4.image = imgportero4
    	portero4.rect = imgportero4.get_rect()
    	portero4.rect.top = 80
    	portero4.rect.left = 200

    	portero5 = pygame.sprite.Sprite()
    	portero5.image = imgportero5
    	portero5.rect = imgportero5.get_rect()
    	portero5.rect.top = 80
    	portero5.rect.left = 270

    	portero6 = pygame.sprite.Sprite()
    	portero6.image = imgportero6
    	portero6.rect = imgportero6.get_rect()
    	portero6.rect.top = portero6.rect.top
    	portero6.rect.left = portero6.rect.left

    	portero7 = pygame.sprite.Sprite()
    	portero7.image = imgportero7
    	portero7.rect = imgportero6.get_rect()
    	portero7.rect.top = 130
    	portero7.rect.left = 200

    	portero8 = pygame.sprite.Sprite()
    	portero8.image = imgportero8
    	portero8.rect = imgportero8.get_rect()
    	portero8.rect.top = 80
    	portero8.rect.left = 290

    	xposGuante = 0
    	yposGuante = 0
    	xposGuante2 = 0
    	yposGuante2 = 0
    	guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    	guante2 = pygame.Rect(xposGuante2, yposGuante2, 6, 6)

    #####Cancha######
    	colorPasto = (43, 171, 23)
    	arbustoImg = pygame.image.load('extra\\arbusto.png')
    	arbustoImg = pygame.transform.scale(arbustoImg, [50,50])
    	#pastos XD#

    	pasto = pygame.image.load('extra\\pasto.png')
    	pasto = pygame.transform.scale(pasto, [600,500])
    	pasto2 = pygame.image.load('extra\\pasto2.jpg')

    	#Postes#
    	colorPostes = (255,255,255)
    	iz = pygame.Rect(100, 50, 10, 160)
    	arr = pygame.Rect(100, 50, 380, 10)
    	ab = pygame.Rect(480, 50, 10, 160)
    	#red#
    	imagenRed = pygame.image.load('portero\\redporteria.png')
    	imagenRed = pygame.transform.scale(imagenRed, [395, 245])

    ####Tiros###
    	numTiros = 5
    	fuente = pygame.font.Font('fuentes/letras.otf', 20)

    	textoMarcador = fuente.render("Marcador:", 4, [0,0,0])
    	####Marcador####
    	#Goles#
    	goles = 0
    	#Fallados#
    	fallados = 0
    	#Imagenes#
    	gol = pygame.image.load('marcador\\gol.jpg')
    	fallado = pygame.image.load('marcador\\fallado.jpg')

    	marcador = pygame.Rect(295, 6, 130, 20)
    	tirosMarcador = 0

    ####Aficion####
    	#borde#
    	colorBordeAficion = (255,255,255)
    	if randomA == "1":
    		colorBordeAficion = (12, 58, 205)
    	elif randomA == "2":
    		colorBordeAficion = (215, 140, 0)
    	bordeAficion = pygame.Rect(0,0,600,150)
    	finalBordeAficion = pygame.Rect(0, 120, 600, 40)
    	fila1 = pygame.Rect(0, 30, 600, 5)
    	fila2 = pygame.Rect(0, 60, 600, 5)
    	fila3 = pygame.Rect(0, 90, 600, 5)

    #####Blancos########
    	imgBlanco = pygame.image.load('blanco.png')
    	imgBlanco = pygame.transform.scale(imgBlanco, (30,30))
    	blanco1 = pygame.sprite.Sprite()
    	blanco2 = pygame.sprite.Sprite()
    	blanco3= pygame.sprite.Sprite()
    	blanco4 = pygame.sprite.Sprite()
    	blanco5 = pygame.sprite.Sprite()

    	blanco1.image = imgBlanco
    	blanco1.rect = imgBlanco.get_rect()
    	blanco1.rect.left = 110
    	blanco1.rect.top = 60

    	blanco2.image = imgBlanco
    	blanco2.rect = imgBlanco.get_rect()
    	blanco2.rect.left = 110
    	blanco2.rect.top = 180

    	blanco3.image = imgBlanco
    	blanco3.rect = imgBlanco.get_rect()
    	blanco3.rect.left = 440
    	blanco3.rect.top = 65

    	blanco4.image = imgBlanco
    	blanco4.rect = imgBlanco.get_rect()
    	blanco4.rect.left = 440
    	blanco4.rect.top = 175

    	blanco5.image = imgBlanco
    	blanco5.rect = imgBlanco.get_rect()
    	blanco5.rect.left = 290
    	blanco5.rect.top = 60

    ####Sonidos####

    	sonidoGol = pygame.mixer.Sound("sonidos\\gol.wav")
    	sonidoGol.set_volume(0.3)
    	sonidoTirar = pygame.mixer.Sound("sonidos\\futboltirar.wav")
    	sonidoTirar.set_volume(0.5)

    #####Auxiliares#####
    	ha_tirado = False
    	porteroX = 0
    	porteroY = 0
    	posiciones = ""
    	colorGuante = [0,0,0]
    	listaTiros = ["1", "2", "3", "4", "5"]
    	tiroRandom = random.choice(listaTiros)
    	fallados = 0
    	golFallado = False
    	fallo = False
    	goles = 0
    	golAnotado = False
    	tirosMarcador = 0
    	golFalladoMarcador1 = False
    	golAnotadoMarcador1 = False
    	golFalladoMarcador2 = False
    	golAnotadoMarcador2 = False
    	golFalladoMarcador3 = False
    	golAnotadoMarcador3 = False
    	golFalladoMarcador4 = False
    	golAnotadoMarcador4 = False
    	golFalladoMarcador5 = False
    	golAnotadoMarcador5 = False

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(blanco1.rect):
    					posiciones = "7"
    				elif cursor.colliderect(blanco2.rect):
    					posiciones = "2"
    				elif cursor.colliderect(blanco3.rect):
    					posiciones = "5"
    				elif cursor.colliderect(blanco4.rect):
    					posiciones = "3"
    				elif cursor.colliderect(blanco5.rect):
    					posiciones = "6"
    				if cursor.colliderect(blanco1.rect) or cursor.colliderect(blanco2.rect) or cursor.colliderect(blanco3.rect) or cursor.colliderect(blanco4.rect) or cursor.colliderect(blanco5.rect):
    					ha_tirado = True
    					tirosMarcador += 1
    					sonidoTirar.play()

    		fps.tick(60)
    		pantalla.fill(colorPasto)

    		pygame.draw.rect(pantalla, colorBordeAficion, bordeAficion)
    		pygame.draw.rect(pantalla, [22, 160, 13], finalBordeAficion)
    		#área chica#
    		pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(0, 155, 600, 500))
    		pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(20, 210, 550, 120))
    		pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(30, 200, 530, 120))
    		pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(0, 210, 600, 10))

    		#Pasto img#
    		pastoParaTodos(pantalla, pasto, pasto2)

    		#puntoPenal#
    		pygame.draw.circle(pantalla, (255,255,255), (295, 415), 15)

    		pygame.draw.rect(pantalla, [211, 211, 211], fila1)
    		pygame.draw.rect(pantalla, [211, 211, 211], fila2)
    		pygame.draw.rect(pantalla, [211, 211, 211], fila3)
    		pygame.draw.rect(pantalla, [255,255,255], marcador)

    		#Arbusto#
    		arbustoParaTodos(pantalla, arbustoImg)

    		#pintar red#
    		pantalla.blit(imagenRed, [95, 10])

    		pygame.draw.rect(pantalla, colorPostes, iz)
    		pygame.draw.rect(pantalla, colorPostes, arr)
    		pygame.draw.rect(pantalla, colorPostes, ab)

    		pantalla.blit(blanco1.image, blanco1.rect)
    		pantalla.blit(blanco2.image, blanco2.rect)
    		pantalla.blit(blanco3.image, blanco3.rect)
    		pantalla.blit(blanco4.image, blanco4.rect)
    		pantalla.blit(blanco5.image, blanco5.rect)
    		pantalla.blit(balonContrario.image, balonContrario.rect)

    		if ha_tirado == False:
    			pantalla.blit(portero1.image, portero1.rect)
    			balonContrario.rect.left = balonPosXInicial
    			balonContrario.rect.top = balonPosYInicial
    			velocidadXContrario = 0
    			velocidadYContrario = 0
    			porteroX = 0
    			porteroY = 0
    			tiroRandom = random.choice(listaTiros)
    			portero2.rect.left = 200
    			portero2.rect.top = 80
    			portero3.rect.left = 245
    			portero3.rect.top = 80
    			portero4.rect.left = 200
    			portero4.rect.top = 80
    			portero5.rect.left = 270
    			portero5.rect.top = 80
    			portero6.rect.left = 245
    			portero6.rect.top = 80
    			portero7.rect.left = 200
    			portero7.rect.top = 130
    			portero8.rect.left = 200
    			portero8.rect.top = 130
    			fallo = False
    			golAnotado = False

    		if ha_tirado == True:
    			if numTiros > 0:
    				if posiciones == "2":
    					pantalla.blit(portero2.image, portero2.rect)
    					xposGuante = portero2.rect.left+11
    					yposGuante = portero2.rect.top+100
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -2
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero2.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "3":

    					pantalla.blit(portero3.image, portero3.rect)
    					xposGuante = portero3.rect.left+122
    					yposGuante = portero3.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 3
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero3.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "4":
    					pantalla.blit(portero4.image, portero4.rect)
    					xposGuante = portero4.rect.left+10
    					yposGuante = portero4.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -3
    					porteroY = 0
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero4.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "5":
    					pantalla.blit(portero5.image, portero5.rect)
    					xposGuante = portero5.rect.left+110
    					yposGuante = portero5.rect.top+10
    					xposGuante2 = portero5.rect.left+130
    					yposGuante2 = portero5.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					guante2 = pygame.Rect(xposGuante2, yposGuante2, 8, 8)
    					porteroX = 1
    					porteroY = 2
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					pygame.draw.rect(pantalla, colorGuante, guante2)
    					portero5.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "6":
    					xposGuante = portero5.rect.left+30
    					yposGuante = portero5.rect.top+6
    					guante = pygame.Rect(xposGuante, yposGuante, 12, 6)
    					portero6.rect.left = 245
    					portero6.rect.top = 80
    					pantalla.blit(portero6.image, portero6.rect)
    					pygame.draw.rect(pantalla, (0,0,0), guante)

    				elif posiciones == "7":
    					pantalla.blit(portero7.image, portero7.rect)
    					xposGuante = portero7.rect.left+9
    					yposGuante = portero7.rect.top+5
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -1
    					porteroY = -1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero7.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "8":
    					pantalla.blit(portero8.image, portero8.rect)
    					xposGuante = portero8.rect.left+135
    					yposGuante = portero8.rect.top+8
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 5
    					porteroY = -2
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero8.rect.move_ip(porteroX, porteroY)

    				####Para el contrario#####

    				if tiroRandom == "1":
    					#Arriba izquierda#
    					velocidadXContrario = -4
    					velocidadYContrario = -9
    				elif tiroRandom == "2":
    						#Abajo izquierda#
    					velocidadXContrario = -5
    					velocidadYContrario = -7
    				elif tiroRandom == "3":
    					#Arriba derecha#
    					velocidadXContrario = 5
    					velocidadYContrario = -10
    				elif tiroRandom == "4":
    					#Abajo izquierda#
    					velocidadXContrario = 5
    					velocidadYContrario = -10
    				elif tiroRandom == "5":
    					#centro#
    					velocidadXContrario = 0
    					velocidadYContrario = -10

    				balonContrario.rect.move_ip(velocidadXContrario, velocidadYContrario)

    		if guante.colliderect(balonContrario.rect) or guante2.colliderect(balonContrario.rect):
    			fallados += 1
    			ha_tirado = False
    			golFallado = True
    			fallo = True
    		if balonContrario.rect.colliderect(blanco1.rect) or balonContrario.rect.colliderect(blanco2.rect) or balonContrario.rect.colliderect(blanco3.rect) or balonContrario.rect.colliderect(blanco4.rect) or balonContrario.rect.colliderect(blanco5.rect):
    			if fallo != True:
    				goles += 1
    				golAnotado = True
    			ha_tirado = False

    		if balonContrario.rect.colliderect(guante) or balonContrario.rect.colliderect(blanco1.rect) or balonContrario.rect.colliderect(blanco2.rect) or balonContrario.rect.colliderect(blanco3.rect) or balonContrario.rect.colliderect(blanco4.rect) or balonContrario.rect.colliderect(blanco5.rect):
    			numTiros-=1

    		if numTiros == 0:
    			resultadoSemifinal(misGoles, goles, miEquipo, randomA)

    ##############################################################

    		if tirosMarcador == 1:
    			#RESULTADO1#
    			if golAnotado == True:
    				golAnotadoMarcador1 = True

    			if fallo == True:
    				golFalladoMarcador1 = True

    		if tirosMarcador == 2:
    			#RESULTADO2#
    			if golAnotado == True:
    				golAnotadoMarcador2 = True

    			if fallo == True:
    				golFalladoMarcador2 = True

    		if tirosMarcador == 3:
    			#RESULTADO3#
    			if golAnotado == True:
    				golAnotadoMarcador3 = True

    			if fallo == True:
    				golFalladoMarcador3 = True

    		if tirosMarcador == 4:
    			#RESULTADO4#
    			if golAnotado == True:
    				golAnotadoMarcador4 = True

    			if fallo == True:
    				golFalladoMarcador4 = True

    		if tirosMarcador == 5:
    			#RESULTADO5#
    			if golAnotado == True:
    				golAnotadoMarcador5 = True

    			if fallo == True:
    				golFalladoMarcador5 = True

    ###################################################################

    		if golAnotadoMarcador1 == True:
    			pantalla.blit(gol, [300, 7])

    		elif golFalladoMarcador1 == True:
    			pantalla.blit(fallado, [300, 7])

    		if golAnotadoMarcador2 == True:
    			pantalla.blit(gol, [325, 7])
    		elif golFalladoMarcador2 == True:
    			pantalla.blit(fallado, [325, 7])

    		if golAnotadoMarcador3 == True:
    			pantalla.blit(gol, [350, 7])
    		elif golFalladoMarcador3 == True:
    			pantalla.blit(fallado, [350, 7])

    		if golAnotadoMarcador4 == True:
    			pantalla.blit(gol, [375, 7])
    		elif golFalladoMarcador4 == True:
    			pantalla.blit(fallado, [375, 7])

    		if golAnotadoMarcador5 == True:
    			pantalla.blit(gol, [400, 7])
    		elif golFalladoMarcador5 == True:
    			pantalla.blit(fallado, [400, 7])


    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		tiros = str(numTiros)
    		tirosRestantes = fuente.render("X {}".format(tiros), 4, [255,255,255])
    		pantalla.blit(tirosRestantes, [30, 10])
    		pantalla.blit(balonesRestantes, [0,10])
    		pantalla.blit(textoMarcador, [200, 5])

    		pygame.display.update()

    def cambioDeRolSemifinal(misGoles, miEquipo, randomA):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	fps = pygame.time.Clock()
    	salir = False
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 30)
    	fondoRol = pygame.image.load('menu\\fondoMenu.jpg')
    	cursor = pygame.Rect(50, 50, 1, 1)
    ####Equipos####
    	todoslosequipos()

    ####Auxiliares#####
    	moverMiEquipoY = 0
    	moverMiEquipoX = 0
    	colorMiEquipo = [225, 225, 225]

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				salir = True
    				pygame.quit()
    		fps.tick(60)
    		pantalla.fill([255,255,255])
    		pantalla.blit(fondoRol, [0,0])

    		if miEquipo == "Chivas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if chivas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [232, 22, 22]
    			chivas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(chivas.image, chivas.rect)
    		####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0

    			if cruzazul.rect.x == 400 or tigres.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0

    			if randomA == "1":
    				cruzazul.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(cruzazul.image, cruzazul.rect)
    			if randomA == "2":
    				tigres.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(tigres.image, tigres.rect)

    		elif miEquipo == "America":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if america.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [225, 200, 18]
    			america.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(america.image, america.rect)
    		####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0

    			if pumas.rect.x == 400 or toluca.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0

    			if randomA == "1":
    				pumas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(pumas.image, pumas.rect)
    			if randomA == "2":
    				toluca.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(toluca.image, toluca.rect)

    		elif miEquipo == "Atlas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if atlas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [153, 9, 9]
    			atlas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(atlas.image, atlas.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0

    			if pumas.rect.x == 400 or toluca.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0

    			if randomA == "1":
    				pumas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(pumas.image, pumas.rect)
    			if randomA == "2":
    				toluca.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(toluca.image, toluca.rect)

    		elif miEquipo == "Toluca":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if toluca.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [255, 19, 19]
    			toluca.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(toluca.image, toluca.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0

    			if america.rect.x == 400 or atlas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0

    			if randomA == "1":
    				america.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(america.image, america.rect)
    			if randomA == "2":
    				atlas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(atlas.image, atlas.rect)

    		elif miEquipo == "Tigres":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if tigres.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [241, 161, 10]
    			tigres.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(tigres.image, tigres.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0

    			if chivas.rect.x == 400 or monterrey.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0

    			if randomA == "1":
    				monterrey.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(monterrey.image, monterrey.rect)
    			if randomA == "2":
    				chivas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(chivas.image, chivas.rect)

    		elif miEquipo == "Cruz Azul":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if cruzazul.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 158, 255]
    			cruzazul.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(cruzazul.image, cruzazul.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0

    			if chivas.rect.x == 400 or monterrey.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0

    			if randomA == "1":
    				monterrey.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(monterrey.image, monterrey.rect)
    			if randomA == "2":
    				chivas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(chivas.image, chivas.rect)

    		elif miEquipo == "Pumas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if pumas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [184, 153, 31]
    			pumas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(pumas.image, pumas.rect)
    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0

    			if america.rect.x == 400 or atlas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0

    			if randomA == "1":
    				america.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(america.image, america.rect)
    			if randomA == "2":
    				atlas.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(atlas.image, atlas.rect)

    		elif miEquipo == "Monterrey":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if monterrey.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 49, 153]
    			monterrey.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(monterrey.image, monterrey.rect)
    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0

    			if cruzazul.rect.x == 400 or tigres.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0

    			if randomA == "1":
    				cruzazul.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(cruzazul.image, cruzazul.rect)
    			if randomA == "2":
    				tigres.rect.move_ip(moverContrarioX, moverContrarioY)
    				pantalla.blit(tigres.image, tigres.rect)

    		continuarFuente = pygame.font.Font('menu\\letrasmenu.ttf', 20)
    		botonContinuar = pygame.Rect(250, 450, 130, 30)
    		textoContinuar = continuarFuente.render("Continuar", 4, [255,255,255])
    		fuentevs = pygame.font.Font('menu\\letrasmenu.ttf', 30)
    		vs = fuentevs.render("vs", 4, [0,0,0])
    		textoMisGoles = fuente.render("Goles: {}".format(misGoles), 4, colorMiEquipo)
    		pantalla.blit(textoMisGoles, [20,400])
    		pantalla.blit(vs, [280, 280])
    		pygame.draw.rect(pantalla, [0,0,0], botonContinuar)
    		pantalla.blit(textoContinuar, [260, 455])
    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()

    		if evento.type == pygame.MOUSEBUTTONDOWN:
    			if cursor.colliderect(botonContinuar):
    				penalesContrarioSemifinal(misGoles, miEquipo, randomA)

    		pygame.display.update()

    def semifinal(miEquipo, equipoContrario, randomA):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600, 500])
    	fps = pygame.time.Clock()
    	salir = False
    	cursor = pygame.Rect(50,50,1,1)

    ###Registrar partido###

    	if miEquipo == "Toluca":
    		archivoPJ = open('sts\\toluca\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Pumas":
    		archivoPJ = open('sts\\pumas\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Monterrey":
    		archivoPJ = open('sts\\monterrey\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Tigres":
    		archivoPJ = open('sts\\tigres\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Cruz Azul":
    		archivoPJ = open('sts\\cruzazul\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Atlas":
    		archivoPJ = open('sts\\atlas\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "America":
    		archivoPJ = open('sts\\america\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()
    	if miEquipo == "Chivas":
    		archivoPJ = open('sts\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    ####Sonidos####

    	sonidoGol = pygame.mixer.Sound("sonidos\\gol.wav")
    	sonidoGol.set_volume(0.3)
    	sonidoTirar = pygame.mixer.Sound("sonidos\\futboltirar.wav")
    	sonidoTirar.set_volume(0.5)

    ####Puntero#####

    	puntero = pygame.Rect(50,50,1,1)
    	rolJugador = True

    ####Balón####
    	imgBalon = pygame.image.load('balonC.png')
    	imgBalon = pygame.transform.scale(imgBalon, (30,30))
    	tirosBalon = pygame.transform.scale(imgBalon, (15, 15))
    	balon = pygame.sprite.Sprite()
    	balon.image = imgBalon
    	balon.rect = imgBalon.get_rect()
    	balonPosXInicial = 280
    	balonPosYInicial = 400
    	balon.rect.left = balonPosXInicial
    	balon.rect.top = balonPosYInicial

    ####portero1######
    	#Inicial#
    	imgportero1 = pygame.image.load('portero\\portero1.png')
    	imgportero1 = pygame.transform.scale(imgportero1, (125,140))
    	imgportero2 = pygame.image.load('portero\\portero2.png')
    	imgportero2 = pygame.transform.scale(imgportero2, (150,110))
    	imgportero3 = pygame.image.load('portero\\portero3.png')
    	imgportero3 = pygame.transform.scale(imgportero3, (140,100))
    	imgportero4 = pygame.image.load('portero\\portero4.png')
    	imgportero4 = pygame.transform.scale(imgportero4, (150,110))
    	imgportero5 = pygame.image.load('portero\\portero5.png')
    	imgportero5 = pygame.transform.scale(imgportero5, (150,110))
    	imgportero6 = pygame.image.load('portero\\portero6.png')
    	imgportero6 = pygame.transform.scale(imgportero6, (125,140))
    	imgportero7 = pygame.image.load('portero\\portero7.png')
    	imgportero7 = pygame.transform.scale(imgportero7, (150,110))
    	imgportero8 = pygame.image.load('portero\\portero8.png')
    	imgportero8 = pygame.transform.scale(imgportero8, (150,110))


    	portero1 = pygame.sprite.Sprite()
    	portero1.image = imgportero1
    	portero1.rect = imgportero1.get_rect()
    	porteroPosXInicial = 80
    	porteroPosYInicial = 245
    	portero1.rect.top = porteroPosXInicial
    	portero1.rect.left = porteroPosYInicial

    	portero2 = pygame.sprite.Sprite()
    	portero2.image = imgportero2
    	portero2.rect = imgportero2.get_rect()
    	portero2.rect.top = 80
    	portero2.rect.left = 200

    	portero3 = pygame.sprite.Sprite()
    	portero3.image = imgportero3
    	portero3.rect = imgportero3.get_rect()
    	portero3.rect.top = 0
    	portero3.rect.left = 0

    	portero4 = pygame.sprite.Sprite()
    	portero4.image = imgportero4
    	portero4.rect = imgportero4.get_rect()
    	portero4.rect.top = 80
    	portero4.rect.left = 200

    	portero5 = pygame.sprite.Sprite()
    	portero5.image = imgportero5
    	portero5.rect = imgportero5.get_rect()
    	portero5.rect.top = 80
    	portero5.rect.left = 270

    	portero6 = pygame.sprite.Sprite()
    	portero6.image = imgportero6
    	portero6.rect = imgportero6.get_rect()
    	portero6.rect.top = portero6.rect.top
    	portero6.rect.left = portero6.rect.left

    	portero7 = pygame.sprite.Sprite()
    	portero7.image = imgportero7
    	portero7.rect = imgportero6.get_rect()
    	portero7.rect.top = 130
    	portero7.rect.left = 200

    	portero8 = pygame.sprite.Sprite()
    	portero8.image = imgportero8
    	portero8.rect = imgportero8.get_rect()
    	portero8.rect.top = 80
    	portero8.rect.left = 290

    	"""NO PONGAS EL 1 PORQUE NO HAY"""
    	posicionesLista = ["2","3","4","5","6","7","8"]
    	if rolJugador == True:
    		posiciones = random.choice(posicionesLista)
    ####Variables de la cancha#####
    	colorPasto = (43, 171, 23)
    	arbustoImg = pygame.image.load('extra\\arbusto.png')
    	arbustoImg = pygame.transform.scale(arbustoImg, [50,50])
    	#pastos XD#

    	pasto = pygame.image.load('extra\\pasto.png')
    	pasto = pygame.transform.scale(pasto, [600,500])
    	pasto2 = pygame.image.load('extra\\pasto2.jpg')

    ####Variables portería#######
    	#Postes#
    	colorPostes = (255,255,255)
    	iz = pygame.Rect(100, 50, 10, 160)
    	arr = pygame.Rect(100, 50, 380, 10)
    	ab = pygame.Rect(480, 50, 10, 160)
    	#red#
    	imagenRed = pygame.image.load('portero\\redporteria.png')
    	imagenRed = pygame.transform.scale(imagenRed, [395, 245])

    ####Aficion####
    	#borde#
    	colorBordeAficion = (255,255,255)
    	if randomA == "1":
    		colorBordeAficion = (12, 58, 205)
    	elif randomA == "2":
    		colorBordeAficion = (215, 140, 0)
    	bordeAficion = pygame.Rect(0,0,600,150)
    	finalBordeAficion = pygame.Rect(0, 120, 600, 40)
    	fila1 = pygame.Rect(0, 30, 600, 5)
    	fila2 = pygame.Rect(0, 60, 600, 5)
    	fila3 = pygame.Rect(0, 90, 600, 5)

    ####Tiros###
    	numTiros = 5

    	fuente = pygame.font.Font('fuentes/letras.otf', 20)

    	imgBlanco = pygame.image.load('blanco.png')
    	imgBlanco = pygame.transform.scale(imgBlanco, (30,30))
    	blanco1 = pygame.sprite.Sprite()
    	blanco2 = pygame.sprite.Sprite()
    	blanco3= pygame.sprite.Sprite()
    	blanco4 = pygame.sprite.Sprite()
    	blanco5 = pygame.sprite.Sprite()

    	blanco1.image = imgBlanco
    	blanco1.rect = imgBlanco.get_rect()
    	blanco1.rect.left = 110
    	blanco1.rect.top = 60

    	blanco2.image = imgBlanco
    	blanco2.rect = imgBlanco.get_rect()
    	blanco2.rect.left = 110
    	blanco2.rect.top = 180

    	blanco3.image = imgBlanco
    	blanco3.rect = imgBlanco.get_rect()
    	blanco3.rect.left = 440
    	blanco3.rect.top = 65

    	blanco4.image = imgBlanco
    	blanco4.rect = imgBlanco.get_rect()
    	blanco4.rect.left = 440
    	blanco4.rect.top = 175

    	blanco5.image = imgBlanco
    	blanco5.rect = imgBlanco.get_rect()
    	blanco5.rect.left = 290
    	blanco5.rect.top = 60

    ####Marcador####
    	#Goles#
    	goles = 0
    	#Fallados#
    	fallados = 0
    	#Imagenes#
    	gol = pygame.image.load('marcador\\gol.jpg')
    	fallado = pygame.image.load('marcador\\fallado.jpg')
    	marcador = pygame.Rect(295, 6, 130, 20)
    	tirosMarcador = 0

    ####Cambiar rol######
    	#cambiarRol = fuente.render("Ahora tú eres el portero, adivina los tiros.", 4, [21, 246, 246])

    ####Variables auxiliares#######
    	ha_tirado = False
    	velocidadX = 0
    	velocidadY = 0
    	segundosInt = 0
    	porteroY = 0
    	porteroX = 0
    	xposGuante = 0
    	yposGuante = 0
    	xposGuante2 = 0
    	yposGuante2 = 0
    	colorGuante = (245, 184, 222)
    	guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    	guante2 = pygame.Rect(xposGuante2, yposGuante2, 6, 6)
    	fallo = False
    	golAnotado = False
    	golFallado = False
    	golFalladoMarcador1 = False
    	golAnotadoMarcador1 = False
    	golFalladoMarcador2 = False
    	golAnotadoMarcador2 = False
    	golFalladoMarcador3 = False
    	golAnotadoMarcador3 = False
    	golFalladoMarcador4 = False
    	golAnotadoMarcador4 = False
    	golFalladoMarcador5 = False
    	golAnotadoMarcador5 = False

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()

    			if numTiros > 0:
    				rolJugador = True
    				if evento.type == pygame.MOUSEBUTTONDOWN:
    					if puntero.colliderect(blanco1.rect):
    						#Arriba izquierda#
    						velocidadX = -4
    						velocidadY = -8

    					elif puntero.colliderect(blanco2.rect):
    						#Abajo izquierda#
    						velocidadX = -5
    						velocidadY = -6

    					elif puntero.colliderect(blanco3.rect):
    						#Arriba derecha#
    						velocidadX = 5
    						velocidadY = -10
    					elif puntero.colliderect(blanco4.rect):
    						#Abajo derecha#
    						velocidadX = 4
    						velocidadY = -6
    					elif puntero.colliderect(blanco5.rect):
    						#centro#

    						velocidadX = 0
    						velocidadY = -8

    					if puntero.colliderect(blanco1.rect) or puntero.colliderect(blanco2.rect) or puntero.colliderect(blanco3.rect) or puntero.colliderect(blanco4.rect) or puntero.colliderect(blanco5.rect):
    						ha_tirado = True
    						tirosMarcador += 1
    						sonidoTirar.play()

    			if numTiros == 0:
    				cambioDeRolSemifinal(goles, miEquipo, randomA)

    		fps.tick(60)
    		pantalla.fill(colorPasto)
    		tiros = str(numTiros)

    		mostrarTiros = fuente.render("X {}".format(tiros), 2, [255,255,255])


    		pygame.draw.rect(pantalla, colorBordeAficion, bordeAficion)
    		pygame.draw.rect(pantalla, (11, 156, 13), finalBordeAficion)

    		#área chica#
    		pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(0, 155, 600, 500))
    		pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(20, 210, 550, 120))
    		pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(30, 200, 530, 120))
    		pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(0, 210, 600, 10))

    		pygame.draw.rect(pantalla, (215,215,215), fila1)
    		pygame.draw.rect(pantalla, (215,215,215), fila2)
    		pygame.draw.rect(pantalla, (215,215,215), fila3)

    		#Pasto img#
    		pastoParaTodos(pantalla, pasto, pasto2)

    		#Arbusto#
    		arbustoParaTodos(pantalla, arbustoImg)

    		pantalla.blit(imagenRed, [95, 10])
    		pygame.draw.rect(pantalla, colorPostes, iz)
    		pygame.draw.rect(pantalla, colorPostes, arr)
    		pygame.draw.rect(pantalla, colorPostes, ab)
    		#puntoPenal#
    		pygame.draw.circle(pantalla, (255,255,255), (295, 415), 15)

    		pantalla.blit(blanco1.image, blanco1.rect)
    		pantalla.blit(blanco2.image, blanco2.rect)
    		pantalla.blit(blanco3.image, blanco3.rect)
    		pantalla.blit(blanco4.image, blanco4.rect)
    		pantalla.blit(blanco5.image, blanco5.rect)

    		if ha_tirado == False:
    			pantalla.blit(portero1.image, portero1.rect)
    			balon.rect.left = balonPosXInicial
    			balon.rect.top = balonPosYInicial
    			velocidadX = 0
    			velocidadY = 0
    			posiciones = random.choice(posicionesLista)
    			portero2.rect.left = 200
    			portero2.rect.top = 80
    			portero3.rect.left = 245
    			portero3.rect.top = 80
    			portero4.rect.left = 200
    			portero4.rect.top = 80
    			portero5.rect.left = 270
    			portero5.rect.top = 80
    			portero6.rect.left = 245
    			portero6.rect.top = 80
    			portero7.rect.left = 200
    			portero7.rect.top = 130
    			portero8.rect.left = 200
    			portero8.rect.top = 130
    			fallo = False
    			golAnotado = False


    		if ha_tirado == True:
    			if numTiros > 0:
    				if posiciones == "2":
    					pantalla.blit(portero2.image, portero2.rect)
    					xposGuante = portero2.rect.left+11
    					yposGuante = portero2.rect.top+100
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -3
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero2.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "3":

    					pantalla.blit(portero3.image, portero3.rect)
    					xposGuante = portero3.rect.left+122
    					yposGuante = portero3.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 2
    					porteroY = 2
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero3.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "4":
    					pantalla.blit(portero4.image, portero4.rect)
    					xposGuante = portero4.rect.left+10
    					yposGuante = portero4.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -1
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero4.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "5":
    					pantalla.blit(portero5.image, portero5.rect)
    					xposGuante = portero5.rect.left+110
    					yposGuante = portero5.rect.top+10
    					xposGuante2 = portero5.rect.left+130
    					yposGuante2 = portero5.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					guante2 = pygame.Rect(xposGuante2, yposGuante2, 8, 8)
    					porteroX = 2
    					porteroY = 0
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					pygame.draw.rect(pantalla, colorGuante, guante2)
    					portero5.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "6":
    					xposGuante = portero5.rect.left+30
    					yposGuante = portero5.rect.top+6
    					guante = pygame.Rect(xposGuante, yposGuante, 12, 6)
    					portero6.rect.left = 245
    					portero6.rect.top = 80
    					pantalla.blit(portero6.image, portero6.rect)
    					pygame.draw.rect(pantalla, (0,0,0), guante)

    				elif posiciones == "7":
    					pantalla.blit(portero7.image, portero7.rect)
    					xposGuante = portero7.rect.left+9
    					yposGuante = portero7.rect.top+5
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -2
    					porteroY = -1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero7.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "8":
    					pantalla.blit(portero8.image, portero8.rect)
    					xposGuante = portero8.rect.left+135
    					yposGuante = portero8.rect.top+8
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 4
    					porteroY = -1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero8.rect.move_ip(porteroX, porteroY)

    		if guante.colliderect(balon.rect) or guante2.colliderect(balon.rect):
    			fallados += 1
    			ha_tirado = False
    			golFallado = True
    			fallo = True
    		if balon.rect.colliderect(blanco1.rect) or balon.rect.colliderect(blanco2.rect) or balon.rect.colliderect(blanco3.rect) or balon.rect.colliderect(blanco4.rect) or balon.rect.colliderect(blanco5.rect):
    			if fallo != True:
    				goles += 1
    				golAnotado = True
    			ha_tirado = False

    		if balon.rect.colliderect(guante) or balon.rect.colliderect(blanco1.rect) or balon.rect.colliderect(blanco2.rect) or balon.rect.colliderect(blanco3.rect) or balon.rect.colliderect(blanco4.rect) or balon.rect.colliderect(blanco5.rect):
    			numTiros-=1

    		balon.rect.move_ip(velocidadX, velocidadY)
    		pantalla.blit(balon.image, balon.rect)

    		pantalla.blit(mostrarTiros, [50, 10])
    		pantalla.blit(tirosBalon, [20,10])

    		pygame.draw.rect(pantalla, (0,0,0), puntero)
    		(puntero.x, puntero.y) = pygame.mouse.get_pos()

    		pygame.draw.rect(pantalla, (255,255,255), marcador)
    		mensajeMarcador = fuente.render("Marcador: ", 2, (0,0,0))
    		pantalla.blit(mensajeMarcador, [205, 7])

    ##############################################################

    		if tirosMarcador == 1:
    			#RESULTADO1#
    			if golAnotado == True:
    				golAnotadoMarcador1 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador1 = True

    		if tirosMarcador == 2:
    			#RESULTADO2#
    			if golAnotado == True:
    				golAnotadoMarcador2 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador2 = True

    		if tirosMarcador == 3:
    			#RESULTADO3#
    			if golAnotado == True:
    				golAnotadoMarcador3 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador3 = True

    		if tirosMarcador == 4:
    			#RESULTADO4#
    			if golAnotado == True:
    				golAnotadoMarcador4 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador4 = True

    		if tirosMarcador == 5:
    			#RESULTADO5#
    			if golAnotado == True:
    				golAnotadoMarcador5 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador5 = True

    ###################################################################

    		if golAnotadoMarcador1 == True:
    			pantalla.blit(gol, [300, 7])

    		elif golFalladoMarcador1 == True:
    			pantalla.blit(fallado, [300, 7])

    		if golAnotadoMarcador2 == True:
    			pantalla.blit(gol, [325, 7])
    		elif golFalladoMarcador2 == True:
    			pantalla.blit(fallado, [325, 7])

    		if golAnotadoMarcador3 == True:
    			pantalla.blit(gol, [350, 7])
    		elif golFalladoMarcador3 == True:
    			pantalla.blit(fallado, [350, 7])

    		if golAnotadoMarcador4 == True:
    			pantalla.blit(gol, [375, 7])
    		elif golFalladoMarcador4 == True:
    			pantalla.blit(fallado, [375, 7])

    		if golAnotadoMarcador5 == True:
    			pantalla.blit(gol, [400, 7])
    		elif golFalladoMarcador5 == True:
    			pantalla.blit(fallado, [400, 7])

    		pygame.display.update()

    def siguienteRonda(miEquipo):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	fps = pygame.time.Clock()
    	salir = False
    	cursor = pygame.Rect(50,50,1,1)
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 15)
    ####Torneo equipos######
    	chivasImg = pygame.image.load('menu\\equipos\\chivas.png')
    	americaImg = pygame.image.load('menu\\equipos\\america.png')
    	atlasImg = pygame.image.load('menu\\equipos\\atlas.png')
    	tolucaImg = pygame.image.load('menu\\equipos\\toluca.png')
    	tigresImg = pygame.image.load('menu\\equipos\\tigres.png')
    	cruzazulImg = pygame.image.load('menu\\equipos\\cruzazul.png')
    	monterreyImg = pygame.image.load('menu\\equipos\\monterrey.png')
    	pumasImg = pygame.image.load('menu\\equipos\\pumas.png')


    	chivasImg = pygame.transform.scale(chivasImg, [30,30])
    	americaImg = pygame.transform.scale(americaImg, [30,30])
    	atlasImg = pygame.transform.scale(atlasImg, [30,30])
    	tolucaImg = pygame.transform.scale(tolucaImg, [30,30])
    	tigresImg = pygame.transform.scale(tigresImg, [30,30])
    	cruzazulImg = pygame.transform.scale(cruzazulImg, [30,30])
    	pumasImg = pygame.transform.scale(pumasImg, [30,30])
    	monterreyImg = pygame.transform.scale(monterreyImg, [30,30])

    	atlas = pygame.sprite.Sprite()
    	atlas.image = atlasImg
    	atlas.rect = atlasImg.get_rect()
    	atlas.rect.left = 30
    	atlas.rect.top = 20

    	america = pygame.sprite.Sprite()
    	america.image = americaImg
    	america.rect = americaImg.get_rect()
    	america.rect.left = 30
    	america.rect.top = 70

    	toluca = pygame.sprite.Sprite()
    	toluca.image = tolucaImg
    	toluca.rect = tolucaImg.get_rect()
    	toluca.rect.left = 30
    	toluca.rect.top = 140

    	pumas = pygame.sprite.Sprite()
    	pumas.image = pumasImg
    	pumas.rect = pumasImg.get_rect()
    	pumas.rect.left = 30
    	pumas.rect.top = 190

    	chivas = pygame.sprite.Sprite()
    	chivas.image = chivasImg
    	chivas.rect = chivasImg.get_rect()
    	chivas.rect.left = 30
    	chivas.rect.top = 255

    	monterrey = pygame.sprite.Sprite()
    	monterrey.image = monterreyImg
    	monterrey.rect = monterreyImg.get_rect()
    	monterrey.rect.left = 30
    	monterrey.rect.top = 300

    	tigres = pygame.sprite.Sprite()
    	tigres.image = tigresImg
    	tigres.rect = tigresImg.get_rect()
    	tigres.rect.left = 30
    	tigres.rect.top = 355

    	cruzazul = pygame.sprite.Sprite()
    	cruzazul.image = cruzazulImg
    	cruzazul.rect = cruzazulImg.get_rect()
    	cruzazul.rect.left = 30
    	cruzazul.rect.top = 405

    ####Texto#######
    	equipoEnPantalla = fuente.render("Tu equipo:", 4, [0,0,0])
    	contrarioEnPantalla = fuente.render("Contrario:", 4, [0,0,0])
    ####Torneo posiciones#####
    	torneo = pygame.image.load('posiciones\\posiciones.jpg')
    	#Equipo que pasa a la siguiente#
    	elegirProx = ["1", "2"]
    		#GrupoA#
    	randomA = random.choice(elegirProx)

    ####Botón continuar####
    	continuar = pygame.Rect(400, 460, 100, 30)
    	colorContinuar = [0,0,0]
    	fuenteContinuar = pygame.font.Font('menu\\letrasmenu.ttf', 15)
    	textoContinuar = fuenteContinuar.render("Continuar", 4, [255,255,255])

    ####Auxiliares####
    	velX = 0
    	velY = 0
    	equipoContrario = ""

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()

    		fps.tick(60)
    		pantalla.fill([255,255,255])
    		pantalla.blit(torneo, [70,30])
    		pantalla.fill([255,255,255])

    		pantalla.blit(torneo, [70,30])
    		#Grupo1#
    		pantalla.blit(atlas.image, atlas.rect)
    		pantalla.blit(america.image, america.rect)
    		#Grupo2#
    		pantalla.blit(toluca.image, toluca.rect)
    		pantalla.blit(pumas.image, pumas.rect)
    		#Grupo3#
    		pantalla.blit(chivas.image, chivas.rect)
    		pantalla.blit(monterrey.image, monterrey.rect)
    		#Grupo4#
    		pantalla.blit(tigres.image, tigres.rect)
    		pantalla.blit(cruzazul.image, cruzazul.rect)
    		#Mi equipo#
    		pantalla.blit(equipoEnPantalla, [0, 475])
    		pantalla.blit(contrarioEnPantalla, [150, 475])

    		pygame.draw.rect(pantalla, colorContinuar, continuar)
    		pantalla.blit(textoContinuar, [406, 465])

    		if miEquipo == "Chivas":
    			pantalla.blit(chivasImg, [90, 470])
    			#Contrario en primer juego#
    			#EL 1 SON LOS QUE SE ACOMODAN  PARA ARRIBA WN
    			if randomA == "1":
    				pantalla.blit(cruzazulImg, [240, 470])
    				equipoContrario = "Cruz Azul"
    			elif randomA == "2":
    				pantalla.blit(tigresImg, [240, 470])
    				equipoContrario = "Tigres"

    		elif miEquipo == "America":
    			pantalla.blit(americaImg, [90, 470])
    			#Contrario en primer juego#
    			if randomA == "1":
    				pantalla.blit(pumasImg, [240, 470])
    				equipoContrario = "Pumas"
    			elif randomA == "2":
    				pantalla.blit(tolucaImg, [240, 470])
    				equipoContrario = "Toluca"

    		elif miEquipo == "Atlas":
    			pantalla.blit(atlasImg, [90, 470])
    			#Contrario en primer juego#
    			if randomA == "1":
    				pantalla.blit(pumasImg, [240, 470])
    				equipoContrario = "Pumas"
    			elif randomA == "2":
    				pantalla.blit(tolucaImg, [240, 470])
    				equipoContrario = "Toluca"

    		elif miEquipo == "Toluca":
    			pantalla.blit(tolucaImg, [90, 470])
    			#Contrario en primer juego#
    			if randomA == "1":
    				pantalla.blit(americaImg, [240, 470])
    				equipoContrario = "America"
    			elif randomA == "2":
    				pantalla.blit(atlasImg, [240, 470])
    				equipoContrario = "Atlas"

    		elif miEquipo == "Tigres":
    			pantalla.blit(tigresImg, [90, 470])
    			#Contrario en primer juego#
    			if randomA == "1":
    				pantalla.blit(monterreyImg, [240, 470])
    				equipoContrario = "Monterrey"
    			elif randomA == "2":
    				pantalla.blit(chivasImg, [240, 470])
    				equipoContrario = "Chivas"

    		elif miEquipo == "Cruz Azul":
    			pantalla.blit(cruzazulImg, [90, 470])
    			#Contrario en primer juego#
    			if randomA == "1":
    				pantalla.blit(monterreyImg, [240, 470])
    				equipoContrario = "Monterrey"
    			elif randomA == "2":
    				pantalla.blit(chivasImg, [240, 470])
    				equipoContrario = "Chivas"

    		elif miEquipo == "Pumas":
    			pantalla.blit(pumasImg, [90, 470])
    			#Contrario en primer juego#
    			if randomA == "1":
    				pantalla.blit(americaImg, [240, 470])
    				equipoContrario = "America"
    			elif randomA == "2":
    				pantalla.blit(atlasImg, [240, 470])
    				equipoContrario = "Atlas"

    		elif miEquipo == "Monterrey":
    			pantalla.blit(monterreyImg, [90, 470])
    			#Contrario en primer juego#
    			if randomA == "1":
    				pantalla.blit(cruzazulImg, [240, 470])
    				equipoContrario = "Cruz Azul"
    			elif randomA == "2":
    				pantalla.blit(tigresImg, [240, 470])
    				equipoContrario = "Tigres"

    ####Si tu equipo está en el grupo A#
    		if miEquipo == "Atlas":
    			velX = 1
    			velY = 0
    			if atlas.rect.left == 180:
    				velX = 0
    				velY = 1
    				if atlas.rect.top == 40:
    					velX = 0
    					velY = 0
    			atlas.rect.move_ip(velX, velY)
    			america.rect.move_ip(0,0)

    			if randomA == "1":
    				velXContrario = 1
    				velYContrario = 0
    				if pumas.rect.left == 180 or monterrey.rect.left == 180 or cruzazul.rect.left == 180:
    					velXContrario = 0
    					velYContrario = -1
    					if pumas.rect.top == 160:
    						velXContrario = 0
    						velYContrario = 0
    				pumas.rect.move_ip(velXContrario, velYContrario)
    				monterrey.rect.move_ip(velXContrario, velYContrario)
    				cruzazul.rect.move_ip(velXContrario, velYContrario)

    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				velXContrario = 1
    				velYContrario = 0
    				if toluca.rect.left == 180 or chivas.rect.left == 180 or tigres.rect.left == 180:
    					velXContrario = 0
    					velYContrario = 1
    					if chivas.rect.top == 265 or toluca.rect.top == 265 or tigres.rect.top == 265:
    						velXContrario = 0
    						velYContrario = 0
    				chivas.rect.move_ip(velXContrario, velYContrario)
    				toluca.rect.move_ip(velXContrario, velYContrario)
    				tigres.rect.move_ip(velXContrario, velYContrario)

    		elif miEquipo == "America":
    			velX = 1
    			velY = 0
    			if america.rect.left == 180:
    				velX = 0
    				velY = -1
    				if america.rect.top == 45:
    					velX = 0
    					velY = 0
    			america.rect.move_ip(velX, velY)
    			atlas.rect.move_ip(0,0)

    			if randomA == "1":
    				velXContrario = 1
    				velYContrario = 0
    				if pumas.rect.left == 180 or monterrey.rect.left == 180 or cruzazul.rect.left == 180:
    					velXContrario = 0
    					velYContrario = -1
    					if pumas.rect.top == 160:
    						velXContrario = 0
    						velYContrario = 0
    				pumas.rect.move_ip(velXContrario, velYContrario)
    				monterrey.rect.move_ip(velXContrario, velYContrario)
    				cruzazul.rect.move_ip(velXContrario, velYContrario)

    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				velXContrario = 1
    				velYContrario = 0
    				if toluca.rect.left == 180 or chivas.rect.left == 180 or tigres.rect.left == 180:
    					velXContrario = 0
    					velYContrario = 1
    					if chivas.rect.top == 265 or toluca.rect.top == 265 or tigres.rect.top == 265:
    						velXContrario = 0
    						velYContrario = 0
    				chivas.rect.move_ip(velXContrario, velYContrario)
    				toluca.rect.move_ip(velXContrario, velYContrario)
    				tigres.rect.move_ip(velXContrario, velYContrario)

    		elif miEquipo == "Toluca":
    			velX = 1
    			velY = 0
    			if toluca.rect.left == 180:
    				velX = 0
    				velY = 1
    				if toluca.rect.top == 150:
    					velX = 0
    					velY = 0
    			toluca.rect.move_ip(velX, velY)
    			pumas.rect.move_ip(0,0)
    			if randomA == "1":
    				velXContrario = 1
    				velYContrario = 0
    				if america.rect.left == 180 or monterrey.rect.left == 180 or cruzazul.rect.left == 180:
    					velXContrario = 0
    					velYContrario = -1
    					if america.rect.top == 35:
    						velXContrario = 0
    						velYContrario = 0
    				america.rect.move_ip(velXContrario, velYContrario)
    				monterrey.rect.move_ip(velXContrario, velYContrario)
    				cruzazul.rect.move_ip(velXContrario, velYContrario)

    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				velXContrario = 1
    				velYContrario = 0
    				if atlas.rect.left == 180 or chivas.rect.left == 180 or tigres.rect.left == 180:
    					velXContrario = 0
    					velYContrario = 1
    					if chivas.rect.top == 265 or atlas.rect.top == 265 or tigres.rect.top == 265:
    						velXContrario = 0
    						velYContrario = 0
    				atlas.rect.move_ip(velXContrario, velYContrario)
    				chivas.rect.move_ip(velXContrario, velYContrario)
    				tigres.rect.move_ip(velXContrario, velYContrario)

    		elif miEquipo == "Pumas":
    			velX = 1
    			velY = 0
    			if pumas.rect.left == 180:
    				velX = 0
    				velY = -1
    				if pumas.rect.top == 150:
    					velX = 0
    					velY = 0
    			pumas.rect.move_ip(velX, velY)
    			toluca.rect.move_ip(0,0)
    			if randomA == "1":
    				velXContrario = 1
    				velYContrario = 0
    				if america.rect.left == 180 or monterrey.rect.left == 180 or cruzazul.rect.left == 180:
    					velXContrario = 0
    					velYContrario = -1
    					if america.rect.top == 35:
    						velXContrario = 0
    						velYContrario = 0
    				america.rect.move_ip(velXContrario, velYContrario)
    				monterrey.rect.move_ip(velXContrario, velYContrario)
    				cruzazul.rect.move_ip(velXContrario, velYContrario)

    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				velXContrario = 1
    				velYContrario = 0
    				if atlas.rect.left == 180 or chivas.rect.left == 180 or tigres.rect.left == 180:
    					velXContrario = 0
    					velYContrario = 1
    					if chivas.rect.top == 265 or atlas.rect.top == 265 or tigres.rect.top == 265:
    						velXContrario = 0
    						velYContrario = 0
    				atlas.rect.move_ip(velXContrario, velYContrario)
    				chivas.rect.move_ip(velXContrario, velYContrario)
    				tigres.rect.move_ip(velXContrario, velYContrario)

    		elif miEquipo == "Chivas":
    			velX = 1
    			velY = 0
    			if chivas.rect.left == 180:
    				velX = 0
    				velY = 1
    				if chivas.rect.top == 265:
    					velX = 0
    					velY = 0
    			chivas.rect.move_ip(velX, velY)
    			monterrey.rect.move_ip(0,0)
    			###Un grupo de 4 equipos###
    			if randomA == "1":
    				velXContrario = 1
    				velYContrario = 0
    				if america.rect.left == 180 or pumas.rect.left == 180 or cruzazul.rect.left == 180:
    					velXContrario = 0
    					velYContrario = -1
    					if america.rect.top == 45 or pumas.rect.top == 45 or cruzazul.rect.top == 45:
    						velXContrario = 0
    						velYContrario = 0
    				america.rect.move_ip(velXContrario, velYContrario)
    				pumas.rect.move_ip(velXContrario, velYContrario)
    				cruzazul.rect.move_ip(velXContrario, velYContrario)

    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				velXContrario = 1
    				velYContrario = 0
    				if atlas.rect.left == 180 or toluca.rect.left == 180 or tigres.rect.left == 180:
    					velXContrario = 0
    					velYContrario = 1
    					if atlas.rect.top == 40 or toluca.rect.top == 40 or tigres.rect.top == 40:
    						velXContrario = 0
    						velYContrario = 0
    				atlas.rect.move_ip(velXContrario, velYContrario)
    				toluca.rect.move_ip(velXContrario, velYContrario)
    				tigres.rect.move_ip(velXContrario, velYContrario)

    		elif miEquipo == "Monterrey":
    			velX = 1
    			velY = 0
    			if monterrey.rect.left == 180:
    				velX = 0
    				velY = -1
    				if monterrey.rect.top == 265:
    					velX = 0
    					velY = 0
    			monterrey.rect.move_ip(velX, velY)
    			chivas.rect.move_ip(0,0)
    			if randomA == "1":
    				velXContrario = 1
    				velYContrario = 0
    				if america.rect.left == 180 or pumas.rect.left == 180 or cruzazul.rect.left == 180:
    					velXContrario = 0
    					velYContrario = -1
    					if america.rect.top == 35:
    						velXContrario = 0
    						velYContrario = 0
    				america.rect.move_ip(velXContrario, velYContrario)
    				pumas.rect.move_ip(velXContrario, velYContrario)
    				cruzazul.rect.move_ip(velXContrario, velYContrario)

    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				velXContrario = 1
    				velYContrario = 0
    				if atlas.rect.left == 180 or toluca.rect.left == 180 or tigres.rect.left == 180:
    					velXContrario = 0
    					velYContrario = 1
    					if toluca.rect.top == 150 or atlas.rect.top == 265 or tigres.rect.top == 265:
    						velXContrario = 0
    						velYContrario = 0
    				atlas.rect.move_ip(velXContrario, velYContrario)
    				toluca.rect.move_ip(velXContrario, velYContrario)
    				tigres.rect.move_ip(velXContrario, velYContrario)

    		elif miEquipo == "Tigres":
    			velX = 1
    			velY = 0
    			if tigres.rect.left == 180:
    				velX = 0
    				velY = 1
    				if tigres.rect.top == 365:
    					velX = 0
    					velY = 0
    			tigres.rect.move_ip(velX, velY)
    			cruzazul.rect.move_ip(0,0)
    			if randomA == "1":
    				velXContrario = 1
    				velYContrario = 0
    				if america.rect.left == 180 or pumas.rect.left == 180 or monterrey.rect.left == 180:
    					velXContrario = 0
    					velYContrario = -1
    					if america.rect.top == 35:
    						velXContrario = 0
    						velYContrario = 0
    				america.rect.move_ip(velXContrario, velYContrario)
    				pumas.rect.move_ip(velXContrario, velYContrario)
    				monterrey.rect.move_ip(velXContrario, velYContrario)

    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				velXContrario = 1
    				velYContrario = 0
    				if atlas.rect.left == 180 or toluca.rect.left == 180 or chivas.rect.left == 180:
    					velXContrario = 0
    					velYContrario = 1
    					if toluca.rect.top == 150 or atlas.rect.top == 265 or chivas.rect.top == 265:
    						velXContrario = 0
    						velYContrario = 0
    				atlas.rect.move_ip(velXContrario, velYContrario)
    				toluca.rect.move_ip(velXContrario, velYContrario)
    				chivas.rect.move_ip(velXContrario, velYContrario)

    		elif miEquipo == "Cruz Azul":
    			velX = 1
    			velY = 0
    			if cruzazul.rect.left == 180:
    				velX = 0
    				velY = -1
    				if cruzazul.rect.top == 365:
    					velX = 0
    					velY = 0
    			cruzazul.rect.move_ip(velX, velY)
    			tigres.rect.move_ip(0,0)
    			if randomA == "1":
    				velXContrario = 1
    				velYContrario = 0
    				if america.rect.left == 180 or pumas.rect.left == 180 or monterrey.rect.left == 180:
    					velXContrario = 0
    					velYContrario = -1
    					if america.rect.top == 35:
    						velXContrario = 0
    						velYContrario = 0
    				america.rect.move_ip(velXContrario, velYContrario)
    				pumas.rect.move_ip(velXContrario, velYContrario)
    				monterrey.rect.move_ip(velXContrario, velYContrario)

    			elif randomA == "2":
    				###Otro grupo de 4 equipos###
    				velXContrario = 1
    				velYContrario = 0
    				if atlas.rect.left == 180 or toluca.rect.left == 180 or chivas.rect.left == 180:
    					velXContrario = 0
    					velYContrario = 1
    					if toluca.rect.top == 150 or atlas.rect.top == 265 or chivas.rect.top == 265:
    						velXContrario = 0
    						velYContrario = 0
    				atlas.rect.move_ip(velXContrario, velYContrario)
    				toluca.rect.move_ip(velXContrario, velYContrario)
    				chivas.rect.move_ip(velXContrario, velYContrario)

    	#######Si mi equipo está en el grupo B#####
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuar):
    					semifinal(miEquipo, equipoContrario, randomA)

    		pygame.display.update()

    def resultadoCuartos(misGoles, goles, miEquipo):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600, 500])
    	fps = pygame.time.Clock()
    	salir = False
    	cursor = pygame.Rect(50, 50, 1, 1)
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 20)

    #####Fondo#####
    	fondo = pygame.image.load('menu\\fondoMenu.jpg')

    ####Equipos####
    	todoslosequipos()

    	####Auxiliares#####
    	moverMiEquipoY = 0
    	moverMiEquipoX = 0
    	colorMiEquipo = [225, 225, 225]

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()

    		fps.tick(60)
    		pantalla.fill([255,255,255])
    		pantalla.blit(fondo, [0,0])
    		if miEquipo == "Chivas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if chivas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [232, 22, 22]
    			chivas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(chivas.image, chivas.rect)
    		####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if monterrey.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			monterrey.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(monterrey.image, monterrey.rect)

    		elif miEquipo == "America":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if america.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [225, 200, 18]
    			america.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(america.image, america.rect)
    		####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if atlas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			atlas.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(atlas.image, atlas.rect)

    		elif miEquipo == "Atlas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if atlas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [153, 9, 9]
    			atlas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(atlas.image, atlas.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if america.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			america.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(america.image, america.rect)

    		elif miEquipo == "Toluca":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if toluca.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [255, 19, 19]
    			toluca.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(toluca.image, toluca.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if pumas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			pumas.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(pumas.image, pumas.rect)
    		elif miEquipo == "Tigres":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if tigres.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [241, 161, 10]
    			tigres.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(tigres.image, tigres.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if cruzazul.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			cruzazul.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(cruzazul.image, cruzazul.rect)

    		elif miEquipo == "Cruz Azul":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if cruzazul.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 158, 255]
    			cruzazul.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(cruzazul.image, cruzazul.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if tigres.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			tigres.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(tigres.image, tigres.rect)

    		elif miEquipo == "Pumas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if pumas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [184, 153, 31]
    			pumas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(pumas.image, pumas.rect)

    			moverContrarioX = 4
    			moverContrarioY = 0
    			if toluca.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			toluca.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(toluca.image, toluca.rect)

    		elif miEquipo == "Monterrey":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if monterrey.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 49, 153]
    			monterrey.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(monterrey.image, monterrey.rect)

    			moverContrarioX = 4
    			moverContrarioY = 0
    			if chivas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			chivas.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(chivas.image, chivas.rect)

    		textoMisGoles = fuente.render("Goles {}".format(misGoles), 4, colorMiEquipo)
    		textoGolesContrario = fuente.render("Goles {}".format(goles), 4, [0,0,0])
    		textovs = fuente.render("vs", 4, [0,0,0])
    		pantalla.blit(textoMisGoles, [50, 400])
    		pantalla.blit(textoGolesContrario, [450, 400])
    		pantalla.blit(textovs, [300, 250])
    ####Si quedan en empate######
    		if goles == misGoles:
    			textoEmpate = fuente.render("EMPATE. Continuan los penales.",4, [6, 139, 199])
    			pantalla.blit(textoEmpate, [100, 10])
    			continuarEmpate = pygame.Rect(250,450, 120, 30)
    			pygame.draw.rect(pantalla, [26, 139, 199], continuarEmpate)
    			textoContinuar = fuente.render("Continuar", 4, [0,0,0])
    			pantalla.blit(textoContinuar, [255, 453])
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuarEmpate):
    						#Registrar partido empatado#
    					if miEquipo == "Toluca":
    						archivoE = open('sts\\toluca\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Pumas":
    						archivoE = open('sts\\pumas\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Monterrey":
    						archivoE = open('sts\\monterrey\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Tigres":
    						archivoE = open('sts\\tigres\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Cruz Azul":
    						archivoE = open('sts\\cruzazul\\e.csv', 'a')
    						archivoE.write("1")
    						archivoE.close()

    					if miEquipo == "Atlas":
    						archivoG = open("sts\\atlas\\e.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "America":
    						archivoG = open("sts\\america\\e.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Chivas":
    						archivoG = open("sts\\e.csv", "a")
    						archivoG.write("1")
    						archivoG.close()
    					principal(pantalla, miEquipo)
    ######Si ganaste######
    		if misGoles > goles:
    			textoGanaste = fuente.render("GANASTE. Pasas a la siguiente ronda.",4, [26, 199, 29])
    			pantalla.blit(textoGanaste, [100, 10])
    			continuarGanaste = pygame.Rect(250,450, 120, 30)
    			pygame.draw.rect(pantalla, [26, 199, 29], continuarGanaste)
    			textoContinuar = fuente.render("Continuar", 4, [0,0,0])
    			pantalla.blit(textoContinuar, [255, 453])
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuarGanaste):
    				#Registrar partido ganado#
    					if miEquipo == "Toluca":
    						archivoG = open('sts\\toluca\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Pumas":
    						archivoG = open('sts\\pumas\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Monterrey":
    						archivoG = open('sts\\monterrey\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Tigres":
    						archivoG = open('sts\\tigres\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Cruz Azul":
    						archivoG = open('sts\\cruzazul\\g.csv', 'a')
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Atlas":
    						archivoG = open("sts\\atlas\\g.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "America":
    						archivoG = open("sts\\america\\g.csv", "a")
    						archivoG.write("1")
    						archivoG.close()

    					if miEquipo == "Chivas":
    						archivoG = open("sts\\g.csv", "a")
    						archivoG.write("1")
    						archivoG.close()
    					siguienteRonda(miEquipo)
    ######Si perdiste#######
    		if goles > misGoles:
    			textoPerdiste = fuente.render("PERDISTE. Quedas fuera del torneo.", 4, [199, 26, 26])
    			pantalla.blit(textoPerdiste, [100, 10])
    			continuarPerdiste = pygame.Rect(250,450, 120, 30)
    			pygame.draw.rect(pantalla, [199, 26, 26], continuarPerdiste)
    			textoContinuar = fuente.render("Continuar", 4, [0,0,0])
    			pantalla.blit(textoContinuar, [255, 453])

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(continuarPerdiste):
    					#Registrar partido perdido#
    					if miEquipo == "Toluca":
    						archivoP = open('sts\\toluca\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Pumas":
    						archivoP = open('sts\\pumas\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Monterrey":
    						archivoP = open('sts\\monterrey\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Tigres":
    						archivoP = open('sts\\tigres\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Cruz Azul":
    						archivoP = open('sts\\cruzazul\\p.csv', 'a')
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Atlas":
    						archivoP = open("sts\\atlas\\p.csv", "a")
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "America":
    						archivoP = open("sts\\america\\p.csv", "a")
    						archivoP.write("1")
    						archivoP.close()

    					if miEquipo == "Chivas":
    						archivoP = open("sts\\p.csv", "a")
    						archivoP.write("1")
    						archivoP.close()
    					menu()
    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		pygame.display.update()


    def penalesContrario(misGoles, miEquipo):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	fps = pygame.time.Clock()
    	salir = False
    	cursor = pygame.Rect(50, 50, 1, 1)
    ####Balón######

    	balonPosXInicial = 280
    	balonPosYInicial = 400

    	imgBalonContrario = pygame.image.load('balonC.png')
    	imgBalonContrario = pygame.transform.scale(imgBalonContrario, (30,30))
    	balonContrario = pygame.sprite.Sprite()
    	balonContrario.image = imgBalonContrario
    	balonContrario.rect = imgBalonContrario.get_rect()
    	balonContrario.rect.left = balonPosXInicial
    	balonContrario.rect.top = balonPosYInicial

    	balonesRestantes = pygame.transform.scale(imgBalonContrario, (20, 20))

    	####portero1######
    	#Inicial#
    	imgportero1 = pygame.image.load('portero\\portero1.png')
    	imgportero1 = pygame.transform.scale(imgportero1, (125,140))
    	imgportero2 = pygame.image.load('portero\\portero2.png')
    	imgportero2 = pygame.transform.scale(imgportero2, (150,110))
    	imgportero3 = pygame.image.load('portero\\portero3.png')
    	imgportero3 = pygame.transform.scale(imgportero3, (140,100))
    	imgportero4 = pygame.image.load('portero\\portero4.png')
    	imgportero4 = pygame.transform.scale(imgportero4, (150,110))
    	imgportero5 = pygame.image.load('portero\\portero5.png')
    	imgportero5 = pygame.transform.scale(imgportero5, (150,110))
    	imgportero6 = pygame.image.load('portero\\portero6.png')
    	imgportero6 = pygame.transform.scale(imgportero6, (125,140))
    	imgportero7 = pygame.image.load('portero\\portero7.png')
    	imgportero7 = pygame.transform.scale(imgportero7, (150,110))
    	imgportero8 = pygame.image.load('portero\\portero8.png')
    	imgportero8 = pygame.transform.scale(imgportero8, (150,110))

    	portero1 = pygame.sprite.Sprite()
    	portero1.image = imgportero1
    	portero1.rect = imgportero1.get_rect()
    	porteroPosXInicial = 80
    	porteroPosYInicial = 245
    	portero1.rect.top = porteroPosXInicial
    	portero1.rect.left = porteroPosYInicial

    	portero2 = pygame.sprite.Sprite()
    	portero2.image = imgportero2
    	portero2.rect = imgportero2.get_rect()
    	portero2.rect.top = 80
    	portero2.rect.left = 200

    	portero3 = pygame.sprite.Sprite()
    	portero3.image = imgportero3
    	portero3.rect = imgportero3.get_rect()
    	portero3.rect.top = 0
    	portero3.rect.left = 0

    	portero4 = pygame.sprite.Sprite()
    	portero4.image = imgportero4
    	portero4.rect = imgportero4.get_rect()
    	portero4.rect.top = 80
    	portero4.rect.left = 200

    	portero5 = pygame.sprite.Sprite()
    	portero5.image = imgportero5
    	portero5.rect = imgportero5.get_rect()
    	portero5.rect.top = 80
    	portero5.rect.left = 270

    	portero6 = pygame.sprite.Sprite()
    	portero6.image = imgportero6
    	portero6.rect = imgportero6.get_rect()
    	portero6.rect.top = portero6.rect.top
    	portero6.rect.left = portero6.rect.left

    	portero7 = pygame.sprite.Sprite()
    	portero7.image = imgportero7
    	portero7.rect = imgportero6.get_rect()
    	portero7.rect.top = 130
    	portero7.rect.left = 200

    	portero8 = pygame.sprite.Sprite()
    	portero8.image = imgportero8
    	portero8.rect = imgportero8.get_rect()
    	portero8.rect.top = 80
    	portero8.rect.left = 290

    	xposGuante = 0
    	yposGuante = 0
    	xposGuante2 = 0
    	yposGuante2 = 0
    	guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    	guante2 = pygame.Rect(xposGuante2, yposGuante2, 6, 6)

    #####Cancha######
    	colorPasto = (43, 171, 23)
    	arbustoImg = pygame.image.load('extra\\arbusto.png')
    	arbustoImg = pygame.transform.scale(arbustoImg, [50,50])
    	#pastos XD#

    	pasto = pygame.image.load('extra\\pasto.png')
    	pasto = pygame.transform.scale(pasto, [600,500])
    	pasto2 = pygame.image.load('extra\\pasto2.jpg')

    	#Postes#
    	colorPostes = (255,255,255)
    	iz = pygame.Rect(100, 50, 10, 160)
    	arr = pygame.Rect(100, 50, 380, 10)
    	ab = pygame.Rect(480, 50, 10, 160)
    	#red#
    	imagenRed = pygame.image.load('portero\\redporteria.png')
    	imagenRed = pygame.transform.scale(imagenRed, [395, 245])

    ####Tiros###
    	numTiros = 5
    	fuente = pygame.font.Font('fuentes/letras.otf', 20)

    	textoMarcador = fuente.render("Marcador:", 4, [0,0,0])
    	####Marcador####
    	#Goles#
    	goles = 0
    	#Fallados#
    	fallados = 0
    	#Imagenes#
    	gol = pygame.image.load('marcador\\gol.jpg')
    	fallado = pygame.image.load('marcador\\fallado.jpg')

    	marcador = pygame.Rect(295, 6, 130, 20)
    	tirosMarcador = 0

    ####Aficion####
    	#borde#
    	colorBordeAficion = (242, 12, 50)
    	bordeAficion = pygame.Rect(0,0,600,150)
    	finalBordeAficion = pygame.Rect(0, 120, 600, 40)
    	fila1 = pygame.Rect(0, 30, 600, 5)
    	fila2 = pygame.Rect(0, 60, 600, 5)
    	fila3 = pygame.Rect(0, 90, 600, 5)

    #####Blancos########
    	imgBlanco = pygame.image.load('blanco.png')
    	imgBlanco = pygame.transform.scale(imgBlanco, (30,30))
    	blanco1 = pygame.sprite.Sprite()
    	blanco2 = pygame.sprite.Sprite()
    	blanco3= pygame.sprite.Sprite()
    	blanco4 = pygame.sprite.Sprite()
    	blanco5 = pygame.sprite.Sprite()

    	blanco1.image = imgBlanco
    	blanco1.rect = imgBlanco.get_rect()
    	blanco1.rect.left = 110
    	blanco1.rect.top = 60

    	blanco2.image = imgBlanco
    	blanco2.rect = imgBlanco.get_rect()
    	blanco2.rect.left = 110
    	blanco2.rect.top = 180

    	blanco3.image = imgBlanco
    	blanco3.rect = imgBlanco.get_rect()
    	blanco3.rect.left = 440
    	blanco3.rect.top = 65

    	blanco4.image = imgBlanco
    	blanco4.rect = imgBlanco.get_rect()
    	blanco4.rect.left = 440
    	blanco4.rect.top = 175

    	blanco5.image = imgBlanco
    	blanco5.rect = imgBlanco.get_rect()
    	blanco5.rect.left = 290
    	blanco5.rect.top = 60

    ####Sonidos####

    	sonidoGol = pygame.mixer.Sound("sonidos\\gol.wav")
    	sonidoGol.set_volume(0.3)
    	sonidoTirar = pygame.mixer.Sound("sonidos\\futboltirar.wav")
    	sonidoTirar.set_volume(0.5)

    #####Auxiliares#####
    	ha_tirado = False
    	porteroX = 0
    	porteroY = 0
    	posiciones = ""
    	colorGuante = [0,0,0]
    	listaTiros = ["1", "2", "3", "4", "5"]
    	tiroRandom = random.choice(listaTiros)
    	fallados = 0
    	golFallado = False
    	fallo = False
    	goles = 0
    	golAnotado = False
    	tirosMarcador = 0
    	golFalladoMarcador1 = False
    	golAnotadoMarcador1 = False
    	golFalladoMarcador2 = False
    	golAnotadoMarcador2 = False
    	golFalladoMarcador3 = False
    	golAnotadoMarcador3 = False
    	golFalladoMarcador4 = False
    	golAnotadoMarcador4 = False
    	golFalladoMarcador5 = False
    	golAnotadoMarcador5 = False

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(blanco1.rect):
    					posiciones = "7"
    				elif cursor.colliderect(blanco2.rect):
    					posiciones = "2"
    				elif cursor.colliderect(blanco3.rect):
    					posiciones = "5"
    				elif cursor.colliderect(blanco4.rect):
    					posiciones = "3"
    				elif cursor.colliderect(blanco5.rect):
    					posiciones = "6"
    				if cursor.colliderect(blanco1.rect) or cursor.colliderect(blanco2.rect) or cursor.colliderect(blanco3.rect) or cursor.colliderect(blanco4.rect) or cursor.colliderect(blanco5.rect):
    					ha_tirado = True
    					tirosMarcador += 1
    					sonidoTirar.play()

    		fps.tick(60)
    		pantalla.fill(colorPasto)

    		pygame.draw.rect(pantalla, colorBordeAficion, bordeAficion)
    		pygame.draw.rect(pantalla, [22, 160, 13], finalBordeAficion)
    		#área chica#
    		pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(0, 155, 600, 500))
    		pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(20, 210, 550, 120))
    		pygame.draw.rect(pantalla, (8, 109, 9), pygame.Rect(30, 200, 530, 120))
    		pygame.draw.rect(pantalla, (232, 232, 232), pygame.Rect(0, 210, 600, 10))

    		#Pasto img#
    		pastoParaTodos(pantalla, pasto, pasto2)

    		#puntoPenal#
    		pygame.draw.circle(pantalla, (255,255,255), (295, 415), 15)

    		pygame.draw.rect(pantalla, [211, 211, 211], fila1)
    		pygame.draw.rect(pantalla, [211, 211, 211], fila2)
    		pygame.draw.rect(pantalla, [211, 211, 211], fila3)
    		pygame.draw.rect(pantalla, [255,255,255], marcador)

    		#Arbusto#
    		arbustoParaTodos(pantalla, arbustoImg)

    		#pintar red#
    		pantalla.blit(imagenRed, [95, 10])

    		pygame.draw.rect(pantalla, colorPostes, iz)
    		pygame.draw.rect(pantalla, colorPostes, arr)
    		pygame.draw.rect(pantalla, colorPostes, ab)

    		pantalla.blit(blanco1.image, blanco1.rect)
    		pantalla.blit(blanco2.image, blanco2.rect)
    		pantalla.blit(blanco3.image, blanco3.rect)
    		pantalla.blit(blanco4.image, blanco4.rect)
    		pantalla.blit(blanco5.image, blanco5.rect)
    		pantalla.blit(balonContrario.image, balonContrario.rect)

    		if ha_tirado == False:
    			pantalla.blit(portero1.image, portero1.rect)
    			balonContrario.rect.left = balonPosXInicial
    			balonContrario.rect.top = balonPosYInicial
    			velocidadXContrario = 0
    			velocidadYContrario = 0
    			porteroX = 0
    			porteroY = 0
    			tiroRandom = random.choice(listaTiros)
    			portero2.rect.left = 200
    			portero2.rect.top = 80
    			portero3.rect.left = 245
    			portero3.rect.top = 80
    			portero4.rect.left = 200
    			portero4.rect.top = 80
    			portero5.rect.left = 270
    			portero5.rect.top = 80
    			portero6.rect.left = 245
    			portero6.rect.top = 80
    			portero7.rect.left = 200
    			portero7.rect.top = 130
    			portero8.rect.left = 200
    			portero8.rect.top = 130
    			fallo = False
    			golAnotado = False

    		if ha_tirado == True:
    			if numTiros > 0:
    				if posiciones == "2":
    					pantalla.blit(portero2.image, portero2.rect)
    					xposGuante = portero2.rect.left+11
    					yposGuante = portero2.rect.top+100
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -2
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero2.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "3":

    					pantalla.blit(portero3.image, portero3.rect)
    					xposGuante = portero3.rect.left+122
    					yposGuante = portero3.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 3
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero3.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "4":
    					pantalla.blit(portero4.image, portero4.rect)
    					xposGuante = portero4.rect.left+10
    					yposGuante = portero4.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -3
    					porteroY = 0
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero4.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "5":
    					pantalla.blit(portero5.image, portero5.rect)
    					xposGuante = portero5.rect.left+110
    					yposGuante = portero5.rect.top+10
    					xposGuante2 = portero5.rect.left+130
    					yposGuante2 = portero5.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					guante2 = pygame.Rect(xposGuante2, yposGuante2, 8, 8)
    					porteroX = 1
    					porteroY = 2
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					pygame.draw.rect(pantalla, colorGuante, guante2)
    					portero5.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "6":
    					xposGuante = portero5.rect.left+30
    					yposGuante = portero5.rect.top+6
    					guante = pygame.Rect(xposGuante, yposGuante, 12, 6)
    					portero6.rect.left = 245
    					portero6.rect.top = 80
    					pantalla.blit(portero6.image, portero6.rect)
    					pygame.draw.rect(pantalla, (0,0,0), guante)

    				elif posiciones == "7":
    					pantalla.blit(portero7.image, portero7.rect)
    					xposGuante = portero7.rect.left+9
    					yposGuante = portero7.rect.top+5
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -1
    					porteroY = -1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero7.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "8":
    					pantalla.blit(portero8.image, portero8.rect)
    					xposGuante = portero8.rect.left+135
    					yposGuante = portero8.rect.top+8
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 5
    					porteroY = -2
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero8.rect.move_ip(porteroX, porteroY)

    				####Para el contrario#####

    				if tiroRandom == "1":
    					#Arriba izquierda#
    					velocidadXContrario = -4
    					velocidadYContrario = -9
    				elif tiroRandom == "2":
    						#Abajo izquierda#
    					velocidadXContrario = -5
    					velocidadYContrario = -7
    				elif tiroRandom == "3":
    					#Arriba derecha#
    					velocidadXContrario = 5
    					velocidadYContrario = -10
    				elif tiroRandom == "4":
    					#Abajo izquierda#
    					velocidadXContrario = 5
    					velocidadYContrario = -10
    				elif tiroRandom == "5":
    					#centro#
    					velocidadXContrario = 0
    					velocidadYContrario = -10

    				balonContrario.rect.move_ip(velocidadXContrario, velocidadYContrario)

    		if guante.colliderect(balonContrario.rect) or guante2.colliderect(balonContrario.rect):
    			fallados += 1
    			ha_tirado = False
    			golFallado = True
    			fallo = True
    		if balonContrario.rect.colliderect(blanco1.rect) or balonContrario.rect.colliderect(blanco2.rect) or balonContrario.rect.colliderect(blanco3.rect) or balonContrario.rect.colliderect(blanco4.rect) or balonContrario.rect.colliderect(blanco5.rect):
    			if fallo != True:
    				goles += 1
    				golAnotado = True
    			ha_tirado = False

    		if balonContrario.rect.colliderect(guante) or balonContrario.rect.colliderect(blanco1.rect) or balonContrario.rect.colliderect(blanco2.rect) or balonContrario.rect.colliderect(blanco3.rect) or balonContrario.rect.colliderect(blanco4.rect) or balonContrario.rect.colliderect(blanco5.rect):
    			numTiros-=1

    		if numTiros == 0:
    			resultadoCuartos(misGoles, goles, miEquipo)

    ##############################################################

    		if tirosMarcador == 1:
    			#RESULTADO1#
    			if golAnotado == True:
    				golAnotadoMarcador1 = True
    				#Goles en contra#
    				if miEquipo == "Toluca":
    					archivoGC = open('sts\\toluca\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Pumas":
    					archivoGC = open('sts\\pumas\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Monterrey":
    					archivoGC = open('sts\\monterrey\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Tigres":
    					archivoGC = open('sts\\tigres\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Cruz Azul":
    					archivoGC = open('sts\\cruzazul\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'Atlas':
    					archivoGC = open('sts\\atlas\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'America':
    					archivoGC = open('sts\\america\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'Chivas':
    					archivoGC = open('sts\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    			if fallo == True:
    				golFalladoMarcador1 = True

    		if tirosMarcador == 2:
    			#RESULTADO2#
    			if golAnotado == True:
    				golAnotadoMarcador2 = True
    				#Goles en contra#
    				if miEquipo == "Toluca":
    					archivoGC = open('sts\\toluca\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Pumas":
    					archivoGC = open('sts\\pumas\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Monterrey":
    					archivoGC = open('sts\\monterrey\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Tigres":
    					archivoGC = open('sts\\tigres\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Cruz Azul":
    					archivoGC = open('sts\\cruzazul\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'Atlas':
    					archivoGC = open('sts\\atlas\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'America':
    					archivoGC = open('sts\\america\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'Chivas':
    					archivoGC = open('sts\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    			if fallo == True:
    				golFalladoMarcador2 = True

    		if tirosMarcador == 3:
    			#RESULTADO3#
    			if golAnotado == True:
    				golAnotadoMarcador3 = True
    				#Goles en contra#
    				if miEquipo == "Toluca":
    					archivoGC = open('sts\\toluca\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Pumas":
    					archivoGC = open('sts\\pumas\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Monterrey":
    					archivoGC = open('sts\\monterrey\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Tigres":
    					archivoGC = open('sts\\tigres\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Cruz Azul":
    					archivoGC = open('sts\\cruzazul\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'Atlas':
    					archivoGC = open('sts\\atlas\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'America':
    					archivoGC = open('sts\\america\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'Chivas':
    					archivoGC = open('sts\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()


    			if fallo == True:
    				golFalladoMarcador3 = True

    		if tirosMarcador == 4:
    			#RESULTADO4#
    			if golAnotado == True:
    				golAnotadoMarcador4 = True
    				#Goles en contra#
    				if miEquipo == "Toluca":
    					archivoGC = open('sts\\toluca\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Pumas":
    					archivoGC = open('sts\\pumas\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Monterrey":
    					archivoGC = open('sts\\monterrey\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Tigres":
    					archivoGC = open('sts\\tigres\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Cruz Azul":
    					archivoGC = open('sts\\cruzazul\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'Atlas':
    					archivoGC = open('sts\\atlas\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'America':
    					archivoGC = open('sts\\america\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'Chivas':
    					archivoGC = open('sts\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()


    			if fallo == True:
    				golFalladoMarcador4 = True

    		if tirosMarcador == 5:
    			#RESULTADO5#
    			if golAnotado == True:
    				golAnotadoMarcador5 = True
    				#Goles en contra#
    				if miEquipo == "Toluca":
    					archivoGC = open('sts\\toluca\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Pumas":
    					archivoGC = open('sts\\pumas\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Monterrey":
    					archivoGC = open('sts\\monterrey\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Tigres":
    					archivoGC = open('sts\\tigres\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == "Cruz Azul":
    					archivoGC = open('sts\\cruzazul\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'Atlas':
    					archivoGC = open('sts\\atlas\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'America':
    					archivoGC = open('sts\\america\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    				if miEquipo == 'Chivas':
    					archivoGC = open('sts\\gc.csv', 'a')
    					archivoGC.write("1")
    					archivoGC.close()

    			if fallo == True:
    				golFalladoMarcador5 = True

    ###################################################################

    		if golAnotadoMarcador1 == True:
    			pantalla.blit(gol, [300, 7])

    		elif golFalladoMarcador1 == True:
    			pantalla.blit(fallado, [300, 7])

    		if golAnotadoMarcador2 == True:
    			pantalla.blit(gol, [325, 7])
    		elif golFalladoMarcador2 == True:
    			pantalla.blit(fallado, [325, 7])

    		if golAnotadoMarcador3 == True:
    			pantalla.blit(gol, [350, 7])
    		elif golFalladoMarcador3 == True:
    			pantalla.blit(fallado, [350, 7])

    		if golAnotadoMarcador4 == True:
    			pantalla.blit(gol, [375, 7])
    		elif golFalladoMarcador4 == True:
    			pantalla.blit(fallado, [375, 7])

    		if golAnotadoMarcador5 == True:
    			pantalla.blit(gol, [400, 7])
    		elif golFalladoMarcador5 == True:
    			pantalla.blit(fallado, [400, 7])


    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		tiros = str(numTiros)
    		tirosRestantes = fuente.render("X {}".format(tiros), 4, [255,255,255])
    		pantalla.blit(tirosRestantes, [30, 10])
    		pantalla.blit(balonesRestantes, [0,10])
    		pantalla.blit(textoMarcador, [200, 5])

    		pygame.display.update()

    def cambioDeRol(misGoles, miEquipo):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	fps = pygame.time.Clock()
    	salir = False
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 30)
    	fondoRol = pygame.image.load('menu\\fondoMenu.jpg')
    	cursor = pygame.Rect(50, 50, 1, 1)
    ####Equipos####
    	todoslosequipos()

    ####Auxiliares#####
    	moverMiEquipoY = 0
    	moverMiEquipoX = 0
    	colorMiEquipo = [225, 225, 225]

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				salir = True
    				pygame.quit()
    		fps.tick(60)
    		pantalla.fill([255,255,255])
    		pantalla.blit(fondoRol, [0,0])

    		if miEquipo == "Chivas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if chivas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [232, 22, 22]
    			chivas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(chivas.image, chivas.rect)
    		####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if monterrey.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			monterrey.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(monterrey.image, monterrey.rect)

    		elif miEquipo == "America":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if america.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [225, 200, 18]
    			america.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(america.image, america.rect)
    		####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if atlas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			atlas.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(atlas.image, atlas.rect)

    		elif miEquipo == "Atlas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if atlas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [153, 9, 9]
    			atlas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(atlas.image, atlas.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if america.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			america.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(america.image, america.rect)

    		elif miEquipo == "Toluca":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if toluca.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [255, 19, 19]
    			toluca.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(toluca.image, toluca.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if pumas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			pumas.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(pumas.image, pumas.rect)
    		elif miEquipo == "Tigres":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if tigres.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [241, 161, 10]
    			tigres.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(tigres.image, tigres.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if cruzazul.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			cruzazul.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(cruzazul.image, cruzazul.rect)

    		elif miEquipo == "Cruz Azul":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if cruzazul.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 158, 255]
    			cruzazul.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(cruzazul.image, cruzazul.rect)

    			####Equipo contrario#####
    			moverContrarioX = 4
    			moverContrarioY = 0
    			if tigres.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			tigres.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(tigres.image, tigres.rect)

    		elif miEquipo == "Pumas":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if pumas.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [184, 153, 31]
    			pumas.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(pumas.image, pumas.rect)

    			moverContrarioX = 4
    			moverContrarioY = 0
    			if toluca.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			toluca.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(toluca.image, toluca.rect)

    		elif miEquipo == "Monterrey":
    			moverMiEquipoX = -4
    			moverMiEquipoY = 0
    			if monterrey.rect.x == 0:
    				moverMiEquipoY = 0
    				moverMiEquipoX = 0
    				colorMiEquipo = [0, 49, 153]
    			monterrey.rect.move_ip(moverMiEquipoX,moverMiEquipoY)
    			pantalla.blit(monterrey.image, monterrey.rect)

    			moverContrarioX = 4
    			moverContrarioY = 0
    			if chivas.rect.x == 400:
    				moverContrarioY = 0
    				moverContrarioX = 0
    			chivas.rect.move_ip(moverContrarioX, moverContrarioY)
    			pantalla.blit(chivas.image, chivas.rect)

    		continuarFuente = pygame.font.Font('menu\\letrasmenu.ttf', 20)
    		botonContinuar = pygame.Rect(250, 450, 130, 30)
    		textoContinuar = continuarFuente.render("Continuar", 4, [255,255,255])
    		fuentevs = pygame.font.Font('menu\\letrasmenu.ttf', 30)
    		vs = fuentevs.render("vs", 4, [0,0,0])
    		textoMisGoles = fuente.render("Goles: {}".format(misGoles), 4, colorMiEquipo)
    		pantalla.blit(textoMisGoles, [20,400])
    		pantalla.blit(vs, [280, 280])
    		pygame.draw.rect(pantalla, [0,0,0], botonContinuar)
    		pantalla.blit(textoContinuar, [260, 455])
    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()

    		if evento.type == pygame.MOUSEBUTTONDOWN:
    			if cursor.colliderect(botonContinuar):
    				penalesContrario(misGoles, miEquipo)

    		pygame.display.update()


    def partidos(pantalla, chivasImg, americaImg, atlasImg, tolucaImg, tigresImg, cruzazulImg, monterreyImg, pumasImg, miEquipo):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	partidosSalir = False
    	torneo = pygame.image.load('posiciones\\posiciones.jpg')

    	chivasImg = pygame.transform.scale(chivasImg, [30,30])
    	americaImg = pygame.transform.scale(americaImg, [30,30])
    	atlasImg = pygame.transform.scale(atlasImg, [30,30])
    	tolucaImg = pygame.transform.scale(tolucaImg, [30,30])
    	tigresImg = pygame.transform.scale(tigresImg, [30,30])
    	cruzazulImg = pygame.transform.scale(cruzazulImg, [30,30])
    	pumasImg = pygame.transform.scale(pumasImg, [30,30])
    	monterreyImg = pygame.transform.scale(monterreyImg, [30,30])
    	equiposTorneo = [chivasImg, americaImg, atlasImg, tolucaImg, tigresImg, cruzazulImg, monterreyImg, pumasImg]

    	botonContinuar = pygame.Rect(400, 450, 110, 30)
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 15)
    	textoContinuar = fuente.render("Continuar", 4, [255,255,255])
    	cursor = pygame.Rect(50,50,1,1)
    	equipoEnPantalla = fuente.render("Tu equipo:", 4, [0,0,0])
    	contrarioEnPantalla = fuente.render("Contrario:", 4, [0,0,0])

    	while partidosSalir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				partidosSalir = True
    				pygame.quit()
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(botonContinuar):
    					principal(pantalla, miEquipo)

    		pantalla.fill([255,255,255])
    		pantalla.blit(torneo, [70,30])
    		#Grupo1#
    		pantalla.blit(atlasImg, [30, 20])
    		pantalla.blit(americaImg, [30, 70])
    		#Grupo2#
    		pantalla.blit(tolucaImg, [30, 140])
    		pantalla.blit(pumasImg, [30, 190])
    		#Grupo3#
    		pantalla.blit(chivasImg, [30, 255])
    		pantalla.blit(monterreyImg, [30, 300])
    		#Grupo4#
    		pantalla.blit(tigresImg, [30, 355])
    		pantalla.blit(cruzazulImg, [30, 405])
    		#Mi equipo#
    		pantalla.blit(equipoEnPantalla, [0, 475])
    		pantalla.blit(contrarioEnPantalla, [150, 475])

    		if miEquipo == "Chivas":
    			pantalla.blit(chivasImg, [90, 470])
    			#Contrario en primer juego#
    			pantalla.blit(monterreyImg, [240, 470])

    		elif miEquipo == "America":
    			pantalla.blit(americaImg, [90, 470])
    			#Contrario en primer juego#
    			pantalla.blit(atlasImg, [240, 470])

    		elif miEquipo == "Atlas":
    			pantalla.blit(atlasImg, [90, 470])
    			#Contrario en primer juego#
    			pantalla.blit(americaImg, [240, 470])

    		elif miEquipo == "Toluca":
    			pantalla.blit(tolucaImg, [90, 470])
    			#Contrario en primer juego#
    			pantalla.blit(pumasImg, [240, 470])

    		elif miEquipo == "Tigres":
    			pantalla.blit(tigresImg, [90, 470])
    			#Contrario en primer juego#
    			pantalla.blit(cruzazulImg, [240, 470])

    		elif miEquipo == "Cruz Azul":
    			pantalla.blit(cruzazulImg, [90, 470])
    			#Contrario en primer juego#
    			pantalla.blit(tigresImg, [240, 470])

    		elif miEquipo == "Pumas":
    			pantalla.blit(pumasImg, [90, 470])
    			#Contrario en primer juego#
    			pantalla.blit(tolucaImg, [240, 470])

    		elif miEquipo == "Monterrey":
    			pantalla.blit(monterreyImg, [90, 470])
    			#Contrario en primer juego#
    			pantalla.blit(chivasImg, [240, 470])


    		pygame.draw.rect(pantalla, [0, 59, 216], botonContinuar)
    		pantalla.blit(textoContinuar, [413, 455])
    		pygame.draw.rect(pantalla, [0,0,0], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()

    		pygame.display.update()

    def elegirEquipo(pantalla):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	elegirSalir = False
    	elegirFps = pygame.time.Clock()
    	fondo = pygame.image.load('menu\\fondoMenu.jpg')
    	fondo = pygame.transform.scale(fondo, [600, 500])
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 20)
    	textoElegirTeam = fuente.render("Elige a tu equipo", 4, [255,255,255])
    	flechaSiguiente = fuente.render("->", 4, [255,255,255])
    	flechaAnterior = fuente.render("<-", 4, [255,255,255])
    	textoElegir = fuente.render("Elegir", 4, [255,255,255])
    	cursor = pygame.Rect(50, 50, 1, 1)

    #####Equipos#####
    	chivasImg = pygame.image.load('menu\\equipos\\chivas.png')
    	chivasImg = pygame.transform.scale(chivasImg, [210,210])
    	chivas = pygame.sprite.Sprite()
    	chivas.image = chivasImg
    	chivas.rect = chivasImg.get_rect()
    	chivas.rect.left = 220
    	chivas.rect.top = 150
    	colorElegirChivas = (225, 3, 3)


    	americaImg = pygame.image.load('menu\\equipos\\america.png')
    	americaImg = pygame.transform.scale(americaImg, [200,200])
    	america = pygame.sprite.Sprite()
    	america.image = americaImg
    	america.rect = americaImg.get_rect()
    	america.rect.left = 440
    	america.rect.top = 150
    	colorElegirAmerica = (237, 221, 21)


    	atlasImg = pygame.image.load('menu\\equipos\\atlas.png')
    	atlasImg = pygame.transform.scale(atlasImg, [200,200])
    	atlas = pygame.sprite.Sprite()
    	atlas.image = atlasImg
    	atlas.rect = atlasImg.get_rect()
    	atlas.rect.left = 660
    	atlas.rect.top = 150
    	colorElegirAtlas = (149, 12, 12)

    	tolucaImg = pygame.image.load('menu\\equipos\\toluca.png')
    	tolucaImg = pygame.transform.scale(tolucaImg, [200,200])
    	toluca = pygame.sprite.Sprite()
    	toluca.image = tolucaImg
    	toluca.rect = tolucaImg.get_rect()
    	toluca.rect.left = 880
    	toluca.rect.top = 150
    	colorElegirToluca = (255, 0, 0)


    	tigresImg = pygame.image.load('menu\\equipos\\tigres.png')
    	tigresImg = pygame.transform.scale(tigresImg, [200,200])
    	tigres = pygame.sprite.Sprite()
    	tigres.image = tigresImg
    	tigres.rect = tigresImg.get_rect()
    	tigres.rect.left = 1100
    	tigres.rect.top = 150
    	colorElegirTigres = (236, 140, 0)


    	cruzazulImg = pygame.image.load('menu\\equipos\\cruzazul.png')
    	cruzazulImg = pygame.transform.scale(cruzazulImg, [200,200])
    	cruzazul = pygame.sprite.Sprite()
    	cruzazul.image = cruzazulImg
    	cruzazul.rect = cruzazulImg.get_rect()
    	cruzazul.rect.left = 1320
    	cruzazul.rect.top = 150
    	colorElegirCruzAzul = (16, 49, 234)


    	monterreyImg = pygame.image.load('menu\\equipos\\monterrey.png')
    	monterreyImg = pygame.transform.scale(monterreyImg, [200,200])
    	monterrey = pygame.sprite.Sprite()
    	monterrey.image = monterreyImg
    	monterrey.rect = monterreyImg.get_rect()
    	monterrey.rect.left = 1760
    	monterrey.rect.top = 150
    	colorElegirMonterrey = (9, 30, 149)


    	pumasImg = pygame.image.load('menu\\equipos\\pumas.png')
    	pumasImg = pygame.transform.scale(pumasImg, [200,200])
    	pumas = pygame.sprite.Sprite()
    	pumas.image = pumasImg
    	pumas.rect = pumasImg.get_rect()
    	pumas.rect.left = 1540
    	pumas.rect.top = 150
    	colorElegirPumas = (141, 122, 29)


    ####Botones siguiente/anterior####
    	colorSiguienteAnterior = (0, 19, 208)
    	siguiente = pygame.Rect(380, 400, 80, 35)
    	anterior = pygame.Rect(180, 400, 80, 35)

    	siguienteX = 0
    	siguienteY = 0
    	vuelta1 = False
    	numVueltas = 0
    	moverseAnt = True
    	moverseSig = True
    	opcion = pygame.mixer.Sound("sonidos\\opcion.wav")
    	opcion.set_volume(0.1)

    ####Boton retroceso####

    	retroceso = pygame.Rect(20,20, 60, 25)
    	textoRetroceso = fuente.render("Atrás", 2, [255,255,255])

    	while elegirSalir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()

    		elegirFps.tick(60)
    		pantalla.fill([255,255,255])
    		pantalla.blit(fondo, [0,0])
    		pantalla.blit(textoElegirTeam, [210, 30])
    		pygame.draw.rect(pantalla, colorSiguienteAnterior, siguiente)
    		pygame.draw.rect(pantalla, colorSiguienteAnterior, anterior)

    		pantalla.blit(chivas.image, chivas.rect) #[220, 150])

    		pantalla.blit(america.image, america.rect) #[440, 150])#* 2

    		pantalla.blit(atlas.image, atlas.rect) #[660, 150])#*3

    		pantalla.blit(toluca.image, toluca.rect) #[880, 150])#*4

    		pantalla.blit(cruzazul.image, cruzazul.rect) #[1100, 150])#*5

    		pantalla.blit(tigres.image, tigres.rect) #[1320, 150])#*6

    		pantalla.blit(pumas.image, pumas.rect) #[1540, 150])#*7

    		pantalla.blit(monterrey.image, monterrey.rect) #[1760, 150])#*8

    		pantalla.blit(flechaSiguiente, [410, 408])
    		pantalla.blit(flechaAnterior, [210, 408])
    		pygame.draw.rect(pantalla, [255,255,255], cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()

    		chivas.rect.move_ip(siguienteX, siguienteY)
    		america.rect.move_ip(siguienteX, siguienteY)
    		atlas.rect.move_ip(siguienteX, siguienteY)
    		toluca.rect.move_ip(siguienteX, siguienteY)
    		cruzazul.rect.move_ip(siguienteX, siguienteY)
    		tigres.rect.move_ip(siguienteX, siguienteY)
    		monterrey.rect.move_ip(siguienteX, siguienteY)
    		pumas.rect.move_ip(siguienteX, siguienteY)

    		if america.rect.left == 220:
    			siguienteX = 0
    			siguienteY = 0
    			elegirAmerica = pygame.Rect(263, 450, 120, 40)
    			pygame.draw.rect(pantalla, colorElegirAmerica, elegirAmerica)
    			pantalla.blit(textoElegir, [285,460])
    			moverseAnt = True
    			moverseSig = True

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(elegirAmerica):
    					miEquipo = "America"
    					partidos(pantalla, chivasImg, americaImg, atlasImg, tolucaImg, tigresImg, cruzazulImg, monterreyImg, pumasImg, miEquipo)
    		if chivas.rect.left == 220:
    			siguienteX = 0
    			siguienteY = 0
    			elegirChivas = pygame.Rect(263, 450, 120, 40)
    			pygame.draw.rect(pantalla, colorElegirChivas, elegirChivas)
    			pantalla.blit(textoElegir, [285,460])
    			moverseSig = True
    			moverseAnt = False

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(elegirChivas):
    					miEquipo = "Chivas"
    					partidos(pantalla, chivasImg, americaImg, atlasImg, tolucaImg, tigresImg, cruzazulImg, monterreyImg, pumasImg, miEquipo)
    		if atlas.rect.left == 220:
    			siguienteX = 0
    			siguienteY = 0
    			elegirAtlas = pygame.Rect(263, 450, 120, 40)
    			pygame.draw.rect(pantalla, colorElegirAtlas, elegirAtlas)
    			pantalla.blit(textoElegir, [285,460])
    			moverseAnt = True
    			moverseSig = True

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(elegirAtlas):
    					miEquipo = "Atlas"
    					partidos(pantalla, chivasImg, americaImg, atlasImg, tolucaImg, tigresImg, cruzazulImg, monterreyImg, pumasImg, miEquipo)
    		if toluca.rect.left == 220:
    			siguienteX = 0
    			siguienteY = 0
    			elegirToluca = pygame.Rect(263, 450, 120, 40)
    			pygame.draw.rect(pantalla, colorElegirToluca, elegirToluca)
    			pantalla.blit(textoElegir, [285,460])
    			moverseAnt = True
    			moverseSig = True

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(elegirToluca):
    					miEquipo = "Toluca"
    					partidos(pantalla, chivasImg, americaImg, atlasImg, tolucaImg, tigresImg, cruzazulImg, monterreyImg, pumasImg, miEquipo)
    		if cruzazul.rect.left == 220:
    			siguienteX = 0
    			siguienteY = 0
    			elegirCruzAzul = pygame.Rect(263, 450, 120, 40)
    			pygame.draw.rect(pantalla, colorElegirCruzAzul, elegirCruzAzul)
    			pantalla.blit(textoElegir, [285,460])
    			moverseAnt = True
    			moverseSig = True

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(elegirCruzAzul):
    					miEquipo = "Cruz Azul"
    					partidos(pantalla, chivasImg, americaImg, atlasImg, tolucaImg, tigresImg, cruzazulImg, monterreyImg, pumasImg, miEquipo)
    		if tigres.rect.left == 220:
    			siguienteX = 0
    			siguienteY = 0
    			elegirTigres = pygame.Rect(263, 450, 120, 40)
    			pygame.draw.rect(pantalla, colorElegirTigres, elegirTigres)
    			pantalla.blit(textoElegir, [285,460])
    			moverseAnt = True
    			moverseSig = True

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(elegirTigres):
    					miEquipo = "Tigres"
    					partidos(pantalla, chivasImg, americaImg, atlasImg, tolucaImg, tigresImg, cruzazulImg, monterreyImg, pumasImg, miEquipo)
    		if monterrey.rect.left == 220:
    			siguienteX = 0
    			siguienteY = 0
    			elegirMonterrey = pygame.Rect(263, 450, 120, 40)
    			pygame.draw.rect(pantalla, colorElegirMonterrey, elegirMonterrey)
    			pantalla.blit(textoElegir, [285,460])
    			moverseAnt = True
    			moverseSig = False

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(elegirMonterrey):
    					miEquipo = "Monterrey"
    					partidos(pantalla, chivasImg, americaImg, atlasImg, tolucaImg, tigresImg, cruzazulImg, monterreyImg, pumasImg, miEquipo)
    		if pumas.rect.left == 220:
    			siguienteX = 0
    			siguienteY = 0
    			elegirPumas = pygame.Rect(263, 450, 120, 40)
    			pygame.draw.rect(pantalla, colorElegirPumas, elegirPumas)
    			pantalla.blit(textoElegir, [285,460])
    			moverseAnt = True
    			moverseSig = True

    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(elegirPumas):
    					miEquipo = "Pumas"
    					partidos(pantalla, chivasImg, americaImg, atlasImg, tolucaImg, tigresImg, cruzazulImg, monterreyImg, pumasImg, miEquipo)

    		if evento.type == pygame.MOUSEBUTTONDOWN:
    			if moverseSig == True:
    				if cursor.colliderect(siguiente):
    					siguienteX = -10
    					siguienteY = 0
    					numVueltas += 1
    					opcion.play()
    			if moverseAnt == True:
    				if cursor.colliderect(anterior):
    					siguienteX = 10
    					siguienteY = 0
    					opcion.play()
    			if cursor.colliderect(retroceso):
    				menu()

    		pygame.draw.rect(pantalla, (0, 19, 208), retroceso)
    		pantalla.blit(textoRetroceso, [20, 20])

    		pygame.display.update()

    def ventanaCreditos():
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	salir = False
    	cursor = pygame.Rect(50,50,1,1)
    	retroceso = pygame.Rect(20,20,60,25)
    	cuadroTwitter = pygame.Rect(18,384,200,40)
    	cuadroTwitch = pygame.Rect(18,295,200,40)
    	cuadroYoutube = pygame.Rect(315,295,200,40)


    	twitterimg = pygame.image.load('pajaroTwitter.png')
    	twitterimg = pygame.transform.scale(twitterimg, [55,55])
    	twitchimg = pygame.image.load('logoTwitch.png')
    	twitchimg = pygame.transform.scale(twitchimg, [55,55])
    	youtubeimg = pygame.image.load('logoYoutube.png')
    	youtubeimg = pygame.transform.scale(youtubeimg, [55,55])

    	fuenteRedesCreditos = pygame.font.Font('fuentes/creditos.ttf', 25)
    	fuente = pygame.font.Font('fuentes/roboto/Roboto-Regular.ttf', 19)
    	fuenteR = pygame.font.Font('menu\\letrasmenu.ttf', 18)
    	textoRetroceso = fuenteR.render("Atrás", 2, [255,255,255])
    	saludo = pygame.font.Font('fuentes/roboto/Roboto-BlackItalic.ttf', 25).render("Hola", 1000, [255,255,255])
    	mensajeCreditos1 = fuente.render("Mi nombre es Pablo Avelar y desarrollo aplicaciones y algunos", 1000, [255,255,255])
    	mensajeCreditos2 = fuente.render("juegos programando en Python. Éste es mi quinto juego que hago", 1000, [255,255,255])
    	mensajeCreditos3 = fuente.render("usando Python, y hasta ahora es el que más tiempo he estado", 1000, [255,255,255])
    	mensajeCreditos4 = fuente.render("desarrollando. Es un juego simple pero ando progresando.", 1000, [255,255,255])
    	mensajeTwitter = fuenteRedesCreditos.render("@_PabloAvelar", 1000, [255,255,255])
    	mensajeTwitch = fuenteRedesCreditos.render("PablitoAvelar", 1000, [255,255,255])
    	mensajeYoutube = fuenteRedesCreditos.render("PabloAvelar", 1000, [255,255,255])

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(retroceso):
    					menu()

    		pantalla.fill([12, 173, 29])

    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		pygame.draw.rect(pantalla, [255,255,255], cursor)
    		pygame.draw.rect(pantalla,[0, 67, 176],retroceso)
    		pygame.draw.rect(pantalla, [26, 173, 242], cuadroTwitter)
    		pygame.draw.rect(pantalla, [116,87,172], cuadroTwitch)
    		pygame.draw.rect(pantalla, [193, 1, 0], cuadroYoutube)


    		pantalla.blit(textoRetroceso, [22,22])
    		pantalla.blit(saludo, [288,58])

    		pantalla.blit(mensajeCreditos1, [10,120])
    		pantalla.blit(mensajeCreditos2, [10,155])
    		pantalla.blit(mensajeCreditos3, [10,190])
    		pantalla.blit(mensajeCreditos4, [10,225])
    		pantalla.blit(mensajeTwitter, [60,388])
    		pantalla.blit(mensajeTwitch, [60,298])
    		pantalla.blit(mensajeYoutube, [360, 298])

    		pantalla.blit(twitterimg, [5,380])
    		pantalla.blit(twitchimg, [5,290])
    		pantalla.blit(youtubeimg, [300,290])

    		pygame.display.update()

    def ventanaPalmares():
    	import palmares
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	salir = False
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 18)
    	fuentetxt = pygame.font.Font('menu\\letrasmenu.ttf', 15)
    	cursor = pygame.Rect(50,50,1,1)
    	pasto = pygame.image.load('extra\\pasto.png')
    	pasto = pygame.transform.scale(pasto, [600,500])
    	pasto2 = pygame.image.load('extra\\pasto2.jpg')

    	####Boton retroceso####
    	retroceso = pygame.Rect(20,20, 60, 25)
    	textoRetroceso = fuente.render("Atrás", 2, [255,255,255])


    	#Equipos#
    	todoslosequipos()
    	cPalmares = pygame.transform.scale(chivasImg, [50,50])
    	amPalmares = pygame.transform.scale(americaImg, [50,50])
    	atPalmares = pygame.transform.scale(atlasImg, [50,50])
    	tolPalmares = pygame.transform.scale(tolucaImg, [50,50])
    	tigPalmares = pygame.transform.scale(tigresImg, [50,50])
    	cazPalmares = pygame.transform.scale(cruzazulImg, [50,50])
    	mtyPalmares = pygame.transform.scale(monterreyImg, [50,50])
    	pumPalmares = pygame.transform.scale(pumasImg, [50,50])
    ###Separaciones equipos###
    	separarChivas = [230, 11, 11]
    	separacionChivas = pygame.Rect(60 ,90, 600, 40)

    	separarAmerica = [237, 219, 0]
    	separacionAmerica = pygame.Rect(60 ,142, 600, 40)

    	separarAtlas = [142, 7, 7]
    	separacionAtlas = pygame.Rect(60 ,194, 600, 40)

    	separarToluca = [255, 0, 0]
    	separacionToluca = pygame.Rect(60 ,246, 600, 40)

    	separarPumas = [180, 124, 18]
    	separacionPumas = pygame.Rect(60 ,298, 600, 40)

    	separarMonterrey = [1, 12, 101]
    	separacionMonterrey = pygame.Rect(60 ,350, 600, 40)

    	separarTigres = [219, 145, 16]
    	separacionTigres = pygame.Rect(60 ,402, 600, 40)

    	separarCruzAzul = [35, 116, 218]
    	separacionCruzAzul = pygame.Rect(60 ,454, 600, 40)

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(retroceso):
    					menu()

    		pantalla.fill([90, 90, 93])
    		pantalla.blit(pasto, [0,0])
    		pantalla.blit(pasto2, [0,250])
    		pantalla.blit(pasto2, [0,0])
    		pantalla.blit(pasto2, [0,100])
    		pantalla.blit(pasto2, [0,150])
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		pygame.draw.rect(pantalla, [255,255,255], cursor)
    		pygame.draw.rect(pantalla,[0, 67, 176],retroceso)
    		#pygame.draw.rect(pantalla, separarXcolor, fila1)
    		pantalla.blit(textoRetroceso, [22,22])

    		pygame.draw.rect(pantalla, separarChivas, separacionChivas)
    		pantalla.blit(cPalmares, [6,80])
    		pygame.draw.rect(pantalla, separarAmerica, separacionAmerica)
    		pantalla.blit(amPalmares, [6,132])
    		pygame.draw.rect(pantalla, separarAtlas, separacionAtlas)
    		pantalla.blit(atPalmares, [6,184])
    		pygame.draw.rect(pantalla, separarToluca, separacionToluca)
    		pantalla.blit(tolPalmares, [6,236])
    		pygame.draw.rect(pantalla, separarPumas, separacionPumas)
    		pantalla.blit(pumPalmares, [6,288])
    		pygame.draw.rect(pantalla, separarMonterrey, separacionMonterrey)
    		pantalla.blit(mtyPalmares, [6,340])
    		pygame.draw.rect(pantalla, separarTigres, separacionTigres)
    		pantalla.blit(tigPalmares, [6,392])
    		pygame.draw.rect(pantalla, separarCruzAzul, separacionCruzAzul)
    		pantalla.blit(cazPalmares, [6,444])

    		palmares.registrosPalmares(pantalla)

    		pygame.display.update()

    def menu():
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])

    	menuSalir = False
    	menuFps = pygame.time.Clock()

    	fondo = pygame.image.load('fondohd.jpg')

    	botonJugar = pygame.Rect(50, 420, 150, 60)
    	botonSalir = pygame.Rect(390, 420, 150, 60)
    	botonPalmares = pygame.Rect(505, 338, 85, 50)
    	botonCreditos = pygame.Rect(5, 348, 85, 50)

    	colorBotonJugar = (0, 0, 0)
    	colorBotonSalir = (155, 10, 10)
    	colorBotonPalmares = (200, 180, 10)
    	colorBotonCreditos = (124, 197, 253)

    	cursor = pygame.Rect(50, 50, 1, 1)
    	fuente = pygame.font.Font('menu\\letrasmenu.ttf', 30)
    	fuentepal = pygame.font.Font('menu\\letrasmenu.ttf', 15)
    	fuenteCreditos = pygame.font.Font('menu\\letrasmenu.ttf', 10)
    	textoJugar = fuente.render("JUGAR", 4, [255,255,255])
    	textoSalir = fuente.render("SALIR", 4, [255,255,255])
    	textoPalmares = fuentepal.render("PALMARÉS", 4, [255,255,255])
    	textoCreditos = fuentepal.render("CRÉDITOS", 4, [255,255,255])
    	#textoMensaje = fuenteCreditos.render("Éste es mi quinto juego que hago en python :D", 4, [255,255,255])

    	while menuSalir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				menuSalir = True
    				pygame.quit()
    			if evento.type == pygame.MOUSEBUTTONDOWN:
    				if cursor.colliderect(botonSalir):
    					menuSalir = True
    					pygame.quit()
    				elif cursor.colliderect(botonJugar):
    					elegirEquipo(pantalla)
    				elif cursor.colliderect(botonPalmares):
    					ventanaPalmares()
    				elif cursor.colliderect(botonCreditos):
    					ventanaCreditos()

    		menuFps.tick(60)
    		pantalla.fill((255,255,255))
    		pantalla.blit(fondo, [0,0])
    		pygame.draw.rect(pantalla, colorBotonJugar, botonJugar)
    		pygame.draw.rect(pantalla, colorBotonSalir, botonSalir)
    		pygame.draw.rect(pantalla, colorBotonPalmares, botonPalmares)
    		pygame.draw.rect(pantalla, colorBotonCreditos, botonCreditos)

    ####Al tener el cursor sobre el botón para que se vea bien cute####
    		if cursor.colliderect(botonJugar):
    			colorBotonJugar = (242, 147, 8)
    		else:
    			colorBotonJugar = (188, 112, 1)

    		if cursor.colliderect(botonSalir):
    			colorBotonSalir = (205, 15, 15)
    		else:
    			colorBotonSalir = (155, 10, 10)

    		if cursor.colliderect(botonPalmares):
    			colorBotonPalmares = (232, 209, 13)
    		else:
    			colorBotonPalmares = (200, 180, 10)

    		if cursor.colliderect(botonCreditos):
    			colorBotonCreditos = (124, 197, 253)
    		else:
    			colorBotonCreditos = (85,172,238)

    		pygame.draw.rect(pantalla, (255,255,255), cursor)
    		(cursor.left, cursor.top) = pygame.mouse.get_pos()
    		pantalla.blit(textoJugar, [76, 435])
    		pantalla.blit(textoSalir, [415, 435])
    		pantalla.blit(textoPalmares, [511, 357])
    		pantalla.blit(textoCreditos, [11, 362])
    		#pantalla.blit(textoMensaje, [0, 0])

    		pygame.display.update()


    def principal(pantalla, miEquipo):
    	pygame.init()
    	pantalla = pygame.display.set_mode([600,500])
    	salir = False
    	fps = pygame.time.Clock()
    ###Registrar partido###

    	if miEquipo == "Toluca":
    		archivoPJ = open('sts\\toluca\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Pumas":
    		archivoPJ = open('sts\\pumas\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Monterrey":
    		archivoPJ = open('sts\\monterrey\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Tigres":
    		archivoPJ = open('sts\\tigres\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Cruz Azul":
    		archivoPJ = open('sts\\cruzazul\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Atlas":
    		archivoPJ = open('sts\\atlas\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "America":
    		archivoPJ = open('sts\\america\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    	if miEquipo == "Chivas":
    		archivoPJ = open('sts\\pj.csv', 'a')
    		archivoPJ.write("1")
    		archivoPJ.close()

    ####Sonidos####

    	sonidoGol = pygame.mixer.Sound("sonidos\\gol.wav")
    	sonidoGol.set_volume(0.3)
    	sonidoTirar = pygame.mixer.Sound("sonidos\\futboltirar.wav")
    	sonidoTirar.set_volume(0.5)

    ####Puntero#####

    	puntero = pygame.Rect(50,50,1,1)
    	rolJugador = True

    ####Balón####
    	imgBalon = pygame.image.load('balonC.png')
    	imgBalon = pygame.transform.scale(imgBalon, (30,30))
    	tirosBalon = pygame.transform.scale(imgBalon, (15, 15))
    	balon = pygame.sprite.Sprite()
    	balon.image = imgBalon
    	balon.rect = imgBalon.get_rect()
    	balonPosXInicial = 280
    	balonPosYInicial = 400
    	balon.rect.left = balonPosXInicial
    	balon.rect.top = balonPosYInicial

    ####portero1######
    	#Inicial#
    	imgportero1 = pygame.image.load('portero\\portero1.png')
    	imgportero1 = pygame.transform.scale(imgportero1, (125,140))
    	imgportero2 = pygame.image.load('portero\\portero2.png')
    	imgportero2 = pygame.transform.scale(imgportero2, (150,110))
    	imgportero3 = pygame.image.load('portero\\portero3.png')
    	imgportero3 = pygame.transform.scale(imgportero3, (140,100))
    	imgportero4 = pygame.image.load('portero\\portero4.png')
    	imgportero4 = pygame.transform.scale(imgportero4, (150,110))
    	imgportero5 = pygame.image.load('portero\\portero5.png')
    	imgportero5 = pygame.transform.scale(imgportero5, (150,110))
    	imgportero6 = pygame.image.load('portero\\portero6.png')
    	imgportero6 = pygame.transform.scale(imgportero6, (125,140))
    	imgportero7 = pygame.image.load('portero\\portero7.png')
    	imgportero7 = pygame.transform.scale(imgportero7, (150,110))
    	imgportero8 = pygame.image.load('portero\\portero8.png')
    	imgportero8 = pygame.transform.scale(imgportero8, (150,110))


    	portero1 = pygame.sprite.Sprite()
    	portero1.image = imgportero1
    	portero1.rect = imgportero1.get_rect()
    	porteroPosXInicial = 80
    	porteroPosYInicial = 245
    	portero1.rect.top = porteroPosXInicial
    	portero1.rect.left = porteroPosYInicial

    	portero2 = pygame.sprite.Sprite()
    	portero2.image = imgportero2
    	portero2.rect = imgportero2.get_rect()
    	portero2.rect.top = 80
    	portero2.rect.left = 200

    	portero3 = pygame.sprite.Sprite()
    	portero3.image = imgportero3
    	portero3.rect = imgportero3.get_rect()
    	portero3.rect.top = 0
    	portero3.rect.left = 0

    	portero4 = pygame.sprite.Sprite()
    	portero4.image = imgportero4
    	portero4.rect = imgportero4.get_rect()
    	portero4.rect.top = 80
    	portero4.rect.left = 200

    	portero5 = pygame.sprite.Sprite()
    	portero5.image = imgportero5
    	portero5.rect = imgportero5.get_rect()
    	portero5.rect.top = 80
    	portero5.rect.left = 270

    	portero6 = pygame.sprite.Sprite()
    	portero6.image = imgportero6
    	portero6.rect = imgportero6.get_rect()
    	portero6.rect.top = portero6.rect.top
    	portero6.rect.left = portero6.rect.left

    	portero7 = pygame.sprite.Sprite()
    	portero7.image = imgportero7
    	portero7.rect = imgportero6.get_rect()
    	portero7.rect.top = 130
    	portero7.rect.left = 200

    	portero8 = pygame.sprite.Sprite()
    	portero8.image = imgportero8
    	portero8.rect = imgportero8.get_rect()
    	portero8.rect.top = 80
    	portero8.rect.left = 290

    	"""NO PONGAS EL 1 PORQUE NO HAY"""
    	posicionesLista = ["2","3","4","5","6","7","8"]
    	if rolJugador == True:
    		posiciones = random.choice(posicionesLista)
    ####Variables de la cancha#####
    	colorPasto = (43, 171, 23)
    	arbustoImg = pygame.image.load('extra\\arbusto.png')
    	arbustoImg = pygame.transform.scale(arbustoImg, [50,50])
    	#pastos XD#

    	pasto = pygame.image.load('extra\\pasto.png')
    	pasto = pygame.transform.scale(pasto, [600,500])
    	pasto2 = pygame.image.load('extra\\pasto2.jpg')

    	#pastos XD#

    	pasto = pygame.image.load('extra\\pasto.png')
    	pasto = pygame.transform.scale(pasto, [600,500])
    	pasto2 = pygame.image.load('extra\\pasto2.jpg')

    ####Variables portería#######
    	#Postes#
    	colorPostes = (255,255,255)
    	iz = pygame.Rect(100, 50, 10, 160)
    	arr = pygame.Rect(100, 50, 380, 10)
    	ab = pygame.Rect(480, 50, 10, 160)
    	#red#
    	imagenRed = pygame.image.load('portero\\redporteria.png')
    	imagenRed = pygame.transform.scale(imagenRed, [395, 245])

    ####Aficion####
    	#borde#
    	colorBordeAficion = (242, 12, 50)
    	bordeAficion = pygame.Rect(0,0,600,150)
    	finalBordeAficion = pygame.Rect(0, 120, 600, 40)
    	fila1 = pygame.Rect(0, 30, 600, 5)
    	fila2 = pygame.Rect(0, 60, 600, 5)
    	fila3 = pygame.Rect(0, 90, 600, 5)

    ####Tiros###
    	numTiros = 5

    	fuente = pygame.font.Font('fuentes/letras.otf', 20)

    	imgBlanco = pygame.image.load('blanco.png')
    	imgBlanco = pygame.transform.scale(imgBlanco, (30,30))
    	blanco1 = pygame.sprite.Sprite()
    	blanco2 = pygame.sprite.Sprite()
    	blanco3= pygame.sprite.Sprite()
    	blanco4 = pygame.sprite.Sprite()
    	blanco5 = pygame.sprite.Sprite()

    	blanco1.image = imgBlanco
    	blanco1.rect = imgBlanco.get_rect()
    	blanco1.rect.left = 110
    	blanco1.rect.top = 60

    	blanco2.image = imgBlanco
    	blanco2.rect = imgBlanco.get_rect()
    	blanco2.rect.left = 110
    	blanco2.rect.top = 180

    	blanco3.image = imgBlanco
    	blanco3.rect = imgBlanco.get_rect()
    	blanco3.rect.left = 440
    	blanco3.rect.top = 65

    	blanco4.image = imgBlanco
    	blanco4.rect = imgBlanco.get_rect()
    	blanco4.rect.left = 440
    	blanco4.rect.top = 175

    	blanco5.image = imgBlanco
    	blanco5.rect = imgBlanco.get_rect()
    	blanco5.rect.left = 290
    	blanco5.rect.top = 60

    ####Marcador####
    	#Goles#
    	goles = 0
    	#Fallados#
    	fallados = 0
    	#Imagenes#
    	gol = pygame.image.load('marcador\\gol.jpg')
    	fallado = pygame.image.load('marcador\\fallado.jpg')
    	marcador = pygame.Rect(295, 6, 130, 20)
    	tirosMarcador = 0

    ####Cambiar rol######
    	#cambiarRol = fuente.render("Ahora tú eres el portero, adivina los tiros.", 4, [21, 246, 246])

    ####Variables auxiliares#######
    	ha_tirado = False
    	velocidadX = 0
    	velocidadY = 0
    	segundosInt = 0
    	porteroY = 0
    	porteroX = 0
    	xposGuante = 0
    	yposGuante = 0
    	xposGuante2 = 0
    	yposGuante2 = 0
    	colorGuante = (245, 184, 222)
    	guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    	guante2 = pygame.Rect(xposGuante2, yposGuante2, 6, 6)
    	fallo = False
    	golAnotado = False
    	golFallado = False
    	golFalladoMarcador1 = False
    	golAnotadoMarcador1 = False
    	golFalladoMarcador2 = False
    	golAnotadoMarcador2 = False
    	golFalladoMarcador3 = False
    	golAnotadoMarcador3 = False
    	golFalladoMarcador4 = False
    	golAnotadoMarcador4 = False
    	golFalladoMarcador5 = False
    	golAnotadoMarcador5 = False

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()

    			if numTiros > 0:
    				rolJugador = True
    				if evento.type == pygame.MOUSEBUTTONDOWN:
    					if puntero.colliderect(blanco1.rect):
    						#Arriba izquierda#
    						velocidadX = -4
    						velocidadY = -8

    					elif puntero.colliderect(blanco2.rect):
    						#Abajo izquierda#
    						velocidadX = -5
    						velocidadY = -6

    					elif puntero.colliderect(blanco3.rect):
    						#Arriba derecha#
    						velocidadX = 5
    						velocidadY = -10
    					elif puntero.colliderect(blanco4.rect):
    						#Abajo derecha#
    						velocidadX = 4
    						velocidadY = -6
    					elif puntero.colliderect(blanco5.rect):
    						#centro#

    						velocidadX = 0
    						velocidadY = -8

    					if puntero.colliderect(blanco1.rect) or puntero.colliderect(blanco2.rect) or puntero.colliderect(blanco3.rect) or puntero.colliderect(blanco4.rect) or puntero.colliderect(blanco5.rect):
    						ha_tirado = True
    						tirosMarcador += 1
    						sonidoTirar.play()

    			if numTiros == 0:
    				cambioDeRol(goles, miEquipo)

    		fps.tick(60)
    		pantalla.fill(colorPasto)
    		tiros = str(numTiros)

    		mostrarTiros = fuente.render("X {}".format(tiros), 2, [255,255,255])


    		pygame.draw.rect(pantalla, colorBordeAficion, bordeAficion)
    		pygame.draw.rect(pantalla, (11, 156, 13), finalBordeAficion)
    		pygame.draw.rect(pantalla, [211, 211, 211], fila1)
    		pygame.draw.rect(pantalla, [211, 211, 211], fila2)
    		pygame.draw.rect(pantalla, [211, 211, 211], fila3)
    		#Pasto img#
    		pastoParaTodos(pantalla, pasto, pasto2)

    		#Arbusto#
    		arbustoParaTodos(pantalla, arbustoImg)


    		#pintar red#
    		pantalla.blit(imagenRed, [95, 10])
    		pygame.draw.rect(pantalla, colorPostes, iz)
    		pygame.draw.rect(pantalla, colorPostes, arr)
    		pygame.draw.rect(pantalla, colorPostes, ab)
    		#puntoPenal#
    		pygame.draw.circle(pantalla, (255,255,255), (295, 415), 15)

    		pantalla.blit(blanco1.image, blanco1.rect)
    		pantalla.blit(blanco2.image, blanco2.rect)
    		pantalla.blit(blanco3.image, blanco3.rect)
    		pantalla.blit(blanco4.image, blanco4.rect)
    		pantalla.blit(blanco5.image, blanco5.rect)

    		if ha_tirado == False:
    			pantalla.blit(portero1.image, portero1.rect)
    			balon.rect.left = balonPosXInicial
    			balon.rect.top = balonPosYInicial
    			velocidadX = 0
    			velocidadY = 0
    			posiciones = random.choice(posicionesLista)
    			portero2.rect.left = 200
    			portero2.rect.top = 80
    			portero3.rect.left = 245
    			portero3.rect.top = 80
    			portero4.rect.left = 200
    			portero4.rect.top = 80
    			portero5.rect.left = 270
    			portero5.rect.top = 80
    			portero6.rect.left = 245
    			portero6.rect.top = 80
    			portero7.rect.left = 200
    			portero7.rect.top = 130
    			portero8.rect.left = 200
    			portero8.rect.top = 130
    			fallo = False
    			golAnotado = False


    		if ha_tirado == True:
    			if numTiros > 0:
    				if posiciones == "2":
    					pantalla.blit(portero2.image, portero2.rect)
    					xposGuante = portero2.rect.left+11
    					yposGuante = portero2.rect.top+100
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -3
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero2.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "3":

    					pantalla.blit(portero3.image, portero3.rect)
    					xposGuante = portero3.rect.left+122
    					yposGuante = portero3.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 2
    					porteroY = 2
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero3.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "4":
    					pantalla.blit(portero4.image, portero4.rect)
    					xposGuante = portero4.rect.left+10
    					yposGuante = portero4.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -1
    					porteroY = 1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero4.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "5":
    					pantalla.blit(portero5.image, portero5.rect)
    					xposGuante = portero5.rect.left+110
    					yposGuante = portero5.rect.top+10
    					xposGuante2 = portero5.rect.left+130
    					yposGuante2 = portero5.rect.top+90
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					guante2 = pygame.Rect(xposGuante2, yposGuante2, 8, 8)
    					porteroX = 2
    					porteroY = 0
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					pygame.draw.rect(pantalla, colorGuante, guante2)
    					portero5.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "6":
    					xposGuante = portero5.rect.left+30
    					yposGuante = portero5.rect.top+6
    					guante = pygame.Rect(xposGuante, yposGuante, 12, 6)
    					portero6.rect.left = 245
    					portero6.rect.top = 80
    					pantalla.blit(portero6.image, portero6.rect)
    					pygame.draw.rect(pantalla, (0,0,0), guante)

    				elif posiciones == "7":
    					pantalla.blit(portero7.image, portero7.rect)
    					xposGuante = portero7.rect.left+9
    					yposGuante = portero7.rect.top+5
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = -2
    					porteroY = -1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero7.rect.move_ip(porteroX, porteroY)

    				elif posiciones == "8":
    					pantalla.blit(portero8.image, portero8.rect)
    					xposGuante = portero8.rect.left+135
    					yposGuante = portero8.rect.top+8
    					guante = pygame.Rect(xposGuante, yposGuante, 6, 6)
    					porteroX = 4
    					porteroY = -1
    					pygame.draw.rect(pantalla, colorGuante, guante)
    					portero8.rect.move_ip(porteroX, porteroY)

    		if guante.colliderect(balon.rect) or guante2.colliderect(balon.rect):
    			fallados += 1
    			ha_tirado = False
    			golFallado = True
    			fallo = True
    		if balon.rect.colliderect(blanco1.rect) or balon.rect.colliderect(blanco2.rect) or balon.rect.colliderect(blanco3.rect) or balon.rect.colliderect(blanco4.rect) or balon.rect.colliderect(blanco5.rect):
    			if fallo != True:
    				goles += 1
    				golAnotado = True
    			ha_tirado = False

    		if balon.rect.colliderect(guante) or balon.rect.colliderect(blanco1.rect) or balon.rect.colliderect(blanco2.rect) or balon.rect.colliderect(blanco3.rect) or balon.rect.colliderect(blanco4.rect) or balon.rect.colliderect(blanco5.rect):
    			numTiros-=1

    		balon.rect.move_ip(velocidadX, velocidadY)
    		pantalla.blit(balon.image, balon.rect)

    		pantalla.blit(mostrarTiros, [50, 10])
    		pantalla.blit(tirosBalon, [20,10])

    		pygame.draw.rect(pantalla, (0,0,0), puntero)
    		(puntero.x, puntero.y) = pygame.mouse.get_pos()

    		pygame.draw.rect(pantalla, (255,255,255), marcador)
    		mensajeMarcador = fuente.render("Marcador: ", 2, (0,0,0))
    		pantalla.blit(mensajeMarcador, [205, 7])

    ##############################################################

    		if tirosMarcador == 1:
    			#RESULTADO1#
    			if golAnotado == True:
    				golAnotadoMarcador1 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador1 = True

    		if tirosMarcador == 2:
    			#RESULTADO2#
    			if golAnotado == True:
    				golAnotadoMarcador2 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador2 = True

    		if tirosMarcador == 3:
    			#RESULTADO3#
    			if golAnotado == True:
    				golAnotadoMarcador3 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador3 = True

    		if tirosMarcador == 4:
    			#RESULTADO4#
    			if golAnotado == True:
    				golAnotadoMarcador4 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador4 = True

    		if tirosMarcador == 5:
    			#RESULTADO5#
    			if golAnotado == True:
    				golAnotadoMarcador5 = True
    				#Gol a favor#
    				if miEquipo == "Toluca":
    					archivoGF = open('sts\\toluca\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Pumas":
    					archivoGF = open('sts\\pumas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Monterrey":
    					archivoGF = open('sts\\monterrey\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Tigres":
    					archivoGF = open('sts\\tigres\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == "Cruz Azul":
    					archivoGF = open('sts\\cruzazul\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Atlas':
    					archivoGF = open('sts\\atlas\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'America':
    					archivoGF = open('sts\\america\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()

    				if miEquipo == 'Chivas':
    					archivoGF = open('sts\\gf.csv', 'a')
    					archivoGF.write("1")
    					archivoGF.close()
    				sonidoGol.play()

    			if fallo == True:
    				golFalladoMarcador5 = True

    ###################################################################

    		if golAnotadoMarcador1 == True:
    			pantalla.blit(gol, [300, 7])

    		elif golFalladoMarcador1 == True:
    			pantalla.blit(fallado, [300, 7])

    		if golAnotadoMarcador2 == True:
    			pantalla.blit(gol, [325, 7])
    		elif golFalladoMarcador2 == True:
    			pantalla.blit(fallado, [325, 7])

    		if golAnotadoMarcador3 == True:
    			pantalla.blit(gol, [350, 7])
    		elif golFalladoMarcador3 == True:
    			pantalla.blit(fallado, [350, 7])

    		if golAnotadoMarcador4 == True:
    			pantalla.blit(gol, [375, 7])
    		elif golFalladoMarcador4 == True:
    			pantalla.blit(fallado, [375, 7])

    		if golAnotadoMarcador5 == True:
    			pantalla.blit(gol, [400, 7])
    		elif golFalladoMarcador5 == True:
    			pantalla.blit(fallado, [400, 7])

    		pygame.display.update()

    	pygame.quit()

    def animacionInicial():
    	pygame.init()
    	pantalla = pygame.display.set_mode([600, 500])
    	logo = pygame.image.load('fondohd.jpg')
    	pygame.display.set_icon(logo)
    	pygame.display.set_caption("Liguilla MX")
    	salir = False
    	fps = pygame.time.Clock()

    	balonImg = pygame.image.load('balonIntro.png')
    	balonImg = pygame.transform.scale(balonImg, [118, 119])
    	balon = pygame.sprite.Sprite()
    	balon.image = balonImg
    	balon.rect = balonImg.get_rect()
    	balon.rect.left = 250
    	balon.rect.top = 520
    	moverX = 0
    	moverY = -10
    	fuente = pygame.font.Font('fuentes/intro.ttf', 40)
    	fuenteRedes = pygame.font.Font('fuentes/intro.ttf', 25)
    	sonidoIntro = pygame.mixer.Sound("sonidos\\drop.wav")
    	sonidoIntro.set_volume(0.2)

    	colorTwitter = [0, 197, 241]
    	colorTwitch = [119, 49, 188]

    	txtTwitter = fuenteRedes.render("@_PabloAvelar", 4, colorTwitter)
    	txtTwitch = fuenteRedes.render("PablitoAvelar", 4, colorTwitch)
    	txtPablo = fuente.render("Pablo", 4, [0,0,0])
    	txtAvelar = fuente.render("Avelar", 4, [0,0,0])

    	twitterIcono = pygame.image.load('twitter.png')
    	twitterIcono = pygame.transform.scale(twitterIcono, [30,30])

    	twitchIcono = pygame.image.load('twitch.png')
    	twitchIcono = pygame.transform.scale(twitchIcono, [30,30])

    	while salir != True:
    		for evento in pygame.event.get():
    			if evento.type == pygame.QUIT:
    				pygame.quit()
    		fps.tick(60)
    		pantalla.fill([255,255,255])

    		if balon.rect.top == 200:
    			reloj = pygame.time.get_ticks()/1000
    			moverY = 0
    			sonidoIntro.play()
    			if reloj >= 2.2:
    				sonidoIntro.stop()
    			pantalla.blit(txtPablo, [125,250])
    			pantalla.blit(txtAvelar, [400,250])

    			pantalla.blit(twitterIcono, [60, 350])
    			pantalla.blit(txtTwitter, [100,350])

    			pantalla.blit(twitchIcono, [350, 350])
    			pantalla.blit(txtTwitch, [390,350])
    			if reloj >= 3:
    				menu()

    		balon.rect.move_ip(moverX, moverY)
    		pantalla.blit(balon.image, balon.rect)

    		pygame.display.update()
except Exception as e:
    if "display surface quit" in str(e):
        pass

if __name__ == "__main__":
	animacionInicial()
