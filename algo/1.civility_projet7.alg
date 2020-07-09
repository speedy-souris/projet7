<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="SI (accueil==donneeCivility) ALORS"/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2lignes="" F2etat="inactif" F2para="" F2defaut=""/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <param nbDecimales="8" epaisseurLigne="2" maxBoucle="500000" arrondiAuto="vrai" epaisseurPoint="2" totalBoucles="5000000" totalAffichages="1000"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#civility" algoitem="civility EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#donneeCivility" algoitem="donneeCivility EST_DU_TYPE CHAINE"/>
        <item code="1#NOMBRE#incivility" algoitem="incivility EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#accueil" algoitem="accueil EST_DU_TYPE CHAINE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="19#Initialisation des donnees" algoitem="//Initialisation des donnees"/>
        <item code="5#civility#0#pasliste" algoitem="civility PREND_LA_VALEUR 0"/>
        <item code="5#donneeCivility#&quot;bonjour&quot;#pasliste" algoitem="donneeCivility PREND_LA_VALEUR &quot;bonjour&quot;"/>
        <item code="5#incivility#0#pasliste" algoitem="incivility PREND_LA_VALEUR 0"/>
        <item code="19#Accueil Utilisateur" algoitem="//Accueil Utilisateur"/>
        <item code="4#Bonjour mon petit#1" algoitem="AFFICHER &quot;Bonjour mon petit&quot;"/>
        <item code="2#accueil#pasliste" algoitem="LIRE accueil"/>
        <item code="15#civility==0 ET incivility&lt;3" algoitem="TANT_QUE (civility==0 ET incivility&lt;3) FAIRE">
            <item code="16#debuttantque" algoitem="DEBUT_TANT_QUE"/>
            <item code="6#accueil==donneeCivility" algoitem="SI (accueil==donneeCivility) ALORS">
                <item code="7#debutsi" algoitem="DEBUT_SI"/>
                <item code="5#civility#1#pasliste" algoitem="civility PREND_LA_VALEUR 1"/>
                <item code="8#finsi" algoitem="FIN_SI"/>
                <item code="9#sinon" algoitem="SINON">
                    <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                    <item code="6#incivility&lt;=3" algoitem="SI (incivility&lt;=3) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="4#Tu es impoli#1" algoitem="AFFICHER &quot;Tu es impoli&quot;"/>
                        <item code="5#incivility#incivility+1#pasliste" algoitem="incivility PREND_LA_VALEUR incivility+1"/>
                        <item code="2#accueil#pasliste" algoitem="LIRE accueil"/>
                        <item code="6#accueil==donneeCivility" algoitem="SI (accueil==donneeCivility) ALORS">
                            <item code="7#debutsi" algoitem="DEBUT_SI"/>
                            <item code="5#civility#1#pasliste" algoitem="civility PREND_LA_VALEUR 1"/>
                            <item code="8#finsi" algoitem="FIN_SI"/>
                        </item>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                    </item>
                    <item code="11#finsinon" algoitem="FIN_SINON"/>
                </item>
            </item>
            <item code="17#fintantque" algoitem="FIN_TANT_QUE"/>
        </item>
        <item code="6#civility!=1" algoitem="SI (civility!=1) ALORS">
            <item code="7#debutsi" algoitem="DEBUT_SI"/>
            <item code="4#cette impolitesse me fatigue...#1" algoitem="AFFICHER &quot;cette impolitesse me fatigue...&quot;"/>
            <item code="4#ATTENTE 24H00 (Repos Grandpy)#1" algoitem="AFFICHER &quot;ATTENTE 24H00 (Repos Grandpy)&quot;"/>
            <item code="8#finsi" algoitem="FIN_SI"/>
            <item code="9#sinon" algoitem="SINON">
                <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                <item code="4#Pose ta question !#1" algoitem="AFFICHER &quot;Pose ta question !&quot;"/>
                <item code="11#finsinon" algoitem="FIN_SINON"/>
            </item>
        </item>
        <item code="19#demande utilisateur" algoitem="//demande utilisateur"/>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
