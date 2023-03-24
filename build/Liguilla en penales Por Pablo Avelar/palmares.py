import pygame

def registrosPalmares(pantalla):
	fuentetxt = pygame.font.Font('menu\\letrasmenu.ttf', 15)
	fuentetitulo = pygame.font.Font('menu\\letrasmenu.ttf', 22)
		###Texto###
	pj = fuentetxt.render("PJ", 4, [255,255,255])
	ganados = fuentetxt.render("G", 4, [255,255,255])
	empatados = fuentetxt.render("E", 4, [255,255,255])
	perdidos = fuentetxt.render("P", 4, [255,255,255])

	golesAFavor = fuentetxt.render("GF", 4, [255,255,255])
	golesEnContra = fuentetxt.render("GC", 4, [255,255,255])

	trofeo = pygame.image.load('trofeo.png')
	trofeo = pygame.transform.scale(trofeo, [65,50])

#Titulo#
	titulo = fuentetitulo.render("PALMARÉS",8,[255,255,255])
	pantalla.blit(titulo, [260,10])

#########CHIVAS###########
	#Registros de estadísticas#
	archivoPJ = open('sts\\pj.csv')
	leerPJ = archivoPJ.read()
	numPJ = len(leerPJ)
	strnumPJ = str(numPJ)
	archivoPJ.close()
	txtPJ = fuentetxt.render(strnumPJ,4,[255,255,255])

	archivoG = open('sts\\g.csv')
	leerG = archivoG.read()
	numG = len(leerG)
	strnumG = str(numG)
	archivoG.close()
	txtG = fuentetxt.render(strnumG,4,[255,255,255])

	archivoE = open('sts\\e.csv')
	leerE = archivoE.read()
	numE = len(leerE)
	strnumE = str(numE)
	archivoE.close()
	txtE = fuentetxt.render(strnumE,4,[255,255,255])

	archivoP = open('sts\\p.csv')
	leerP = archivoP.read()
	numP = len(leerP)
	strnumP = str(numP)
	archivoP.close()
	txtP = fuentetxt.render(strnumP,4,[255,255,255])

	archivoGF = open('sts\\gf.csv')
	leerGF = archivoGF.read()
	numGF = len(leerGF)
	strnumGF = str(numGF)
	archivoGF.close()
	txtGF = fuentetxt.render(strnumGF,4,[255,255,255])

	archivoGC = open('sts\\gc.csv')
	leerGC = archivoGC.read()
	numGC = len(leerGC)
	strnumGC = str(numGC)
	archivoGC.close()
	txtGC = fuentetxt.render(strnumGC,4,[255,255,255])

	archivoTitulos = open('sts\\t.csv')
	leerTitulos = archivoTitulos.read()
	numTitulos = len(leerTitulos)
	strnumTitulos = str(numTitulos)
	archivoTitulos.close()
	txtTitulos = fuentetxt.render(strnumTitulos,4,[255,255,255])
	#########CHIVAS###########
	####mostrar texto####
	pantalla.blit(pj, [75, 70])
	 #mostrar partidos ganados#
	pantalla.blit(txtPJ, [75 ,98])

	pantalla.blit(ganados, [155, 70])
	 #mostrar partidos ganados#
	pantalla.blit(txtG, [155, 98])

	pantalla.blit(empatados, [235, 70])
	 #mostrar partidos empatados#
	pantalla.blit(txtE, [235, 98])

	pantalla.blit(perdidos, [315, 70])
	 #mostrar partidos perdidos#
	pantalla.blit(txtP, [315, 98])

	pantalla.blit(golesAFavor, [395, 70])
	 #mostrar goles a favor#
	pantalla.blit(txtGF, [395, 98])

	pantalla.blit(golesEnContra, [475, 70])
	 #mostrar goles en contra#
	pantalla.blit(txtGC, [475, 98])

	pantalla.blit(trofeo, [527, 40])
	 #mostrar titulos ganados#
	pantalla.blit(txtTitulos, [550, 98])

