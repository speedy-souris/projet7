<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="SI (civility==0) ALORS"/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2defaut="" F2etat="inactif" F2para="" F2lignes=""/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <param epaisseurLigne="2" nbDecimales="8" arrondiAuto="vrai" maxBoucle="500000" epaisseurPoint="2" totalAffichages="1000" totalBoucles="5000000"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions">
        <item algoitem="FONCTION afficheFatigue( )" code="201#afficheFatigue# ">
            <item algoitem="VARIABLES_FONCTION" code="202#declarationsvariablesfonction"/>
            <item algoitem="DEBUT_FONCTION" code="203#debutfonction"/>
            <item algoitem="AFFICHER &quot;Je suis bien fatigué !&quot;" code="4#Je suis bien fatigué !#1"/>
            <item algoitem="AFFICHER &quot;repasse me voir demain !&quot;" code="4#repasse me voir demain !#1"/>
            <item algoitem="FIN_FONCTION" code="204#finfonction"/>
        </item>
    </item>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="question EST_DU_TYPE CHAINE" code="1#CHAINE#question"/>
        <item algoitem="civility EST_DU_TYPE NOMBRE" code="1#NOMBRE#civility"/>
        <item algoitem="donneeCivility EST_DU_TYPE CHAINE" code="1#CHAINE#donneeCivility"/>
        <item algoitem="incivility EST_DU_TYPE NOMBRE" code="1#NOMBRE#incivility"/>
        <item algoitem="quotas EST_DU_TYPE NOMBRE" code="1#NOMBRE#quotas"/>
        <item algoitem="nbrQuestion EST_DU_TYPE NOMBRE" code="1#NOMBRE#nbrQuestion"/>
        <item algoitem="accueil EST_DU_TYPE CHAINE" code="1#CHAINE#accueil"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="//Initialisation des donnees" code="19#Initialisation des donnees"/>
        <item algoitem="civility PREND_LA_VALEUR 0" code="5#civility#0#pasliste"/>
        <item algoitem="donneeCivility PREND_LA_VALEUR &quot;bonjour&quot;" code="5#donneeCivility#&quot;bonjour&quot;#pasliste"/>
        <item algoitem="incivility PREND_LA_VALEUR 0" code="5#incivility#0#pasliste"/>
        <item algoitem="quotas PREND_LA_VALEUR 0" code="5#quotas#0#pasliste"/>
        <item algoitem="nbrQuestion PREND_LA_VALEUR 0" code="5#nbrQuestion#0#pasliste"/>
        <item algoitem="" code="103#commentaire"/>
        <item algoitem="//Accueil Utilisateur" code="19#Accueil Utilisateur"/>
        <item algoitem="//Attente de cicivilité (politesse==> bonjour)" code="19#Attente de cicivilité (politesse==> bonjour)"/>
        <item algoitem="AFFICHER &quot;Bonjour mon petit&quot;" code="4#Bonjour mon petit#1"/>
        <item algoitem="LIRE accueil" code="2#accueil#pasliste"/>
        <item algoitem="TANT_QUE (civility==0 ET incivility&lt;3) FAIRE" code="15#civility==0 ET incivility&lt;3">
            <item algoitem="DEBUT_TANT_QUE" code="16#debuttantque"/>
            <item algoitem="SI (accueil==donneeCivility) ALORS" code="6#accueil==donneeCivility">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="civility PREND_LA_VALEUR 1" code="5#civility#1#pasliste"/>
                <item algoitem="FIN_SI" code="8#finsi"/>
                <item algoitem="SINON" code="9#sinon">
                    <item algoitem="DEBUT_SINON" code="10#debutsinon"/>
                    <item algoitem="SI (incivility&lt;=3) ALORS" code="6#incivility&lt;=3">
                        <item algoitem="DEBUT_SI" code="7#debutsi"/>
                        <item algoitem="AFFICHER &quot;Tu es impoli&quot;" code="4#Tu es impoli#1"/>
                        <item algoitem="incivility PREND_LA_VALEUR incivility+1" code="5#incivility#incivility+1#pasliste"/>
                        <item algoitem="LIRE accueil" code="2#accueil#pasliste"/>
                        <item algoitem="SI (accueil==donneeCivility) ALORS" code="6#accueil==donneeCivility">
                            <item algoitem="DEBUT_SI" code="7#debutsi"/>
                            <item algoitem="civility PREND_LA_VALEUR 1" code="5#civility#1#pasliste"/>
                            <item algoitem="FIN_SI" code="8#finsi"/>
                        </item>
                        <item algoitem="FIN_SI" code="8#finsi"/>
                    </item>
                    <item algoitem="FIN_SINON" code="11#finsinon"/>
                </item>
            </item>
            <item algoitem="FIN_TANT_QUE" code="17#fintantque"/>
        </item>
        <item algoitem="" code="103#commentaire"/>
        <item algoitem="//Impolitesse (utilisateur ==> ne dit pas bonjour)" code="19#Impolitesse (utilisateur ==> ne dit pas bonjour)"/>
        <item algoitem="SI (civility==0) ALORS" code="6#civility==0">
            <item algoitem="DEBUT_SI" code="7#debutsi"/>
            <item algoitem="AFFICHER &quot;Cette impolitesse me FATIGUE...&quot;" code="4#Cette impolitesse me FATIGUE...#1"/>
            <item algoitem="APPELER_FONCTION afficheFatigue()" code="206#afficheFatigue()"/>
            <item algoitem="FIN_SI" code="8#finsi"/>
            <item algoitem="SINON" code="9#sinon">
                <item algoitem="DEBUT_SINON" code="10#debutsinon"/>
                <item algoitem="" code="103#commentaire"/>
                <item algoitem="//demande utilisateur (politesse de l'utilisateur ==> a dit bonjour)" code="19#demande utilisateur (politesse de l'utilisateur ==> a dit bonjour)"/>
                <item algoitem="TANT_QUE (quotas==0) FAIRE" code="15#quotas==0">
                    <item algoitem="DEBUT_TANT_QUE" code="16#debuttantque"/>
                    <item algoitem="nbrQuestion PREND_LA_VALEUR nbrQuestion+1" code="5#nbrQuestion#nbrQuestion+1#pasliste"/>
                    <item algoitem="AFFICHER &quot;Que veux tu savoir ?&quot;" code="4#Que veux tu savoir ?#1"/>
                    <item algoitem="LIRE question" code="2#question#pasliste"/>
                    <item algoitem="" code="103#commentaire"/>
                    <item algoitem="//Quotas dépassé (Fatigue extreme  ==> épuisement de Grandpy)" code="19#Quotas dépassé (Fatigue extreme  ==> épuisement de Grandpy)"/>
                    <item algoitem="SI (nbrQuestion>=10) ALORS" code="6#nbrQuestion>=10">
                        <item algoitem="DEBUT_SI" code="7#debutsi"/>
                        <item algoitem="quotas PREND_LA_VALEUR 1" code="5#quotas#1#pasliste"/>
                        <item algoitem="FIN_SI" code="8#finsi"/>
                    </item>
                    <item algoitem="" code="103#commentaire"/>
                    <item algoitem="//Fatigue légére de Grandpy" code="19#Fatigue légére de Grandpy"/>
                    <item algoitem="SI (nbrQuestion==5) ALORS" code="6#nbrQuestion==5">
                        <item algoitem="DEBUT_SI" code="7#debutsi"/>
                        <item algoitem="AFFICHER &quot;Houla ma mémoire n'est plus ce qu'elle était&quot;" code="4#Houla ma mémoire n'est plus ce qu'elle était#1"/>
                        <item algoitem="FIN_SI" code="8#finsi"/>
                    </item>
                    <item algoitem="" code="103#commentaire"/>
                    <item algoitem="//Réponse de GrandPy" code="19#Réponse de GrandPy"/>
                    <item algoitem="AFFICHER &quot;Voici ta réponse&quot;" code="4#Voici ta réponse#1"/>
                    <item algoitem="FIN_TANT_QUE" code="17#fintantque"/>
                </item>
                <item algoitem="" code="103#commentaire"/>
                <item algoitem="APPELER_FONCTION afficheFatigue()" code="206#afficheFatigue()"/>
                <item algoitem="FIN_SINON" code="11#finsinon"/>
            </item>
        </item>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
