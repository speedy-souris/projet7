<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="SI (decency==0) ALORS"/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2para="" F2etat="inactif" F2defaut="" F2lignes=""/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <param arrondiAuto="vrai" totalBoucles="5000000" totalAffichages="1000" maxBoucle="500000" nbDecimales="8" epaisseurPoint="2" epaisseurLigne="2"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#CHAINE#question" algoitem="question EST_DU_TYPE CHAINE"/>
        <item code="1#NOMBRE#decency" algoitem="decency EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#indecency" algoitem="indecency EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#donneeIndecency" algoitem="donneeIndecency EST_DU_TYPE CHAINE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="19#Initialisation des donnees" algoitem="//Initialisation des donnees"/>
        <item code="5#decency#0#pasliste" algoitem="decency PREND_LA_VALEUR 0"/>
        <item code="5#donneeIndecency#&quot;ancetre&quot;#pasliste" algoitem="donneeIndecency PREND_LA_VALEUR &quot;ancetre&quot;"/>
        <item code="5#indecency#0#pasliste" algoitem="indecency PREND_LA_VALEUR 0"/>
        <item code="19#demande  Utilisateur" algoitem="//demande  Utilisateur"/>
        <item code="2#question#pasliste" algoitem="LIRE question"/>
        <item code="15#decency==0 ET indecency&lt;3" algoitem="TANT_QUE (decency==0 ET indecency&lt;3) FAIRE">
            <item code="16#debuttantque" algoitem="DEBUT_TANT_QUE"/>
            <item code="6#question!=donneeIndecency" algoitem="SI (question!=donneeIndecency) ALORS">
                <item code="7#debutsi" algoitem="DEBUT_SI"/>
                <item code="5#decency#1#pasliste" algoitem="decency PREND_LA_VALEUR 1"/>
                <item code="8#finsi" algoitem="FIN_SI"/>
                <item code="9#sinon" algoitem="SINON">
                    <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                    <item code="6#indecency&lt;=3" algoitem="SI (indecency&lt;=3) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="4#Tu n'es pas courtois#1" algoitem="AFFICHER &quot;Tu n'es pas courtois&quot;"/>
                        <item code="5#indecency#indecency+1#pasliste" algoitem="indecency PREND_LA_VALEUR indecency+1"/>
                        <item code="2#question#pasliste" algoitem="LIRE question"/>
                        <item code="6#question!=donneeIndecency" algoitem="SI (question!=donneeIndecency) ALORS">
                            <item code="7#debutsi" algoitem="DEBUT_SI"/>
                            <item code="5#decency#1#pasliste" algoitem="decency PREND_LA_VALEUR 1"/>
                            <item code="8#finsi" algoitem="FIN_SI"/>
                        </item>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                    </item>
                    <item code="11#finsinon" algoitem="FIN_SINON"/>
                </item>
            </item>
            <item code="17#fintantque" algoitem="FIN_TANT_QUE"/>
        </item>
        <item code="6#decency==0" algoitem="SI (decency==0) ALORS">
            <item code="7#debutsi" algoitem="DEBUT_SI"/>
            <item code="4#Ce manque de courtoisie me FATIGUE...#1" algoitem="AFFICHER &quot;Ce manque de courtoisie me FATIGUE...&quot;"/>
            <item code="8#finsi" algoitem="FIN_SI"/>
            <item code="9#sinon" algoitem="SINON">
                <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                <item code="4#Que veux tu savoir ?#1" algoitem="AFFICHER &quot;Que veux tu savoir ?&quot;"/>
                <item code="11#finsinon" algoitem="FIN_SINON"/>
            </item>
        </item>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