#########AMÉRICA###########
	#Registros de estadísticas#
	archivoPJamerica = open('sts\\america\\pj.csv')
	leerPJamerica = archivoPJamerica.read()
	numPJamerica = len(leerPJamerica)
	strnumPJamerica = str(numPJamerica)
	archivoPJamerica.close()
	txtPJamerica = fuentetxt.render(strnumPJamerica,4,[255,255,255])

	archivoGamerica = open('sts\\america\\g.csv')
	leerGamerica = archivoGamerica.read()
	numGamerica = len(leerGamerica)
	strnumGamerica = str(numGamerica)
	archivoGamerica.close()
	txtGamerica = fuentetxt.render(strnumGamerica,4,[255,255,255])

	archivoEamerica = open('sts\\america\\e.csv')
	leerEamerica = archivoEamerica.read()
	numEamerica = len(leerEamerica)
	strnumEamerica = str(numEamerica)
	archivoEamerica.close()
	txtEamerica = fuentetxt.render(strnumEamerica,4,[255,255,255])

	archivoPamerica = open('sts\\america\\p.csv')
	leerPamerica = archivoPamerica.read()
	numPamerica = len(leerPamerica)
	strnumPamerica = str(numPamerica)
	archivoPamerica.close()
	txtPamerica = fuentetxt.render(strnumPamerica,4,[255,255,255])

	archivoGFamerica = open('sts\\america\\gf.csv')
	leerGFamerica = archivoGFamerica.read()
	numGFamerica = len(leerGFamerica)
	strnumGFamerica = str(numGFamerica)
	archivoGFamerica.close()
	txtGFamerica = fuentetxt.render(strnumGFamerica,4,[255,255,255])

	archivoGCamerica = open('sts\\america\\gc.csv')
	leerGCamerica = archivoGCamerica.read()
	numGCamerica = len(leerGCamerica)
	strnumGCamerica = str(numGCamerica)
	archivoGCamerica.close()
	txtGCamerica = fuentetxt.render(strnumGCamerica,4,[255,255,255])

	archivoTitulosAmerica = open('sts\\america\\t.csv')
	leerTitulosAmerica = archivoTitulosAmerica.read()
	numTitulosAmerica = len(leerTitulosAmerica)
	strnumTitulosAmerica = str(numTitulosAmerica)
	archivoTitulosAmerica.close()
	txtTitulosAmerica = fuentetxt.render(strnumTitulosAmerica,4,[255,255,255])

	####mostrar texto####
	 #mostrar partidos ganados#
	pantalla.blit(txtPJamerica, [75 ,150])

	 #mostrar partidos ganados#
	pantalla.blit(txtGamerica, [155, 150])

	 #mostrar partidos empatados#
	pantalla.blit(txtEamerica, [235, 150])

	 #mostrar partidos perdidos#
	pantalla.blit(txtPamerica, [315, 150])

	 #mostrar goles a favor#
	pantalla.blit(txtGFamerica, [395, 150])

	 #mostrar goles en contra#
	pantalla.blit(txtGCamerica, [475, 150])

	 #mostrar titulos ganados#
	pantalla.blit(txtTitulosAmerica, [550, 150])

