<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2lignes="" F2para="" F2etat="inactif" F2defaut=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param arrondiAuto="vrai" totalBoucles="5000000" nbDecimales="8" totalAffichages="1000" epaisseurLigne="2" maxBoucle="500000" epaisseurPoint="2"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES">
        <item code="201#afficheFatigue# " algoitem="FONCTION afficheFatigue( )">
            <item code="202#declarationsvariablesfonction" algoitem="VARIABLES_FONCTION"/>
            <item code="203#debutfonction" algoitem="DEBUT_FONCTION"/>
            <item code="4#Je suis bien fatigué !#1" algoitem="AFFICHER &quot;Je suis bien fatigué !&quot;"/>
            <item code="4#repasse me voir demain !#1" algoitem="AFFICHER &quot;repasse me voir demain !&quot;"/>
            <item code="204#finfonction" algoitem="FIN_FONCTION"/>
        </item>
    </item>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#CHAINE#question" algoitem="question EST_DU_TYPE CHAINE"/>
        <item code="1#NOMBRE#civility" algoitem="civility EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#donneeCivility" algoitem="donneeCivility EST_DU_TYPE CHAINE"/>
        <item code="1#NOMBRE#incivility" algoitem="incivility EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#quotas" algoitem="quotas EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#nbrQuestion" algoitem="nbrQuestion EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#accueil" algoitem="accueil EST_DU_TYPE CHAINE"/>
        <item code="1#NOMBRE#decency" algoitem="decency EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#indecency" algoitem="indecency EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#answer" algoitem="answer EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#donneeIndecency" algoitem="donneeIndecency EST_DU_TYPE CHAINE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="19#Initialisation des donnees" algoitem="//Initialisation des donnees"/>
        <item code="5#civility#0#pasliste" algoitem="civility PREND_LA_VALEUR 0"/>
        <item code="5#donneeCivility#&quot;bonjour&quot;#pasliste" algoitem="donneeCivility PREND_LA_VALEUR &quot;bonjour&quot;"/>
        <item code="5#incivility#0#pasliste" algoitem="incivility PREND_LA_VALEUR 0"/>
        <item code="5#quotas#0#pasliste" algoitem="quotas PREND_LA_VALEUR 0"/>
        <item code="5#nbrQuestion#0#pasliste" algoitem="nbrQuestion PREND_LA_VALEUR 0"/>
        <item code="5#decency#0#pasliste" algoitem="decency PREND_LA_VALEUR 0"/>
        <item code="5#donneeIndecency#&quot;ancetre&quot;#pasliste" algoitem="donneeIndecency PREND_LA_VALEUR &quot;ancetre&quot;"/>
        <item code="5#indecency#0#pasliste" algoitem="indecency PREND_LA_VALEUR 0"/>
        <item code="5#answer#0#pasliste" algoitem="answer PREND_LA_VALEUR 0"/>
        <item code="103#commentaire" algoitem=""/>
        <item code="19#Accueil Utilisateur" algoitem="//Accueil Utilisateur"/>
        <item code="19#Attente de cicivilité (politesse==> bonjour)" algoitem="//Attente de cicivilité (politesse==> bonjour)"/>
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
        <item code="103#commentaire" algoitem=""/>
        <item code="19#Impolitesse (utilisateur ==> ne dit pas bonjour)" algoitem="//Impolitesse (utilisateur ==> ne dit pas bonjour)"/>
        <item code="6#civility==0" algoitem="SI (civility==0) ALORS">
            <item code="7#debutsi" algoitem="DEBUT_SI"/>
            <item code="4#Cette impolitesse me FATIGUE...#1" algoitem="AFFICHER &quot;Cette impolitesse me FATIGUE...&quot;"/>
            <item code="206#afficheFatigue()" algoitem="APPELER_FONCTION afficheFatigue()"/>
            <item code="8#finsi" algoitem="FIN_SI"/>
            <item code="9#sinon" algoitem="SINON">
                <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                <item code="103#commentaire" algoitem=""/>
                <item code="19#demande utilisateur (politesse de l'utilisateur ==> a dit bonjour)" algoitem="//demande utilisateur (politesse de l'utilisateur ==> a dit bonjour)"/>
                <item code="15#quotas==0" algoitem="TANT_QUE (quotas==0) FAIRE">
                    <item code="16#debuttantque" algoitem="DEBUT_TANT_QUE"/>
                    <item code="5#nbrQuestion#nbrQuestion+1#pasliste" algoitem="nbrQuestion PREND_LA_VALEUR nbrQuestion+1"/>
                    <item code="5#answer#1#pasliste" algoitem="answer PREND_LA_VALEUR 1"/>
                    <item code="4#Que veux tu savoir ?#1" algoitem="AFFICHER &quot;Que veux tu savoir ?&quot;"/>
                    <item code="2#question#pasliste" algoitem="LIRE question"/>
                    <item code="103#commentaire" algoitem=""/>
                    <item code="19#Quotas dépassé (Fatigue extreme  ==> épuisement de Grandpy)" algoitem="//Quotas dépassé (Fatigue extreme  ==> épuisement de Grandpy)"/>
                    <item code="6#nbrQuestion>=10" algoitem="SI (nbrQuestion>=10) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="5#quotas#1#pasliste" algoitem="quotas PREND_LA_VALEUR 1"/>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                    </item>
                    <item code="103#commentaire" algoitem=""/>
                    <item code="19#Fatigue légére de Grandpy" algoitem="//Fatigue légére de Grandpy"/>
                    <item code="6#nbrQuestion==5" algoitem="SI (nbrQuestion==5) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="4#Houla ma mémoire n'est plus ce qu'elle était#1" algoitem="AFFICHER &quot;Houla ma mémoire n'est plus ce qu'elle était&quot;"/>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                    </item>
                    <item code="103#commentaire" algoitem=""/>
                    <item code="19#utilisateur grossier" algoitem="//utilisateur grossier"/>
                    <item code="6#question!=donneeIndecency" algoitem="SI (question!=donneeIndecency) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="5#decency#1#pasliste" algoitem="decency PREND_LA_VALEUR 1"/>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                        <item code="9#sinon" algoitem="SINON">
                            <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                            <item code="6#indecency&lt;=3" algoitem="SI (indecency&lt;=3) ALORS">
                                <item code="7#debutsi" algoitem="DEBUT_SI"/>
                                <item code="4#Tu n'es pas courtois ... !#1" algoitem="AFFICHER &quot;Tu n'es pas courtois ... !&quot;"/>
                                <item code="5#answer#0#pasliste" algoitem="answer PREND_LA_VALEUR 0"/>
                                <item code="5#decency#0#pasliste" algoitem="decency PREND_LA_VALEUR 0"/>
                                <item code="5#indecency#indecency+1#pasliste" algoitem="indecency PREND_LA_VALEUR indecency+1"/>
                                <item code="5#nbrQuestion#nbrQuestion-1#pasliste" algoitem="nbrQuestion PREND_LA_VALEUR nbrQuestion-1"/>
                                <item code="6#nbrQuestion&lt;0" algoitem="SI (nbrQuestion&lt;0) ALORS">
                                    <item code="7#debutsi" algoitem="DEBUT_SI"/>
                                    <item code="5#nbrQuestion#0#pasliste" algoitem="nbrQuestion PREND_LA_VALEUR 0"/>
                                    <item code="8#finsi" algoitem="FIN_SI"/>
                                </item>
                                <item code="8#finsi" algoitem="FIN_SI"/>
                            </item>
                            <item code="11#finsinon" algoitem="FIN_SINON"/>
                        </item>
                    </item>
                    <item code="103#commentaire" algoitem=""/>
                    <item code="19#Réponse de GrandPy" algoitem="//Réponse de GrandPy"/>
                    <item code="6#indecency>=3" algoitem="SI (indecency>=3) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="4#Ce manque de courtoisie me FATIGUE ... !#1" algoitem="AFFICHER &quot;Ce manque de courtoisie me FATIGUE ... !&quot;"/>
                        <item code="5#quotas#1#pasliste" algoitem="quotas PREND_LA_VALEUR 1"/>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                        <item code="9#sinon" algoitem="SINON">
                            <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                            <item code="6#answer==1" algoitem="SI (answer==1) ALORS">
                                <item code="7#debutsi" algoitem="DEBUT_SI"/>
                                <item code="4#Voici ta réponse#1" algoitem="AFFICHER &quot;Voici ta réponse&quot;"/>
                                <item code="8#finsi" algoitem="FIN_SI"/>
                            </item>
                            <item code="11#finsinon" algoitem="FIN_SINON"/>
                        </item>
                    </item>
                    <item code="103#commentaire" algoitem=""/>
                    <item code="17#fintantque" algoitem="FIN_TANT_QUE"/>
                </item>
                <item code="103#commentaire" algoitem=""/>
                <item code="206#afficheFatigue()" algoitem="APPELER_FONCTION afficheFatigue()"/>
                <item code="11#finsinon" algoitem="FIN_SINON"/>
            </item>
        </item>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
