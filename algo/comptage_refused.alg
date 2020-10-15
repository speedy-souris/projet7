<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="SI (question==&quot;bonjour&quot;) ALORS"/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2lignes="" F2defaut="" F2etat="inactif" F2para=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param epaisseurPoint="2" totalAffichages="1000" epaisseurLigne="2" arrondiAuto="vrai" maxBoucle="500000" totalBoucles="5000000" nbDecimales="8"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES">
        <item code="201#contenu2# " algoitem="FONCTION contenu2( )">
            <item code="202#declarationsvariablesfonction" algoitem="VARIABLES_FONCTION">
                <item code="1#NOMBRE#nb_contenu2" algoitem="nb_contenu2 EST_DU_TYPE NOMBRE"/>
            </item>
            <item code="203#debutfonction" algoitem="DEBUT_FONCTION"/>
            <item code="5#nb_contenu2#ALGOBOX_ALEA_ENT(1,3)#pasliste" algoitem="nb_contenu2 PREND_LA_VALEUR ALGOBOX_ALEA_ENT(1,3)"/>
            <item code="6#nb_contenu2==1" algoitem="SI (nb_contenu2==1) ALORS">
                <item code="7#debutsi" algoitem="DEBUT_SI"/>
                <item code="5#question#&quot;ma question ....&quot;#pasliste" algoitem="question PREND_LA_VALEUR &quot;ma question ....&quot;"/>
                <item code="8#finsi" algoitem="FIN_SI"/>
                <item code="9#sinon" algoitem="SINON">
                    <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                    <item code="6#nb_contenu2==2" algoitem="SI (nb_contenu2==2) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="5#question#&quot;je n'ai pas compris ... !&quot;#pasliste" algoitem="question PREND_LA_VALEUR &quot;je n'ai pas compris ... !&quot;"/>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                    </item>
                    <item code="6#nb_contenu2==3" algoitem="SI (nb_contenu2==3) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="5#question#&quot;vieux&quot;#pasliste" algoitem="question PREND_LA_VALEUR &quot;vieux&quot;"/>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                    </item>
                    <item code="11#finsinon" algoitem="FIN_SINON"/>
                </item>
            </item>
            <item code="205#question" algoitem="RENVOYER question"/>
            <item code="204#finfonction" algoitem="FIN_FONCTION"/>
        </item>
        <item code="201#contenu# " algoitem="FONCTION contenu( )">
            <item code="202#declarationsvariablesfonction" algoitem="VARIABLES_FONCTION">
                <item code="1#NOMBRE#nb_contenu" algoitem="nb_contenu EST_DU_TYPE NOMBRE"/>
            </item>
            <item code="203#debutfonction" algoitem="DEBUT_FONCTION"/>
            <item code="5#nb_contenu#ALGOBOX_ALEA_ENT(1,4)#pasliste" algoitem="nb_contenu PREND_LA_VALEUR ALGOBOX_ALEA_ENT(1,4)"/>
            <item code="6#nb_contenu==1" algoitem="SI (nb_contenu==1) ALORS">
                <item code="7#debutsi" algoitem="DEBUT_SI"/>
                <item code="5#question#&quot;bonjour&quot;#pasliste" algoitem="question PREND_LA_VALEUR &quot;bonjour&quot;"/>
                <item code="8#finsi" algoitem="FIN_SI"/>
                <item code="9#sinon" algoitem="SINON">
                    <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                    <item code="6#nb_contenu==2" algoitem="SI (nb_contenu==2) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="5#question#&quot;sss&quot;#pasliste" algoitem="question PREND_LA_VALEUR &quot;sss&quot;"/>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                    </item>
                    <item code="6#nb_contenu==3" algoitem="SI (nb_contenu==3) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="5#question#&quot;aaa&quot;#pasliste" algoitem="question PREND_LA_VALEUR &quot;aaa&quot;"/>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                    </item>
                    <item code="6#nb_contenu==4" algoitem="SI (nb_contenu==4) ALORS">
                        <item code="7#debutsi" algoitem="DEBUT_SI"/>
                        <item code="5#question#&quot;vieux&quot;#pasliste" algoitem="question PREND_LA_VALEUR &quot;vieux&quot;"/>
                        <item code="8#finsi" algoitem="FIN_SI"/>
                    </item>
                    <item code="11#finsinon" algoitem="FIN_SINON"/>
                </item>
            </item>
            <item code="205#question" algoitem="RENVOYER question"/>
            <item code="204#finfonction" algoitem="FIN_FONCTION"/>
        </item>
    </item>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#CHAINE#question" algoitem="question EST_DU_TYPE CHAINE"/>
        <item code="1#CHAINE#comprehension" algoitem="comprehension EST_DU_TYPE CHAINE"/>
        <item code="1#CHAINE#civility" algoitem="civility EST_DU_TYPE CHAINE"/>
        <item code="1#CHAINE#decency" algoitem="decency EST_DU_TYPE CHAINE"/>
        <item code="1#NOMBRE#nb_incivility" algoitem="nb_incivility EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#nb_indecency" algoitem="nb_indecency EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#nb_incomprehension" algoitem="nb_incomprehension EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#nb_request" algoitem="nb_request EST_DU_TYPE NOMBRE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="19#initialisation du comportement utililisateur" algoitem="//initialisation du comportement utililisateur"/>
        <item code="5#comprehension#&quot;faux&quot;#pasliste" algoitem="comprehension PREND_LA_VALEUR &quot;faux&quot;"/>
        <item code="5#civility#&quot;faux&quot;#pasliste" algoitem="civility PREND_LA_VALEUR &quot;faux&quot;"/>
        <item code="5#decency#&quot;faux&quot;#pasliste" algoitem="decency PREND_LA_VALEUR &quot;faux&quot;"/>
        <item code="19#initialisation compteur" algoitem="//initialisation compteur"/>
        <item code="5#nb_incivility#0#pasliste" algoitem="nb_incivility PREND_LA_VALEUR 0"/>
        <item code="5#nb_indecency#0#pasliste" algoitem="nb_indecency PREND_LA_VALEUR 0"/>
        <item code="5#nb_incomprehension#0#pasliste" algoitem="nb_incomprehension PREND_LA_VALEUR 0"/>
        <item code="5#nb_request#0#pasliste" algoitem="nb_request PREND_LA_VALEUR 0"/>
        <item code="19#Debut Programme" algoitem="//Debut Programme"/>
        <item code="15#nb_incivility&lt;3 ET nb_indecency&lt;3 ET nb_incomprehension&lt;3 ET question !=&quot;bonjour&quot;" algoitem="TANT_QUE (nb_incivility&lt;3 ET nb_indecency&lt;3 ET nb_incomprehension&lt;3 ET question !=&quot;bonjour&quot;) FAIRE">
            <item code="16#debuttantque" algoitem="DEBUT_TANT_QUE"/>
            <item code="4#Bonjour, que puis je pour toi  ... ?#1" algoitem="AFFICHER &quot;Bonjour, que puis je pour toi  ... ?&quot;"/>
            <item code="206#contenu()" algoitem="APPELER_FONCTION contenu()"/>
            <item code="3#question#1#pasliste" algoitem="AFFICHER question"/>
            <item code="17#fintantque" algoitem="FIN_TANT_QUE"/>
        </item>
        <item code="6#question==&quot;bonjour&quot;" algoitem="SI (question==&quot;bonjour&quot;) ALORS">
            <item code="7#debutsi" algoitem="DEBUT_SI"/>
            <item code="5#civility#&quot;vrai&quot;#pasliste" algoitem="civility PREND_LA_VALEUR &quot;vrai&quot;"/>
            <item code="5#comprehension#&quot;faux&quot;#pasliste" algoitem="comprehension PREND_LA_VALEUR &quot;faux&quot;"/>
            <item code="5#decency#&quot;faux&quot;#pasliste" algoitem="decency PREND_LA_VALEUR &quot;faux&quot;"/>
            <item code="5#nb_incivility#0#pasliste" algoitem="nb_incivility PREND_LA_VALEUR 0"/>
            <item code="5#nb_indecency#0#pasliste" algoitem="nb_indecency PREND_LA_VALEUR 0"/>
            <item code="5#nb_incomprehension#0#pasliste" algoitem="nb_incomprehension PREND_LA_VALEUR 0"/>
            <item code="5#nb_request#0#pasliste" algoitem="nb_request PREND_LA_VALEUR 0"/>
            <item code="103#commentaire" algoitem=""/>
            <item code="15#nb_indecency&lt;3 ET nb_incomprehension&lt;3 ET nb_request&lt;10" algoitem="TANT_QUE (nb_indecency&lt;3 ET nb_incomprehension&lt;3 ET nb_request&lt;10) FAIRE">
                <item code="16#debuttantque" algoitem="DEBUT_TANT_QUE"/>
                <item code="4#Pose ta question ... !#1" algoitem="AFFICHER &quot;Pose ta question ... !&quot;"/>
                <item code="206#contenu2()" algoitem="APPELER_FONCTION contenu2()"/>
                <item code="3#question#1#pasliste" algoitem="AFFICHER question"/>
                <item code="6#question==&quot;ma question ....&quot;" algoitem="SI (question==&quot;ma question ....&quot;) ALORS">
                    <item code="7#debutsi" algoitem="DEBUT_SI"/>
                    <item code="5#comprehension#&quot;vrai&quot;#pasliste" algoitem="comprehension PREND_LA_VALEUR &quot;vrai&quot;"/>
                    <item code="5#decency#&quot;vrai&quot;#pasliste" algoitem="decency PREND_LA_VALEUR &quot;vrai&quot;"/>
                    <item code="5#nb_request#nb_request+1#pasliste" algoitem="nb_request PREND_LA_VALEUR nb_request+1"/>
                    <item code="8#finsi" algoitem="FIN_SI"/>
                    <item code="9#sinon" algoitem="SINON">
                        <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                        <item code="6#question==&quot;vieux&quot;" algoitem="SI (question==&quot;vieux&quot;) ALORS">
                            <item code="7#debutsi" algoitem="DEBUT_SI"/>
                            <item code="5#nb_indecency#nb_indecency+1#pasliste" algoitem="nb_indecency PREND_LA_VALEUR nb_indecency+1"/>
                            <item code="4#tu es grossier ... !#1" algoitem="AFFICHER &quot;tu es grossier ... !&quot;"/>
                            <item code="5#comprehension#&quot;vrai&quot;#pasliste" algoitem="comprehension PREND_LA_VALEUR &quot;vrai&quot;"/>
                            <item code="5#decency#&quot;faux&quot;#pasliste" algoitem="decency PREND_LA_VALEUR &quot;faux&quot;"/>
                            <item code="8#finsi" algoitem="FIN_SI"/>
                        </item>
                        <item code="6#question==&quot;je n'ai pas compris ... !&quot;" algoitem="SI (question==&quot;je n'ai pas compris ... !&quot;) ALORS">
                            <item code="7#debutsi" algoitem="DEBUT_SI"/>
                            <item code="5#nb_incomprehension#nb_incomprehension+1#pasliste" algoitem="nb_incomprehension PREND_LA_VALEUR nb_incomprehension+1"/>
                            <item code="5#comprehension#&quot;faux&quot;#pasliste" algoitem="comprehension PREND_LA_VALEUR &quot;faux&quot;"/>
                            <item code="5#decency#&quot;faux&quot;#pasliste" algoitem="decency PREND_LA_VALEUR &quot;faux&quot;"/>
                            <item code="8#finsi" algoitem="FIN_SI"/>
                        </item>
                        <item code="11#finsinon" algoitem="FIN_SINON"/>
                    </item>
                </item>
                <item code="17#fintantque" algoitem="FIN_TANT_QUE"/>
            </item>
            <item code="8#finsi" algoitem="FIN_SI"/>
            <item code="9#sinon" algoitem="SINON">
                <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                <item code="6#question==&quot;vieux&quot;" algoitem="SI (question==&quot;vieux&quot;) ALORS">
                    <item code="7#debutsi" algoitem="DEBUT_SI"/>
                    <item code="5#nb_indecency#nb_indecency+1#pasliste" algoitem="nb_indecency PREND_LA_VALEUR nb_indecency+1"/>
                    <item code="4#tu es Grossier ... !#1" algoitem="AFFICHER &quot;tu es Grossier ... !&quot;"/>
                    <item code="5#comprehension#&quot;vrai&quot;#pasliste" algoitem="comprehension PREND_LA_VALEUR &quot;vrai&quot;"/>
                    <item code="8#finsi" algoitem="FIN_SI"/>
                </item>
                <item code="6#question==&quot;aaa&quot;" algoitem="SI (question==&quot;aaa&quot;) ALORS">
                    <item code="7#debutsi" algoitem="DEBUT_SI"/>
                    <item code="5#nb_incomprehension#nb_incomprehension+1#pasliste" algoitem="nb_incomprehension PREND_LA_VALEUR nb_incomprehension+1"/>
                    <item code="4#je ne comprend pas ... !#1" algoitem="AFFICHER &quot;je ne comprend pas ... !&quot;"/>
                    <item code="8#finsi" algoitem="FIN_SI"/>
                </item>
                <item code="6#question==&quot;sss&quot;" algoitem="SI (question==&quot;sss&quot;) ALORS">
                    <item code="7#debutsi" algoitem="DEBUT_SI"/>
                    <item code="5#nb_incivility#nb_incivility+1#pasliste" algoitem="nb_incivility PREND_LA_VALEUR nb_incivility+1"/>
                    <item code="4#tu es impoli ... !#1" algoitem="AFFICHER &quot;tu es impoli ... !&quot;"/>
                    <item code="8#finsi" algoitem="FIN_SI"/>
                </item>
                <item code="11#finsinon" algoitem="FIN_SINON"/>
            </item>
        </item>
        <item code="4#  #1" algoitem="AFFICHER &quot;  &quot;"/>
        <item code="4#nb_incivility ==> #0" algoitem="AFFICHER &quot;nb_incivility ==> &quot;"/>
        <item code="3#nb_incivility#1#pasliste" algoitem="AFFICHER nb_incivility"/>
        <item code="4#nb_indecency ==> #0" algoitem="AFFICHER &quot;nb_indecency ==> &quot;"/>
        <item code="3#nb_indecency#1#pasliste" algoitem="AFFICHER nb_indecency"/>
        <item code="4#nb_incomprehension ==> #0" algoitem="AFFICHER &quot;nb_incomprehension ==> &quot;"/>
        <item code="3#nb_incomprehension#1#pasliste" algoitem="AFFICHER nb_incomprehension"/>
        <item code="4#valeur de civility ==> #0" algoitem="AFFICHER &quot;valeur de civility ==> &quot;"/>
        <item code="3#civility#1#pasliste" algoitem="AFFICHER civility"/>
        <item code="4#nb_request ==> #0" algoitem="AFFICHER &quot;nb_request ==> &quot;"/>
        <item code="3#nb_request#1#pasliste" algoitem="AFFICHER nb_request"/>
        <item code="4# #1" algoitem="AFFICHER &quot; &quot;"/>
        <item code="6#nb_incivility==3" algoitem="SI (nb_incivility==3) ALORS">
            <item code="7#debutsi" algoitem="DEBUT_SI"/>
            <item code="4#je deteste toute cette impolitesse ... !#1" algoitem="AFFICHER &quot;je deteste toute cette impolitesse ... !&quot;"/>
            <item code="8#finsi" algoitem="FIN_SI"/>
            <item code="9#sinon" algoitem="SINON">
                <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                <item code="6#nb_indecency==3" algoitem="SI (nb_indecency==3) ALORS">
                    <item code="7#debutsi" algoitem="DEBUT_SI"/>
                    <item code="4#je deteste toute cette grossièreté ... !#1" algoitem="AFFICHER &quot;je deteste toute cette grossièreté ... !&quot;"/>
                    <item code="8#finsi" algoitem="FIN_SI"/>
                </item>
                <item code="6#nb_incomprehension==3" algoitem="SI (nb_incomprehension==3) ALORS">
                    <item code="7#debutsi" algoitem="DEBUT_SI"/>
                    <item code="4#je ne comprend plus rien dans le comprotement de la nouvelle génération ... !#1" algoitem="AFFICHER &quot;je ne comprend plus rien dans le comprotement de la nouvelle génération ... !&quot;"/>
                    <item code="8#finsi" algoitem="FIN_SI"/>
                </item>
                <item code="11#finsinon" algoitem="FIN_SINON"/>
            </item>
        </item>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