#########ATLAS###########
	#Registros de estadísticas#
	archivoPJatlas = open('sts\\atlas\\pj.csv')
	leerPJatlas = archivoPJatlas.read()
	numPJatlas = len(leerPJatlas)
	strnumPJatlas = str(numPJatlas)
	archivoPJatlas.close()
	txtPJatlas = fuentetxt.render(strnumPJatlas,4,[255,255,255])

	archivoGatlas = open('sts\\atlas\\g.csv')
	leerGatlas = archivoGatlas.read()
	numGatlas = len(leerGatlas)
	strnumGatlas = str(numGatlas)
	archivoGatlas.close()
	txtGatlas = fuentetxt.render(strnumGatlas,4,[255,255,255])

	archivoEatlas = open('sts\\atlas\\e.csv')
	leerEatlas = archivoEatlas.read()
	numEatlas = len(leerEatlas)
	strnumEatlas = str(numEatlas)
	archivoEatlas.close()
	txtEatlas = fuentetxt.render(strnumEatlas,4,[255,255,255])

	archivoPatlas= open('sts\\atlas\\p.csv')
	leerPatlas= archivoPatlas.read()
	numPatlas = len(leerPatlas)
	strnumPatlas= str(numPatlas)
	archivoPatlas.close()
	txtPatlas = fuentetxt.render(strnumPatlas,4,[255,255,255])

	archivoGFatlas = open('sts\\atlas\\gf.csv')
	leerGFatlas = archivoGFatlas.read()
	numGFatlas = len(leerGFatlas)
	strnumGFatlas = str(numGFatlas)
	archivoGFatlas.close()
	txtGFatlas = fuentetxt.render(strnumGFatlas,4,[255,255,255])

	archivoGCatlas = open('sts\\atlas\\gc.csv')
	leerGCatlas = archivoGCatlas.read()
	numGCatlas = len(leerGCatlas)
	strnumGCatlas = str(numGCatlas)
	archivoGCatlas.close()
	txtGCatlas = fuentetxt.render(strnumGCatlas,4,[255,255,255])

	archivoTitulosAtlas = open('sts\\atlas\\t.csv')
	leerTitulosAtlas = archivoTitulosAtlas.read()
	numTitulosAtlas = len(leerTitulosAtlas)
	strnumTitulosAtlas = str(numTitulosAtlas)
	archivoTitulosAtlas.close()
	txtTitulosAtlas = fuentetxt.render(strnumTitulosAtlas,4,[255,255,255])
	####mostrar texto####
	 #mostrar partidos ganados#
	pantalla.blit(txtPJatlas, [75 ,202])

	 #mostrar partidos ganados#
	pantalla.blit(txtGatlas, [155, 202])

	 #mostrar partidos empatados#
	pantalla.blit(txtEatlas, [235, 202])

	 #mostrar partidos perdidos#
	pantalla.blit(txtPatlas, [315, 202])

	 #mostrar goles a favor#
	pantalla.blit(txtGFatlas, [395, 202])

	 #mostrar goles en contra#
	pantalla.blit(txtGCatlas, [475, 202])

	 #mostrar titulos ganados#
	pantalla.blit(txtTitulosAtlas, [550, 202])

#########TOLUCA###########
	#Registros de estadísticas#
	archivoPJtoluca = open('sts\\toluca\\pj.csv')
	leerPJtoluca = archivoPJtoluca.read()
	numPJtoluca = len(leerPJtoluca)
	strnumPJtoluca = str(numPJtoluca)
	archivoPJtoluca.close()
	txtPJtoluca = fuentetxt.render(strnumPJtoluca,4,[255,255,255])

	archivoGtoluca = open('sts\\toluca\\g.csv')
	leerGtoluca = archivoGtoluca.read()
	numGtoluca = len(leerGtoluca)
	strnumGtoluca = str(numGtoluca)
	archivoGtoluca.close()
	txtGtoluca = fuentetxt.render(strnumGtoluca,4,[255,255,255])

	archivoEtoluca = open('sts\\toluca\\e.csv')
	leerEtoluca = archivoEtoluca.read()
	numEtoluca = len(leerEtoluca)
	strnumEtoluca = str(numEtoluca)
	archivoEtoluca.close()
	txtEtoluca = fuentetxt.render(strnumEtoluca,4,[255,255,255])

	archivoPtoluca= open('sts\\toluca\\p.csv')
	leerPtoluca= archivoPtoluca.read()
	numPtoluca = len(leerPtoluca)
	strnumPtoluca= str(numPtoluca)
	archivoPtoluca.close()
	txtPtoluca = fuentetxt.render(strnumPtoluca,4,[255,255,255])

	archivoGFtoluca = open('sts\\toluca\\gf.csv')
	leerGFtoluca = archivoGFtoluca.read()
	numGFtoluca = len(leerGFtoluca)
	strnumGFtoluca = str(numGFtoluca)
	archivoGFtoluca.close()
	txtGFtoluca = fuentetxt.render(strnumGFtoluca,4,[255,255,255])

	archivoGCtoluca = open('sts\\toluca\\gc.csv')
	leerGCtoluca = archivoGCtoluca.read()
	numGCtoluca = len(leerGCtoluca)
	strnumGCtoluca = str(numGCtoluca)
	archivoGCtoluca.close()
	txtGCtoluca = fuentetxt.render(strnumGCtoluca,4,[255,255,255])

	archivoTitulosToluca = open('sts\\toluca\\t.csv')
	leerTitulosToluca = archivoTitulosToluca.read()
	numTitulosToluca = len(leerTitulosToluca)
	strnumTitulosToluca = str(numTitulosToluca)
	archivoTitulosToluca.close()
	txtTitulosToluca = fuentetxt.render(strnumTitulosToluca,4,[255,255,255])
	####mostrar texto####
	 #mostrar partidos ganados#
	pantalla.blit(txtPJtoluca, [75 ,254])

	 #mostrar partidos ganados#
	pantalla.blit(txtGtoluca, [155, 254])

	 #mostrar partidos empatados#
	pantalla.blit(txtEtoluca, [235, 254])

	 #mostrar partidos perdidos#
	pantalla.blit(txtPtoluca, [315, 254])

	 #mostrar goles a favor#
	pantalla.blit(txtGFtoluca, [395, 254])

	 #mostrar goles en contra#
	pantalla.blit(txtGCtoluca, [475, 254])

	 #mostrar titulos ganados#
	pantalla.blit(txtTitulosToluca, [550, 254])

#########PUMAS###########
	#Registros de estadísticas#
	archivoPJpumas = open('sts\\pumas\\pj.csv')
	leerPJpumas = archivoPJpumas.read()
	numPJpumas = len(leerPJpumas)
	strnumPJpumas = str(numPJpumas)
	archivoPJpumas.close()
	txtPJpumas = fuentetxt.render(strnumPJpumas,4,[255,255,255])

	archivoGpumas = open('sts\\pumas\\g.csv')
	leerGpumas = archivoGpumas.read()
	numGpumas = len(leerGpumas)
	strnumGpumas = str(numGpumas)
	archivoGpumas.close()
	txtGpumas = fuentetxt.render(strnumGpumas,4,[255,255,255])

	archivoEpumas = open('sts\\pumas\\e.csv')
	leerEpumas = archivoEpumas.read()
	numEpumas = len(leerEpumas)
	strnumEpumas = str(numEpumas)
	archivoEpumas.close()
	txtEpumas = fuentetxt.render(strnumEpumas,4,[255,255,255])

	archivoPpumas= open('sts\\pumas\\p.csv')
	leerPpumas= archivoPpumas.read()
	numPpumas = len(leerPpumas)
	strnumPpumas= str(numPpumas)
	archivoPpumas.close()
	txtPpumas = fuentetxt.render(strnumPpumas,4,[255,255,255])

	archivoGFpumas = open('sts\\pumas\\gf.csv')
	leerGFpumas = archivoGFpumas.read()
	numGFpumas = len(leerGFpumas)
	strnumGFpumas = str(numGFpumas)
	archivoGFpumas.close()
	txtGFpumas = fuentetxt.render(strnumGFpumas,4,[255,255,255])

	archivoGCpumas = open('sts\\pumas\\gc.csv')
	leerGCpumas = archivoGCpumas.read()
	numGCpumas = len(leerGCpumas)
	strnumGCpumas = str(numGCpumas)
	archivoGCpumas.close()
	txtGCpumas = fuentetxt.render(strnumGCpumas,4,[255,255,255])

	archivoTitulosPumas = open('sts\\pumas\\t.csv')
	leerTitulosPumas = archivoTitulosPumas.read()
	numTitulosPumas = len(leerTitulosPumas)
	strnumTitulosPumas = str(numTitulosPumas)
	archivoTitulosPumas.close()
	txtTitulosPumas = fuentetxt.render(strnumTitulosPumas,4,[255,255,255])
	####mostrar texto####
	 #mostrar partidos ganados#
	pantalla.blit(txtPJpumas, [75 ,306])

	 #mostrar partidos ganados#
	pantalla.blit(txtGpumas, [155, 306])

	 #mostrar partidos empatados#
	pantalla.blit(txtEpumas, [235, 306])

	 #mostrar partidos perdidos#
	pantalla.blit(txtPpumas, [315, 306])

	 #mostrar goles a favor#
	pantalla.blit(txtGFpumas, [395, 306])

	 #mostrar goles en contra#
	pantalla.blit(txtGCpumas, [475, 306])

	 #mostrar titulos ganados#
	pantalla.blit(txtTitulosPumas, [550, 306])

#########Monterrey###########
	#Registros de estadísticas#
	archivoPJmonterrey = open('sts\\monterrey\\pj.csv')
	leerPJmonterrey = archivoPJmonterrey.read()
	numPJmonterrey = len(leerPJmonterrey)
	strnumPJmonterrey = str(numPJmonterrey)
	archivoPJmonterrey.close()
	txtPJmonterrey = fuentetxt.render(strnumPJmonterrey,4,[255,255,255])

	archivoGmonterrey = open('sts\\monterrey\\g.csv')
	leerGmonterrey = archivoGmonterrey.read()
	numGmonterrey = len(leerGmonterrey)
	strnumGmonterrey = str(numGmonterrey)
	archivoGmonterrey.close()
	txtGmonterrey = fuentetxt.render(strnumGmonterrey,4,[255,255,255])

	archivoEmonterrey = open('sts\\monterrey\\e.csv')
	leerEmonterrey = archivoEmonterrey.read()
	numEmonterrey = len(leerEmonterrey)
	strnumEmonterrey = str(numEmonterrey)
	archivoEmonterrey.close()
	txtEmonterrey = fuentetxt.render(strnumEmonterrey,4,[255,255,255])

	archivoPmonterrey= open('sts\\monterrey\\p.csv')
	leerPmonterrey= archivoPmonterrey.read()
	numPmonterrey = len(leerPmonterrey)
	strnumPmonterrey= str(numPmonterrey)
	archivoPmonterrey.close()
	txtPmonterrey = fuentetxt.render(strnumPmonterrey,4,[255,255,255])

	archivoGFmonterrey = open('sts\\monterrey\\gf.csv')
	leerGFmonterrey = archivoGFmonterrey.read()
	numGFmonterrey = len(leerGFmonterrey)
	strnumGFmonterrey = str(numGFmonterrey)
	archivoGFmonterrey.close()
	txtGFmonterrey = fuentetxt.render(strnumGFmonterrey,4,[255,255,255])

	archivoGCmonterrey = open('sts\\monterrey\\gc.csv')
	leerGCmonterrey = archivoGCmonterrey.read()
	numGCmonterrey = len(leerGCmonterrey)
	strnumGCmonterrey = str(numGCmonterrey)
	archivoGCmonterrey.close()
	txtGCmonterrey = fuentetxt.render(strnumGCmonterrey,4,[255,255,255])

	archivoTitulosMonterrey = open('sts\\monterrey\\t.csv')
	leerTitulosMonterrey = archivoTitulosMonterrey.read()
	numTitulosMonterrey = len(leerTitulosMonterrey)
	strnumTitulosMonterrey = str(numTitulosMonterrey)
	archivoTitulosMonterrey.close()
	txtTitulosMonterrey = fuentetxt.render(strnumTitulosMonterrey,4,[255,255,255])
	####mostrar texto####
	 #mostrar partidos ganados#
	pantalla.blit(txtPJmonterrey, [75 ,358])

	 #mostrar partidos ganados#
	pantalla.blit(txtGmonterrey, [155, 358])

	 #mostrar partidos empatados#
	pantalla.blit(txtEmonterrey, [235, 358])

	 #mostrar partidos perdidos#
	pantalla.blit(txtPmonterrey, [315, 358])

	 #mostrar goles a favor#
	pantalla.blit(txtGFmonterrey, [395, 358])

	 #mostrar goles en contra#
	pantalla.blit(txtGCmonterrey, [475, 358])

	 #mostrar titulos ganados#
	pantalla.blit(txtTitulosMonterrey, [550, 358])

#########TIGRES###########
	#Registros de estadísticas#
	archivoPJtigres = open('sts\\tigres\\pj.csv')
	leerPJtigres = archivoPJtigres.read()
	numPJtigres = len(leerPJtigres)
	strnumPJtigres = str(numPJtigres)
	archivoPJtigres.close()
	txtPJtigres = fuentetxt.render(strnumPJtigres,4,[255,255,255])

	archivoGtigres = open('sts\\tigres\\g.csv')
	leerGtigres = archivoGtigres.read()
	numGtigres = len(leerGtigres)
	strnumGtigres = str(numGtigres)
	archivoGtigres.close()
	txtGtigres = fuentetxt.render(strnumGtigres,4,[255,255,255])

	archivoEtigres = open('sts\\tigres\\e.csv')
	leerEtigres = archivoEtigres.read()
	numEtigres = len(leerEtigres)
	strnumEtigres = str(numEtigres)
	archivoEtigres.close()
	txtEtigres = fuentetxt.render(strnumEtigres,4,[255,255,255])

	archivoPtigres= open('sts\\tigres\\p.csv')
	leerPtigres= archivoPtigres.read()
	numPtigres = len(leerPtigres)
	strnumPtigres= str(numPtigres)
	archivoPtigres.close()
	txtPtigres = fuentetxt.render(strnumPtigres,4,[255,255,255])

	archivoGFtigres = open('sts\\tigres\\gf.csv')
	leerGFtigres = archivoGFtigres.read()
	numGFtigres = len(leerGFtigres)
	strnumGFtigres = str(numGFtigres)
	archivoGFtigres.close()
	txtGFtigres = fuentetxt.render(strnumGFtigres,4,[255,255,255])

	archivoGCtigres = open('sts\\tigres\\gc.csv')
	leerGCtigres = archivoGCtigres.read()
	numGCtigres = len(leerGCtigres)
	strnumGCtigres = str(numGCtigres)
	archivoGCtigres.close()
	txtGCtigres = fuentetxt.render(strnumGCtigres,4,[255,255,255])

	archivoTitulosTigres = open('sts\\tigres\\t.csv')
	leerTitulosTigres = archivoTitulosTigres.read()
	numTitulosTigres = len(leerTitulosTigres)
	strnumTitulosTigres = str(numTitulosTigres)
	archivoTitulosTigres.close()
	txtTitulosTigres = fuentetxt.render(strnumTitulosTigres,4,[255,255,255])
	####mostrar texto####
	 #mostrar partidos ganados#
	pantalla.blit(txtPJtigres, [75 ,410])

	 #mostrar partidos ganados#
	pantalla.blit(txtGtigres, [155, 410])

	 #mostrar partidos empatados#
	pantalla.blit(txtEtigres, [235, 410])

	 #mostrar partidos perdidos#
	pantalla.blit(txtPtigres, [315, 410])

	 #mostrar goles a favor#
	pantalla.blit(txtGFtigres, [395, 410])

	 #mostrar goles en contra#
	pantalla.blit(txtGCtigres, [475, 410])

	 #mostrar titulos ganados#
	pantalla.blit(txtTitulosTigres, [550, 410])

#########CRUZ AZUL###########
	#Registros de estadísticas#
	archivoPJcruzazul = open('sts\\cruzazul\\pj.csv')
	leerPJcruzazul = archivoPJcruzazul.read()
	numPJcruzazul = len(leerPJcruzazul)
	strnumPJcruzazul = str(numPJcruzazul)
	archivoPJcruzazul.close()
	txtPJcruzazul = fuentetxt.render(strnumPJcruzazul,4,[255,255,255])

	archivoGcruzazul = open('sts\\cruzazul\\g.csv')
	leerGcruzazul = archivoGcruzazul.read()
	numGcruzazul = len(leerGcruzazul)
	strnumGcruzazul = str(numGcruzazul)
	archivoGcruzazul.close()
	txtGcruzazul = fuentetxt.render(strnumGcruzazul,4,[255,255,255])

	archivoEcruzazul = open('sts\\cruzazul\\e.csv')
	leerEcruzazul = archivoEcruzazul.read()
	numEcruzazul = len(leerEcruzazul)
	strnumEcruzazul = str(numEcruzazul)
	archivoEcruzazul.close()
	txtEcruzazul = fuentetxt.render(strnumEcruzazul,4,[255,255,255])

	archivoPcruzazul= open('sts\\cruzazul\\p.csv')
	leerPcruzazul= archivoPcruzazul.read()
	numPcruzazul = len(leerPcruzazul)
	strnumPcruzazul= str(numPcruzazul)
	archivoPcruzazul.close()
	txtPcruzazul = fuentetxt.render(strnumPcruzazul,4,[255,255,255])

	archivoGFcruzazul = open('sts\\cruzazul\\gf.csv')
	leerGFcruzazul = archivoGFcruzazul.read()
	numGFcruzazul = len(leerGFcruzazul)
	strnumGFcruzazul = str(numGFcruzazul)
	archivoGFcruzazul.close()
	txtGFcruzazul = fuentetxt.render(strnumGFcruzazul,4,[255,255,255])

	archivoGCcruzazul = open('sts\\cruzazul\\gc.csv')
	leerGCcruzazul = archivoGCcruzazul.read()
	numGCcruzazul = len(leerGCcruzazul)
	strnumGCcruzazul = str(numGCcruzazul)
	archivoGCcruzazul.close()
	txtGCcruzazul = fuentetxt.render(strnumGCcruzazul,4,[255,255,255])

	archivoTitulosCruzAzul = open('sts\\cruzazul\\t.csv')
	leerTitulosCruzAzul = archivoTitulosCruzAzul.read()
	numTitulosCruzAzul = len(leerTitulosCruzAzul)
	strnumTitulosCruzAzul = str(numTitulosCruzAzul)
	archivoTitulosCruzAzul.close()
	txtTitulosCruzAzul = fuentetxt.render(strnumTitulosCruzAzul,4,[255,255,255])
	####mostrar texto####
	 #mostrar partidos ganados#
	pantalla.blit(txtPJcruzazul, [75 ,462])

	 #mostrar partidos ganados#
	pantalla.blit(txtGcruzazul, [155, 462])

	 #mostrar partidos empatados#
	pantalla.blit(txtEcruzazul, [235, 462])

	 #mostrar partidos perdidos#
	pantalla.blit(txtPcruzazul, [315, 462])

	 #mostrar goles a favor#
	pantalla.blit(txtGFcruzazul, [395, 462])

	 #mostrar goles en contra#
	pantalla.blit(txtGCcruzazul, [475, 462])

	 #mostrar titulos ganados#
	pantalla.blit(txtTitulosCruzAzul, [550, 462])