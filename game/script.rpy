init offset = 490

label splashscreen:
    scene black onlayer master
    with Pause(0.5)

    show splash1 onlayer master
    with fade
    with Pause(2.0)

    show splash2 onlayer master
    with fade
    with Pause(2.0)

    show splash3 onlayer master
    with fade
    with Pause(2.0)

    show splash4 onlayer master
    with fade
    with Pause(2.0)

    show splash5 onlayer master
    with fade
    with Pause(2.0)

    scene black onlayer master
    with fade

    return

init -990 screen credits:
    tag menu

    window:
        style "gm_root"

    frame:
        style "menu_frame"
        xmargin 10
        ymargin 10
        has side "t c r b"

        label _("\"VENTI MESI\"") bottom_margin 10
        viewport id "vp":
            mousewheel True
            has vbox spacing 10

            text _("Una visual novel di We Are Müesli (Claudia Molinari e Matteo Pozzi)\ncon la collaborazione di Francesco Fontana")
            text "www.wearemuesli.it"
            text " "
            text _("Realizzata con il contributo di Coop Lombardia")
            text _("in occasione del progetto della Città di Sesto San Giovanni \"Oggi, 25 aprile 1945\"")
            text _("(un'iniziativa in collaborazione con Associazione Ventimila Leghe, con il contributo di Fondazione Cariplo, consulenza scientifica di Fondazione ISEC, patrocinio di Regione Lombardia)")
            text _("Un ringraziamento speciale all'Assessora alla Cultura Rita Innocenti e al suo staff")
            text " "
            text _("Colonna sonora originale: Francesco Fontana")
            text _("Voce narrante: Germano Lanzoni")
            text _("I testi recitati sono tratti da \"Il dizionario del partigiano anonimo\" (\"Storie della Resistenza\", Sellerio editore Palermo, 2013) e da \"Eravamo come voi - Storie di ragazzi che scelsero di resistere\" di Marco Rovelli (Editori Laterza, 2015)")
            text _("Effetti sonori: www.freesound.org")
            text " "
            text _("Dedicato alle nostre famiglie, in particolare a nonna Lina, nonno Mario, papà Benito")
            text _("Grazie anche a: Marco Besana, Ilaria Brusadelli, Mattia Carattello, Fabio Cereda, Gianni Cetera, Giorgio De Vecchi, Dolmen Studio, Lodovico Gualzetti, Martino Iniziato, Llaura Mcgee, Franco Pozzi, Marco Rovelli")
            text " "
            text _("Bibliografia:")
            text "- Ornello Bizzarri - \"Medico per forza - Taccuino di prigionia\", Guerra Edizioni, 1996"
            text "- Fabio Cereda e Giorgio De Vecchi - \"Sesto San Giovanni 1943-1945 - Scenari della Liberazione\", Giorgio Tarantola Editore, 2015"
            text "- Beppe Fenoglio - \"Una questione privata\", Einaudi, 1986"
            text "- Biancamaria Magini - \"Sesto... Ieri\", Giorgio Tarantola Editore, 2014"
            text "- www.anpi.it"
            text "- www.comune.cinisello-balsamo.mi.it"
            text "- www.sestosg.net"
            text " "
            text "Made with Ren'Py, 2015"
            text "www.renpy.org"

        vbar value YScrollValue("vp")
        textbutton "INDIETRO":
            action Return()
            top_margin 10


init -490 python:
    config.rollback_enabled = False

init -490:


    $ coc = 0


    $ calcio = True


    $ luce = False
    $ topic1 = False
    $ topic2 = False


    $ bad1 = False
    $ bad2 = False
    $ bad3 = False
    $ badcounter = 0
    $ isBurning = False


    $ levi = False
    $ styron = False


    $ verocounter = 0

    $ vite = 3


    $ ScioperoSi = False
    $ ScioperoNo = False


    $ rightcount = 0
    $ right1 = False
    $ right2 = False
    $ right3 = False
    $ right4 = False
    $ right5 = False
    $ right6 = False
    $ right7 = False
    $ right8 = False


    $ maiale = False
    $ galline = False
    $ cachi = False
    $ giacomo = False
    $ generosa = False
    $ operosa = False


    $ love = False


    $ bencounter = 0
    $ marcounter = 0


    $ ardentissima = False
    $ infaticabile = False
    $ fede = False
    $ camerati = False
    $ fascismo = False
    $ riscossa = False


    $ lettera1 = False
    $ lettera2 = False
    $ lettera3 = False
    $ lettera4 = False
    $ lettera1good = False
    $ lettera2good = False
    $ lettera3good = False
    $ lettera4good = False
    $ lettera5good = False
    $ lcountgood = 0


    $ s20casa = False
    $ s20ordini = False
    $ s20boh = False
    $ s19good = False
    $ s19bad = False
    $ s17good = False
    $ s17bad = False
    $ s16god = False
    $ s16man = False
    $ s2prisongood = False
    $ s2prisonbad = False
    $ s2torture = False
    $ s14sciopero = False
    $ s14nosciopero = False
    $ s15good = False
    $ s15bad = False
    $ s12good = False
    $ s12bad = False
    $ s11good = False
    $ s11bad = False
    $ s9fratello = False
    $ s9compagno = False
    $ s13bacio = False
    $ s13nobacio = False
    $ s7benitodead = False
    $ s7martadead = False
    $ s6good = False
    $ s6bad = False
    $ s3good = False
    $ s3bad = False



image splash1 = "images/intro/CREDITS-01.png"
image splash2 = "images/intro/CREDITS-02.png"
image splash3 = "images/intro/CREDITS-03.png"
image splash4 = "images/intro/CREDITS-04.png"
image splash5 = "images/intro/CREDITS-05.png"


image n20 = "images/00_RN/RN-20.png"
image n19 = "images/00_RN/RN-19.png"
image n18 = "images/00_RN/RN-18.png"
image n17 = "images/00_RN/RN-17.png"
image n16 = "images/00_RN/RN-16.png"
image n15 = "images/00_RN/RN-15.png"
image n14 = "images/00_RN/RN-14.png"
image n13 = "images/00_RN/RN-13.png"
image n12 = "images/00_RN/RN-12.png"
image n11 = "images/00_RN/RN-11.png"
image n10 = "images/00_RN/RN-10.png"
image n09 = "images/00_RN/RN-09.png"
image n08 = "images/00_RN/RN-08.png"
image n07 = "images/00_RN/RN-07.png"
image n06 = "images/00_RN/RN-06.png"
image n05 = "images/00_RN/RN-05.png"
image n04 = "images/00_RN/RN-04.png"
image n03 = "images/00_RN/RN-03.png"
image n02 = "images/00_RN/RN-02.png"
image n01 = "images/00_RN/RN-01.png"


image c20 = "images/00_CARTELLI/CARTELLI-20.png"
image c19 = "images/00_CARTELLI/CARTELLI-19.png"
image c18 = "images/00_CARTELLI/CARTELLI-18.png"
image c17 = "images/00_CARTELLI/CARTELLI-17.png"
image c16 = "images/00_CARTELLI/CARTELLI-16.png"
image c15 = "images/00_CARTELLI/CARTELLI-15.png"
image c14 = "images/00_CARTELLI/CARTELLI-14.png"
image c13 = "images/00_CARTELLI/CARTELLI-13.png"
image c12 = "images/00_CARTELLI/CARTELLI-12.png"
image c11 = "images/00_CARTELLI/CARTELLI-11.png"
image c10 = "images/00_CARTELLI/CARTELLI-10.png"
image c09 = "images/00_CARTELLI/CARTELLI-09.png"
image c08 = "images/00_CARTELLI/CARTELLI-08.png"
image c07 = "images/00_CARTELLI/CARTELLI-07.png"
image c06 = "images/00_CARTELLI/CARTELLI-06.png"
image c05 = "images/00_CARTELLI/CARTELLI-05.png"
image c04 = "images/00_CARTELLI/CARTELLI-04.png"
image c03 = "images/00_CARTELLI/CARTELLI-03.png"
image c02 = "images/00_CARTELLI/CARTELLI-02.png"
image c01 = "images/00_CARTELLI/CARTELLI-01.png"
image c00 = "images/00_CARTELLI/CARTELLI-00.png"

image credits1 = "images/END CREDITS/END_CREDITS-01.png"
image credits2 = "images/END CREDITS/END_CREDITS-02.png"
image credits3 = "images/END CREDITS/END_CREDITS-03.png"
image credits4 = "images/END CREDITS/END_CREDITS-04.png"
image credits5 = "images/END CREDITS/END_CREDITS-05.png"
image credits6 = "images/END CREDITS/END_CREDITS-06.png"
image credits7 = "images/END CREDITS/END_CREDITS-07.png"
image credits8 = "images/END CREDITS/END_CREDITS-08.png"
image credits9 = "images/END CREDITS/END_CREDITS-09.png"
image credits10 = "images/END CREDITS/END_CREDITS-10.png"
image credits11 = "images/END CREDITS/END_CREDITS-11.png"
image credits12 = "images/END CREDITS/END_CREDITS-12.png"
image credits13 = "images/END CREDITS/END_CREDITS-13.png"
image credits14 = "images/END CREDITS/END_CREDITS-14.png"
image credits15 = "images/END CREDITS/END_CREDITS-15.png"
image credits16 = "images/END CREDITS/END_CREDITS-16.png"
image credits17 = "images/END CREDITS/END_CREDITS-17.png"
image credits18 = "images/END CREDITS/END_CREDITS-18.png"


image bg20 = "images/BG/BK_W-01.png"

image bg19 2 = "images/BG/BK-02.png"
image bg19_HALFW = "images/BG/BK-HALFWHITE.png"
image bg19_HALFP = "images/BG/BK-HALFPNK.png"

image bg_Stelle = "images/BG/BK-07.png"

image mainmenu:
    "images/intro/TITLE SCREEN-01.png" with fade
    pause 3.0
    "images/intro/TITLE SCREEN-02.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-03.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-04.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-05.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-06.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-07.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-08.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-09.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-10.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-11.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-12.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-13.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-14.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-15.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-16.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-17.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-18.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-19.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-20.png" with dissolve
    pause 1.5
    "images/intro/TITLE SCREEN-21.png" with dissolve
    pause 3.0
    "images/intro/TITLE SCREEN-22.png" with dissolve




image s20 1 = "images/20/FLAG-01.png"
image s20 2 = "images/20/FLAG-02.png"
image s20 3 = "images/20/FLAG-03.png"
image s20 4 = "images/20/FLAG-04.png"
image s20 5 = "images/20/FLAG-08.png"

image s20 g:
    "images/20/FLAG-01.png"
    pause 0.5
    "images/20/FLAG-05.png"
    pause 0.5
    "images/20/FLAG-06.png"
    pause 0.5
    "images/20/FLAG-01.png"
    pause 0.5
    "images/20/FLAG-07.png"
    pause 0.5
    "images/20/FLAG-01.png"
    pause 0.5
    "images/20/FLAG-03.png"
    pause 0.5
    "images/20/FLAG-01.png"
    pause 0.5
    "images/20/FLAG-02.png"
    pause 0.5
    repeat

image s20 8 = "images/20/HOME-01.png"
image s20 9 = "images/20/HOME-02.png"

image achar = "images/20/MILITARY-01.png"
image bchar = "images/20/MILITARY-06.png"

image aeye:
    "images/20/MILITARY-02.png"
    pause 5.0
    "images/20/MILITARY-03.png"
    pause 0.1
    repeat

image beye:
    "images/20/MILITARY-07.png"
    pause 3.0
    "images/20/MILITARY-08.png"
    pause 0.1
    repeat

image amouth OFF = "images/20/MILITARY-04.png"
image amouth ON:
    "images/20/MILITARY-04.png"
    pause 0.1
    "images/20/MILITARY-05.png"
    pause 0.1
    "images/20/MILITARY-04.png"
    pause 0.1
    "images/20/MILITARY-05.png"
    pause 0.1
    "images/20/MILITARY-04.png"
    pause 0.1
    "images/20/MILITARY-05.png"
    pause 0.1
    "images/20/MILITARY-04.png"
    pause 0.1
    "images/20/MILITARY-05.png"
    pause 0.1
    "images/20/MILITARY-04.png"
    pause 0.1
    "images/20/MILITARY-05.png"
    pause 0.1
    "images/20/MILITARY-04.png"
image bmouth OFF = "images/20/MILITARY-09.png"
image bmouth ON:
    "images/20/MILITARY-09.png"
    pause 0.1
    "images/20/MILITARY-10.png"
    pause 0.1
    "images/20/MILITARY-09.png"
    pause 0.1
    "images/20/MILITARY-10.png"
    pause 0.1
    "images/20/MILITARY-09.png"
    pause 0.1
    "images/20/MILITARY-10.png"
    pause 0.1
    "images/20/MILITARY-09.png"
    pause 0.1
    "images/20/MILITARY-10.png"
    pause 0.1
    "images/20/MILITARY-09.png"
    pause 0.1
    "images/20/MILITARY-10.png"
    pause 0.1
    "images/20/MILITARY-09.png"

image badoglio = VBox("images/20/BADOGLIO-01.png", "images/20/BADOGLIO-01.png")

transform -490 loop:
    ypos 0.0
    linear 20.0 ypos -1.0
    repeat


image s19 1 = "images/19/BOYS-19.png"
image s19_2 = "images/19/BOYS-14.png"
image s19_3 = "images/19/BOYS-13.png"
image s19_4 = "images/19/BOYS-06.png"
image s19 5 = "images/19/BOYS-26.png"

image cloud1:
    "images/19/BOYS-15.png"
    xpos 1.25 yanchor 0.75
    linear 10.0 xpos -0.5
    repeat

image cloud2:
    "images/19/BOYS-16.png"
    xpos 1.25 yanchor 0.8
    linear 8.0 xpos -0.5
    repeat

image cloud3:
    "images/19/BOYS-17.png"
    xpos 1.25 yanchor 0.85
    linear 7.5 xpos -0.5
    repeat

image cloud4:
    "images/19/BOYS-18.png"
    xpos 1.25 yanchor 0.65
    linear 12.0 xpos -0.5
    repeat

image dchar = "images/19/BOYS-01.png"
image echar = "images/19/BOYS-08.png"
image echarback:
    "images/19/BOYS-07.png"
    ypos 1.0
    linear 1.0 ypos 1.05
    linear 1.0 ypos 1.0
    repeat
image echarback_still = "images/19/BOYS-07.png"

image deye:
    "images/19/BOYS-02.png"
    pause 5.0
    "images/19/BOYS-03.png"
    pause 0.1
    repeat

image eeye:
    "images/19/BOYS-09.png"
    pause 3.0
    "images/19/BOYS-10.png"
    pause 0.1
    repeat

image dmouth OFF = "images/19/BOYS-05.png"
image dmouth ON:
    "images/19/BOYS-04.png"
    pause 0.1
    "images/19/BOYS-05.png"
    pause 0.1
    "images/19/BOYS-04.png"
    pause 0.1
    "images/19/BOYS-05.png"
    pause 0.1
    "images/19/BOYS-04.png"
    pause 0.1
    "images/19/BOYS-05.png"
    pause 0.1
    "images/19/BOYS-04.png"
    pause 0.1
    "images/19/BOYS-05.png"
    pause 0.1
    "images/19/BOYS-04.png"
    pause 0.1
    "images/19/BOYS-05.png"
    pause 0.1
    "images/19/BOYS-05.png"
image emouth OFF = "images/19/BOYS-12.png"
image emouth ON:
    "images/19/BOYS-12.png"
    pause 0.1
    "images/19/BOYS-11.png"
    pause 0.1
    "images/19/BOYS-12.png"
    pause 0.1
    "images/19/BOYS-11.png"
    pause 0.1
    "images/19/BOYS-12.png"
    pause 0.1
    "images/19/BOYS-11.png"
    pause 0.1
    "images/19/BOYS-12.png"
    pause 0.1
    "images/19/BOYS-11.png"
    pause 0.1
    "images/19/BOYS-12.png"
    pause 0.1
    "images/19/BOYS-11.png"
    pause 0.1
    "images/19/BOYS-12.png"

image mondiali = VBox("images/19/MONDIALI.png", "images/19/MONDIALI.png")


image s18pelle = "images/BG/BK-04.png"
image s18 1 = "images/18/BENITO-01.png"
image aereopiccolo = "images/18/BENITO-aereo.png"
image cchar = "images/18/BENITO-02.png"
image c2char = "images/18/BENITO-05.png"
image braccia = "images/18/BENITO-09.png"

image sparo:
    "images/18/BENITO-sparo2.png"
    pause 0.2
    "images/18/BENITO-sparo1.png"
    pause 0.2
    "images/18/BENITO-sparo2.png"
    pause 0.2
    "images/18/BENITO-sparo1.png"
    pause 0.2
    "images/18/BENITO-sparo2.png"
    pause 0.2
    "images/18/BENITO-sparo1.png"
    pause 0.2
    repeat

transform -490 mitra:
    xpos 1.0 xanchor 0.0
    linear 6 xanchor 0.8 xpos 0.0
    repeat

transform -490 pippo:
    xpos 1.0 xanchor 0.0
    linear 6 xanchor 0.8 xpos 0.0
    repeat

transform -490 mitra2:
    ypos 0.0 yanchor 0.0
    linear 3 ypos 0.03
    linear 3 ypos -0.02
    linear 3 ypos 0.0
    repeat

transform -490 pippo2:
    ypos 0.0 yanchor 0.0
    linear 3 ypos 0.03
    linear 3 ypos -0.02
    linear 3 ypos 0.0
    repeat

image cmouth OFF = "images/18/BENITO-07.png"
image cmouth ON:
    "images/18/BENITO-07.png"
    pause 0.1
    "images/18/BENITO-06.png"
    pause 0.1
    "images/18/BENITO-07.png"
    pause 0.1
    "images/18/BENITO-06.png"
    pause 0.1
    "images/18/BENITO-07.png"
    pause 0.1
    "images/18/BENITO-06.png"
    pause 0.1
    "images/18/BENITO-07.png"
    pause 0.1
    "images/18/BENITO-06.png"
    pause 0.1
    "images/18/BENITO-07.png"
    pause 0.1
    "images/18/BENITO-06.png"
    pause 0.1
    "images/18/BENITO-07.png"

image c2mouth OFF = "images/18/BENITO-11.png"
image c2mouth ON:
    "images/18/BENITO-11.png"
    pause 0.1
    "images/18/BENITO-12.png"
    pause 0.1
    "images/18/BENITO-11.png"
    pause 0.1
    "images/18/BENITO-12.png"
    pause 0.1
    "images/18/BENITO-11.png"
    pause 0.1
    "images/18/BENITO-12.png"
    pause 0.1
    "images/18/BENITO-11.png"
    pause 0.1
    "images/18/BENITO-12.png"
    pause 0.1
    "images/18/BENITO-11.png"
    pause 0.1
    "images/18/BENITO-12.png"
    pause 0.1
    "images/18/BENITO-11.png"

image ceye:
    "images/18/BENITO-04.png"
    pause 4.0
    "images/18/BENITO-03.png"
    pause 0.1
    repeat

image c2eye:
    "images/18/BENITO-10_2.png"
    pause 4.0
    "images/18/BENITO-10.png"
    pause 0.1
    repeat



image s17_1 = "images/17/17-01.png"
image fuoco1 = "images/17/17-13.png"

image fuoco:
    "images/17/17-13.png"
    parallel:
        alpha 0.8
        linear 1.0 alpha 0.5
        linear 1.0 alpha 0.8
        repeat
    parallel:
        ypos 0.8 yanchor 0.0
        linear 2.0 ypos 0.55
        linear 1.5 ypos 0.65
        linear 2.0 ypos 0.45
        linear 1.5 ypos 0.55
        linear 2.0 ypos 0.3
        linear 2.5 ypos 0.5
        linear 1.0 ypos 0.45
        linear 3.0 ypos 0.65
        linear 2.0 ypos 0.55
        linear 2.0 ypos 0.8
        repeat

image fchar = "images/17/17-02.png"
image gchar = "images/17/17-07.png"


image feye:
    "images/17/17-03.png"
    pause 5.0
    "images/17/17-04.png"
    pause 0.1
    repeat

image geye:
    "images/17/17-08.png"
    pause 3.0
    "images/17/17-09.png"
    pause 0.4
    "images/17/17-08.png"
    pause 3.0
    "images/17/17-09.png"
    pause 0.1
    "images/17/17-08.png"
    pause 0.1
    "images/17/17-09.png"
    pause 0.1
    "images/17/17-08.png"
    pause 0.1
    "images/17/17-09.png"
    pause 0.1
    "images/17/17-08.png"
    pause 0.1
    "images/17/17-09.png"
    pause 0.4
    repeat

image fmouth OFF = "images/17/17-06.png"
image fmouth ON:
    "images/17/17-06.png"
    pause 0.1
    "images/17/17-05.png"
    pause 0.1
    "images/17/17-06.png"
    pause 0.1
    "images/17/17-05.png"
    pause 0.1
    "images/17/17-06.png"
    pause 0.1
    "images/17/17-05.png"
    pause 0.1
    "images/17/17-06.png"
    pause 0.1
    "images/17/17-05.png"
    pause 0.1
    "images/17/17-06.png"
    pause 0.1
    "images/17/17-05.png"
    pause 0.1
    "images/17/17-06.png"


image gmouth OFF = "images/17/17-12.png"
image gmouth ON:
    "images/17/17-12.png"
    pause 0.1
    "images/17/17-11.png"
    pause 0.1
    "images/17/17-12.png"
    pause 0.1
    "images/17/17-11.png"
    pause 0.1
    "images/17/17-12.png"
    pause 0.1
    "images/17/17-11.png"
    pause 0.1
    "images/17/17-12.png"
    pause 0.1
    "images/17/17-11.png"
    pause 0.1
    "images/17/17-12.png"
    pause 0.1
    "images/17/17-11.png"
    pause 0.1
    "images/17/17-12.png"


image s16 = "images/16/16-01.png"
image hchar = "images/16/16-03.png"
image ichar = "images/16/16-02.png"

image auschwitz treno = HBox("images/16/16-13.png", "images/16/16-13.png")

transform -490 looptreno:
    xpos 0
    linear 60.0 xpos -4935
    repeat

image auschwitz fila = HBox("images/16/16-12.png", "images/16/16-12.png")

transform -490 loopfila:
    xpos 0
    linear 60.0 xpos -4966
    repeat

image cancello1:
    "images/16/CANCELLOFRONTEA.png"
    xanchor 1.0 xpos 0.0
    linear 3.0 xanchor 0.0 xpos 0.0

image cancello2:
    "images/16/CANCELLOFRONTEB.png"
    xanchor 0.0 xpos 1.0
    linear 3.0 xanchor 0.0 xpos 0.0

image cancello3:
    "images/16/CANCELLORETROA.png"
    xanchor 1.0 xpos 0.0
    linear 3.0 xanchor 0.0 xpos 0.0

image cancello4:
    "images/16/CANCELLORETROB.png"
    xanchor 0.0 xpos 1.0
    linear 3.0 xanchor 0.0 xpos 0.0

image heye:
    "images/16/16-06.png"
    pause 5.0
    "images/16/16-07.png"
    pause 0.1
    repeat

image ieye:
    "images/16/16-04.png"
    pause 3.0
    "images/16/16-05.png"
    pause 0.1
    repeat

image hmouth OFF = "images/16/16-11.png"
image hmouth ON:
    "images/16/16-11.png"
    pause 0.1
    "images/16/16-10.png"
    pause 0.1
    "images/16/16-11.png"
    pause 0.1
    "images/16/16-10.png"
    pause 0.1
    "images/16/16-11.png"
    pause 0.1
    "images/16/16-10.png"
    pause 0.1
    "images/16/16-11.png"
    pause 0.1
    "images/16/16-10.png"
    pause 0.1
    "images/16/16-11.png"
    pause 0.1
    "images/16/16-10.png"
    pause 0.1
    "images/16/16-11.png"
image imouth OFF = "images/16/16-09.png"
image imouth ON:
    "images/16/16-09.png"
    pause 0.1
    "images/16/16-08.png"
    pause 0.1
    "images/16/16-09.png"
    pause 0.1
    "images/16/16-08.png"
    pause 0.1
    "images/16/16-09.png"
    pause 0.1
    "images/16/16-08.png"
    pause 0.1
    "images/16/16-09.png"
    pause 0.1
    "images/16/16-08.png"
    pause 0.1
    "images/16/16-09.png"
    pause 0.1
    "images/16/16-08.png"
    pause 0.1
    "images/16/16-09.png"




image s14 pelle = "images/14/14-01.png"
image s14_capelli = "images/14/14-02.png"
image s14sfondo 1 = "images/14/14-03.png"
image s14sfondo 2 = "images/14/14-11.png"
image s14 folla = "images/14/14-04.png"

transform -490 rivolta:
    ypos 1.0
    linear 3.0 ypos 1.1
    linear 3.0 ypos 1.0
    repeat

image keye:
    "images/14/14-05.png"
    pause 5.0
    "images/14/14-06.png"
    pause 0.1
    repeat

image kmouth OFF = "images/14/14-07.png"
image kmouth ON:
    "images/14/14-07.png"
    pause 0.1
    "images/14/14-08.png"
    pause 0.1
    "images/14/14-07.png"
    pause 0.1
    "images/14/14-08.png"
    pause 0.1
    "images/14/14-07.png"
    pause 0.1
    "images/14/14-08.png"
    pause 0.1
    "images/14/14-07.png"
    pause 0.1
    "images/14/14-08.png"
    pause 0.1
    "images/14/14-07.png"
    pause 0.1
    "images/14/14-08.png"
    pause 0.1
    "images/14/14-07.png"



image casa = "images/15/15-12.png"
image origlio = "images/15/15-03.png"
image jpelle OK = "images/15/15-02.png"
image jpelle UK = "images/15/15-13.png"

image j1 = "images/15/15-09.png"
image j2 = "images/15/15-10.png"
image j3 = "images/15/15-11.png"


image jmouth OFF = "images/15/15-06.png"
image jmouth ON:
    "images/15/15-06.png"
    pause 0.1
    "images/15/15-07.png"
    pause 0.1
    "images/15/15-06.png"
    pause 0.1
    "images/15/15-07.png"
    pause 0.1
    "images/15/15-06.png"
    pause 0.1
    "images/15/15-07.png"
    pause 0.1
    "images/15/15-06.png"
    pause 0.1
    "images/15/15-07.png"
    pause 0.1
    "images/15/15-06.png"
    pause 0.1

image jeye:
    "images/15/15-04.png"
    pause 4.0
    "images/15/15-05.png"
    pause 0.1
    repeat

transform -490 camminata1:
    xpos 0.0 xanchor 0.0
    linear 0.5 xpos 0.05
    linear 1 xpos -0.05
    linear 1 xpos 0.0
    repeat

transform -490 camminata2:
    xpos 0.0 xanchor 0.0
    linear 2 xpos -0.2
    linear 2 xpos 0.0
    repeat

transform -490 camminata3:
    xpos 0.0 xanchor 0.0
    linear 0.5 xpos -0.05
    linear 1 xpos 0.1
    linear 1 xpos -0.1
    linear 1 xpos 0.0
    repeat



image nmouth OFF = "images/12/12-10.png"
image nmouth ON:
    "images/12/12-10.png"
    pause 0.1
    "images/12/12-11.png"
    pause 0.1
    "images/12/12-10.png"
    pause 0.1
    "images/12/12-11.png"
    pause 0.1
    "images/12/12-10.png"
    pause 0.1
    "images/12/12-11.png"
    pause 0.1
    "images/12/12-10.png"
    pause 0.1
    "images/12/12-11.png"
    pause 0.1
    "images/12/12-10.png"
    pause 0.1
    "images/12/12-11.png"
    pause 0.1
    "images/12/12-10.png"

image n1eye:
    "images/12/12-09.png"
    pause 5.0
    "images/12/12-08.png"
    pause 0.1
    repeat

image n2eye:
    "images/12/12-03.png"
    pause 3.0
    "images/12/12-04.png"
    pause 0.1
    repeat

image s12 = "images/12/12-01.png"
image n2char = "images/12/12-02.png"
image n1chara = "images/12/12-06.png"
image n1charb = "images/12/12-07.png"

image volantino = VBox("images/12/12-12.png", "images/12/12-12.png")

transform -490 loopcane:
    ypos 0
    linear 20.0 ypos -1184
    repeat



image bici_ferma = "images/11/11_5-BICIGRANDE.png"
image s11_sfondo = "images/11/11_2-SFONDO_ombra.png"
image s11_sfondo2 = "images/11/11_1-BICI.png"

image bici ferma:
    "images/11/11_5-BICIGRANDE.png"
    xpos 0.4

image bici normale:
    "images/11/11_5-BICIGRANDE.png"
    parallel:
        xpos 0.4
        linear 1.3 xpos 0.3
        linear 1.1 xpos 0.4
        linear 1.3 xpos 0.3
        linear 1.4 xpos 0.35
        linear 1.3 xpos 0.4
        repeat
    parallel:
        ypos 1.0
        ypos 1.0
        linear 0.3 ypos 1.02
        linear 0.3 ypos 1.0
        repeat

image bici via:
    "images/11/11_5-BICIGRANDE.png"
    xpos 0.4
    linear 0.5 xpos 0.35
    linear 0.5 xpos 2.0

image bandiera1 = "images/11/11_2-SFONDO_ombra.png"

image bandiera = HBox("images/11/11_2-SFONDO_ombra.png", "images/11/11_2-SFONDO_ombra.png")

transform -490 scorrere:
    xpos 0.0
    linear 3.0 xpos -1.0
    repeat



image pmouth OFF = "images/10/10-08.png"
image pmouth ON:
    "images/10/10-08.png"
    pause 0.1
    "images/10/10-07.png"
    pause 0.1
    "images/10/10-08.png"
    pause 0.1
    "images/10/10-07.png"
    pause 0.1
    "images/10/10-08.png"
    pause 0.1
    "images/10/10-07.png"
    pause 0.1
    "images/10/10-08.png"
    pause 0.1
    "images/10/10-07.png"
    pause 0.1
    "images/10/10-08.png"
    pause 0.1
    "images/10/10-07.png"
    pause 0.1
    "images/10/10-08.png"

image peye:
    "images/10/10-09.png"
    pause 3.0
    "images/10/10-10.png"
    pause 0.1
    repeat

image s10 ma = "images/10/10-02.png"
image s10 pa = "images/10/10-03.png"
image s10 so = "images/10/10-04.png"
image s10 zi = "images/10/10-06.png"
image s10 cu = "images/10/10-05.png"
image s10 ca = "images/10/10-01.png"
image s10 all = "images/10/10-11.png"



image qchar = "images/9/9-01.png"
image strage = "images/9/9-02.png"

image insieme = "images/9/9-03.png"

image targa = "images/9/9-08.png"

image qeye:
    "images/9/9-04.png"
    pause 5.0
    "images/9/9-05.png"
    pause 0.1
    repeat

image qmouth OFF = "images/9/9-06.png"
image qmouth ON:
    "images/9/9-06.png"
    pause 0.1
    "images/9/9-07.png"
    pause 0.1
    "images/9/9-06.png"
    pause 0.1
    "images/9/9-07.png"
    pause 0.1
    "images/9/9-06.png"
    pause 0.1
    "images/9/9-07.png"
    pause 0.1
    "images/9/9-06.png"
    pause 0.1
    "images/9/9-07.png"
    pause 0.1
    "images/9/9-06.png"
    pause 0.1
    "images/9/9-07.png"
    pause 0.1
    "images/9/9-06.png"
    pause 0.1



image pg m = "images/13/13-01.png"
image pg l = "images/13/13-02.png"




image s13_13 = "images/13/13-13.png"
image torcia:
    "images/13/13-16.png"
    alignaround (.5, .5)
    linear 2.0 clockwise circles 3 xalign .5 yalign .5
    pause 5.0
    linear 3.0 zoom 2.0
    pause 3.0
    linear 1.0 zoom 1.0
    repeat

image occhio_l:
    "images/13/13-07.png"
    pause 3.0
    "images/13/13-09.png"
    pause 0.1
    repeat

image occhio_m:
    "images/13/13-08.png"
    pause 3.0
    "images/13/13-10.png"
    pause 0.1
    repeat

image lmouth OFF = "images/13/13-12.png"
image lmouth ON:
    "images/13/13-12.png"
    pause 0.1
    "images/13/13-11.png"
    pause 0.1
    "images/13/13-12.png"
    pause 0.1
    "images/13/13-11.png"
    pause 0.1
    "images/13/13-12.png"
    pause 0.1
    "images/13/13-11.png"
    pause 0.1
    "images/13/13-12.png"
    pause 0.1
    "images/13/13-11.png"
    pause 0.1
    "images/13/13-12.png"
    pause 0.1
    "images/13/13-11.png"
    pause 0.1
    "images/13/13-12.png"



image bg7 = "images/7/7_1 SFONDO.png"
image s07 15 = "images/7/7_18 FUMO.png"
image s07 16 = "images/7/7_a_1 SFONDO.png"
image s07 17 = "images/7/7_a_1 SFONDO copy.png"
image s07 21 = "images/7/7_copiaOcchio CHIU.png"
image rmouth_urlo = "images/7/7_boccaUrlo.png"

image rchar = "images/7/7_3 SCUOLA BAMBINI.png"
image rcharNo = "images/7/7_7 CAPELLI NOO.png"

image reye:
    "images/7/7_copiaOcchio APER.png"
    pause 5.0
    "images/7/7_copiaOcchio CHIU.png"
    pause 0.1
    repeat

image rmouth OFF = "images/7/7_boccaChiusa.png"
image rmouth ON:
    "images/7/7_boccaChiusa.png"
    pause 0.1
    "images/7/7_boccaAperta.png"
    pause 0.1
    "images/7/7_boccaChiusa.png"
    pause 0.1
    "images/7/7_boccaAperta.png"
    pause 0.1
    "images/7/7_boccaChiusa.png"
    pause 0.1
    "images/7/7_boccaAperta.png"
    pause 0.1
    "images/7/7_boccaChiusa.png"
    pause 0.1
    "images/7/7_boccaAperta.png"
    pause 0.1
    "images/7/7_boccaChiusa.png"
    pause 0.1
    "images/7/7_boccaAperta.png"
    pause 0.1
    "images/7/7_boccaChiusa.png"
    pause 0.1
    "images/7/7_boccaAperta.png"
    pause 0.1
    "images/7/7_boccaChiusa.png"

image nuvole = HBox("images/7/7_2 NUVOLE.png", "images/7/7_2 NUVOLE.png")
image nuvole2 = HBox("images/7/7_2 NUVOLE.png", "images/7/7_2 NUVOLE.png")

transform -490 passaggio:
    xpos 0.0
    linear 12.0 xpos -1.0
    repeat

transform -490 passaggio2:
    xpos 0.0 ypos 0.4
    linear 9.0 xpos -1.0
    repeat

transform -490 passaggio3:
    xpos 0.0 ypos 0.4
    linear 20.0 xpos -1.0
    repeat

transform -490 passaggio4:
    xpos 0.0 ypos 0.4
    linear 16.0 xpos -1.0
    repeat

image aereo = "images/7/7_4 AEREO.png"

transform -490 volo:
    xpos -1.0
    linear 2.0 xpos 1.5

image bombaPiccola = "images/7/7_6 BOMBA PICCOLA.png"

transform -490 sganciata1:
    ypos 0.0
    linear 1.0 ypos 1.0

transform -490 sganciataSullaScuola:
    ypos 0.0
    linear 0.1 ypos 0.1

image bombaGrande = "images/7/7_5 BOMBA GRANDE.png"

transform -490 sganciata2:
    "images/7/7_5 BOMBA GRANDE.png"
    ypos -0.4
    linear 0.5 ypos 0.5

image esplosione:
    "images/7/7_7 CAPELLI NOO.png" with Dissolve(0.2)
    pause 0.4
    "images/7/7_8 ESPLOSIONE1.png" with Dissolve(0.2)
    pause 0.1
    "images/7/7_9 ESPLOSIONE2.png" with Dissolve(0.2)
    pause 0.1
    "images/7/7_10 ESPLOSIONE3.png" with Dissolve(0.2)
    pause 0.1
    "images/7/7_11 ESPLOSIONE4.png" with Dissolve(0.2)
    pause 0.1
    "images/7/7_12 ESPLOSIONE5.png" with Dissolve(0.2)
    pause 0.1
    "images/7/7_13 ESPLOSIONE6.png" with Dissolve(0.2)
    pause 0.1
    "images/7/7_14 ESPLOSIONE7.png" with Dissolve(0.2)
    pause 0.1
    "images/7/7_15 ESPLOSIONE8.png" with Dissolve(0.2)
    pause 0.1
    "images/7/7_16 ESPLOSIONE9.png" with Dissolve(0.2)
    pause 0.1
    "images/7/7_17 ESPLOSIONE10.png" with Dissolve(0.2)
    pause 0.1
    "images/7/7_18 FUMO.png" with Dissolve(0.2)
    pause 0.1



image s06 1 = "images/6/6_01-START.png"
image s06 2 = "images/6/6_02-DISSOL A NERO.png"


image ss2char = "images/6/6_08-PROSP OPERA-SS2.png"

image ss2BigChar = "images/6/6_13-CAMBIO PROSPETTIVA_2.png"
image opchar = "images/6/6_18-PROSP SSvsOP.png"

image ss1eye:
    "images/6/6_06-OCCHI APER SS1.png"
    pause 5.0
    "images/6/6_07-OCCHI CHIU SS1.png"
    pause 0.1
    repeat

image opeye:
    "images/6/6_21-OCCHI APER OP1.png"
    pause 3.0
    "images/6/6_22-OCCHI CHIU OP1.png"
    pause 0.1
    repeat

image ss1mouth OFF = "images/6/6_05-BOCCA CHIU SS1.png"
image ss1mouth ON:
    "images/6/6_05-BOCCA CHIU SS1.png"
    pause 0.1
    "images/6/6_04-BOCCA APER SS1.png"
    pause 0.1
    "images/6/6_05-BOCCA CHIU SS1.png"
    pause 0.1
    "images/6/6_04-BOCCA APER SS1.png"
    pause 0.1
    "images/6/6_05-BOCCA CHIU SS1.png"
    pause 0.1
    "images/6/6_04-BOCCA APER SS1.png"
    pause 0.1
    "images/6/6_05-BOCCA CHIU SS1.png"

image opmouth OFF = "images/6/6_20-BOCCA CHIU OP1.png"
image opmouth ON:
    "images/6/6_20-BOCCA CHIU OP1.png"
    pause 0.1
    "images/6/6_19-BOCCA APER OP1.png"
    pause 0.1
    "images/6/6_20-BOCCA CHIU OP1.png"
    pause 0.1
    "images/6/6_19-BOCCA APER OP1.png"
    pause 0.1
    "images/6/6_20-BOCCA CHIU OP1.png"
    pause 0.1
    "images/6/6_19-BOCCA APER OP1.png"
    pause 0.1
    "images/6/6_20-BOCCA CHIU OP1.png"

image ss1Bigmouth OFF = "images/6/6_14-BOCCA CHIU BIG SS1.png"
image ss1Bigmouth ON:
    "images/6/6_14-BOCCA CHIU BIG SS1.png"
    pause 0.1
    "images/6/6_15-BOCCA APER BIG SS1.png"
    pause 0.1
    "images/6/6_14-BOCCA CHIU BIG SS1.png"
    pause 0.1
    "images/6/6_15-BOCCA APER BIG SS1.png"
    pause 0.1
    "images/6/6_14-BOCCA CHIU BIG SS1.png"
    pause 0.1
    "images/6/6_15-BOCCA APER BIG SS1.png"
    pause 0.1
    "images/6/6_14-BOCCA CHIU BIG SS1.png"

image ss2Bigmouth OFF = "images/6/6_16-BOCCA CHIU BIG SS2.png"
image ss2Bigmouth ON:
    "images/6/6_16-BOCCA CHIU BIG SS2.png"
    pause 0.1
    "images/6/6_17-BOCCA APER BIG SS2.png"
    pause 0.1
    "images/6/6_16-BOCCA CHIU BIG SS2.png"
    pause 0.1
    "images/6/6_17-BOCCA APER BIG SS2.png"
    pause 0.1
    "images/6/6_16-BOCCA CHIU BIG SS2.png"
    pause 0.1
    "images/6/6_17-BOCCA APER BIG SS2.png"
    pause 0.1
    "images/6/6_16-BOCCA CHIU BIG SS2.png"



image s5 1 = "images/5/5_1-ANZIANA.png"
image s5 2 = "images/5/5_2-MUSSOLINI PINK.png"
image s5 3 = "images/5/5_3-MUSSOLINI GREY.png"



image s04_1 = "images/4/4_1-BASE.png"
image s04_2 = "images/4/4_2-INCUBO_SPINNING.png"
image s04_3 = "images/4/4_3-WAKEUP-SPINNING.png"


image s04_4 = "images/4/4_boccaAperta.png"
image s04_7 = "images/4/4_occhiChiusi.png"

image ueye:
    "images/4/4_occhiAperti.png"
    pause 2.0
    "images/4/4_occhiChiusi.png"
    pause 0.1
    repeat

image umouth OFF = "images/4/4_boccaChiusa.png"
image umouth ON:
    "images/4/4_boccaChiusa.png"
    pause 0.1
    "images/4/4_boccaAperta.png"
    pause 0.1
    "images/4/4_boccaChiusa.png"
    pause 0.1
    "images/4/4_boccaAperta.png"
    pause 0.1
    "images/4/4_boccaChiusa.png"
    pause 0.1
    "images/4/4_boccaAperta.png"
    pause 0.1
    "images/4/4_boccaChiusa.png"
    pause 0.1

image incuboFermo = "images/4/4_3-WAKEUP-SPINNING.png"

image incubo:
    "images/4/4_3-WAKEUP-SPINNING.png"
    rotate 0
    linear 1.0 rotate 360
    repeat

image falo:
    "images/4/fuoco1.png"
    pause 0.1
    "images/4/fuoco2.png"
    pause 0.1
    "images/4/fuoco8.png"
    pause 0.1
    "images/4/fuoco6.png"
    pause 0.1
    "images/4/fuoco7.png"
    pause 0.1
    "images/4/fuoco2.png"
    pause 0.1
    "images/4/fuoco4.png"
    pause 0.1
    "images/4/fuoco3.png"
    pause 0.1
    "images/4/fuoco5.png"
    pause 0.1
    repeat

image sveglia:
    "images/4/4_2-INCUBO_SPINNING.png"
    rotate 0
    linear 0.2 rotate -360
    repeat



image vchar 2 = "images/3/3-02.png"
image bg3 = "images/3/3-03.png"
image lettera = "images/3/3-05.png"
image ink:
    "images/3/3-04_TRANSP.png"
    xanchor 1.0 xpos 0.0
    linear 6.0 xanchor 0.0 xpos 1.0
    repeat

image vmouth OFF = "images/3/3-09.png"
image vmouth ON:
    "images/3/3-09.png"
    pause 0.1
    "images/3/3-10.png"
    pause 0.1
    "images/3/3-09.png"
    pause 0.1
    "images/3/3-10.png"
    pause 0.1
    "images/3/3-09.png"
    pause 0.1
    "images/3/3-10.png"
    pause 0.1
    "images/3/3-09.png"
    pause 0.1
    "images/3/3-10.png"
    pause 0.1
    "images/3/3-09.png"
    pause 0.1

image veye:
    "images/9/9-04.png"
    pause 4.0
    "images/9/9-05.png"
    pause 0.1
    repeat



image wchar 2 = "images/8/8_7-TESTABUCATA.png"
image wchar 1 = "images/8/8_2-DISPERATO.png"

image w1 = "images/8/8_4-LALTRO.png"
image w2 = "images/8/8_3-LEI.png"
image w3 = "images/8/8_5-LAGUARDIA.png"

image sfondo = "images/8/8_1-SFONDO.png"

image filo:
    "images/8/8_6-FILO.png"
    xalign 0.0 xpos 0
    pause 0.1
    xalign 0.0 xpos -2
    pause 0.1
    yalign 0.0 ypos 0
    pause 0.1
    yalign 0.0 ypos -1
    pause 0.1
    repeat

image wmouth OFF = "images/8/8-06.png"
image wmouth ON:
    "images/8/8-06.png"
    pause 0.1
    "images/8/8-07.png"
    pause 0.1
    "images/8/8-06.png"
    pause 0.1
    "images/8/8-07.png"
    pause 0.1
    "images/8/8-06.png"
    pause 0.1
    "images/8/8-07.png"
    pause 0.1
    "images/8/8-06.png"
    pause 0.1
    "images/8/8-07.png"
    pause 0.1
    "images/8/8-06.png"
    pause 0.1

image weye:
    "images/8/8-04.png"
    pause 4.0
    "images/8/8-05.png"
    pause 0.1
    repeat

transform -490 pattuglia:
    xpos 0.0 xanchor 0.0
    linear 3 xpos 0.05
    linear 4 xpos -0.05
    linear 3 xpos 0.0
    repeat

transform -490 fantasma:
    xpos 0.0 xanchor 0.0
    parallel:
        alpha 1.0
        linear 6 alpha 0.0
        linear 6 alpha 1.0
        repeat

transform -490 camminata4:
    xpos 0.0 xanchor 0.07
    linear 3 xpos 0.3
    linear 3 xpos 0.0
    repeat

image tortura1:
    "images/2/6_LUCE.png"
    pause 3.0
    "#000000"
    pause 0.5
    "images/2/6_LUCE.png"
    pause 0.2
    "#000000"
    pause 0.5
    "images/2/6_LUCE.png"
    pause 1.0
    "#000000"
    pause 3.0
    "images/2/6_LUCE.png"
    pause 1.0
    "#000000"
    pause 10.0
    "images/2/6_LUCE.png"
    pause 6.0
    "#000000"
    pause 1.5
    repeat

image tortura0:
    "images/2/6_LUCE.png"
    parallel:
        xalign 0.0 xpos 0
        pause 0.1
        xalign 0.0 xpos -0.025
        pause 0.1
        yalign 0.0 ypos 0
        pause 0.1
        yalign 0.0 ypos -0.025
        pause 0.1
        repeat
    parallel:
        alpha 1.0
        pause 0.1
        alpha 0.0
        pause 0.1
        alpha 1.0
        pause 0.1
        alpha 0.0
        pause 0.1
        alpha 1.0
        pause 5.0
        alpha 0.0
        pause 1.0
        alpha 1.0
        pause 0.1
        alpha 0.0
        pause 0.1
        alpha 1.0
        pause 0.1
        alpha 0.0
        pause 0.1
        alpha 1.0
        pause 3.0
        alpha 0.0
        pause 0.5
        alpha 1.0
        pause 1.5
        alpha 0.0
        pause 3.0
        repeat

image tortura2 = "images/2/6_TORTURATO.png"



image cinema = "images/1/1-01.png"

image zeye:
    "images/1/1-02.png"
    pause 4.0
    "images/1/1-03.png"
    pause 0.1
    repeat

image end 0 = "images/TITLE SCREEN.png"
image end 20 casa = "images/1/20_CASA.png"
image end 20 ordini = "images/1/20_GUERRA.png"
image end 20 boh = "images/1/20_SCELTA.png"
image end 19 bad = "images/1/19_VIENICONME.png"
image end 19 good = "images/1/19_AMICI.png"
image end 18 = "images/1/18_PIPPO.png"
image end 17 bad = "images/1/17_BORSA_NERA.png"
image end 17 good = "images/1/17-BUONO.png"
image end 16 = "images/1/16_DEPORTAZIONE_EBREI.png"
image end 15 = "images/1/15_ATTENTATO_TORTURA.png"
image end 14 sciopero = "images/1/14_OPERAIA_OPERAI.png"
image end 14 nosciopero = "images/1/14_OPERAIA_FACCIA.png"
image end 13 good = "images/1/13_RADIOLONDRA_ADOLESCENTE.png"
image end 13 bad = "images/1/13_RADIOLONDRA.png"
image end 12 = "images/1/12_VOLANTINO_FASCISTA.png"
image end 11 = "images/1/11_BICI.png"
image end 10 = "images/1/10_CAVALLO.png"
image end 9 = "images/1/9_LORETO.png"
image end 8 nobacio = "images/1/8_COPRIFUOCO_GOODBYE.png"
image end 8 bacio = "images/1/8_COPRIFUOCO_KISS.png"
image end 7 = "images/1/7_GORLA.png"
image end 6 = "images/1/6_SS.png"
image end 5 = "images/1/5_MILANO.png"
image end 4 = "images/1/4_MAIALE_BRUCIA.png"
image end 3 = "images/1/3_LETTERA.png"
image end 2 = "images/1/2_QUESTIONE.png"
image end 1 = "images/intro/TITLE SCREEN-22.png"

transform -490 schermo:
    xalign 0.0 xpos 0
    pause 0.1
    xalign 0.0 xpos -2
    pause 0.1
    yalign 0.0 ypos 0
    pause 0.1
    yalign 0.0 ypos -1
    pause 0.1
    repeat




define -490 b = Character(_('Soldato Pini'), color="#496b47", image="bmouth")
define -490 a = Character(_('Sergente Guidi'), color="#70377a", image="amouth")

define -490 d = Character(_('Soldato Tedesco'), color="#c87f10", image="dmouth")
define -490 e = Character('Giuseppe', color="#5673b2", image="emouth")

define -490 c = Character('Benito', color="#bf4e21", image="cmouth")
define -490 c2 = Character('Orzolino', color="#74a0c4", image="c2mouth")

define -490 f = Character('Giulio', color="#e58a26", image="fmouth")
define -490 g = Character('oiluiG', color="#d32928", image="gmouth")

define -490 h = Character('Kostoyed', color="#9e602c", image="hmouth")
define -490 i = Character(_('Padre Alfonso'), color="#f7d64a", image="imouth")

define -490 x = Character(_('Torturato'), color="#961d1e", image="umouth")
define -490 x1 = Character(_('Torturatore'), color="#e4e4e4")

define -490 k = Character('Gianna', color="#5673b2", image="kmouth")

define -490 j = Character('Sara', color="#bf4e21", image="jmouth")
define -490 j2 = Character(_('Famiglia'), color="#5673b2")

define -490 n1 = Character('Sergio', color="#c87f10", image="nmouth")
define -490 n2 = Character('Baldo', color="#c3a682")

define -490 o = Character('Marina', color="#5673b2")
define -490 o1 = Character(_('Guardia'), color="#46a034")

define -490 p1 = Character(_('Papà dell\'Emilio'), color="#e4e4e4", image="pmouth")
define -490 p2 = Character(_('Mamma dell\'Emilio'), color="#d32928", image="pmouth")
define -490 p3 = Character(_('Zio dell\'Emilio'), color="#e58a26", image="pmouth")
define -490 p4 = Character(_('Sorella dell\'Emilio'), color="#c3a682", image="pmouth")
define -490 p5 = Character(_('Cugino dell\'Emilio'), color="#74a0c4", image="pmouth")

define -490 q = Character('Nanda', color="#961d1e", image="qmouth")
define -490 q2 = Character(_('Martiri di Piazzale Loreto'), color="#961d1e", image="qmouth")

define -490 l = Character('Nicola', color="#e4e4e4", image="lmouth")
define -490 m = Character('Luca', color="#e4e4e4", image="lmouth")

define -490 r = Character('Donata', color="#f7d64a", image="rmouth")

define -490 op = Character('Fausto', color="#bf4e21", image="opmouth")
define -490 ss1 = Character('SchutzStaffel #1', color="#496b47", image="ss1mouth")
define -490 ss2 = Character('SchutzStaffel #2', color="#46a034", image="ss2mouth")
define -490 ss1Big = Character('SchutzStaffel #1', color="#496b47", image="ss1Bigmouth")
define -490 ss2Big = Character('SchutzStaffel #2', color="#46a034", image="ss2Bigmouth")

define -490 t = Character('Linda', color="#e4e4e4", image="lmouth")
define -490 t2 = Character('Mussolini', color="#e4e4e4", image="lmouth")

define -490 u = Character('Ernesto', color="#961d1e", image="umouth")
define -490 u1 = Character(_('I vicini'), color="#70377a")

define -490 v = Character('Tina', color="#74a0c4", image="vmouth")

define -490 w = Character('Milton', color="#961d1e", image="wmouth")

define -490 y = Character('Zeno', color="#961d1e")




label start:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n20 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/20-BADOGLIO_3.mp3"
    centered "{size=48}{cps=20}- BADOGLIO -\nUn personaggio, scialbo, che sta al Sud,\ncon gli americani.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    $ renpy.pause(4.0, hard=True)
    $ renpy.music.set_volume(0.4, channel='sound')
    play sound "audio/sound/Armistizio 8 settembre 1943.mp3"
    scene c20 onlayer master with fade
    $ renpy.pause(5.0, hard=True)
    scene s20 4 onlayer master with fade
    $ renpy.pause(5.0, hard=True)
    scene badoglio onlayer master at loop
    show s20 1 onlayer master
    show achar onlayer master
    show bchar onlayer master
    show aeye onlayer master
    show beye onlayer master
    show amouth OFF onlayer master
    show bmouth OFF onlayer master
    with dissolve
    play music "audio/20_badoglio.mp3"
    b ON "Sergente Guidi... Sergente Guidi!"
    a ON "Soldato Pini."
    b ON "Ma che fa lì, sergente, non ha sentito la radio?"
    b ON "È finita la guerra!"
    a ON "Sì, ho sentito la radio."
    b ON "E allora?! Ha sentito cos'ha detto il maresciallo Badoglio? Tutti a casa! Tutti a casa!"
    a ON "A casa..."
    b ON "Che c'è, sergente?"
    a ON "Pini... Ha ascoltato con attenzione il proclama di Badoglio?"
    show s20 3 onlayer master

    b ON "Con attenzione, sissignore. L'Italia ha firmato l'armistizio con Eisenhower e gli Alleati, e..."
    a ON "E?"
    b ON "Me lo sono scritto per non sbagliare, sergente..."
    b ON "Ecco qua: \"ogni atto di ostilità contro le forze anglo-americane deve cessare da parte delle forze italiane\"."
    a ON "Nient'altro?"
    b ON "Ah sì: \"in ogni luogo\". In ogni luogo, capisce sergente? È finita la guerra!"
    a ON "È finita {i}una{/i} guerra, Pini."
    show s20 1 onlayer master
    a ON "Un'altra sta per cominciare."
    a ON "Presto, domani, forse oggi, forse è già iniziata."
    b ON "Ma che dice, sergente? Se abbiamo firmato la pace con gli americani che erano i nemici..."
    b ON "... con chi la dobbiamo fare la guerra?"
    a ON "Già: con chi, Pini?"
    b ON "I... tedeschi?"
    show s20 2 onlayer master

    a ON "I tedeschi."
    b ON "Ma i tedeschi non erano amici?!"
    menu:
        b "Ma i tedeschi non erano amici?!"
        "Sì, Pini: i tedeschi {i}erano{/i} amici.":
            jump mese20_a
        "No, Pini: i tedeschi non sono mai stati amici.":
            jump mese20_b

    label mese20_a:
        a ON "Sì, i tedeschi {i}erano{/i} amici."
        a ON "Perché erano nemici dei nostri nemici. Ma ora che il nemico è diventato amico..."
        a ON "... i tedeschi sono diventati i nemici dei nostri amici. E quindi nemici."
        show s20 g onlayer master

        b ON "Sono confuso, sergente."
        a ON "Anche io Pini, anche io."
        a ON "Ma di una cosa sono sicuro: da oggi, per la Germania, l'Italia è un paese nemico, un paese di traditori..."
        a ON "... un paese da occupare."
        a ON "E senza nemmeno bisogno di invaderlo, perché il nemico è già qui."
        b ON "Ma stanno arrivando gli americani, no? Anzi sono già qui, in Italia, è per questo che ci siamo arresi, no?"
        a ON "Gli americani sono ancora in Sicilia. E l'Italia è lunga, molto lunga, Pini."
        a ON "Potranno volerci settimane, forse mesi prima che arrivino fin qui al Nord."
        b ON "E... quindi?"
        $ ui.timer(3.0, ui.jumps("mese20_aa"))
        menu:
            b "E... quindi?"
            "Quindi... >>":
                jump mese20_c
            "Quindi... >>":
                jump mese20_a2
    label mese20_aa:
        menu:
            b "E... quindi?"
            "Quindi... aspettiamo.":
                jump mese20_c
            "Quindi... seguiamo gli ordini.":
                jump mese20_a2

    label mese20_b:
        a ON "No, i tedeschi non sono mai stati amici."
        a ON "Come non sono amici gli americani, o gli inglesi, o i francesi, o gli svizzeri."
        b ON "Gli svizzeri sono nemici?! Ma gli svizzeri non erano neutrali?"
        a ON "È questo il problema di questa porca guerra, Pini, è proprio questo."
        b ON "La... Svizzera?"
        a ON "No."
        show s20 g onlayer master

        a ON "Il problema è il fatto che parliamo di \"amici\" o \"nemici\" come se li conoscessimo uno per uno..."
        a ON "... Migliaia di tedeschi e americani e inglesi, migliaia e milioni di persone che non conosceremo mai."
        a ON "Che non vedremo mai in faccia."
        a ON "E li chiamiamo \"amici\", come se fossero i nostri compagni di scuola, o i nostri vicini di casa, o i nostri cari."
        a ON "{i}Quelli{/i} sono i tuoi amici, Pini."
        b ON "E... quindi?"
        $ ui.timer(3.0, ui.jumps("mese20_bb"))
        menu:
            b "E... quindi?"
            "Quindi... >>":
                jump mese20_b2
            "Quindi... >>":
                jump mese20_c
    label mese20_bb:
        menu:
            b "E... quindi?"
            "Quindi... torna da loro.":
                jump mese20_b2
            "Quindi... aspettiamo.":
                jump mese20_c

        label mese20_a2:
            show s20 1 onlayer master
            a ON "Quindi... Seguiamo gli ordini."
            b ON "Sono qui per questo, sergente. Per seguire i suoi, di ordini."
            a ON "E io quelli del tenente, e il tenente del capitano, e il capitano del generale, e il generale del Governo Badoglio."
            b ON "E siamo punto e a capo, sergente."
            a ON "Siamo punto e a capo, Pini."
            a ON "Ma siamo anche soldati del Regio Esercito italiano. E obbedire agli ordini è il nostro dovere."
            b ON "Sissignore."
            b ON "Cioè, con tutto il rispetto, io non ho capito..."
            b ON "Quali sono gli ordini?"
            menu:
                b "Quali sono gli ordini?"
                "Non lo so.":
                    jump mese20_c2
                "\"Cessare ogni ostilità contro gli anglo-americani. Reagire ad eventuali attacchi da qualsiasi altra provenienza\".":
                    jump mese20_a3

        label mese20_b2:
            show s20 1 onlayer master
            a ON "Quindi... torna da loro."
            a ON "Torna a casa."
            a ON "Pensandoci, Pini, hai ragione. Tutti a casa!"
            b ON "Tutti a casa!"
            a ON "A casa... sì."
            b ON "E lei che fa sergente, non viene?"
            menu:
                b "E lei che fa sergente, non viene?"
                "Sì.":
                    jump mese20_b3
                "Non lo so.":
                    jump mese20_c2

        label mese20_c:
            show s20 1 onlayer master
            a ON "Quindi... Aspettiamo."
            b ON "Aspettare? E cosa?"
            jump mese20_c2

            label mese20_a3:
                a ON "Cessare ogni ostilità contro gli anglo-americani. Reagire ad eventuali attacchi da qualsiasi altra provenienza."
                b ON "..."
                b ON "Sergente?"
                a ON "Pini."
                show s20 9 onlayer master
                with dissolve
                b ON "Quindi a casa non si torna?"
                a ON "Non sono questi gli ordini."
                b ON "Gli altri stanno già tornando a casa."
                a ON "Non sono questi gli ordini."
                b ON "Ho capito."
                b ON "Sergente?"
                a ON "Pini."
                b ON "Io resto qui con lei a reagire ad eventuali attacchi."
                b ON "Da qualsiasi altra provenienza."
                a ON "Da qualsiasi altra provenienza."
                b ON "Sergente?"
                a ON "Pini."
                b ON "Me lo ordinerà lei quando reagire?"
                a ON "Sì, Pini."
                $ s20ordini = True
                jump mese19

            label mese20_b3:
                a ON "Sì."
                show s20 8 onlayer master
                with dissolve
                a ON "Sì vengo, Pini."
                b ON "E allora andiamo, sergente!"
                a ON "Pini..."
                b ON "Sissignore?"
                a ON "Il tuo nome."
                b ON "... Pini, signore."
                a ON "Il tuo nome di battesimo."
                b ON "Carlo, signore. Mi chiamo Carlo."
                a ON "Giovanni. Io mi chiamo Giovanni."
                b ON "Lo so, signore..."
                a ON "Giovanni. Chiamami Giovanni, Carlo."
                b ON "Sissignore, sergente... Giovanni."
                a ON "Ciao Carlo. Ci vediamo a casa."
                b ON "A casa! Tutti a casa! Tutti a casa!"
                $ s20casa = True
                jump mese19

            label mese20_c2:
                a ON "Non lo so."
                a ON "Non so più nulla, Pini."
                a ON "Tornare a casa, seguire gli ordini, aspettare..."
                a ON "Scegliere."
                a ON "Era più facile, prima."
                b ON "Prima?"
                a ON "Credere. Obbedire. Combattere."
                a ON "Non erano scelte, era... così."
            label mese20_cc1:
                if coc == 3:
                    jump mese20_cc0

                menu:
                    "credere":
                        $ coc += 1
                        jump mese20_cc2
                    "obbedire":
                        $ coc += 1
                        jump mese20_cc2
                    "combattere":
                        $ coc += 1
                        jump mese20_cc2
            label mese20_cc2:
                if coc == 3:
                    jump mese20_cc0

                menu:
                    "combattere":
                        $ coc += 1
                        jump mese20_cc3
                    "credere":
                        $ coc += 1
                        jump mese20_cc3
                    "obbedire":
                        $ coc += 1
                        jump mese20_cc3
            label mese20_cc3:
                if coc == 3:
                    jump mese20_cc0

                menu:
                    "obbedire":
                        $ coc += 1
                        jump mese20_cc0
                    "combattere":
                        $ coc += 1
                        jump mese20_cc0
                    "credere":
                        $ coc += 1
                        jump mese20_cc0

            label mese20_cc0:
                menu:
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
                    "SCEGLIERE":
                        jump mese20_cc
            label mese20_cc:
                show s20 5 onlayer master
                b ON "Sergente?"
                b ON "Sergente!"
                b ON "Va tutto bene?"
                a ON "Va tutto bene, Pini."
                a ON "Ora va tutto bene."
                a ON "Vai Pini, fa' la tua scelta."
                b ON "E lei allora, sergente?"
                a ON "Sceglierò."
                a ON "È quello che fanno gli uomini, no?"
                a ON "Scegliere."
                $ s20boh = True
                jump mese19

label mese19:
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, channel='sound')
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n19 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/19 TEDESCHI_1.mp3"
    centered "{size=48}{cps=18}- TEDESCHI -\nAdesso, noi che ce li siamo trovati di fronte,\nsappiamo che non sono invincibili.\nSono esseri umani, coraggiosi e vili\ncome gli uomini di tutto il mondo.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c19 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    scene bg19 2 onlayer master
    show echarback onlayer master
    with fade
    play music "audio/19_documenti.mp3"
    d ON "Papier, bitte..."
    d ON "PAPIER, BITTE!"
    scene bg19_HALFW onlayer master
    show bg19_HALFP onlayer master
    show s19 5 onlayer master
    show echarback_still onlayer master
    show dchar onlayer master
    show deye onlayer master
    show dmouth OFF onlayer master

    d ON "Italiener!"
    scene bg19_HALFW onlayer master
    show bg19_HALFP onlayer master
    show cloud1 onlayer master
    show cloud2 onlayer master
    show cloud3 onlayer master
    show cloud4 onlayer master
    show s19 1 onlayer master
    show dchar onlayer master
    show deye onlayer master
    show dmouth OFF onlayer master
    show echar onlayer master
    show eeye onlayer master
    show emouth OFF onlayer master
    with dissolve
    e ON "Di... dice a me?"
    d ON "Papier, bitte... Schnell!"
    e ON "Va bene, va bene... Scusa!"
    e ON "Volevo dire... mi scusi."
    d ON "Wie heißen Sie?"
    e OFF "...?"
    d OFF "..."
    d ON "Nome."
    e ON "Giuseppe."
    d ON "Ah, Giuseppe..."
    d ON "\"Giuseppe Meazza\"!"
    e ON "Eh, magari..."
    e ON "Anche se adesso gioca nel Varese, il Pepin è sempre il migliore!"
    e ON "Pensa che da ragazzo mio papà giocava con lui al campetto qui a Greco."
    d OFF "..."
    show s19_4 onlayer master
    d ON "Papier, bitte..."
    $ ui.timer(1.5, ui.jumps("mese19_02"))
    menu:
        d "Papier, bitte..."
        "Questo vuole controllarmi i documenti... >>":
            $ calcio = False
            jump mese19_02
    label mese19_02:
    $ ui.timer(1.5, ui.jumps("mese19_03"))
    menu:
        d "Papier, bitte..."
        "Questo vuole controllarmi i documenti...":
            $ calcio = False
            jump mese19_a
        "Ma è un ragazzo, avrà la mia età... >>":
            jump mese19_b
    label mese19_03:
    $ ui.timer(1.5, ui.jumps("mese19_04"))
    menu:
        d "Papier, bitte..."
        "Questo vuole controllarmi i documenti...":
            $ calcio = False
            jump mese19_a
        "Ma è un ragazzo, avrà la mia età...":
            jump mese19_b
        "... e se invece gli chiedessi... >>":
            jump mese19_b
    label mese19_04:
    $ ui.timer(1.5, ui.jumps("mese19_05"))
    menu:
        d "Papier, bitte..."
        "Questo vuole controllarmi i documenti...":
            $ calcio = False
            jump mese19_a
        "Ma è un ragazzo, avrà la mia età...":
            jump mese19_b
        "... e se invece gli chiedessi...":
            jump mese19_b
        "... Ti piace il calcio? >>":
            jump mese19_b
    label mese19_05:
    $ ui.timer(1.5, ui.jumps("mese19_06"))
    menu:
        d "Papier, bitte..."
        "Questo vuole controllarmi i documenti...":
            $ calcio = False
            jump mese19_a
        "Ma è un ragazzo, avrà la mia età...":
            jump mese19_b
        "... e se invece gli chiedessi...":
            jump mese19_b
        "... Ti piace il calcio?":
            jump mese19_b
        "Buona idea! >>":
            jump mese19_b
    label mese19_06:
    $ ui.timer(3.0, ui.jumps("mese19_05"))
    menu:
        d "Papier, bitte..."
        "Questo vuole controllarmi i documenti...":
            $ calcio = False
            jump mese19_a
        "Ma è un ragazzo, avrà la mia età...":
            jump mese19_b
        "... e se invece gli chiedessi...":
            jump mese19_b
        "... Ti piace il calcio?":
            jump mese19_b
        "Pessima idea... >>":
            $ calcio = False
            jump mese19_a
    label mese19_a:
        e ON "I documenti, sì..."
        show s19_2 behind eeye onlayer master
        show s19_3 behind eeye onlayer master
        with dissolve
        e ON "Sto andando a lavorare in fabbrica quindi..."
        e ON "Ce li ho qui..."
        e ON "Ora li prendo, eh..."
        e ON "... Einen momento..."
        jump mese19_bb
    label mese19_b:
        e ON "... Ti piace il calcio?"
        hide s19_4 onlayer master
        d ON "Calcio?"
        d ON "Fußball!"
        show mondiali behind s19 onlayer master at loop
        with dissolve
        d ON "Bello fußball!"
        d ON "Io parlo poco italiano."
        d ON "Io molto bravo calcio!"
    label mese19_bb:
        if calcio == False:
            d ON "Schnell, Giuseppe Meazza..."
        if calcio == True:
            d ON "Giuseppe Meazza... Campione del mondo!"
        if calcio == False:
            e ON "Ancora con questo Giuseppe Meazza..."
            e ON "Ma allora ti piace proprio il calcio!"
            e ON "Giuseppe Meazza... Campione del mondo!"
        e ON "E non una... due volte!"
        e ON "Pensa che al mondiale del '34 mio papà mi ha portato a San Siro a vedere la semifinale con l'Austria!"
        e ON "E peccato che voi l'abbiate persa con la Cecoslovacchia... Italia-Germania sarebbe stata una bella finale!"
        d OFF "...?"
        e ON "Ma quello era prima della guerra..."
        e ON "E oltre a tutto il resto, la guerra ci ha tolto pure il mondiale del '42!"
        hide s19_4 onlayer master
        d ON "Italien-Deutschland... Weltmeisterschaft..."
        d ON "Weltmeisterschaft sechs und vierzig! Quattro... sei!"
        e ON "Quattro-sei... Quarantasei?"
        e ON "Il mondiale del '46?!"
        d ON "Sì... Tu, Italien... io, Deutschland!"
        e ON "Ho capito! Ci vediamo al prossimo mondiale, io Italia, tu Germania!"
        d ON "Ja, Italia-Germania! Finale campione del mondo!"
        e ON "Magari, magari..."
        e OFF "..."
        d OFF "..."
        e ON "Allora..."
        menu:
            e "Allora..."
            "... Io vado, amico.":
                jump mese19_aa
            "... Ecco i documenti.":
                jump mese19_c
        label mese19_aa:
            e ON "... Io vado, amico."
            e ON "Ci vediamo al mondiale del '46!"
            d OFF "..."
            show black behind s19 onlayer master
            show s19_4 onlayer master
            d ON "Italiener!"
            d ON "No papier?"
            e ON "Ma... Io credevo..."
            d ON "Tu, venire con me."
            e ON "Ma..."
            e ON "No, aspetta!"
            e ON "Ce li ho i documenti!"
            e ON "CE LI HO!"
            scene black onlayer master
            with fade
            d ON "... SCHNELL!"
            $ s19bad = True
            jump mese18
        label mese19_c:
            e ON "... Ecco i documenti."
            e ON "Cioè, un attimo che li cerco..."
            e ON "Einen momento, eh..."
            d ON "Ah... Italiener!"
            d ON "Dieses Mal drücke ich noch einmal beide Augen zu."
            e OFF "...?"
            d ON "Tu... andare!"
            e ON "... Posso andare?"
            d ON "Andare, andare."
            e OFF "..."
            e ON "... Grazie."
            d ON "Bitteschön..."
            scene black onlayer master
            with fade
            d ON "... Giuseppe Meazza!"
            $ s19good = True
            jump mese18



label mese18:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n18 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/18 PIPPO_1.mp3"
    centered "{size=48}{cps=18}- PIPPO -\nIl suo non sembra un rumore di motori,\nma l’ansito di un mostruoso animale.\nE fin che il battito delle sue grosse ali non si affievolisce\ntratteniamo il respiro.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c18 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    play music "audio/18_pippo.mp3"
    scene s18pelle onlayer master
    show s18 1 onlayer master
    show cchar onlayer master
    show ceye onlayer master
    show cmouth OFF onlayer master
    with dissolve
    c ON "Orzolino..."
    c ON "Non riesco a dormire..."
    menu:
        c "Non riesco a dormire..."
        "Posso tenere la luce accesa?":
            jump mese18_a
        "Mi racconti una storia?":
            jump mese18_b
    label mese18_a:
    c ON "Posso tenere la luce accesa?"
    c ON "Ho un po' paura..."
    scene bg_Stelle onlayer master
    show c2char onlayer master
    show c2eye onlayer master
    show c2mouth OFF onlayer master
    show braccia onlayer master
    with dissolve
    c2 ON "Non ricordi cosa ti ha detto nonna Linda?"
    c2 ON "\"Guarda che se non spegni la luce arriva il Pippo\"!"
    c ON "Il Pippo..."
    c ON "Mi racconti la storia del Pippo?"
    c2 ON "E va bene..."
    c2 ON "Il Pippo è uno strano aeroplano."
    show aereopiccolo behind c2char onlayer master at pippo
    show sparo behind aereopiccolo onlayer master at mitra
    with dissolve
    c2 ON "Un aeroplano che passa sopra casa nostra tutte le notti."
    c2 ON "E se vede una luce accesa..."
    c2 ON "BUM! Ci butta una bomba!"
    jump mese18_bb

    label mese18_b:
    c ON "Mi racconti una storia?"
    c ON "Mi racconti la storia del Pippo?"
    c2 ON "E va bene..."
    c2 ON "Il Pippo è uno strano aeroplano."
    show aereopiccolo behind s18 onlayer master at pippo
    show sparo behind aereopiccolo onlayer master at mitra
    with dissolve
    c2 ON "Un aeroplano che passa sopra casa nostra tutte le notti."
    c2 ON "E se vede una luce accesa..."
    c2 ON "BUM! Ci butta una bomba!"
    label mese18_bb:
    scene s18pelle onlayer master
    show s18 1 onlayer master
    show cchar onlayer master
    show ceye onlayer master
    show cmouth OFF onlayer master
    with dissolve
    c ON "Orzolino..."
    menu:
        c "Orzolino..."
        "Tu l'hai mai vista una bomba?":
            $ luce = True
            jump mese18_c
        "Perché il Pippo butta le bombe?":
            jump mese18_d

    label mese18_d:
    c ON "Perché il Pippo butta le bombe?"
    c2 ON "Mistero!"
    c ON "Ma chi è il Pippo?"
    c2 ON "Nessuno lo sa!"
    c ON "Ma insomma... il Pippo è buono o è cattivo?"
    scene bg_Stelle onlayer master
    show c2char onlayer master
    show c2eye onlayer master
    show c2mouth OFF onlayer master
    show braccia onlayer master
    show aereopiccolo behind c2char onlayer master at pippo
    show sparo behind aereopiccolo onlayer master at mitra
    with dissolve
    c2 ON "C'è chi dice che sia buono, chi cattivo..."
    c2 ON "Chi che sia tedesco, chi italiano, chi americano o inglese..."
    c2 ON "Chi piccolo e chi grande, che abbia uno o due motori, le bombe o la mitragliatrice..."
    c ON "Davvero?!"
    c2 ON "Davvero."
    c ON "Ma com'è possibile?!"
    c ON "Che il Pippo sia buono e cattivo e tedesco e americano e grande e piccolo..."
    c2 ON "Il Pippo è tutto e niente."
    c2 ON "Tutti e nessuno."
    c2 ON "Il Pippo..."
    c2 ON "... è la guerra."
    c2 ON "Come il sole o la pioggia o il vento o la neve."
    c2 ON "Semplicemente... c'è."
    jump mese18_cc

    label mese18_c:
    c ON "Tu l'hai mai vista una bomba?"
    c ON "Io sì!"
    c ON "Cioè... Da lontano."
    c ON "Però non fanno mica paura, le bombe!"
    show aereopiccolo behind s18 onlayer master at pippo2
    show sparo behind aereopiccolo onlayer master at mitra2
    with dissolve
    c ON "Anzi, sono belle... Fanno delle belle luci!"
    c ON "E io ho paura del buio, non delle luci."
    c2 ON "Non ricordi cosa ti ha detto nonna Linda?"
    c2 ON "\"Le bombe fanno i morti\"!"
    c2 ON "Bisogna avere paura delle bombe!"
    label mese18_cc:
    c ON "Ho capito..."
    c OFF "..."
    scene s18pelle onlayer master
    show s18 1 onlayer master
    show cchar onlayer master
    show ceye onlayer master
    show cmouth OFF onlayer master
    with dissolve
    c ON "Però, Orzolino..."
    label mese18_c0:
    menu:
        "Se spengo la luce..." if topic1 == False:
            jump mese18_e
        "Se accendo la luce..." if topic2 == False:
            jump mese18_f
        "Ma allora..." if topic1 and topic2 == True:
            jump mese18_g
    label mese18_e:
    $ topic1 = True
    scene black onlayer master
    with fade
    c ON "Se spengo la luce..."
    c ON "... ho paura del buio."
    jump mese18_c0
    label mese18_f:
    $ topic2 = True
    scene s18pelle onlayer master
    show s18 1 onlayer master
    show cchar onlayer master
    show ceye onlayer master
    show cmouth OFF onlayer master
    with dissolve
    c ON "Se accendo la luce..."
    c ON "... arriva il Pippo e mi butta una bomba."
    if luce == True:
        c ON "E bisogna aver paura delle bombe."
        c ON "... Anche se fanno delle belle luci!"
    jump mese18_c0
    label mese18_g:
    scene bg_Stelle onlayer master
    show c2char onlayer master
    show c2eye onlayer master
    show c2mouth OFF onlayer master
    show braccia onlayer master
    with dissolve
    c ON "Ma allora..."
    c ON "Come faccio a non avere paura?"
    c2 "..."
    label mese18_h:
    $ ui.timer(0.1, ui.jumps("mese18_i"))
    menu:
        "bombe":
            jump mese18_m
        "mamma":
            jump mese18_m
        "pippo":
            jump mese18_m
    label mese18_i:
    $ ui.timer(0.1, ui.jumps("mese18_l"))
    menu:
        "luce":
            jump mese18_m
        "morti":
            jump mese18_m
        "nonna":
            jump mese18_m
    label mese18_l:
    $ ui.timer(0.1, ui.jumps("mese18_h"))
    menu:
        "aereo":
            jump mese18_m
        "buio":
            jump mese18_m
        "guerra":
            jump mese18_m
    label mese18_m:
    c2 "..."
    c2 ON "Dormi, Benito."
    c2 ON "Ci sono qua io, per te."
    c "E per Bianca?"
    c2 ON "Nonna Linda ha fatto un angioletto anche per lei..."
    c "..."
    c "Grazie."
    c2 ON "È a questo che servono gli angeli custodi, giusto?"
    scene s18pelle onlayer master
    show s18 1 onlayer master
    show cchar onlayer master
    show ceye onlayer master
    show cmouth OFF onlayer master
    with dissolve
    c OFF "..."
    c ON "Giusto!"
    scene black onlayer master
    with fade
    c OFF "..."
    c ON "Orzolino..."
    scene s18pelle onlayer master
    show s18 1 onlayer master
    show cchar onlayer master
    show ceye onlayer master
    show cmouth OFF onlayer master
    with dissolve
    c ON "Un'ultima cosa..."
    c ON "Tu che sei il mio angelo custode..."
    c ON "Perché la mamma mi ha chiamato Benito?"
    scene bg_Stelle onlayer master
    show c2char onlayer master
    show c2eye onlayer master
    show c2mouth OFF onlayer master
    show braccia onlayer master
    with dissolve
    c2 ON "Non ricordi cosa ti ha detto nonna Linda?"
    c OFF "..."
    c2 ON "\"Per avere un cucchiaino di formaggio in più, alla mensa\"."
    jump mese17



label mese17:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n17 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/17 PAURA_2.mp3"
    centered "{size=48}{cps=15}- PAURA -\nChi dice di non averne è un bugiardo.\nNessuno di noi può giurare che sarà vivo domani.\nO anche stasera.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c17 onlayer master with fade

    $ renpy.pause(3.0, hard=True)
    play music "audio/17_borsa Nera.mp3" fadein 2.0
    scene bg20 onlayer master
    show s17_1 onlayer master
    show fchar onlayer master
    show feye onlayer master
    show fmouth OFF onlayer master
    with dissolve
    pause 0.2


    f ON "Oggi sarà un lunga giornata."
    f OFF "..."
    f ON "Questa guerra è una maledizione..."
    f ON "... ma devo impegnarmi il più possibile per aiutare il mio paese!"
    f OFF "..."
    f ON "Stavolta sono riuscito a portar giù dalla Svizzera un bel carico di sale da smerciare."
    f ON "40 chili... una bella conquista."
    f ON "Dovrebbe bastare ad almeno 4 famiglie per conservare il maiale, quest'inverno."

    hide s17_1 onlayer master
    hide fchar onlayer master
    hide feye onlayer master
    hide fmouth OFF onlayer master

    show gchar onlayer master
    show geye onlayer master
    show gmouth OFF onlayer master
    show s17_1 onlayer master
    show fchar onlayer master
    show feye onlayer master
    show fmouth OFF onlayer master
    with dissolve
    pause 3.0
    menu:
        f "Dovrebbe bastare ad almeno 4 famiglie per conservare il maiale, quest'inverno."
        "Come no, Giulio... Sempre che possano permetterselo!":
            $ bad1 = True
            $ badcounter +=1
            jump mese17_a
        "Bravo Giulio... Stai facendo la cosa giusta.":
            jump mese17_a

    label mese17_a:
    if bad1 == True:
        show fuoco behind s17_1 onlayer master
        $ isBurning = True
        g ON "Come no, Giulio... Sempre che possano permetterselo!"
    elif bad1 == False:
        g ON "Bravo Giulio... Stai facendo la cosa giusta."
    g ON "... Non credi?"
    f ON "Io faccio il possibile... quello è il prezzo del mio lungo viaggio."
    f ON "... e del rischio che corro, a fare lo spallone."
    g ON "Già... Se non avessi fatto il contrabbandiere, avresti fatto l'emigrato... Chissà dove."
    g ON "... Un bel rischio comunque."
    f ON "Ho fatto la mia scelta. E non me ne pento. Sono un lavoratore, come tutti gli altri."
    g ON "Come tutti gli altri? Sul giornale non ho letto di aumenti di stipendio per gli operai in Pirelli..."
    g ON "... E invece il prezzo del pane è 8 volte quello di 5 anni fa."
    g ON "Se posso essere sincero... non è tanto il viaggio, ma è il tuo stomaco che brontola troppo."
    g ON "Ma forse mi sbaglio..."
    menu:
        g "Ma forse mi sbaglio..."
        "Ti ricordi... {i}quel{/i} giorno?":
            jump mese17_a2
        "Hai forse dimenticato... {i}quel{/i} giorno?":
            $ bad2 = True
            $ badcounter +=1
            jump mese17_a2

    label mese17_a2:
    if bad2 == True:
        g ON "Hai forse dimenticato... {i}quel{/i} giorno?"
        if isBurning == False:
            show fuoco behind s17_1 onlayer master
            $ isBurning = True
    elif bad2 == False:
        g ON "Ti ricordi... {i}quel{/i} giorno?"
    f ON "{i}Quel{/i} giorno..."
    g ON "Quella donna se lo ricorda bene..."
    f ON "Quella donna..."
    f ON "Capelli lunghi, mossi..."
    f ON "Occhi chiari..."
    g ON "Proprio lei."
    g ON "{i}Quel{/i} giorno, quella donna non ha potuto dare da mangiare a suo figlio..."
    g ON "E sai perché?"
    f ON "Perché...?"
    g ON "Perché le mancavano 3 lire e 20 per comprare il riso che avevi portato giù in città."
    f ON "Ma non potevo fare altrimenti!"
    f ON "Se concedo un favore a uno, poi tutti pretenderanno lo stesso!"
    f ON "E sono tempi duri per tutti, lo sai."
    menu:
        f "E sono tempi duri per tutti, lo sai."
        "... Specie per quella donna. Suo figlio è morto ieri.":
            $ bad3 = True
            $ badcounter +=1
            jump mese17_a3
        "... Sono tempi duri per tutti... Lo so.":
            jump mese17_a3

    label mese17_a3:
    if bad3 == True:
        g ON "... Specie per quella donna. Suo figlio è morto ieri."
        if isBurning == False:
            show fuoco behind s17_1 onlayer master
            $ isBurning = True
    elif bad3 == False:
        g ON "... Sono tempi duri per tutti... Lo so."
    f ON "... Ma quel bambino non ce l'avrebbe fatta comunque, anche con un po' di riso in più."
    g ON "Beh..."
    g ON "Forse ora potrai coprire il suo corpo col tuo bel cappotto di lana."
    f ON "Era spacciato fin dall'inizio..."
    g ON "... O magari comprare un mazzo di fiori per la famiglia."
    f ON "... Fin dall'inizio di questa maledetta guerra."
    g ON "... Sono certo che apprezzeranno il pensiero."
    f ON "Lui, come tanti altri."
    f OFF "..."
    if badcounter >=2:

        scene black onlayer master with fade
        g "Lui, come anche te."
        $ renpy.pause(1.0, hard=True)
        g "... La pistola è sul tavolo."
        menu:
            g "... La pistola è sul tavolo."
            "Premi il grilletto":
                $ s17bad = True
                jump mese17_a4

    elif badcounter <2:
        g ON "Non pensarci... Non ricapiterà."
        g OFF "..."
        menu:
            g "... Sbrigati, stai facendo tardi."
            "Esci di casa":
                $ s17good = True
                jump mese17_b4

    label mese17_a4:
    stop music
    play sound "audio/sound/184382_qubodup_mortar-shots_def.mp3"
    $ renpy.pause(4.0, hard=True)
    jump mese16

    label mese17_b4:
    scene black onlayer master with fade
    g "..."
    jump mese16



label mese16:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n16 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/16 NOTTE_1.mp3"
    centered "{size=48}{cps=13}- NOTTE -\nCi sono notti brevissime e notti eterne.\nCiascuno di noi conserva il ricordo\ndi una notte terribile.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c16 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    scene bg20 onlayer master
    play music "audio/16_binario21.mp3"
    menu:
        "\"C'è Auschwitz, quindi non può esserci Dio. Non trovo una soluzione al dilemma. La cerco, ma non la trovo\".":
            $ levi = True
            $ s16god = True
            jump mese16_00
        "\"L'affermazione più profonda che sia mai stata pronunciata a proposito di Auschwitz non fu affatto un'affermazione, ma una risposta. La domanda: 'Ditemi, dov'era Dio, ad Auschwitz?'. E la risposta: 'E l'uomo, dov'era?'\"":
            $ styron = True
            $ s16man = True
            jump mese16_00

    label mese16_00:
    scene hchar onlayer master
    show ichar onlayer master
    show s16 onlayer master
    show heye onlayer master
    show ieye onlayer master
    show hmouth OFF onlayer master
    show imouth OFF onlayer master
    with fade
    menu:
        "Dove, Padre?":
            jump mese16a
        "Come, Padre?":
            jump mese16b
        "Quando, Padre?":
            jump mese16c
        "Perché, Padre?":
            jump mese16d

    label mese16a:
    h ON "Dove, Padre?"
    i ON "Prego, figliolo?"
    h ON "Mi chiedevo \"dove\", Padre."
    h ON "Dove sia diretto quel treno in partenza dal Binario 21."
    jump mese16e

    label mese16b:
    h ON "Come, Padre?"
    i ON "Prego, figliolo?"
    h ON "Mi chiedevo \"come\", Padre."
    h ON "Come siamo arrivati fino a qui."
    i ON "Fino a qui... in guerra, intendi?"
    h ON "Intendo fino a questo binario."
    h ON "Il Binario 21."
    jump mese16e

    label mese16c:
    h ON "Quando, Padre?"
    i ON "Prego, figliolo?"
    h ON "Mi chiedevo \"quando\", Padre."
    i ON "Quando... finirà la guerra, intendi?"
    h ON "Quando partirà quel treno."
    h ON "Quello al Binario 21."
    jump mese16e

    label mese16d:
    h ON "Perché, Padre?"
    i ON "Prego, figliolo?"
    h ON "Mi chiedevo \"perché\", Padre."
    h ON "Perché tutte quelle persone in fila al Binario 21."
    jump mese16e

    label mese16e:
    i ON "Ma...?"
    i OFF "..."
    i ON "In questa stazione i binari ordinari arrivano solo fino al 20!"
    i ON "Il Binario 21... non esiste."
    h ON "Oh, certo."
    h ON "\"Il Binario 21 non esiste\"."
    h ON "Mi perdoni... Non era mia intenzione darle disturbo."
    i ON "Nessun disturbo, figliolo."
    i ON "Mi chiamo Padre Alfonso."
    h ON "Kostoyed."
    h ON "Piacere di conoscerla."
    i ON "In Stazione Centrale per andare o per venire?"
    menu:
        i "In Stazione Centrale per andare o per venire?"
        "Vado.":
            jump mese16_f
        "Vengo.":
            jump mese16_g

    label mese16_f:
        h ON "Vado."
        h ON "Vado via da Milano, via dall'Italia, via dall'Europa."
        h ON "Questo vecchio continente è perduto."
        jump mese16_h

    label mese16_g:
        h ON "Vengo."
        h ON "Vengo a Milano per liberare l'Italia, per liberare l'Europa."
        h ON "Questo vecchio continente merita di essere salvato."
        jump mese16_h

    label mese16_h:
        h ON "E lei, Padre?"
        i ON "Io... resto."
        i ON "Restare è il mio dovere."
        h ON "Il suo dovere, capisco."
        h OFF "..."
        h ON "E mi dica..."
        h ON "Anche chiudere gli occhi è un suo dovere, Padre?"
        i ON "Non... non capisco."
        h ON "Non finga di non vedere ciò che sta succedendo questa notte."
        h ON "Questa notte terribile."
        h ON "Il Binario 21 potrà anche essere segreto, nascosto, sotterraneo, invisibile..."
        h ON "Potremo scoprirlo solo al termine di questa guerra."
        h ON "Ma sappiamo entrambi che esiste."
        show auschwitz fila behind s16 onlayer master at loopfila
        with dissolve
        h ON "... Vede?"
        i ON "..."
        i ON "Vedo."
        h ON "E sappiamo benissimo chi sono e dove vanno tutte quelle persone."
        show auschwitz treno behind s16 onlayer master at looptreno
        with Dissolve(5.0)
        h ON "\"Oggi agisco in accordo con la volontà del Creatore Onnipotente...\""
        h ON "\"... difendendomi dagli Ebrei, combatto per l'opera del Signore\"."
        h ON "Sbaglio o il Signore Onnipotente di cui parla il Führer è il suo stesso Signore Onnipotente... Padre?"
        i ON "Sbagli."
        i ON "\"Il bolscevismo è un figlio illegittimo del Cristianesimo. L'uno e l'altro sono un'invenzione degli Ebrei\"."
        i ON "Se intendi citare Adolf Hitler, figliolo, fallo con cognizione di causa."
        i ON "Agli occhi dei nazisti, siamo tutti fratelli."
        i ON "Bolscevichi come te, e cristiani come me."
        i ON "E tutti fratelli delle persone su quel treno."
        i ON "Siamo tutti Ebrei."
        hide auschwitz onlayer master
        show cancello1 onlayer master
        show cancello2 onlayer master
        show cancello3 onlayer master
        show cancello4 onlayer master
        with dissolve
        $ renpy.pause(2.5, hard=True)
        if levi == True:
            h ON "Con la differenza che noi siamo ancora vivi, Padre."
            i ON "Ma anche quelle persone lo sono! Li stanno trasferendo, certo..."
            h ON "\"Deportando\". Li stanno deportando."
            i ON "Deportando, d'accordo, ma se Dio vuole..."
            h ON "\"Dio\"?"
            h ON "Non c'è un Dio alla stazione d'arrivo di quel treno."
            h ON "Non il loro né il suo, Padre."
            i "..."
            h ON "Ha ragione a restare in silenzio, Padre."
            h ON "Ma ricordi."
            h ON "Quando ci allonteneremo da qui, da questo binario, avremo il dovere di parlare."
            i "..."
            i ON "Amen."
            "{i}\"C'è Auschwitz, quindi non può esserci Dio. Non trovo una soluzione al dilemma. La cerco, ma non la trovo\".{/i} "
            "{i}Primo Levi{/i}"
            jump mese2
        elif styron == True:
            h "..."
            i ON "C'è un antico libro, attribuito a Re Salomone, che fa parte sia della Tanakh ebraica, sia della Bibbia cristiana, e che mi è caro."
            i ON "Si chiama Qoelet, o l'Ecclesiaste."
            h ON "Lo conosco bene... \"Vanitas vanitatum\"."
            i ON "Non solo."
            i ON "Ripeti con me, figliolo."
            i ON "C'è un tempo per nascere e un tempo per morire..."
            h ON "Un tempo per uccidere e un tempo per guarire..."
            i ON "Un tempo per cercare e un tempo per perdere..."
            h ON "Un tempo per tacere e un tempo per parlare..."
            i ON "Un tempo per la guerra, e un tempo per la pace."
            h "..."
            h ON "\"Un tempo per la pace\"..."
            h ON "Dopo la guerra, dopo questo binario, dopo tutto questo... Verrà il tempo, Padre?"
            i ON "Verrà."
            i ON "Dipende solo da noi."
            "{i}\"L'affermazione più profonda che sia mai stata pronunciata a proposito di Auschwitz non fu affatto un'affermazione, ma una risposta. La domanda: 'Ditemi, dov'era Dio, ad Auschwitz?'. E la risposta: 'E l'uomo, dov'era?'\"{/i}"
            "{i}William Clark Styron{/i}"
            jump mese2



label mese2:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n15 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/2 FUGA_2.mp3"
    centered "{size=48}{cps=18}- FUGA -\nLa nostra non è una guerra classica.\nPerciò la fuga vi è ammessa,\nne è anzi la prima regola.\nLa nostra è una continua fuga,\nma allo stesso tempo è un continuo attacco.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c15 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    scene black onlayer master with fade


    "Il 10 febbraio 1944, un gruppo clandestino della V sezione aeronautica della Breda organizza un attentato alla Casa del Fascio di Sesto San Giovanni al Rondò."
    "Il gruppo è composto da 8 persone, a capo delle quali è Oreste Ghirotti, ex operaio milanese, ora titolare di un negozio di frutta."
    "Il palo è Carlo Talamucci, tecnico Breda, residente proprio di fronte alla Casa del Fascio."
    "Un motofurgone gappista consegna le armi per l'azione in Piazza 4 novembre."
    "Un partigiano, infiltrato nel Partito Fascista Repubblicano, ha il compito di lasciare la porta della Casa del Fascio aperta dietro di sé, per consentire l'azione."
    "Due giorni dopo l'attentato, l'infiltrato viene arrestato."
    play music "audio/2_assalto.mp3" fadein 2.0
    "E torturato."

    scene tortura2 onlayer master
    show umouth OFF onlayer master
    with fade
    x1 "PARLA!"
    x1 "Parla, dicci come avete fatto!"
    show tortura0 onlayer master
    x1 "Dicci tutto ciò che sai, cane d'un partigiano!"
    jump mese2_domanda1

label mese2_domanda1:
    x1 "Quanti eravate?!"
    menu:
        x1 "Quanti eravate?!"
        "Eravamo in 8.":
            jump mese2_vero1
        "Andate al diavolo, maiali!":
            jump mese2_insulto



label mese2_insulto:
    $ vite -=1
    x ON "Andate al diavolo, maiali!"
    x1 "..."
    x1 "Forse non ci siamo capiti..."
    x1 "Se fai il duro, peggiorerai solo la tua situazione..."
    x1 "La tua..."
    x1 "... E forse anche quella della tua famiglia!"
    x "..."
    x1 "Chissà cosa potrebbe accadere a te..."
    x1 "... E a loro."
    x "..."
    x1 "Forza, riproviamo."
    jump mese2_domanda1bis

label mese2_domanda1bis:
    x1 "Quanti eravate?!"
    menu:
        x1 "Quanti eravate?!"
        "Eravamo in 10.":
            jump mese2_mezzo1
        "Non ricordo... pochi.":
            jump mese2_falsoa
        "Eravamo in 8.":
            jump mese2_vero1
        "Eravamo in 4.":
            jump mese2_falsob



label mese2_mezzo1:
    x ON "Eravamo in 10."
    x1 "..."
    x1 "Ne sei certo?"
    x "..."
    x1 "Va bene, voglio fidarmi."
    x1 "Verificheremo comunque, stanne certo."
    x1 "... e in caso andremo a fare meglio i conti..."
    x1 "... direttamente a casa tua."
    x "..."
    x1 "È tutto più facile quando si collabora."
    x1 "Procediamo."

    jump mese2_domanda2
label mese2_vero1:
    x ON "Eravamo in 8."
    x1 "..."
    x1 "... 8 uomini dei vostri, per 3 dei nostri."
    x1 "Non vi è andata troppo bene... potevate fare di meglio, in 8."
    x "..."
    x1 "Visto?"
    x1 "Non è difficile quando si collabora."
    x1 "Dovresti però chiarirmi ancora alcune cose..."
    x1 "Apri bene le orecchie."
    play music "audio/2_assalto.mp3" fadein 2.0
    $ verocounter +=1
    jump mese2_domanda2

label mese2_falsoa:
    $ vite -=1
    x ON "Non ricordo... pochi."
    jump mese2_falsocontinue

label mese2_falsob:
    $ vite -=1
    x ON "Eravamo in 4."
    jump mese2_falsocontinue

label mese2_falsocontinue:
    x1 "..."
    if vite ==0:
        jump mese2_morte
    x1 "Non è possibile."
    x1 "I testimoni affermano di aver visto che eravate circa una decina..."
    x1 "Perché tenti di fregarci..?"
    x1 "Perché devi rendere tutto così difficile?"
    x1 "Chissà cosa ne pensano i tuoi compagni..."
    x1 "Se sapessero che dalle tue risposte..."
    x1 "... dipende anche la loro vita!"
    x1 "Sarebbero d'accordo con me."
    x1 "Non trovi?"
    x1 "Riproviamoci."
    jump mese2_domanda1bis


label mese2_domanda2:
    x1 "..."
    x1 "Se tu hai lasciato la porta aperta perché gli altri potessero entrare e fare quella strage..."
    x1 "... Chi ha dato il segnale?"
    x1 "Stavate forse sorvegliando la Casa del Fascio?"
    x1 "Dimmi... illuminami!"
    jump mese2_domanda2bis

label mese2_domanda2bis:
    menu:
        x1 "Chi ha dato il segnale?"
        "Non lo conosco! So solo che vive lì vicino.":
            jump mese2_mezzo2
        "Il palo era Carlo Talamucci, tecnico Breda.":
            jump mese2_vero2
        "Era un nuovo membro, un calzolaio della zona.":
            jump mese2_falso2
        "...":
            jump mese2_falso2bis


label mese2_vero2:
    x ON "Il palo era Carlo Talamucci, tecnico Breda."
    x1 "..."
    x1 "Carlo Talamucci, sì..."
    x1 "Lo teniamo d'occhio da un po'..."
    x1 "Facciamo partire le indagini..."
    x1 "Lo andremo a prendere a breve."
    x1 "Ti stai dimostrando una risorsa utile..."
    x1 "Come ti fa sentire?"
    x "..."
    x ON "Male."
    x1 "Su su, non roviniamo questa piacevole discussione..."
    x1 "Dicci..."
    $ verocounter +=1
    jump mese2_domanda3
label mese2_mezzo2:
    x ON "Non lo conosco! So solo che vive lì vicino."
    x1 "..."
    x1 "... abitava lì vicino?"
    x1 "Probabilmente spiava al sicuro da casa sua..."
    x1 "Come un topo che teme l'arrivo del gatto."
    x1 "Bene, ispezioneremo gli appartamenti."
    x1 "Le finestre che si affacciano sulla Casa del Fascio non sono molte..."
    x1 "Che dire..."
    x1 "Continuiamo così, e forse rivedrai l'alba di domani..."
    x1 "Forse..."

    jump mese2_domanda3
label mese2_falso2:
    $ vite -=1
    x ON "Era un nuovo membro, un calzolaio della zona."
    x1 "..."
    if vite ==0:
        jump mese2_morte
    x1 "Un calzolaio in zona?"
    x1 "Strano, frequento regolarmente la Casa del Fascio e non ho mai visto un calzolaio da quelle parti."
    x1 "Ne sei proprio sicuro...?"
    x1 "O forse devo rinfrescarti la memoria sul peso delle tue azioni?"
    x1 "Forse dovrei semplicemente ordinare l'esecuzione di un paio di gappisti."
    x1 "O forse ho sentito male ciò che mi hai detto..."
    x1 "Con tutti i bombardamenti di quei maledetti americani, le mie orecchie fischiano di continuo."
    x1 "Riproviamoci."
    jump mese2_domanda2bis

label mese2_falso2bis:
    $ vite -=1
    if vite ==0:
        jump mese2_morte
    x1 "..."
    x1 "... Perché?"
    x1 "... Non vuoi proprio bene ai tuoi cari."
    x1 "Mi pare evidente."
    x1 "Mi stai facendo innervosire, sai?"
    x1 "Forza, rispondi!"
    jump mese2_domanda2bis



label mese2_domanda3:
    x1 "..."
    x1 "Con questa domanda puoi salvare molte persone, sai?"
    x1 "Molte al prezzo di una."
    x1 "Ultima domanda, ultima domanda..."
    jump mese2_domanda3bis

label mese2_domanda3bis:
    menu:
        x1 "Chi ha organizzato l'attentato?"
        "So solo che è un ex operaio, già indagato in passato.":
            jump mese2_mezzo3
        "Il responsabile è Oreste Ghirotti. Lasciatemi andare ora!":
            jump mese2_vero3
        "Non so chi sia, ho ricevuto direttive da terzi.":
            jump mese2_falso3



label mese2_mezzo3:
    x ON "So solo che è un ex operaio, già indagato in passato."
    x1 "..."
    x1 "Un ex operaio?"
    x1 "Mi prendi in giro?"
    x1 "Sai quanti ne abbiamo presi? Sai quanti ne abbiamo portati via?"
    x1 "Quelli che sono stati così fortunati da perdere solamente il lavoro non sono molti, è vero."
    x1 "Ma questo non restringe molto il campo."
    x ON "Non so altro, lo giuro!"
    x1 "Che tu sappia ancora qualcosa mi pare evidente..."
    x1 "Ma potremmo andare avanti per un mese."
    x1 "Il tempo a nostra disposizione è finito."

    jump mese2_verifica
label mese2_vero3:
    x ON "Il responsabile è Oreste Ghirotti. Lasciatemi andare ora!"
    x1 "..."
    x1 "Ghirotti? Ci mancava solo un pretesto per acciuffare quel maledetto."
    x1 "Grazie... Grazie davvero!"
    x "... Lasciatemi andare, vi ho detto tutto."
    x1 "... A tempo debito, a tempo debito."
    x1 "Ci hai detto molto, e ti ringraziamo..."
    $ verocounter +=1

    jump mese2_verifica
label mese2_falso3:
    $ vite -= 1
    x ON "Non so chi sia, ho ricevuto direttive da terzi."
    x1 "..."
    if vite ==0:
        jump mese2_morte
    x1 "Da terzi?"
    x1 "Chi sono? Di chi stai parlando?"
    x1 "Non farmi perdere la pazienza."
    x1 "Forza, fuori i nomi."
    x1 "Avanti!"
    jump mese2_domanda3bis


label mese2_verifica:
    if verocounter >=2:
        jump mese2_verofin
    elif verocounter <2:
        jump mese2_falsofin

label mese2_falsofin:
    x1 "Bene..."
    x1 "Credo proprio che le nostre indagini andranno meglio con gli elementi che ci hai dato."
    x1 "Ti faremo avere un comodo letto in prigione."
    x1 "Forse ti fucileranno in settimana..."
    x ON "COSA?!"
    x1 "Manderemo una lettera ai tuoi cari, non preoccuparti!"
    x ON "Ma vi ho detto quello che sapevo!"
    x1 "Non era abbastanza."
    x ON "Non è mai abbastanza per voi..."
    x1 "Forse..."
    x1 "Forse."
    x "..."
    x1 "Ma i morti non si lamentano."
    $ s2prisongood = True
    jump mese14

label mese2_verofin:
    x1 "Ci hai detto molto..."
    x1 "Sorprendente direi."
    x ON "O vile...?"
    x1 "Non essere duro con te stesso."
    x1 "Non sei il primo che parla."
    x1 "E non sarai di certo l'ultimo."
    x ON "...Posso andare?"
    x1 "Andare dove?"
    x1 "Abbiamo un comodo letto in cella che ti aspetta."
    x1 "Ti piacerà, vedrai."
    x ON "Cosa?!"
    x "Ma vi ho detto tutto quello che sapevo!"
    x1 "E noi abbiamo molto apprezzato! Infatti non verrai fucilato pubblicamente..."
    x1 "... A differenza delle persone che ci hai segnalato!"
    x ON "..."
    x1 "Grazie ancora..."
    x1 "Grazie!"
    $ s2prisonbad = True
    jump mese14

label mese2_morte:
    x1 "Basta!"
    x1 "Mi hai stancato."
    x1 "PORTATELO VIA!"
    x1 "Torturatelo. Fategli dire ogni cosa."
    x1 "Ogni"
    x1 "Singola"
    x1 "Cosa."
    x1 "Parlerai..."
    x1 "Te lo giuro."
    x1 "Parlerai!"
    $ s2torture = True
    jump mese14






label mese14:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n14 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/14 CITTA'_1.mp3"
    centered "{size=48}{cps=18}- CITTÀ -\nQualcuno dei nostri c’è entrato, di notte,\ne gli è parso di essere finito in un labirinto, in una trappola.\nEppure buona parte delle persone che l’abitano è con noi.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c14 onlayer master with fade

    $ renpy.pause(3.0, hard=True)
    play music "audio/14_scioperoGenerale.mp3" fadein 2.0
    scene s14 pelle onlayer master
    show s14sfondo 2 onlayer master
    show s14_capelli onlayer master
    show keye onlayer master
    show kmouth OFF onlayer master
    with dissolve
    k ON "Oggi..."
    k ON "Oggi è il giorno dello Sciopero."
    k ON "Il Comitato di Agitazione ha dato l'ordine..."
    k ON "... ed eccoci qui."
    k ON "Certo..."
    k ON "Mi chiedo quale sia veramente la cosa giusta da fare..."
    jump mese14_loop

    label mese14_loop:
        menu:
            k "Mi chiedo quale sia veramente la cosa giusta da fare..."
            "Meglio scioperare":
                if ScioperoSi == True:
                    jump mese14_a0
                $ ScioperoSi = True
                jump mese14_a
            "Meglio non scioperare":
                if ScioperoNo == True:
                    jump mese14_b0
                $ ScioperoNo = True
                jump mese14_b
            "... Ma perché stiamo scioperando?" if ScioperoSi and ScioperoNo == True:
                jump mese14_c

label mese14_a:
    k ON "Meglio scioperare..."
    k OFF "..."
    k ON "Meglio...?"
    k ON "Ma se sciopero..."
    k ON "Ci sospenderanno la paga."
    k ON "Ci arresteranno."
    k ON "Ci deporteranno."
    k ON "E Benito e Bianca come faranno a mangiare?"
    k ON "Io come farò a mangiare?"
    k ON "... e mia madre? È anziana, e non più in salute."
    k ON "... Giovanni, spero che almeno tu abbia qualcosa da mettere sotto i denti..."
    k ON "... ovunque tu sia."
    jump mese14_a0

label mese14_a0:
    k ON "Forse scioperare..."
    k ON "... non è la soluzione migliore."
    jump mese14_loop

label mese14_b:
    k ON "Meglio non scioperare..."
    k OFF "..."
    k ON "Meglio...?"
    k ON "Ma se non sciopero..."
    k ON "Non cambierà mai nulla."
    k ON "La mia, la nostra situazione."
    k ON "La situazione di centinaia di operai."
    k ON "La situazione di migliaia di famiglie."
    k ON "La situazione di milioni di persone, in questo paese in guerra..."
    jump mese14_b0

label mese14_b0:
    k ON "Forse scioperare..."
    k ON "... è la soluzione migliore."
    jump mese14_loop

label mese14_c0:
    k "Sì, anche per questo."
    jump mese14_c00
label mese14_c:
    show s14 folla onlayer master at rivolta
    with dissolve
label mese14_c00:
    k ON "... Ma perché stiamo scioperando?"
    k ON "Perché stiamo davvero scioperando?"
    k ON "Per chi, per cosa?"
    jump mese14_c1

label mese14_c1:
    $ ui.timer(1.0, ui.jumps("mese14_scelta1"))
    menu:
        "Per i nostri figli... >>":
            jump mese14_c0
label mese14_scelta1:
    $ ui.timer(1.0, ui.jumps("mese14_scelta2"))
    menu:
        "Per i nostri figli...":
            jump mese14_c0
        "Per le nostre madri... >>":
            jump mese14_c0
label mese14_scelta2:
    $ ui.timer(1.0, ui.jumps("mese14_scelta3"))
    menu:
        "Per i nostri figli...":
            jump mese14_c0
        "Per le nostre madri...":
            jump mese14_c0
        "Per i nostri mariti... >>":
            jump mese14_c0
label mese14_scelta3:
    $ ui.timer(2.0, ui.jumps("mese14_scelta4"))
    menu:
        "Per i nostri figli...":
            jump mese14_c0
        "Per le nostre madri...":
            jump mese14_c0
        "Per i nostri mariti...":
            jump mese14_c0
        "Per il pane... >>":
            jump mese14_c0
label mese14_scelta4:
    menu:
        "Per i nostri figli...":
            jump mese14_c0
        "Per le nostre madri...":
            jump mese14_c0
        "Per i nostri mariti...":
            jump mese14_c0
        "Per il pane...":
            jump mese14_c0
        "... e per la PACE.":
            jump mese14_c2

label mese14_c2:
    k ON "Stiamo scioperando per i nostri figli,{w=1.0} per le nostre madri,{w=1.0} per i nostri mariti,{w=1.0} per il pane,{w=1.0} ma soprattutto..."
    show s14sfondo 1 onlayer master
    with dissolve
    k ON "... Per la pace."
    k ON "Per la fine di questa guerra."
    k ON "Per la fine di questa occupazione."
    k ON "Per la Liberazione."
    k ON "... A qualunque costo?"
    menu:
        k "... A qualunque costo?"
        "Sì.":
            jump mese14_fin1
        "No.":
            jump mese14_fin2

label mese14_fin1:
    k ON "Sì."
    k ON "Sciopererò."
    k ON "... A qualunque costo."
    $ s14sciopero = True
    jump mese15

label mese14_fin2:
    scene s14 pelle onlayer master
    show s14sfondo 2 onlayer master
    show s14_capelli onlayer master
    show keye onlayer master
    show kmouth OFF onlayer master
    k ON "No."
    k ON "Non posso scioperare..."
    k ON "Il rischio è troppo alto."
    k ON "Ed io ho bisogno di quei soldi."
    k ON "Di quei pochi, maledetti soldi."
    k OFF "..."
    k ON "Maledetti."
    $ s14nosciopero = True
    jump mese15


label mese15:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n13 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/15 INGLESI_2.mp3"
    centered "{size=48}{cps=18}- INGLESI -\nDa un anno aspettiamo che sferrino l’offensiva,\nma non si decidono mai.\nEssi calcolano il rischio,\nnoi no.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c13 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    play music "audio/15_radiolondra.mp3"
    scene black onlayer master
    j2 "Che ci fai ancora alzata, Sara?"
    j2 "Fila a letto!"
    j "Ma io..."
    j2 "FILA!"
    scene casa onlayer master
    show jpelle OK onlayer master
    show origlio onlayer master

    show jeye onlayer master
    show jmouth OFF onlayer master
    with dissolve
    j ON "Ogni sera la stessa storia..."
    j ON "Si riuniscono tutti intorno alla radio per ascoltare quegli strani incomprensibili messaggi..."
    hide jpelle onlayer master
    show j3 behind origlio onlayer master at camminata3
    show j1 behind origlio onlayer master at camminata1
    show j2 behind origlio onlayer master at camminata2
    with dissolve
    j2 "Presto!"
    j2 "Sta per iniziare Radio Londra!"
    j2 "Dev'essere un messaggio speciale..."
    j2 "Mi raccomando, cerchiamo di ricordarci bene tutti quello che dirà il Colonnello Buonasera..."

    $ renpy.music.set_volume(0.1, channel='music')
    $ renpy.music.set_volume(1.5, channel='sound')
    play sound "audio/sound/rlondra_1intro.mp3" fadeout 0.3
    hide j3 onlayer master
    hide j1 onlayer master
    hide j2 onlayer master
    show jpelle UK behind origlio onlayer master
    with dissolve
    $ renpy.pause(14.0, hard=True)
    "{cps=11}{i}Parla Londra. Trasmettiamo alcuni messaggi speciali.{/i}{/cps}{p=6.0}{nw}"
    play sound "audio/sound/rlondra_2felice.mp3" fadeout 0.3
    "{cps=11}{i}Felice non è felice.{/i}{/cps}{p=4.0}{nw}"
    play sound "audio/sound/rlondra_3pioggia.mp3" fadeout 0.3
    "{cps=11}{i}È cessata la pioggia.{/i}{/cps}{p=4.0}{nw}"
    play sound "audio/sound/rlondra_4barba.mp3" fadeout 0.3
    "{cps=11}{i}La mia barba è bionda.{/i}{/cps}{p=4.0}{nw}"
    play sound "audio/sound/rlondra_5mucca.mp3" fadeout 0.3
    "{cps=11}{i}La mucca non dà latte.{/i}{/cps}{p=4.0}{nw}"
    play sound "audio/sound/rlondra_6Giacomone.mp3" fadeout 0.3
    "{cps=11}{i}Giacomone bacia Maometto.{/i}{/cps}{p=4.0}{nw}"
    play sound "audio/sound/rlondra_7Scarpestrette.mp3" fadeout 0.3
    "{cps=11}{i}Le scarpe mi stanno strette.{/i}{/cps}{p=4.0}{nw}"
    play sound "audio/sound/rlondra_8Pappagallo.mp3"fadeout 0.3
    "{cps=11}{i}Il pappagallo è rosso.{/i}{/cps}{p=4.0}{nw}"
    play sound "audio/sound/rlondra_9Aquila.mp3" fadeout 0.3
    "{cps=11}{i}L'aquila vola.{/i}{/cps}{p=4.0}{nw}"
    play sound "audio/sound/rlondra_10fine.mp3" fadeout 0.3
    "{cps=11}{i}Parla Londra. Abbiamo trasmesso alcuni messaggi speciali.{/i}{/cps}{p=6.0}{nw}"
    $ renpy.music.set_volume(1.0, channel='music')
    $ renpy.music.set_volume(1.0, channel='sound')

    hide jpelle onlayer master
    show j3 behind origlio onlayer master
    show j1 behind origlio onlayer master
    show j2 behind origlio onlayer master
    with dissolve
    j2 "..."
    j2 "Allora... ricordate tutti tutto?"
    menu:
        j2 "Com'era Felice?"
        "Triste":
            jump mese15b
        "Felice":
            jump mese15b
        "Non felice":
            $ right1 = True
            $ rightcount +=1
            jump mese15b
    label mese15b:
    j2 "Felice è felice, chiaro!"
    if right1 == True:
        j ON "Ma no!"
        j ON "Felice non è felice... Ne sono sicura!"
    menu:
        j2 "Che è successo alla pioggia?"
        "È iniziata":
            jump mese15c
        "È cessata":
            $ right2 = True
            $ rightcount +=1
            jump mese15c
        "È caduta":
            jump mese15c
    label mese15c:
    j2 "La pioggia è caduta."
    j2 "Certo, che altro può fare la pioggia se non cadere?"
    if right2 == True:
        j ON "Cessata!"
        j ON "È cessata la pioggia..."
    menu:
        j2 "Di che colore era la barba?"
        "Rossa":
            jump mese15d
        "Bionda":
            $ right3 = True
            $ rightcount +=1
            jump mese15d
        "Bianca":
            jump mese15d
    label mese15d:
    j2 "Questa me la ricordo bene: rossa!"
    j2 "\"La mia barba è rossa\", ha detto così."
    if right3 == True:
        j ON "\"La mia barba è bionda\"..."
        j ON "Il Colonnello ha detto che la sua barba era bionda!"
    menu:
        j2 "Cosa non dava la mucca?"
        "Latte":
            $ right4 = True
            $ rightcount +=1
            jump mese15e
        "Carne":
            jump mese15e
        "Uova":
            jump mese15e
    label mese15e:
    j2 "Beh, latte e carne la mucca li dà..."
    j2 "... quindi uova. La mucca non dà uova!"
    if right4 == True:
        j ON "Sì ma... non questa."
        j ON "Questa mucca non dà il latte."
    menu:
        j2 "Chi baciava Maometto?"
        "L'aquila":
            jump mese15f
        "Felice":
            jump mese15f
        "Giacomone":
            $ right5 = True
            $ rightcount +=1
            jump mese15f
    label mese15f:
    j2 "Secondo me era l'aquila, o quel Felice di prima."
    j2 "L'aquila! Sono sicuro che era l'aquila!"
    if right5 == True:
        j ON "Non era l'aquila..."
        j ON "Era Giacomone. \"Giacomone bacia Maometto\"."
    menu:
        j2 "Come stavano le scarpe?"
        "Giuste":
            jump mese15g
        "Larghe":
            jump mese15g
        "Strette":
            $ right6 = True
            $ rightcount +=1
            jump mese15g
    label mese15g:
    j2 "Giuste. Le scarpe stanno giuste."
    j2 "Eh, magari...!"
    j2 "Giusto!"
    if right6 == True:
        j ON "E invece no, sbagliato..."
        j ON "\"Le scarpe mi stanno strette\", così ha detto."
    menu:
        j2 "E il pappagallo?"
        "È rosso":
            $ right7 = True
            $ rightcount +=1
            jump mese15h
        "È biondo":
            jump mese15h
        "Vola":
            jump mese15h
    label mese15h:
    j2 "Tu l'hai mai visto un pappagallo?"
    j2 "Io no. Ma penso voli."
    if right7 == True:
        j ON "Oh no..."
        j ON "È rosso!"
    menu:
        j2 "E che faceva l'aquila?"
        "Non è felice":
            jump mese15i
        "Non vola":
            jump mese15i
        "Vola":
            $ right8 = True
            $ rightcount +=1
            jump mese15i
    label mese15i:
    j2 "Beh, se il pappagallo volava..."
    j2 "... l'aquila no!"
    j2 "Anche perché già stava baciando Maometto prima, eh."
    if right8 == True:
        j ON "Niente da fare..."
        j ON "L'aquila vola."
        j ON "Sono certa che l'aquila volasse!"
    if rightcount >=5:
        j ON "Hanno sbagliato tutto."
        j ON "Non ricordano un solo messaggio giusto!"
        j ON "Forse dovrei dirglielo..."
        j ON "Anche se dovrei essere a letto, e non qui a origliare..."
        j "..."
        j ON "E adesso cosa faccio?"
        menu:
            j "E adesso cosa faccio?"
            "Io glielo dico...":
                jump mese15l
            "Io torno a letto...":
                jump mese15m
    elif rightcount <5:
        jump mese15m

    label mese15l:
        j ON "Io glielo dico..."
        j ON "Papà... Mamma...!"
        scene black onlayer master
        with fade
        j2 "Che ci fai ancora alzata, Sara?"
        j2 "Fila a letto!"
        j "Ma io..."
        j2 "FILA!"
        j2 "..."
        j2 "A volte mi chiedo se sia giusto trattare Sara in questo modo..."
        j2 "Lo sai perché lo facciamo..."
        j2 "Per proteggerla."
        j2 "Chissà cosa potrebbe succederle se dicesse alla persona sbagliata... che stiamo dalla parte giusta."
        j2 "..."
        j2 "A proposito..."
        j2 "... di che colore era il pappagallo?"
        $ s15good = True
        jump mese12
    label mese15m:
        j ON "Io torno a letto..."
        j ON "Chissà..."
        j ON "Forse un giorno ci capirò anche io qualcosa, di questa strana guerra!"
        $ s15bad = True
        jump mese12


label mese12:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n12 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/12 VITTORIO EMANUELE_1.mp3"
    centered "{size=48}{cps=15}- VITTORIO EMANUELE -\nEra piccolo col fascismo.\nSenza fascismo non è cresciuto di un pollice.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c12 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    scene n2char onlayer master
    show s12 onlayer master
    show n1chara onlayer master
    show n1charb onlayer master
    show n1eye onlayer master
    show n2eye onlayer master
    show nmouth OFF onlayer master
    play music "audio/12_volantino.mp3"
    n1 ON "Ho ricevuto un volantino, Baldo..."
    show volantino behind s12 onlayer master at loopcane
    with dissolve
    n1 ON "È destinato \"agli sbandati, ai renitenti, e ai disertori\"..."
    n2 "WOOF WOOF."
    n1 ON "Hai ragione, Baldo: io non sono né l'uno, né l'altro, né l'altro ancora."
    n1 ON "Sono un imprenditore, un uomo onesto, un uomo che crede nella Grande Madre Italia..."
    n1 ON "... e che crede ancora nel suo grande Re Vittorio Emanuele."
    n2 "WOOF WOOF... WOOF!"
    n1 ON "Baldo...! Lo sai che non mi piacciono le battute sulla statura del Re."
    n2 "WOOF..."
    n1 ON "Ah, intendevi \"piccolo\" dentro, non fuori?"
    n1 ON "Farò finta di non aver sentito, birbone."
    n1 ON "Fatto sta che un passaggio di questo volantino mi preoccupa, e non poco."
    n1 ON "Quando dice \"considerino\"..."
    n1 ON "\"Lo considerino le famiglie che possono ai congiunti dall'animo dubbioso...\""
    n1 ON "\"... far giungere una voce di sereno richiamo alla realtà\"."
    n2 "WOOF WOOF WOOF WOOF."
    n1 ON "Sì, sono d'accordo... In effetti è un bel capolavoro di eufemismo."
    n2 "WOOF WOOF?"
    n1 ON "Ma sì, certo che ho capito cosa vuol dire..."
    n1 ON "Vuol dire che chi conosce sbandati, renitenti o disertori li dovrebbe denunciare."
    n2 "WOOF?"
    n1 ON "Sì, mio malgrado..."
    n1 ON "Uno lo conosco bene."
    n1 ON "È il figlio della Mirella."
    n1 ON "Era soldato, l'8 settembre è scappato ed è tornato qui in paese."
    n1 ON "Da allora se ne sta nascosto, come dice il volantino, \"persistendo nell'assenza\"."
    n2 "WOOF WOOF?"
    n1 ON "Come faccio a saperlo?"
    n1 ON "Lo sto nascondendo io."
    n2 "WOOOOF!"
    n1 ON "Lo so, lo so, Baldo... Avrei dovuto parlartene prima."
    n1 ON "È che la Mirella lavora con me da vent'anni, è la mia dipendente più fedele."
    n1 ON "E anche se quello che mi ha chiesto è una roba da matti... come facevo a dirle di no?"
    n2 "WOOF WOOF?"
    n1 ON "Mi ha chiesto di tenerle nascosto il figlio su in archivio."
    n2 "WOOF?!"
    n1 ON "Sì, in ditta da me."
    n2 "WOOF."
    n1 ON "... Da noi, va bene. In ditta da noi."
    n1 OFF "..."
    n1 ON "\"Considerino\"..."
    n1 ON "Sono un imprenditore io, \"considerare\" è la cosa che faccio da sempre e che so fare meglio."
    n1 ON "Ma in questo caso..."
    n1 ON "In questo caso non so proprio cosa fare, cosa considerare..."
    n1 ON "Se l'affetto che ho per la Mirella, anche se c'ha un figlio disertore..."
    n1 ON "... O il mio dovere di camerata."
    n1 ON "... E suddito di Vittorio Emanuele."
    n2 "WOOF WOOF WOOF, WOOF?"
    n1 ON "Ho letto, Baldo..."
    n1 ON "Ho letto come prosegue il volantino."
    n1 ON "\"Oltre l'ora fissata, un'infamante pena aspetta fatalmente gli ostinati e gli incerti\"."
    n1 ON "E \"incerto\" è esattamente ciò che sono io, oggi."
    n1 OFF "..."
    n1 ON "Cosa dovrei fare, Baldo?"
    n1 ON "Continuare a nasconderlo oppure denunciarlo?"
    label mese12a:
    $ ui.timer(2.5, ui.jumps("mese12b"))
    menu:
        n1 "Continuare a nasconderlo oppure denunciarlo?"
        "WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF >>":
            jump mese12_1
        "WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF >>":
            jump mese12_2
    label mese12b:
    $ ui.timer(2.0, ui.jumps("mese12c"))
    menu:
        n1 "Continuare a nasconderlo oppure denunciarlo?"
        "Se solo potessi capirmi, padrone... >>":
            jump mese12_1
        "Se solo potessi capirmi, padrone... >>":
            jump mese12_2
    label mese12c:
    $ ui.timer(3.0, ui.jumps("mese12d"))
    menu:
        n1 "Continuare a nasconderlo oppure denunciarlo?"
        "Brucia quel volantino infame! >>":
            jump mese12_1
        "Fa' ciò che dice il volantino! >>":
            jump mese12_2
    label mese12d:
    $ ui.timer(7.0, ui.jumps("mese12e"))
    menu:
        n1 "Continuare a nasconderlo oppure denunciarlo?"
        "Sai benissimo che fine farà il figlio della Mirella se lo denunci. Finirà deportato dai tedeschi, o torturato in qualche sotterraneo, o fucilato in piazza. >>":
            jump mese12_1
        "Sai benissimo che fine farai se i fascisti scoprono che lo stai nascondendo. Addio alla ditta e ai sacrifici di una vita... o forse addio alla vita! >>":
            jump mese12_2
    label mese12e:
    $ ui.timer(9.0, ui.jumps("mese12f"))
    menu:
        n1 "Continuare a nasconderlo oppure denunciarlo?"
        "Credi pure in ciò che vuoi, nella tua \"Grande Madre Italia\", in quel piccolo Re fuggito a Brindisi o in questa ridicola Repubblichina. Non mi importa ciò in cui credi; mi importa ciò che fai. >>":
            jump mese12_1
        "E poi l'hai detto tu: sei un uomo onesto, un uomo di buona volontà, fedele al focolare e alla Patria. La Mirella non può chiederti di andare contro i tuoi stessi valori, i valori in cui hai sempre creduto. >>":
            jump mese12_2
    label mese12f:
    $ ui.timer(5.0, ui.jumps("mese12c"))
    menu:
        n1 "Continuare a nasconderlo oppure denunciarlo?"
        "Tieni nascosto quel ragazzo. >>":
            jump mese12_1
        "Denuncia quel ragazzo. >>":
            jump mese12_2

    label mese12_1:
        n2 "WOOF WOOF WOOF WOOF"
        n1 OFF "..."
        n1 ON "Se solo potessi davvero capirti, Baldo."
        n1 OFF "..."
        n1 ON "Basta, ho deciso."
        n1 ON "Come dice il volantino: \"in tempo ancora, oggi: domani non più!\"..."
        n1 OFF "..."
        n1 ON "E oggi è tempo di bruciare questo volantino infame."
        hide volantino onlayer master
        show n2char onlayer master
        n2 "..."
        n2 "... Grazie."
        $ s12good = True
        jump mese11

    label mese12_2:
        n1 OFF "..."
        n1 ON "Se solo potessi davvero capirti, Baldo."
        n1 OFF "..."
        n1 ON "Basta, ho deciso."
        n1 ON "Come dice il volantino: \"in tempo ancora, oggi: domani non più!\"..."
        n1 OFF "..."
        n1 ON "E oggi è tempo di fare ciò che dice il volantino."
        n2 "..."
        n2 "WOOF."
        $ s12bad = True
        jump mese11


label mese11:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n11 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/11 DIVISA_1.mp3"
    centered "{size=48}{cps=25}- DIVISA -\nNon ne esiste una di rigore,\nperciò sono tutte buone.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c11 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    play music "audio/11_bicipartigiana.mp3"

    scene bandiera onlayer master at scorrere
    show bici normale onlayer master
    with fade

    o "Quanti ne mancano...?"
    o "Ancora 5 chilometri e sono arrivata."
    o "\"La staffetta partigiana\", già..."
    o "Nella mia divisa da signorina per bene!"
    jump mese11_gira1

label mese11_gira1:
    menu:
        "Gira a destra":
            jump mese11_a1
        "Gira a sinistra":
            jump mese11_a1

label mese11_a1:
    o "Oggi devo stare molto attenta."
    o "Oggi si festeggia..."
    o "... Ma si piange."
    o "Oggi si porta a casa una vittoria..."
    o "... Ma anche una sconfitta."
    jump mese11_gira2

label mese11_gira2:
    menu:
        "Gira a sinistra":
            jump mese11_a2
        "Vai dritto":
            jump mese11_a2

label mese11_a2:
    o "Ieri è stata liberata Roma."
    o "I fascisti incassano il colpo..."
    o "E oggi Mussolini cosa fa, a Milano...?"
    o "... Dichiara Lutto Nazionale!"
    o "..."
    o "C'è chi festeggia, e c'è chi piange."
    jump mese11_gira3

label mese11_gira3:
    menu:
        "Vai dritto":
            jump mese11_a3
        "Gira a destra":
            jump mese11_a3

label mese11_a3:
    o "La Resistenza, dopo tutto, è un po' come la bicicletta."
    o "Messaggio dopo messaggio."
    o "Azione dopo azione."
    o "Come una ruota che gira..."
    o "Spinta da pedalate forti e convinte..."
    o "Macina chilometri..."
    o "Se prende velocità può sembrare inarrestabile..."
    o "E come ogni bicicletta, prima o poi, si deve anche fermare."
    o "Ma noi ci fermeremo..."
    o "... solo quando tutto questo sarà finito!"
    o "Se continuiamo a resistere..."
    o "Possiamo farcela!"
    jump mese11_gira4

label mese11_gira4:
    menu:
        "Controlla la cartina":
            jump mese11_b
        "Vai dritto":
            jump mese11_c

label mese11_c:
    o "Sono tre mesi ormai che faccio questa tratta."
    o "Ma non mi abituerò mai a pedalare con questi pacchetti nascosti nel vestito..."
    o "... Non importa!"
    o "... È per una buona causa."
    o "È per LA causa."
    jump mese11_bivio

label mese11_b:
    o "Sono tre mesi ormai che faccio questa tratta."
    o "Ma mi scordo sempre di quel dannato posto di blocco dei fascisti..."
    o "Bene che ho controllato la cartina..."
    o "... Alla prossima devo ricordarmi di andare a destra!"
    o "..."
    o "Ormai vado in bici tutto il giorno, tutti i giorni..."
    o "Ma non mi abituerò mai a pedalare con questi pacchetti nascosti nel vestito..."
    o "...È per una buona causa."
    o "È per LA causa."
    jump mese11_bivio

label mese11_bivio:
    menu:
        "Gira a destra":
            jump mese11_bfin1
        "Gira a sinistra":
            jump mese11_afin1

label mese11_afin1:
    o "..."
    o "... Cosa?!"
    o "Oh no!"
    o "Un posto di blocco!"
    scene black onlayer master with fade
    o1 "FERMA!"
    scene bandiera1 onlayer master
    show bici ferma onlayer master
    with fade
    o1 "DOCUMENTI!"
    o "Sì, un momento..."
    o "..."
    o1 "..."
    menu:
        "Cerca i documenti nella borsa":
            jump mese11_afin2
        "Scappa via":
            show bici via onlayer master
            $ renpy.pause(3.0, hard=True)
            jump mese11_afin3

label mese11_afin2:
    o1 "COS'HA SOTTO LA GIACCA?"
    o "Cosa?"
    o1 "MI FACCIA CONTROLLARE!"
    o "No! Mi stia lontano!"
    show bici via onlayer master
    $ renpy.pause(3.0, hard=True)
    jump mese11_afin3

label mese11_afin3:
    scene black onlayer master with fade
    pause 0.3
    o1 "FERMA!"
    play sound "audio/sound/212600__pgi__machine-gun-001-triple-shot.mp3"
    $ renpy.pause(5.0, hard=True)
    $ s11bad = True
    jump mese10

label mese11_bfin1:
    o "..."
    o "... Quel posto di blocco è piazzato in un punto davvero strategico."
    o "Saranno anche crudeli e spietati..."
    o "... Ma sanno il fatto loro quando si parla di organizzazione."
    scene black onlayer master with fade
    o "La buona notizia, però, è che..."
    scene bandiera onlayer master
    show bici ferma onlayer master
    with fade
    $ renpy.pause(0.3, hard=True)
    show bici via onlayer master
    $ renpy.pause(1.0, hard=True)
    o "Noi siamo più bravi!"
    $ s11good = True
    jump mese10



label mese10:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n10 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/10 REPUBBLICHINI_1.mp3"
    centered "{size=48}{cps=20}- REPUBBLICHINI -\nSe ne stanno in città,\npreferibilmente al sicuro,\ncon le scarpe lustre,\nil ciuffo fuori del berretto.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c10 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    play music "audio/10_famigliafin.mp3"
    scene s10 so onlayer master
    show peye onlayer master
    show pmouth OFF onlayer master
    p4 ON "Mamma! Papà! Hanno beccato l'Emilio!"
    show s10 ma onlayer master
    p2 ON "Oh Signore!"
    show s10 pa onlayer master
    p1 ON "Beccato?! Chi l'ha beccato?"
    show s10 so onlayer master
    p4 ON "Un repubblichino, giù in paese!"
    show s10 pa onlayer master
    p1 ON "Ho capito, sarà stato quel fascistone del figlio dell'Ernesto..."
    show s10 cu onlayer master
    p5 ON "Zio Mario, cos'è un repubblichino?"
    show s10 pa onlayer master
    p1 ON "Te lo spiego dopo, Giacomo... Ora pensiamo all'Emilio!"
    show s10 zi onlayer master
    p3 ON "E cosa ti hanno detto, Carolina?"
    show s10 so onlayer master
    p4 ON "Mi hanno detto di dirvi che vogliono il cavallo!"
    show s10 pa onlayer master
    p1 ON "Il cavallo?!"
    show s10 so onlayer master
    p4 ON "Sì, se gli portiamo il cavallo ci ridanno l'Emilio, altrimenti..."
    show s10 ma onlayer master
    p2 ON "Oh Signore... Un cavallo in cambio di mio figlio?!"
    show s10 pa onlayer master
    p1 ON "Di nostro figlio!"
    show s10 so onlayer master
    p4 ON "Di mio fratello!"
    show s10 zi onlayer master
    p3 ON "Di mio nipote!"
    show s10 cu onlayer master
    p5 ON "Di mio cugino!"
    show s10 so onlayer master
    p4 ON "E allora... che si fa?"
    menu:
        p4 "E allora... che si fa?"
        "Portiamogli il cavallo!":
            jump mese10_1

    label mese10_1:
        show s10 so onlayer master
        p2 ON "Portiamogli il cavallo!"
        show s10 cu onlayer master
        p5 ON "Ma io gli voglio bene, al Furia!"
        show s10 so onlayer master
        p4 ON "Giacomo! L'Emilio rischia di lasciarci la pelle e tu pensi al cavallo?"
        show s10 zi onlayer master
        p3 ON "Un attimo, il Giacomo non ha tutti i torti... Quel cavallo è importantissimo per la nostra cascina!"
        show s10 pa onlayer master
        p1 ON "In effetti... Senza cavallo rischia di essere un'annata difficile."
        show s10 ma onlayer master
        p2 ON "Ma Mario!"
        show s10 zi onlayer master
        p3 ON "Adele, ci dev'essere un'altra soluzione..."
        label mese10_0:
        show s10 so onlayer master
        p4 ON "E allora... che si fa?"
        menu:
            p4 "E allora... che si fa?"
            "Portiamogli il maiale!" if maiale == False:
                $ maiale = True
                jump mese10_2
            "Portiamogli le galline!" if galline == False:
                $ galline = True
                jump mese10_3
            "Portiamogli i cachi!" if cachi == False:
                $ cachi = True
                jump mese10_4
            "Portiamogli il Giacomo!" if giacomo == False:
                $ giacomo = True
                jump mese10_5
            "Non vorrete lasciargli l'Emilio?" if maiale and galline and cachi and giacomo == True:
                jump mese10_6

    label mese10_2:
        show s10 zi onlayer master
        p3 ON "Portiamogli il maiale!"
        show s10 pa onlayer master
        p1 ON "Ma il maiale ci serve anche più del cavallo!"
        show s10 ma onlayer master
        p2 ON "È vero, il maiale è la bestia più preziosa che abbiamo... sperando di riuscire a tirare fino al prossimo inverno."
        show s10 cu onlayer master
        p5 ON "E poi gli voglio bene, al porcello!"
        jump mese10_0

    label mese10_3:
        show s10 ma onlayer master
        p2 ON "Portiamogli le galline!"
        show s10 pa onlayer master
        p1 ON "Le galline... Se quei fascistoni pensano che mio figlio valga quanto un cavallo..."
        p1 ON "... non penso proprio basteranno le quattro galline spiumate che ci restano!"
        show s10 zi onlayer master
        p3 ON "È vero... Ce ne vorrebbero almeno una dozzina, o anche di più."
        show s10 cu onlayer master
        p5 ON "Non ho capito... Se l'Emilio vale un cavallo, e un cavallo vale dodici galline, e le galline fanno l'uovo..."
        p5 ON "... quante uova vale l'Emilio?"
        show s10 zi onlayer master
        p3 ON "... Lasciamo stare."
        jump mese10_0

    label mese10_4:
        show s10 cu onlayer master
        p5 ON "Portiamogli i cachi!"
        show s10 pa onlayer master
        p1 ON "Ma non è ancora stagione, di cachi!"
        show s10 ma onlayer master
        p2 ON "Purtroppo... Anche perché quella dei cachi è l'ultima pianta buona che ci è rimasta."
        jump mese10_0

    label mese10_5:
        show s10 pa onlayer master
        p1 ON "Portiamogli il Giacomo!"
        show s10 cu onlayer master
        p5 ON "Ma Zio Mario!"
        show s10 zi onlayer master
        p3 ON "Ma dai, Giacomo... Lo zio stava scherzando!"
        show s10 ma onlayer master
        p2 ON "... Stavi scherzando, vero?"
        jump mese10_0

    label mese10_6:
        show s10 so onlayer master
        p4 ON "Non vorrete lasciargli l'Emilio?"
        show s10 cu onlayer master
        p5 OFF "..."
        show s10 so onlayer master
        p4 ON "Zio?!"
        show s10 zi onlayer master
        p3 OFF "..."
        show s10 so onlayer master
        p4 ON "Papà?!"
        show s10 pa onlayer master
        p1 OFF "..."
        show s10 so onlayer master
        p4 ON "Mamma?!"
        show s10 ma onlayer master
        p2 OFF "..."
        show s10 so onlayer master
        p4 OFF "..."
        show s10 cu onlayer master
        p5 ON "No."
        show s10 so onlayer master
        p4 ON "Giacomo?!"
        show s10 cu onlayer master
        p5 ON "Sarò anche scemo, ma nessun cavallo o maiale o gallina o uovo o caco vale come mio cugino."
        show s10 so onlayer master
        p4 OFF "..."
        show s10 cu onlayer master
        p5 ON "Non avremo più un cavallo e avremo tanta fame, ma avremo tanta fame tutti insieme."
        show s10 so onlayer master
        p4 ON "\"Tutti insieme\"..."
        show s10 all onlayer master
        with dissolve

        p2 ON "Compreso l'Emilio... Mio figlio!"

        p1 ON "Nostro figlio!"

        p3 ON "Mio nipote!"

        p4 ON "Mio fratello!"

        p5 ON "Mio cugino!"

        p4 ON "E allora... che si fa?"
        menu:
            p4 "E allora... che si fa?"
            "Portiamogli il cavallo...":
                jump mese10_7

    label mese10_7:

        p4 ON "Portiamogli il cavallo...{w=1.0} a quei maledetti fascistoni!"
        show s10 ca onlayer master
        with fade
        "{i}\"Se gli oceani di lacrime che il mostro ha fatto versare nella storia dell'uomo potessero venir misurati con le situazioni grottesche che la sua imbecillità ha provocato, nessuno avrebbe più dubbi sulla comicità del potere e sulla necessità di spiegarlo in termini di commedia anziché di tragedia\".{/i}"
        "{i}Oriana Fallaci, \"Intervista con il Potere\"{/i}"
        jump mese9



label mese9:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n09 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/9 RAFFICA_2.mp3"
    centered "{size=48}{cps=18}- RAFFICA -\nUna parola in cui si concentrano l’odio e la violenza.\nUna parola di questa guerra.\nQualche volta l’uomo che spara\nriesce a vedere negli occhi l’altro che insacca i colpi.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c09 onlayer master with fade
    $ renpy.pause(3.0, hard=True)


    play music "audio/9_stragediLoreto.mp3" fadein 4.0
    $ renpy.pause(1.0, hard=True)
    scene black onlayer master

    "Uomini buttati sul marciapiede, contro lo steccato, come sacchi di immondizia."
    "\"Banditi catturati con le armi in pugno\", ci hanno detto."
    "Intorno, la gente è muta; il sole, cocente."
    "Intorno agli uomini morti, altri uomini, con la divisa nera, vivi; ma fermi, immobili, a far la guardia..."
    "... come se i morti potessero alzarsi, e andare via."
    "Ma forse..."
    "... Forse, possono ancora parlare."

    show qchar onlayer master
    show qeye onlayer master
    show qmouth OFF onlayer master
    with dissolve
    pause 1.0

    q ON "L'ho appena saputo!"
    q ON "Ma che è successo? E quanti sono?!"
    "Li hanno ammazzati i fascisti, e li hanno scaricati qui, in Piazzale Loreto."
    $ ui.timer(2.0, ui.jumps("mese9_a2"))
    menu:
        "Sono tanti... >>":
            jump mese9_b

label mese9_a2:
    $ ui.timer(2.0, ui.jumps("mese9_a3"))
    menu:
        "Sono tanti...":
            jump mese9_b
        "Sono troppi... >>":
            jump mese9_b

label mese9_a3:
    $ ui.timer(2.0, ui.jumps("mese9_a4"))
    menu:
        "Sono tanti...":
            jump mese9_b
        "Sono troppi...":
            jump mese9_b
        "Sono 15. >>":
            jump mese9_b

label mese9_a4:
    menu:
        "Sono tanti...":
            jump mese9_b
        "Sono troppi...":
            jump mese9_b
        "Sono 15.":
            jump mese9_b
        "Non li voglio nemmeno contare.":
            jump mese9_b

label mese9_b:
    q ON "Non credo ai miei occhi..."

    scene strage onlayer master
    with dissolve
    pause 5.0

    q ON "I fascisti ci hanno messo anche un cartello?"
    "Sì..."
    "\"Questi sono assassini\", c'è scritto."
    q ON "\"Questi\"..."
    q ON "Ma chi?"
    q ON "I morti, o i veri assassini?"
    q ON "Sembra quasi siano stati i partigiani a mettere quel cartello, per denunciare chi li ha uccisi..."
    q ON "In fondo..."
    q ON "Loro continuano a parlare..."
    q ON "Non li senti?"
    "...?"

    scene insieme onlayer master
    show qeye onlayer master
    show qmouth OFF onlayer master
    with dissolve

    q2 ON "Anche questa settimana siamo riusciti a stampare il giornale clandestino."
    q2 ON "Le armi scarseggiano ma con l'aiuto di alcuni amici riusciremo a rifornirci."
    q2 ON "Ci avete ucciso e lasciato qui a marcire sotto il sole..."
    q2 ON "Avrete ciò che meritate."

    "Li sento."
    "Tutti li sentono."
    "Anche i fascisti..."
    "... Li sentiranno."

    scene qchar onlayer master
    show qeye onlayer master
    show qmouth OFF onlayer master
    with dissolve

    q ON "Ma lì in mezzo, forse, c'è anche mio fratello."
    "Mi dispiace moltissimo..."
    menu:
        "Mi dispiace moltissimo..."
        "Vorresti andare a controllare?":
            jump mese9_b1

label mese9_b1:
    scene targa onlayer master
    with Dissolve (6)
    q "...{p=5.0}{nw}"
    label mese9_b1x:
    menu:
        "Gian Antonio Bravin":
            jump mese9_false
        "Renzo del Riccio":
            jump mese9_false
        "Andrea Esposito":
            jump mese9_false
        "Domenico Fiorani":
            jump mese9_false
        "Umberto Fogagnolo":
            jump mese9_true2
        "Tullio Galimberti":
            jump mese9_false
        "Vittorio Gasparini":
            jump mese9_false
        "Emidio Mastrodomenico":
            jump mese9_false
        "Angelo Poletti":
            jump mese9_false
        "Salvatore Principato":
            jump mese9_false
        "Andrea Ragni":
            jump mese9_false
        "Giulio Casiraghi":
            jump mese9_true1
        "Eraldo Soncini":
            jump mese9_false
        "Libero Temolo":
            jump mese9_false
        "Vitale Vertemati":
            jump mese9_false

label mese9_false:
    q "No..."
    q "..."
    q "Non è lui, mio fratello..."
    q "Anche se è come se lo fosse."
    jump mese9_b1x

label mese9_true1:
    scene qchar onlayer master
    show qeye onlayer master
    show qmouth OFF onlayer master
    with dissolve
    q "..."
    q ON "Giulio..."
    q ON "Non..."
    q ON "Io..."
    q "..."
    q ON "Devo andare."
    $ s9fratello = True
    jump mese13

label mese9_true2:
    scene qchar onlayer master
    show qeye onlayer master
    show qmouth OFF onlayer master
    with dissolve
    q ON "Lui..."
    q ON "Umberto? Se c'è lui significa che..."
    q ON "Anche mio fratello, sicuramente..."
    q ON "Giulio..."
    q OFF "..."
    q ON "Devo andare."
    $ s9compagno = True
    jump mese13



label mese13:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n08 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/13 ALBA_1.mp3"
    centered "{size=48}{cps=18}- ALBA -\nQuando spunta,\npuò essere troppo tardi.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c08 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    play music "audio/13_coprifuoco.mp3" fadein 2.0

    scene pg l onlayer master


    show lmouth OFF onlayer master
    show occhio_l onlayer master
    show occhio_m onlayer master
    with dissolve

    l ON "Ciao Luca."
    show torcia onlayer master

    show pg m onlayer master


    with dissolve

    m ON "Nicola..."
    m ON "Eccoci qui, come ogni notte."

    show pg l onlayer master


    with dissolve

    l ON "Questo dannato coprifuoco..."
    l ON "È freddo e pericoloso qua fuori..."

    show pg m onlayer master


    with dissolve

    m ON "Dannato o benedetto coprifuoco?"
    m ON "Il coprifuoco, in un certo senso, ci protegge..."
    m ON "Non credi?"

    show pg l onlayer master


    with dissolve

    l ON "Non mi sento poi così protetto all'idea che possiamo vederci solo dalle 9 di sera alle 5 del mattino..."

    show pg m onlayer master


    with dissolve

    m ON "Ma siamo al sicuro..."

    show pg l onlayer master


    with dissolve

    l ON "Sì... anche se è assurdo sentirsi al sicuro proprio nelle ore in cui tutti hanno più paura."
    l ON "Ammesso poi che i fascisti non ci trovino."
    l ON "Altrimenti rischiamo di finire come quelli di Loreto."

    show pg m onlayer master


    with dissolve

    m ON "Andrà tutto bene."
    m "..."

    show pg l onlayer master


    with dissolve

    l ON "Dunque..."
    l ON "Quali sono gli incarichi per i prossimi giorni?"

    show pg m onlayer master


    with dissolve

    jump mese13_a

label mese13_a:
    $ ui.timer(3.0, ui.jumps("mese13_b"))
    menu:
        l "Quali sono gli incarichi per i prossimi giorni?"
        "Mezzogiorno di domani, questa volta è un cinema.":
            jump mese13_part1

label mese13_b:
    $ ui.timer(2.5, ui.jumps("mese13_a"))
    menu:
        l "Quali sono gli incarichi per i prossimi giorni?"
        "Mezzogiorno di domani, questa volta è un cinema.":
            jump mese13_part1
        "... Come stai?":
            $ love = True
            jump mese13_amanti1

label mese13_amanti1:

    m ON "... Come stai?"

    show pg l onlayer master


    with dissolve

    l ON "Sto bene, Luca... Sto bene."
    l ON "Ma non è il momento di parlarne..."
    l ON "Per favore."

    show pg m onlayer master


    with dissolve

    m ON "Scusa."
    jump mese13_part1

label mese13_part1:

    m ON "... Mezzogiorno di domani, questa volta è un cinema."
    m ON "Niente errori."
    m ON "Entriamo, lanciamo i volantini, e si sparisce."
    m ON "Chiaro?"

    show pg l onlayer master


    with dissolve

    l ON "Chiaro."
    l ON "Come li recuperiamo i volantini?"

    show pg m onlayer master


    with dissolve

    m ON "Questa volta è più difficile, i fascisti sorvegliano molto la zona in questo periodo."
    jump mese13_a1

label mese13_a1:
    $ ui.timer(2.5, ui.jumps("mese13_b1"))
    menu:
        m "Questa volta è più difficile, i fascisti sorvegliano molto la zona in questo periodo."
        "La staffetta seguirà un percorso alternativo, ci si trova in via Fortezza.":
            jump mese13_part2

label mese13_b1:
    $ ui.timer(2.5, ui.jumps("mese13_a1"))
    menu:
        m "Questa volta è più difficile, i fascisti sorvegliano molto la zona in questo periodo."
        "La staffetta seguirà un percorso alternativo, ci si trova in via Fortezza.":
            jump mese13_part2
        "Quindi, per favore, stai attento...":
            $ love = True
            jump mese13_amanti2

label mese13_amanti2:
    show pg m onlayer master


    with dissolve

    m ON "Quindi, per favore, stai attento..."

    show pg l onlayer master


    with dissolve

    l ON "Starò attento."
    l ON "... Anche tu, mi raccomando."

    show pg m onlayer master


    with dissolve

    m "..."
    m ON "Sì."

    show pg l onlayer master


    with dissolve

    l ON "Dunque, come li recuperiamo i volantini...?"
    jump mese13_part2

label mese13_part2:

    show pg m onlayer master


    with dissolve

    m ON "La staffetta seguirà un percorso alternativo, ci si trova in via Fortezza."
    m ON "Puntuali."

    show pg l onlayer master


    with dissolve

    l ON "Puntuali."

    show pg m onlayer master


    with dissolve

    m ON "Ricordati."
    m ON "Si entra e si sparisce."
    m ON "Soprattutto nel caso in cui le cose si mettano male."
    m ON "Ricordi l'attentato di febbraio?"
    m ON "Qualcosa è andato storto, ma tutti sono riusciti a salvarsi."
    m "..."
    m ON "La fuga..."
    m ON "La fuga è la prima regola."
    m ON "Chiaro?"

    show pg l onlayer master


    with dissolve

    l ON "Chiaro."
    l ON "Ma non preoccuparti per me."
    l ON "Domani andrà tutto bene."
    l ON "Ti fidi di me?"

    show pg m onlayer master


    with dissolve

    m ON "Mi fido."

    show pg l onlayer master


    with dissolve

    l "..."
    l ON "Di notte sembra tutto così chiaro, e perfetto."
    l ON "Il giorno ci regala solo paura, e confusione."
    l "..."
    l ON "Vorrei vivere di notte, tutta la mia vita, Luca."

    show pg m onlayer master


    with dissolve

    m ON "Anche io."
    jump mese13_a3

label mese13_a3:
    $ ui.timer(2.5, ui.jumps("mese13_b3"))
    menu:
        "Tutta la mia vita...":
            jump mese13_part4

label mese13_b3:
    $ ui.timer(2.5, ui.jumps("mese13_a3"))
    menu:
        "Tutta la mia vita...":
            if love == True:
                jump mese13_amanti4
            jump mese13_part4
        "... con te.":
            jump mese13_amanti4

label mese13_part4:

    show pg m onlayer master


    with dissolve

    m ON "Tutta la mia vita..."
    m ON "... Per sognare un mondo che forse non vedremo mai."
    m ON "A domani, Nicola."

    show pg l onlayer master


    with dissolve

    l ON "A domani, Luca."
    $ s13nobacio = True
    jump mese7

label mese13_amanti4:

    show pg m onlayer master


    with dissolve

    m ON "Tutta la mia vita..."
    m ON "... con te."
    m ON "Noi due e nessun altro..."
    m ON "Senza incarichi, paura, e confusione."
    m ON "Senza fascisti."

    show pg l onlayer master


    with dissolve

    l ON "E senza guerra."

    show s13_13 onlayer master with dissolve

    $ renpy.pause(10.0, hard=True)
    $ s13bacio = True
    jump mese7



label mese7:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n07 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/7 MORTE_1.mp3"
    centered "{size=48}{cps=15}- MORTE -\nNon se ne parla mai, ma è sempre con noi.\nCiascuno si è immaginato la propria.\nSarebbe una sorpresa troppo spiacevole\ntrovarsela dinanzi, all’improvviso,\nsenza essere preparati a riceverla.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c07 onlayer master with fade
    $ renpy.pause(1.0, hard=True)
    play music "audio/7_stragedigorla.mp3" fadein 4.0
    $ renpy.pause(2.0, hard=True)
    scene black onlayer master
    r "Faceva..."
    r "... faceva fresco."
    r "Questo me lo ricordo."
    r "..."
    r "Il cielo..."
    r "... prima terso, e poi..."
    scene bg7 onlayer master
    show nuvole onlayer master at passaggio
    show nuvole2 onlayer master at passaggio2
    with fade
    r "... e poi il gelo."
    r "Un gelo insolito."
    r "Un gelo aspro..."
    r "... acre, come polvere da sparo."
    scene black onlayer master with fade
    r "Io cerco e cerco e..."
    r "..."
    r "... cerco."
    r "..."
    r "Cos'altro..."
    r "... c'è qualcos'altro che avrei potuto fare, di diverso?"
    scene bg7 onlayer master
    show nuvole onlayer master at passaggio
    show nuvole2 onlayer master at passaggio2
    with fade
    r "Hanno dichiarato lo stato d'allerta!"
    r "Tra poco bombarderanno la zona!"
    r "..."
    scene black onlayer master with dissolve
    r "Ma l'allarme..."
    r "... è arrivato tardi."
    r "Troppo tardi."
    r "E troppo confuso."
    r "E a quel punto..."
    r "I bombardieri erano già sopra di noi."
    label mese7_a:
    scene bg7 onlayer master
    show nuvole onlayer master at passaggio
    show nuvole2 onlayer master at passaggio2

    play sound "audio/sound/aereo.mp3" fadein 0.5
    $ renpy.pause(1.0, hard=True)
    show aereo onlayer master at volo
    r "Oh mio Dio!"
    r "Questa volta ci attaccano..."
    r "... ci attaccano davvero!"
    scene black onlayer master with fade
    r "Dapprima penso a me. A salvarmi. A correre al riparo."
    r "Nel rifugio più vicino."
    r "Vedo Mario, il panettiere, mi grida \"corri Donata, corri, questi sganciano sul serio\"..."
    r "Attraverso Viale Monza... Attraverso un paio di altre strade, non ricordo bene..."
    r "Poi, all'improvviso, mi ritrovo di fronte alla scuola Francesco Crispi."


    scene rchar onlayer master
    show reye onlayer master
    show rmouth OFF onlayer master

    r "La mia migliore amica..."
    r "... Gianna!"
    r "Sarà in fabbrica, a quest'ora..."
    r "Ma i suoi bambini, di Gianna..."
    r "Benito e Bianca..."
    r "... Sono lì!"
    show black onlayer master
    r "... Rivedo i bambini, le maestre."
    r "C'è chi sta uscendo dalla scuola, tornando a casa, cercando un rifugio..."
    scene rchar onlayer master
    show reye onlayer master
    show rmouth OFF onlayer master

    r "... Ma in cortile vedo poche, troppe poche sagome."
    r "\"Dentro alla scuola ci saranno almeno 150, 200 bambini\", penso."
    r "Mi concentro per capire se li vedo, Benito e Bianca."
    r "Ma mi sembrano tutti uguali..."
    scene black onlayer master
    r "E poi a me manca della vista."
    r "L'ho persa in fabbrica, al lavoro."
    r "Al saldatore."
    scene rchar onlayer master
    show reye onlayer master
    show rmouth OFF onlayer master

    r "Non possono essere lì."
    r "Quelli mi sembrano bambini della terza... riconosco Lelino."
    scene black onlayer master
    r "Bianca fa la quinta e Benito è più piccolo, un soldino di cacio."
    r "E adesso..."
    scene rchar onlayer master
    show reye onlayer master
    show rmouth OFF onlayer master
    r ON "... Dove vado?"
    r ON "Cosa faccio?"
    r ON "Sono confusa, non capisco più nulla, non vedo più niente..."
    scene black onlayer master
    r "Penso solo alla Gianna che è in fabbrica..."
    r "E ai suoi bambini, che sono qui, senza di lei..."
    $ ui.timer(4.0, ui.jumps("mese7_menu1"))
    menu:
        r "Da chi vado prima?"
        "Parto dal secondo piano, dalla classe di Benito... >>":
            $ bencounter +=1
            jump mese7_a
        "Parto dal quarto piano, dalla classe di Bianca... >>":
            $ marcounter +=1
            jump mese7_a

label mese7_menu1:
    $ ui.timer(3.0, ui.jumps("mese7_menu2"))
    menu:
        r "Ogni secondo è prezioso!"
        "Benito! Dove sei?! >>":
            $ bencounter +=1
            jump mese7_a
        "Bianca! Dove sei?! >>":
            $ marcounter +=1
            jump mese7_a

label mese7_menu2:
    menu:
        r "PRESTO!"
        "BENITO!":
            $ bencounter +=1
            jump mese7_a
        "BIANCA!":
            $ marcounter +=1
            jump mese7_a

label mese7_a:
    scene bg7 onlayer master
    show nuvole onlayer master at passaggio
    show nuvole2 onlayer master at passaggio2

    play sound "audio/sound/aereo.mp3" fadein 0.5
    $ renpy.pause(1.0, hard=True)
    show aereo onlayer master at volo
    r "Sento l'aereo sopra di noi."
    show black onlayer master with fade




    r "Ma loro... non li vedo!"
    $ ui.timer(3.0, ui.jumps("mese7_menu3"))
    menu:
        r "Il tempo stringe."
        "Guarda a destra... >>":
            $ bencounter +=1
            jump mese7_b
        "Guarda a sinistra... >>>":
            $ marcounter +=1
            jump mese7_b
label mese7_menu3:
    $ ui.timer(2.0, ui.jumps("mese7_menu4"))
    menu:
        r "Forse è qui..."
        "... a destra! >>":
            $ bencounter +=1
            jump mese7_b
        "... a sinistra! >>":
            $ marcounter +=1
            jump mese7_b
label mese7_menu4:
    menu:
        r "Non farò mai in tempo!"
        "Riguarda a destra...":
            $ bencounter +=1
            jump mese7_b
        "Riguarda a sinistra...":
            $ marcounter +=1
            jump mese7_b

label mese7_b:
    r "... Niente!"
    r "Oddio... Ma dove sono?!"
    $ ui.timer(3.0, ui.jumps("mese7_menu5"))
    menu:
        r "Forse..."
        "... in segreteria?! >>":
            $ bencounter +=1
            jump mese7_c
        "... nei bagni?! >>":
            $ marcounter +=1
            jump mese7_c
label mese7_menu5:
    $ ui.timer(3.0, ui.jumps("mese7_menu6"))
    menu:
        r "O forse sono appena usciti?"
        "Cerca all'entrata! >>":
            $ bencounter +=1
            jump mese7_c
        "Cerca in cortile! >>":
            $ marcounter +=1
            jump mese7_c
label mese7_menu6:
    menu:
        r "Non c'è più tempo!"
        "...":
            $ bencounter +=1
            jump mese7_c
        "...":
            $ marcounter +=1
            jump mese7_c

label mese7_c:
    if bencounter >=2:
        jump mese7_benito
    elif marcounter >=2:
        jump mese7_martina

label mese7_benito:
    r "Eccoti!"
    r "Benito!"
    r "Benito, presto, dammi la mano... Andiamo a cercare tua sorella!"
    jump mese7_bomba1

label mese7_martina:
    r "Eccoti!"
    r "Bianca!"
    r "Bianca, presto dammi la mano... Andiamo a cercare tuo fratello!"
    jump mese7_bomba1

label mese7_bomba1:
    $ renpy.pause(0.5, hard=True)
    stop music fadeout 2.0


    scene bg7 onlayer master
    show nuvole onlayer master at passaggio

    show bombaPiccola onlayer master at sganciata1

    $ renpy.pause(0.5, hard=True)
    scene black onlayer master
    with fade
    $ renpy.pause(0.5, hard=True)



    scene bg7 onlayer master
    show nuvole2 onlayer master at passaggio3
    show bombaGrande onlayer master at sganciata2

    $ renpy.pause(0.5, hard=True)
    scene black onlayer master
    with fade


















label mese7_bomba2:

    scene rcharNo onlayer master
    show reye onlayer master

    $ renpy.pause(2.0, hard=True)
    show bombaPiccola onlayer master at sganciataSullaScuola
    pause 0.07
    scene black onlayer master with fade

    play sound "audio/sound/esplosione.mp3" 
    $ renpy.pause(3.0, hard=True)
    show esplosione onlayer master
    $ renpy.pause(1.5, hard=True)
    show s07 15 onlayer master

    if bencounter >=2:
        jump mese7_benito2
    elif marcounter >=2:
        jump mese7_martina2

label mese7_benito2:
    r "..."
    r "Benito! Afferra la mia mano!"
    r "Andiamo via!"
    scene black onlayer master with fade
    play music "audio/7_stragedigorla.mp3" fadein 4.0
    r "..."
    r "Ho visto distintamente le bombe cadere."
    r "Ma non ho avuto un'altra possibilità."
    r "Perdonami Gianna..."
    scene s07 17 onlayer master with dissolve
    r "... ma ho dovuto fare una scelta..."
    r "... e sono riuscita a salvare solo Benito."
    pause 2.0
    scene black onlayer master with fade
    r "Solo lui."
    $ s7martadead = True
    jump mese6

label mese7_martina2:
    r "..."
    r "Bianca! Afferra la mia mano"
    r "Andiamo via!"
    scene black onlayer master with fade
    play music "audio/7_stragedigorla.mp3" fadein 4.0
    r "..."
    r "Ho visto distintamente le bombe cadere."
    r "Ma non ho avuto un'altra possibilità."
    r "Perdonami Gianna..."
    show s07 16 onlayer master with dissolve
    r "... ma ho dovuto fare una scelta..."
    r "... e sono riuscita a salvare solo Bianca."
    pause 2.0
    scene black onlayer master with fade
    r "Solo lei."
    $ s7benitodead = True
    jump mese6



label mese6:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n06 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/6 POLITICA_3.mp3"
    centered "{size=48}{cps=15}- POLITICA -\nI giovani non amano e non sanno farne.\nI più anziani la preferiscono alle azioni di guerra.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c06 onlayer master with fade

    $ renpy.pause(3.0, hard=True)
    play music "audio/6_deportazionePirelli.mp3"
    scene s06 1 onlayer master
    with fade
    $ renpy.pause(3.0, hard=True)
    op "Che cosa...?"
    op "Ma che succede oggi in fabbrica?!"
    scene s06 2 onlayer master
    with dissolve
    op "..."
    op "Le SS?"
    op "Qui?!"
    op "..."
    op "Ma cosa vogliono da noi?"
    op "Da... me?!"
    scene ss2char onlayer master
    show ss1eye onlayer master
    show ss1mouth OFF onlayer master
    with dissolve
    op "..."
    ss1 ON "§§§§§§sestosangiovanni§§§§§§§§..."
    ss1 ON "@@@@@@@@lista@@."
    ss1 ON "pirelli§§§§?"
    ss1 ON "breda@@@@falck@@."
    op "..."
    ss1 ON "§§§§§§§§§§§§treni§§§§§§§§§."
    ss1 ON "@@@italiano@@?"
    menu:
        ss1 "@@@italiano@@?"
        "Sì...?":
            jump mese6_1
        "No...?":
            jump mese6_1
        "Cosa...? Non capisco!":
            jump mese6_1

    label mese6_1:
        ss1 ON "§§§§partigiano?!"
        $ ui.timer(5.0, ui.jumps("mese6_1b"))
        menu:
            ss1 "§§§§partigiano?!"
            "Partigiano? No, non c'entro, io non faccio politica!":
                jump mese6_2
            "Partigiano? Se anche lo fossi, non ve lo direi.":
                jump mese6_2
            "...":
                jump mese6_2

    label mese6_1b:
        op "..."
        ss1 ON "rispondi@@@@@@@@italiano@@!"
        menu:
            ss1 "rispondi@@@@@@@@italiano@@!"
            "Sono solo un operaio...":
                jump mese6_2
            "Non ho nulla da dire.":
                jump mese6_2

    label mese6_2:
        ss1 ON "§§§§§§§§§§§§assassino§§§?"
        ss1 ON "traditore@@@@@@"
        ss1 ON "torre§§colombo§villa§§§§leone§conti§§§§§§§barbieri§§bassi§§§§§§§§§§§§§§§§§§§§"
        ss1 ON "@@@@@@@@tuttiuguali@."
        ss1 ON "morti§§§§§§§§animali§§§§§§"
        menu:
            ss1 "quando§§§§§§§§§§§§§?"
            "Quando? Quando cosa?! Io non so nulla!":
                jump mese6_3
            "Se solo capissi il tedesco...":
                jump mese6_3

    label mese6_3:
        ss1 ON "bene§§§§§§§§§§mai§§§§§§§§"
        ss1 ON "@@@@@@deportazione@@@@@@@@"
        op ON "... quando finirà questo incubo?"

        scene ss2BigChar onlayer master
        show ss1Bigmouth OFF onlayer master
        show ss2Bigmouth OFF onlayer master
        with fade
        ss2Big ON "... Quando lo decideremo noi, italiano!"
        ss1Big ON "Direi che qua abbiamo quasi finito... Non sembra uno di quelli..."
        ss2Big ON "... Quelli, già. Quelli che credono di poter fare politica anche in fabbrica!"
        ss1Big ON "... Ma io lo deporterei comunque!"
        scene opchar onlayer master
        show opmouth OFF onlayer master
        show opeye onlayer master
        with dissolve
        op ON "¶¶¶¶¶¶¶ ¶¶¶ ¶¶¶¶¶¶ ¶?"
        ss1 "Uno in più, uno in meno..."
        ss2 "Due in più, due in meno..."
        ss1 "O tre, o quattro, o cinque..."
        ss2 "... Non fa tutta questa differenza!"
        ss1 "Dunque... che ne facciamo di questo?"
        op ON "¶¶¶, ¶ ¶¶¶¶¶¶ ¶¶¶¶ ¶¶ ¶!!!"
        ss1 "Non saprei... So che ne servono di sana e robusta costituzione, su nei campi, in Germania..."
        op ON "¶¶ ¶¶¶¶!"
        ss2 "... Che dice?"
        ss1 "Non capisco una parola!"
        ss2 "Certo che l'italiano è una lingua proprio strana..."
        ss1 "A stento distinguo i suoni che emette!"
        op ON "¶¶¶?!"
        ss2 "Insomma, quanti hai detto che ne mancano da controllare?"
        ss1 "Ancora un centinaio."
        ss2 "Diamoci una mossa, allora... Tanto, nel dubbio..."
        ss1 "... Sono tutti partigiani!"
        ss2 "Allora, italiano... ultima possibilità! Hai qualcosa da dire in tua difesa?"
        $ ui.timer(5.0, ui.jumps("mese6_a4"))
        menu:
            ss2 "Allora, italiano... ultima possibilità! Hai qualcosa da dire in tua difesa?"
            "¶¶¶ ¶¶ ¶!":
                jump mese6_b4
            "¶¶ ¶¶ ¶¶¶¶ ¶¶¶¶¶...":
                jump mese6_a4
    label mese6_a4:
        op ON "¶¶ ¶¶ ¶¶¶¶ ¶¶¶¶¶..."
        ss1 "... Sinceramente, quello che ha da dire non mi interessa..."
        ss2 "Dovremmo procedere."
        ss1 "Procediamo."
        menu:
            ss1 "Procediamo."
            "¶¶ ¶¶ ¶¶¶¶ ¶¶¶¶¶?":
                jump mese6_a5
            "¶¶¶¶¶¶¶¶!":
                jump mese6_a5
            "¶ ¶¶ ¶¶¶ ¶¶¶¶¶?!":
                jump mese6_a5

    label mese6_a5:
        op ON "¶¶ ¶¶ ¶¶¶¶? ¶¶¶¶¶¶¶¶! ¶ ¶¶ ¶¶¶ ¶¶¶¶¶?!"
        ss2 "... Ma quanto parla?!"
        ss1 "Basta... andiamo avanti! Forse ho visto quel terrorista che cerchiamo da settimane."
        ss2 "Quello con i capelli biondi, laggiù in fondo?"
        ss1 "Lui."
        ss2 "È il tuo giorno fortunato, italiano..."
        ss1 "... Ma sta' attento a cosa fai... A noi non sfugge niente!"
        op ON "¶¶ ¶¶ ¶¶¶¶? ¶¶¶¶¶¶¶¶! ¶ ¶¶ ¶¶¶ ¶¶¶¶¶?!"
        scene black onlayer master with fade
        pause 2.0   
        op "..."
        op "Grazie al cielo..."
        op "Mi hanno risparmiato."
        op "Ma la cosa più tremenda, più inumana..."
        op "... è che non so nemmeno perché."
        $ s6good = True
        jump mese5

    label mese6_b4:
        op ON "¶¶¶ ¶¶ ¶!"
        ss1 "Che ha detto?"
        ss2 "Poco importa!"
        ss1 "Quanti ne abbiamo già arrestati?"
        ss2 "39."
        ss1 "Allora facciamo numero tondo."
        ss2 "E 40 siano!"
        ss1 "TU! In fila con gli altri!"
        ss2 "C'è un treno che vi aspetta..."
        scene black onlayer master with fade
        pause 2.0   
        op "..."
        op "Un treno..."
        op "Mi deportano..."
        op "Ci deportano..."
        op "... ma non riusciranno a fermarci."
        $ s6bad = True
        jump mese5

label mese5:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n05 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/5 MUSSOLINI_1.mp3"
    centered "{size=48}{cps=18}- MUSSOLINI -\nNon se ne parla che raramente.\nLui non viene a sparare, perciò non conta.\nAi giovani, la sorte di Mussolini non interessa.\nPer essi, è come se fosse già morto.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c05 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    play music "audio/5_Anziana.mp3"
    scene s5 1 onlayer master
    show occhio_l onlayer master
    show lmouth OFF onlayer master
    t ON "È da ieri che ne parlano, alla radio."
    t ON "Hanno detto che sarebbe stata \"una manifestazione di eccezionale importanza\"..."
    t ON "\"Eccezionale\", sì."
    t ON "Come se di cose eccezionali non ne avessimo già avute abbastanza."
    if s7benitodead == True:
        t ON "Un nipote ucciso a scuola, come un topino in trappola, da una bomba dei nostri amici, dei nostri liberatori."
        t ON "Insieme ad altri 180 topini come lui."
    if s7martadead == True:
        t ON "Una nipote uccisa a scuola, come un topino in trappola, da una bomba dei nostri amici, dei nostri liberatori."
        t ON "Insieme ad altri 180 topini come lei."
    t ON "Un intero quartiere senza più bambini..."
    if s14sciopero == True:
        t ON "Una figlia che una mattina è andata a lavorare in fabbrica, come tutti gli altri giorni."
        t ON "E che la sera non è più tornata, solo perché aveva osato chiedere ciò che tutti vogliamo."
        t ON "Un po' di pane, e un po' di pace."
    t ON "Un altro nipote che alle nove della sera, quando scende il coprifuoco, esce di casa per combattere, nell'ombra."
    t ON "E che chissà se tornerà poi, anche lui, alle cinque del mattino."
    t OFF "..."
    t ON "Tutto eccezionale, tutto normale."
    t ON "Di questi tempi ci si abitua a tutto, anche all'eccezionale."
    t OFF "..."
    t ON "E allora..."
    t ON "Cosa ci sarà di eccezionale..."
    hide occhio_l onlayer master
    show s5 2 onlayer master
    show occhio_l onlayer master
    show occhio_m onlayer master
    with dissolve
    t "... in quello lì?"
    t "Come può, tutta quella gente, restare ancora ad ascoltare le sue parole?"
    t "Le sue parole..."
    label mese5_0:
        if camerati and fede and fascismo and riscossa == True:
            jump mese5_000
        menu:
            t "Le sue parole..."
            "\"Camerati, cari camerati milanesi...\"" if camerati == False:
                $ camerati = True
                jump mese5_1
            "\"So che la fede che vi anima è ancora e sempre quella del glorioso squadrismo artefice della rivoluzione delle camicie nere\"." if fede == False:
                $ fede = True
                jump mese5_2
            "\"Il fascismo milanese è all'altezza della sua tradizione primogenita e della sua odierna missione\"." if fascismo == False:
                $ fascismo = True
                jump mese5_3
            "\"È Milano che deve dare e darà gli uomini, le armi, la volontà e il segnale della riscossa\"." if riscossa == False:
                $ riscossa = True
                jump mese5_5

    label mese5_1:
        t2 ON "\"Camerati, cari camerati milanesi...\""
        t "Quanto tempo è passato?"
        t "Più di nove anni, dall'ultima volta che ci siamo visti qui a Milano."
        t "Nove, sì."
        t "Era il '36."
        t2 ON "\"Pace con tutti, coi vicini e coi lontani... Pace armata!\"."
        t "Pace, promettesti..."
        t "Guerra, ci hai dato."
        t "Quattro anni e mezzo di guerra."
        t "..."
        t "Puoi chiamarci pure \"camerati\", se lo vuoi."
        t "Ma non chiamarci \"cari\", bugiardo."
        jump mese5_0

    label mese5_2:
        t2 ON "\"So che la fede che vi anima è ancora e sempre quella del glorioso squadrismo...\""
        t2 ON "\"... artefice della rivoluzione delle camicie nere\"."
        t "\"Rivoluzione?\""
        t "Ancora parli di rivoluzione?"
        t "Non avevo ancora i capelli bianchi, la prima volta che te ne sentii parlare."
        t "E dopo tutto questo tempo, dopo venti e rotti anni di potere, ancora giochi a fare il socialista?"
        t "E quale \"gloria\" poi, quale \"fede\", negli scalmanati che ti vengon dietro solo per il gusto di menar le mani..."
        t "... senza che nessuno possa dirgli \"beh\"."
        t "..."
        t "Se non volete ancora gettare le armi..."
        t "... Almeno gettate le maschere."
        jump mese5_0

    label mese5_3:
        t2 ON "\"Il fascismo milanese è all'altezza della sua tradizione primogenita e della sua odierna missione\"."
        t "\"Missione\"..."
        t "Dove ho già sentito dirti questa parola?"
        t "O forse parlasti di..."
        t2 ON "\"Consegna\"!"
        t2 ON "\"Direttrici di marcia\"!"
        t2 ON "\"Imperioso dovere\"!"
        t "Poco importa."
        t "..."
        t "Oh, certo."
        t "Fu proprio qui, a Milano."
        label mese5_x:
            menu:
                t "Fu proprio qui, a Milano."
                "La tua \"generosa\" Milano" if generosa == False:
                    $ generosa = True
                    jump mese5_x1
                "La tua \"operosa\" Milano" if operosa == False:
                    $ operosa = True
                    jump mese5_x2
                "La tua \"infaticabile\" Milano" if infaticabile == False:
                    $ infaticabile = True
                    jump mese5_x3
                "La tua \"ardentissima\" Milano" if ardentissima == False:
                    $ ardentissima = True
                    jump mese5_x4
                "La tua \"fascistissima\" Milano" if generosa and operosa and infaticabile and ardentissima == True:
                    jump mese5_x5

            label mese5_x1:
                t "\"Generosa\", sì."
                t "Generosa nel pagare 200 lire per un pollo o 2000 per un paio di scarpe buone..."
                t "... quando la paga di un mese in fabbrica arriva sì e no a 1000."
                jump mese5_x

            label mese5_x2:
                t "\"Operosa\", sì."
                t "Operosa nel cercare in qualche modo di sopravvivere, di mettere assieme qualche centinaio di lire..."
                t "... da spendere al mercato nero."
                jump mese5_x

            label mese5_x3:
                t "\"Infaticabile\", sì."
                t "Infaticabile perché, dopo quindici mesi di occupazione, anche la fatica è diventata un lusso..."
                t "... un lusso che non possiamo più permetterci."
                jump mese5_x

            label mese5_x4:
                t "\"Ardentissima\", sì."
                t "Ardentissima del fuoco delle bombe."
                jump mese5_x

            label mese5_x5:
                t "La tua \"fascistissima\" Milano..."
                t "..."
                t "Attento."
                t "Attento a non sentirti troppo a casa."
                t "A volte, è proprio in casa propria che più si rischia di farsi male."
                jump mese5_0

label mese5_5:
    t2 ON "\"È Milano che deve dare e darà gli uomini, le armi, la volontà e il segnale della riscossa\"."
    t "..."
    t "Questo è vero..."
    t "Ma non sono certo gli uomini, le armi, la volontà e la riscossa che ti immagini."
    t "Al contrario!"
    jump mese5_0

label mese5_000:
    show s5 3 onlayer master
    with dissolve
    $ ui.timer(0.3, ui.jumps("mese5_001"))
    menu:
        t "Le sue parole..."
        "\".\"":
            jump mese5_4
label mese5_001:
    $ ui.timer(0.3, ui.jumps("mese5_002"))
    menu:
        t "Le sue parole..."
        "\"...\"":
            jump mese5_4
        "\".\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
label mese5_002:
    $ ui.timer(0.3, ui.jumps("mese5_003"))
    menu:
        t "Le sue parole..."
        "\".....\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
label mese5_003:
    $ ui.timer(0.3, ui.jumps("mese5_004"))
    menu:
        t "Le sue parole..."
        "\"........\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
        "\"........\"":
            jump mese5_4
label mese5_004:
    $ ui.timer(0.3, ui.jumps("mese5_005"))
    menu:
        t "Le sue parole..."
        "\"...............\"":
            jump mese5_4
        "\".......\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
        "\".......\"":
            jump mese5_4
        "\"...............\"":
            jump mese5_4
label mese5_005:
    $ ui.timer(0.3, ui.jumps("mese5_006"))
    menu:
        t "Le sue parole..."
        "\".......................\"":
            jump mese5_4
        "\"...............\"":
            jump mese5_4
        "\".......\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
        "\".......\"":
            jump mese5_4
        "\"...............\"":
            jump mese5_4
        "\".......................\"":
            jump mese5_4
label mese5_006:
    $ ui.timer(0.3, ui.jumps("mese5_007"))
    menu:
        t "Le sue parole..."
        "\"....................................\"":
            jump mese5_4
        "\".......................\"":
            jump mese5_4
        "\"...............\"":
            jump mese5_4
        "\".......\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
        "\".......\"":
            jump mese5_4
        "\"...............\"":
            jump mese5_4
        "\".......................\"":
            jump mese5_4
        "\"....................................\"":
            jump mese5_4
label mese5_007:

    menu:
        t "Le sue parole..."
        "\".........................................................\"":
            jump mese5_4
        "\"....................................\"":
            jump mese5_4
        "\".......................\"":
            jump mese5_4
        "\"...............\"":
            jump mese5_4
        "\".......\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".\"":
            jump mese5_4
        "\"...\"":
            jump mese5_4
        "\".....\"":
            jump mese5_4
        "\".......\"":
            jump mese5_4
        "\"...............\"":
            jump mese5_4
        "\".......................\"":
            jump mese5_4
        "\"....................................\"":
            jump mese5_4
        "\".........................................................\"":
            jump mese5_4

label mese5_4:
    t ON "Vedi?"
    t ON "Le tue parole non hanno più alcun senso, per me."
    t ON "Parli, ma io non ti capisco."
    t ON "Non più."
    t "Parli, ma parleremo anche noi, presto."
    t "Parlerà Longo e parlerà Sereni, parlerà Pertini e parlerà Valiani."
    t "E sarà per dirti una cosa molto semplice."
    t "\"Pena di morte\"."
    t "..."
    show s5 1 onlayer master
    hide occhio_m onlayer master
    t ON "Ci rivediamo presto."
    jump mese4


label mese4:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n04 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/4 SPIA_1.mp3"
    centered "{size=48}{cps=18}- SPIA -\nNel Paese in cui viviamo, tutti lo possono essere.\nPer questo siamo spietati con le spie,\nanche a rischio di cadere in errori.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c04 onlayer master with fade

    $ renpy.pause(3.0, hard=True)
    play music "audio/4_incubo.mp3" fadein 2.0
    scene black onlayer master
    show incuboFermo onlayer master at truecenter
    show umouth OFF onlayer master
    with dissolve
    u "..."
    u ON "Il maiale..."
    u ON "... L'hanno macellato senza il permesso..."
    u ON "... Prendeteli..."
    scene incubo onlayer master at truecenter with Dissolve (0.01)
    pause 3.0
    scene falo onlayer master with Dissolve(5.0)
    pause 1.0
    menu:
        "Lo giuro, non sono stato io!":
            jump mese4_a
        "Sono stato costretto!":
            jump mese4_a
        "Lasciatemi andare e vi dirò i nomi dei veri colpevoli!":
            jump mese4_a

label mese4_a:
    u1 "Ormai è troppo tardi, Ernesto..."
    u1 "La guerra è finita!"
    u1 "E abbiamo vinto noi!"
    u1 "Ora pagherai per tutto il male che hai fatto..."
    u1 "... Spia!"
    u1 "Lo sappiamo da che parte stavi!"
    u1 "Confessa!"
    menu:
        "Ma io... ero dalla vostra parte!":
            jump mese4_a1
        "Ma io... sono un partigiano!":
            jump mese4_a1
        "Ma... ma... ma... ma... ma...":
            jump mese4_a1

label mese4_a1:
    u1 "Sei un maiale, ecco cosa sei."
    u1 "Un boia."
    u1 "Ricordi cosa ti disse l'Angelino, quando lo consegnasti a quei porci?"
    u1 "\"Meglio se muori, perché se sopravvivi e a vincere saremo noi, intorno a te ci sarà solo silenzio.\""
    u1 "\"Vivrai, ma sarà come se tu fossi morto.\""
    u "Non mi ucciderete?"
    u1 "Sei fortunato!"
    u1 "L'Angelino ci ha suggerito di usarti come legna da bruciare..."
    u1 "... per il Falò di Sant'Antonio!"
    u1 "... Il protettore dei maiali."
    u1 "Come te."
    u "Ma... l'Angelino è morto da 6 mesi!"
    u1 "Una punizione azzeccata per uno come te, non trovi?"
    u1 "Hai fatto la spia contro le povere famiglie che non dichiaravano la macellazione del maiale..."
    u1 "... E ora verrai trattato come il maiale che ogni anno macelliamo e mangiamo in queste fredde notti."
    u "Io non ho mai detto nulla!"
    u "Lo giuro!"
    u1 "Certo, Ernesto! Non hai mai detto nulla!"

label mese4_cambio:
    menu:
        "Ma io ero dalla vostra parte!":
            jump mese4_cambio1
        "Ma io sono partigiano come voi!":
            jump mese4_cambio1
        "Ma io non sono una spia!":
            jump mese4_cambio1

label mese4_cambio1:
    menu:
        "Ma io non ero fascista!":
            jump mese4_cambio2
        "Ma io sono stato zitto!":
            jump mese4_cambio2
        "Ma io non sto da nessuna parte!":
            jump mese4_cambio2

label mese4_cambio2:
    menu:
        "Ma io ero d'accordo con voi!":
            jump mese4_cambio3
        "Ma io non ho denunciato l'Angelino!":
            jump mese4_cambio3
        "Ma io non ho mai fatto la spia!":
            jump mese4_cambio3

label mese4_cambio3:
    $ ui.timer(2.3, ui.jumps("mese4_cambio4"))
    menu:
        "Ma io ero al sicuro!":
            jump mese4_cambio4
        "Ma io sono in pericolo!":
            jump mese4_cambio4
        "Ma io perchè sono qui?":
            jump mese4_cambio4

label mese4_cambio4:
    $ ui.timer(2.0, ui.jumps("mese4_cambio5"))
    menu:
        "Ma i fascisti mi hanno ingannato!":
            jump mese4_cambio5
        "Ma i partigiani hanno perso!":
            jump mese4_cambio5
        "Ma Mussolini ve la farà pagare!":
            jump mese4_cambio5

label mese4_cambio5:
    $ ui.timer(1.5, ui.jumps("mese4_cambio6"))
    menu:
        "Ma gli americani hanno perso!":
            jump mese4_cambio6
        "Ma i partigiani hanno vinto!":
            jump mese4_cambio6
        "Ma i fascisti hanno perso!":
            jump mese4_cambio6

label mese4_cambio6:
    $ ui.timer(1.0, ui.jumps("mese4_cambio7"))
    menu:
        "Ma gli americani sono fascisti?!":
            jump mese4_cambio7
        "Ma io sono partigiano?!":
            jump mese4_cambio7
        "Ma voi siete fascisti?!":
            jump mese4_cambio7

label mese4_cambio7:
    $ ui.timer(1.5, ui.jumps("mese4_cambio8"))
    menu:
        "IO SONO UNA SPIA?":
            jump mese4_cambio8
        "VOI SIETE LA SPIA?":
            jump mese4_cambio8
        "QUALCUNO MI AIUTI!":
            jump mese4_cambio8

label mese4_cambio8:
    u "..."
    u1 "L'unica parte in cui ti trovi ora..."
    u1 "È quella dei morti!"
    u1 "Brucia all'inferno, boia!"
    u1 "BRUCIA!"
    jump mese4_fin

label mese4_fin:
    scene sveglia onlayer master at truecenter with dissolve
    show s04_1 onlayer master
    show s04_7 onlayer master
    show umouth OFF onlayer master
    with Dissolve (5.0)
    pause 0.5
    show ueye onlayer master
    u "..."
    u ON "Era solo un incubo."
    u "..."
    u ON "E se diventasse realtà?"
    scene black onlayer master
    with dissolve
    pause 0.5
    jump mese3

label mese3:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n03 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/3 CASA_1.mp3"
    centered "{size=48}{cps=20}- CASA -\nMeglio non pensarci.\nCol tempo, non è poi tanto difficile.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    play music "audio/3_lettera.mp3"
    scene c03 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    scene s18pelle onlayer master
    show vchar 2 onlayer master
    show veye onlayer master
    show vmouth OFF onlayer master
    with fade
    v ON "... Una lettera!"
    v ON "Una lettera da Carlo!"
    v ON "Allora sei vivo!"
    v ON "Il retro della cartolina è mezzo in tedesco e mezzo in italiano."
    v ON "C'è scritto \"corrispondenza dei prigionieri di guerra\"..."
    v ON "... e c'è una sigla strana, scritta a mano, dove dice \"designazione del campo\"..."
    v ON "M.Stamm.Lager.III.D.883\"."
    scene bg3 onlayer master
    show lettera onlayer master
    show vchar 2 onlayer master
    show veye onlayer master
    show vmouth OFF onlayer master
    with Dissolve (5)
    v ON "Chissà cosa significa... E dove sei... Da qualche parte, in Germania..."
    v ON "Devi essere stato catturato dopo l'8 settembre."
    v ON "Magari stavi cercando di tornare qui a casa..."
    v ON "Magari stavi aspettando gli ordini del tuo sergente..."
    v ON "O magari non ci hai capito proprio niente, come non ci abbiamo più capito niente neanche noi."
    v ON "Oh, Carlo..."
    v OFF "..."
    v ON "L'importante è che sei vivo!"
    v ON "E che ci sia scritto il tuo nome, qui... \"Carlo\"..."
    v ON "\"Carlo Pini\"."
    show ink behind lettera onlayer master
    v OFF "..."
    v ON "Cosa mi scrivi, amore mio?"
    label mese3_0:
    menu:
        v "Cosa mi scrivi, amore mio?"
        "\"Cara moglie, con molto piacere ti invio i miei sinceri saluti.\"":
            $ lettera1 = True
            jump mese3_1
        "\"Io sto molto bene, così spero di te e di tutti.\"" if lettera1 == True:
            $ lettera2 = True
            jump mese3_2
        "\"Qua c'è la carta per inviarmi qualche pacco, manda da mangiare e tabacco.\"" if lettera2 == True:
            $ lettera3 = True
            jump mese3_3
        "\"Di nuovo saluti e baci, tuo Carlo.\"" if lettera3 == True:
            $ lettera4 = True
            jump mese3_4
        "Oh... C'è un dettaglio che mi era sfuggito..." if lettera1 and lettera2 and lettera3 and lettera4 == True:
            jump mese3_5

label mese3_1:
    v ON "\"Cara moglie, con molto piacere ti invio i miei sinceri saluti.\""
    label mese3_1a:
    $ ui.timer(4.0, ui.jumps("mese3_1b"))
    menu:
        v "\"Cara moglie, con molto piacere ti invio i miei sinceri saluti.\""
        "Oh, il mio Carlo... >>":
            $ lettera1good = True
            jump mese3_0
        "Che strano, Carlo... >>":
            $ lettera1good = False
            jump mese3_0
    label mese3_1b:
    $ ui.timer(4.0, ui.jumps("mese3_1c"))
    menu:
        v "\"Cara moglie, con molto piacere ti invio i miei sinceri saluti.\""
        "Sempre così educato... >>":
            $ lettera1good = True
            jump mese3_0
        "Così freddo, distante... >>":
            $ lettera1good = False
            jump mese3_0
    label mese3_1c:
    $ ui.timer(5.0, ui.jumps("mese3_1a"))
    menu:
        v "\"Cara moglie, con molto piacere ti invio i miei sinceri saluti.\""
        "Anche rinchiuso in un campo di prigionia, pensi sempre a me! >>":
            $ lettera1good = True
            jump mese3_0
        "Che ti sia dimenticato di me, rinchiuso in quel campo di prigionia? >>":
            $ lettera1good = False
            jump mese3_0

label mese3_2:
    v ON "\"Io sto molto bene, così spero di te e di tutti.\""
    label mese3_2a:
    $ ui.timer(5.0, ui.jumps("mese3_2b"))
    menu:
        v "\"Io sto molto bene, così spero di te e di tutti.\""
        "Stai molto bene... Che gioia, che sollievo! >>":
            $ lettera2good = True
            jump mese3_0
        "Com'è possibile che tu stia molto bene?! >>":
            $ lettera2good = False
            jump mese3_0
    label mese3_2b:
    $ ui.timer(5.0, ui.jumps("mese3_2c"))
    menu:
        v "\"Io sto molto bene, così spero di te e di tutti.\""
        "Sei sempre stato un ragazzo forte e sincero, Carlo... >>":
            $ lettera2good = True
            jump mese3_0
        "Prigioniero lassù in Germania... Lo scrivi solo per illudermi? >>":
            $ lettera2good = False
            jump mese3_0
    label mese3_2c:
    $ ui.timer(5.0, ui.jumps("mese3_2a"))
    menu:
        v "\"Io sto molto bene, così spero di te e di tutti.\""
        "E così gentile, a preoccuparti che anche noi stiamo bene! >>":
            $ lettera2good = True
            jump mese3_0
        "Devi stare tanto male, per sperare che almeno noi stiamo bene... >>":
            $ lettera2good = False
            jump mese3_0

label mese3_3:
    v ON "\"Qua c'è la carta per inviarmi qualche pacco, manda da mangiare e tabacco.\""
    label mese3_3a:
    $ ui.timer(4.0, ui.jumps("mese3_3b"))
    menu:
        v "\"Qua c'è la carta per inviarmi qualche pacco, manda da mangiare e tabacco.\""
        "Il mio solito Carlo... >>":
            $ lettera3good = True
            jump mese3_0
        "Povero Carlo... >>":
            $ lettera3good = False
            jump mese3_0
    label mese3_3b:
    $ ui.timer(5.0, ui.jumps("mese3_3c"))
    menu:
        v "\"Qua c'è la carta per inviarmi qualche pacco, manda da mangiare e tabacco.\""
        "Ti è sempre piaciuto mangiare e fumare! Bravo, amore mio... >>":
            $ lettera3good = True
            jump mese3_0
        "Ti deve mancare il cibo per vivere, se lo chiedi a me... >>":
            $ lettera3good = False
            jump mese3_0
    label mese3_3c:
    $ ui.timer(5.0, ui.jumps("mese3_3a"))
    menu:
        v "\"Qua c'è la carta per inviarmi qualche pacco, manda da mangiare e tabacco.\""
        "Già mi immagino la tua felicità, quando scarterai il mio pacco! >>":
            $ lettera3good = True
            jump mese3_0
        "Ma se pure ti mandassi un pacco, so già che i tedeschi lo terrebbero per sé. >>":
            $ lettera3good = False
            jump mese3_0

label mese3_4:
    v ON "\"Di nuovo saluti e baci, tuo Carlo.\""
    label mese3_4a:
    $ ui.timer(5.0, ui.jumps("mese3_4b"))
    menu:
        v "\"Di nuovo saluti e baci, tuo Carlo.\""
        "Mi baci, Carlo... >>":
            $ lettera4good = True
            jump mese3_0
        "Mi saluti, Carlo... >>":
            $ lettera4good = False
            jump mese3_0
    label mese3_4b:
    $ ui.timer(5.0, ui.jumps("mese3_4c"))
    menu:
        v "\"Di nuovo saluti e baci, tuo Carlo.\""
        "Ti bacio anch'io, mio caro. >>":
            $ lettera4good = True
            jump mese3_0
        "Ti saluto anch'io, mio caro. >>":
            $ lettera4good = False
            jump mese3_0
    label mese3_4c:
    $ ui.timer(5.0, ui.jumps("mese3_4a"))
    menu:
        v "\"Di nuovo saluti e baci, tuo Carlo.\""
        "E ti bacerò ancora, presto, quando sarai tornato qui da me! >>":
            $ lettera4good = True
            jump mese3_0
        "Ma temo sia un saluto d'addio, e che potresti non tornare più da me... >>":
            $ lettera4good = False
            jump mese3_0

label mese3_5:
    v ON "Oh... C'è un dettaglio che mi era sfuggito..."
    v ON "La data di questa lettera..."
    v ON "C'è scritto... \"25.12.1943\"!"
    label mese3_5a:
    $ ui.timer(3.0, ui.jumps("mese3_5b"))
    menu:
        v "C'è scritto... \"25.12.1943\"!"
        "\"25.12\"... il giorno di Natale! >>":
            $ lettera5good = True
            jump mese3_6
        "\"25.12\"... il giorno di Natale! >>":
            $ lettera5good = False
            jump mese3_6
    label mese3_5b:
    $ ui.timer(6.0, ui.jumps("mese3_5c"))
    menu:
        v "\"Di nuovo saluti e baci, tuo Carlo.\""
        "Così bravo, il mio Carlo... Hai calcolato che la lettera ci avrebbe messo mesi ad arrivare... >>":
            $ lettera5good = True
            jump mese3_6
        "Era Natale quando mi hai scritto ma non te ne sei nemmeno accorto, povero Carlo... >>":
            $ lettera5good = False
            jump mese3_6
    label mese3_5c:
    $ ui.timer(5.0, ui.jumps("mese3_5a"))
    menu:
        v "\"Di nuovo saluti e baci, tuo Carlo.\""
        "... E me l'hai scritta così apposta, per non farmi preoccupare! >>":
            $ lettera5good = True
            jump mese3_6
        "La vita in quello \"stammlager\" dev'essere un vero inferno... >>":
            $ lettera5good = False
            jump mese3_6

label mese3_6:
    if lettera1good == True:
        $ lcountgood +=1
    if lettera2good == True:
        $ lcountgood +=1
    if lettera3good == True:
        $ lcountgood +=1
    if lettera4good == True:
        $ lcountgood +=1
    if lettera5good == True:
        $ lcountgood +=1
    if lcountgood >=3:
        jump mese3_good
    else:
        jump mese3_bad

label mese3_good:
    v ON "Carlo..."
    v ON "Questa lettera..."
    v ON "È la gioia più grande che potessi avere."
    v ON "Ora so che presto tornerai da me..."
    v ON "Ti aspetto a casa, amore mio."
    v ON "Ti aspetto..."
    $ s3good = True
    jump mese8

label mese3_bad:
    v ON "Carlo..."
    v ON "Questa lettera..."
    v ON "È il dolore più grande che potessi avere."
    v ON "Ora so che non tornerai più da me..."
    v ON "Addio, amore mio."
    v ON "Addio..."
    $ s3bad = True
    jump mese8

label mese8:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n02 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/8 PARTIGIANI_3.mp3"
    centered "{size=48}{cps=18}- PARTIGIANI -\nCe ne sono di tutti i tipi:\nleali e opportunisti, eroi e doppiogiochisti, consapevoli e no.\nCombattono una delle diecimila guerre\nche l’uomo ha scatenato su questa terra\ne pensano di essere dalla parte della ragione.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c02 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    play music "audio/8_questionePrivata.mp3"
    scene black onlayer master with dissolve
    w ON "Come ci sono arrivato, stanotte, qui, io?"
    scene sfondo onlayer master
    show filo onlayer master
    show wchar 1 onlayer master
    show wmouth OFF onlayer master
    show weye onlayer master
    with dissolve
    w ON "Acquattato di fronte a questo palazzaccio dove i fascisti imprigionano, picchiano e uccidono i miei compagni..."
    w ON "Fascisti... Di questi tempi, ce ne sono di tutti i tipi."
    show w3 behind wchar onlayer master at pattuglia with dissolve
    w ON "Guardia Nazionale, Brigate Nere, Decima Mas, Legione Muti, SS italiane..."
    w ON "Chissà..."
    w ON "Chissà se anche loro pensano di essere dalla parte della ragione."
    w ON "... Come noi."
    w ON "Come me."
    w OFF "..."
    w ON "Io..."
    w ON "Ma chi sono poi, io?"
    label mese8_000:
    menu:
        w "Ma chi sono poi, io?"
        "Sono...":
            jump mese8_1

    label mese8_1:


        menu:
            w "Sono..."
            "Sono un ragazzo":
                jump mese8_2
            "Sono un partigiano":
                jump mese8_3

        label mese8_2:
            w ON "Sono un ragazzo."
            w ON "Un ragazzo di vent'anni che si è innamorato della ragazza sbagliata."
            show wchar 2 onlayer master
            show w2 behind filo onlayer master at fantasma
            with dissolve
            menu:
                w "Un ragazzo che si è innamorato della ragazza sbagliata."
                "La ragazza sbagliata, già...":
                    jump mese8_4
                "... O forse l'unica giusta?":
                    jump mese8_5

            label mese8_4:
                w ON "La ragazza sbagliata, già..."
                w ON "Fulvia..."
                w ON "Com'era bella, la Fulvia."
                w ON "Ma quanto è stata crudele con me."
                menu:
                    w "Ma quanto è stata crudele con me."
                    "Crudele, già...":
                        jump mese8_8
                    "... Ma anche tanto cara.":
                        jump mese8_9

                label mese8_8:
                    w ON "Crudele, già..."
                    w ON "Tradirmi così, in quel modo, mentre ero via, a combattere."
                    w ON "E non con uno qualunque."
                    w ON "Tradirmi con un amico, un compagno..."
                    show wchar 2 onlayer master
                    show w1 behind filo onlayer master at camminata4
                    with dissolve
                    w ON "...Giorgio!"
                    menu:
                        w "Tradirmi con un amico, un compagno... Giorgio!"
                        "Almeno... Questo è quanto sono venuto a sapere.":
                            jump mese8_x
                        "... Ma sarà poi vero?":
                            jump mese8_x

                label mese8_9:
                    w ON "Tanto cara e tanto crudele."
                    w OFF "..."
                    w ON "Tanto cara o tanto crudele?"
                    w ON "C'è una sola persona che mi può dire la verità."
                    w ON "Ed è prigioniera lì dentro."
                    show wchar 2 onlayer master
                    show w1 behind filo onlayer master at camminata4
                    with dissolve
                    w ON "Lui, Giorgio."
                    menu:
                        w "Lui, Giorgio."
                        "... Il mio amico.":
                            jump mese8_x
                        "... Il ragazzo con cui Fulvia mi ha tradito.":
                            jump mese8_x

            label mese8_5:
                w ON "... O forse l'unica giusta?"
                w ON "Sì, Fulvia era l'unica ragazza giusta per me."
                w ON "Com'era bella, la Fulvia."
                w ON "E quanto è stata cara con me."
                menu:
                    w "E quanto è stata cara con me."
                    "Cara, già...":
                        jump mese8_10
                    "... Ma anche tanto crudele.":
                        jump mese8_9

                label mese8_10:
                    w ON "Cara, già..."
                    w ON "Quanto sarà? Un anno, a giorni?"
                    w OFF "..."
                    w ON "Che pazienza che ha avuto, la Fulvia..."
                    w ON "Mi ha atteso, e atteso, e atteso ancora."
                    w ON "Fino a quando... non è stato troppo tardi."
                    w ON "Ma che altro avrebbe potuto fare?"
                    menu:
                        w "Ma che altro avrebbe potuto fare?"
                        "E poi, in fondo, Giorgio è un bravo ragazzo.":
                            jump mese8_x
                        "Giorgio... Non dovevi farmi questo.":
                            jump mese8_x

        label mese8_3:
            w "Sono un partigiano"
            w "Un partigiano impegnato nella sua missione più folle."
            menu:
                w "Un partigiano impegnato nella sua missione più folle."
                "La missione più folle, già...":
                    jump mese8_6
                "... O forse l'unica sensata?":
                    jump mese8_7

            label mese8_6:
                w ON "La missione più folle, già..."
                w ON "Solo, contro un intero comando di fascisti."
                w ON "Per liberare un compagno, uno solo."
                show w1 behind filo onlayer master at camminata4
                with dissolve
                w ON "Giorgio."
                w ON "Solo... come me."
                menu:
                    w "Solo... come me."
                    "Ma ne vale la pena?":
                        jump mese8_11
                    "Ne vale la pena.":
                        jump mese8_12

                label mese8_11:
                    w ON "Ma ne vale la pena?"
                    w ON "Non ne sono più sicuro."
                    w ON "Quante probabilità ho di riuscirci?"
                    w ON "Una su mille? Una su un milione?"
                    menu:
                        w "Una su mille? Una su un milione?"
                        "Fosse anche una su un miliardo...!":
                            jump mese8_x
                        "Resta una missione folle, disperata.":
                            jump mese8_x

                label mese8_12:
                    w ON "Ne vale la pena."
                    w ON "Certo che ne vale la pena."
                    w ON "Non mi importa se i fascisti che tengono Giorgio prigioniero lì dentro pensano anche loro di essere dalla parte della ragione."
                    w ON "Dalla parte della ragione, siamo noi."
                    menu:
                        w "Dalla parte della ragione, siamo noi."
                        "Non ho dubbi sulla mia scelta.":
                            jump mese8_x
                        "È andata così, come doveva andare.":
                            jump mese8_x

            label mese8_7:
                w ON "... O forse l'unica sensata?"
                w ON "Liberare un compagno prigioniero dei fascisti."
                show w1 behind filo onlayer master at camminata4
                with dissolve
                w ON "E non un compagno come gli altri."
                w ON "Giorgio, un amico."
                menu:
                    w "Giorgio, un amico."
                    "Glielo devo.":
                        jump mese8_13
                    "Ma ne vale la pena?":
                        jump mese8_11

                label mese8_13:
                    w ON "Glielo devo."
                    w ON "Lui farebbe lo stesso per me."
                    menu:
                        w "Lui farebbe lo stesso per me."
                        "Ne sono sicuro.":
                            jump mese8_x
                        "Forse.":
                            jump mese8_x

label mese8_x:
    w ON "Ma ora basta con tutti questi pensieri!"
    w ON "Potrei restare qui a pensare all'infinito."
    w ON "Ma ora non è più il momento di pensare."
    w ON "Bisogna agire."
    w OFF "..."
    w ON "... ORA!"
    scene black onlayer master
    pause 1.0
    play sound "audio/sound/212600__pgi__machine-gun-001-triple-shot.mp3"
    menu:
        "... Sparano! Fermati, Milton.":
            jump mese8_x2
        "... Non importa! Corri, Milton.":
            jump mese8_x3

label mese8_x2:
    w "Vedi?"
    w "Vedi cosa sarebbe potuto succederti?"
    w "Pensa, Milton."
    w "Pensa, prima di agire."
    jump mese8_0

label mese8_x3:
    pause 0.5
    play sound "audio/sound/212600__pgi__machine-gun-001-triple-shot.mp3"
    menu:
        "... Sparano ancora! Fermo!":
            jump mese8_x2
        "... No, non ti fermare! Continua a correre!":
            jump mese8_x4

label mese8_x4:
    pause 0.5
    play sound "audio/sound/212600__pgi__machine-gun-001-triple-shot.mp3"
    menu:
        "... FERMO!":
            jump mese8_x2
        "... AVANTI!":
            jump mese8_x5

label mese8_x5:
    play sound "audio/sound/212600__pgi__machine-gun-001-triple-shot.mp3"
    w "Avanti, Milton..."
    w "Sempre avanti."
    jump mese1

label mese8_0:
    scene sfondo onlayer master
    show filo onlayer master
    show wchar 1 onlayer master
    show wmouth OFF onlayer master
    show weye onlayer master
    show w3 behind wchar onlayer master at pattuglia
    with dissolve
    jump mese8_000


label mese1:
    stop music fadeout 2.0
    scene black onlayer master
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/248237_jarredgibb_match-strike-and-light-01_CUT.mp3"
    $ renpy.pause(0.2, hard=True)
    scene n01 onlayer master with fade
    $ renpy.pause(2.5, hard=True)
    scene black onlayer master
    play sound "audio/voice/1 DOMANI_1.mp3"
    centered "{size=48}{cps=15}- DOMANI -\nSi spera sempre che sia migliore.\nChe sia finalmente l’ultimo giorno\ndi questa storia.{/cps}{/size}\n__________\n\n{size=36}dal \"Dizionario del Partigiano Anonimo\"{/size}\n\n\n{p=2.0}{size=24}clicca per continuare{/size}"
    scene c01 onlayer master with fade
    $ renpy.pause(3.0, hard=True)
    play music "audio/1_medico.mp3"
    scene black onlayer master
    show cinema onlayer master
    show zeye onlayer master
    with fade
    y "Vengo qui."
    y "Vengo qui, a smettere di pensare."
    y "Vengo qui, a ricordarmi che sono ancora un uomo."
    y "Ancora prima di essere un italiano, un non ebreo, un non partigiano, un non fascista."
    y "Vengo qui, al cinema."
    show end 0 behind cinema onlayer master at schermo
    with dissolve
    y "Sono un uomo, dunque."
    y "Un uomo che resiste."
    y "Che resiste alla fame, alla morte, alla rabbia, alla paura, ai soprusi."
    y "Che resiste a tutte le brutture che da troppi mesi ci circondano."
    y "Troppi mesi... Quanti?"
    y "E ci siamo dentro tutti, in questa specie di scatola di fiammiferi che è la guerra."
    y "I cattivi che non hanno più paura di niente, e i buoni che hanno dimenticato cosa vuol dire sperare."
    y "Tutti."
    y "..."
    y "Ma sono anche un medico, io."
    y "E per un medico non ci sono buoni o cattivi."
    y "..."
    y "La pellicola va... ed io, anziché smettere di pensare, penso."
    y "Penso al mio amico Ornello, prigioniero in Germania, che si è improvvisato medico."
    y "Per salvare da morte certa tanti altri prigionieri come lui."
    y "Medico anche lui. Medico per forza."
    y "Penso a lui, e a quella forza che a volte perdo, ma che spero di ritrovare..."
    y "... domani."
    y "Perché è non riuscire a pensare al domani, la vera malattia."
    y "Perché un domani, uno qualunque, c'è sempre."
    y "Per tutti."
    if s20casa == True:
        show end 20 casa onlayer master
        with dissolve
        y "Per quelli che hanno sperato di tornare a casa, e abbandonare la guerra..."
    if s20ordini == True:
        show end 20 ordini onlayer master
        with dissolve
        y "Per quelli che hanno deciso di seguire gli ordini, fino alla fine..."
    if s20boh == True:
        show end 20 boh onlayer master
        with dissolve
        y "Per quelli che hanno aspettato che qualcun altro scegliesse per loro..."
    if s19good == True:
        show end 19 good onlayer master
        with dissolve
        y "... E per chi ha fatto pace con il nemico."
    if s19bad == True:
        show end 19 bad onlayer master
        with dissolve
        y "... E per chi si sente grande, solo perché ha una divisa addosso."
    show end 18 onlayer master
    with dissolve
    y "Per gli innocenti, che confondono la luce delle bombe per stelle cadenti..."
    if s17good == True:
        show end 17 good onlayer master
        with dissolve
        y "... E per chi sta ancora imparando a fare i conti con la propria coscienza."
    if s17bad == True:
        show end 17 bad onlayer master
        with dissolve
        y "... E per chi è stato dannato dalla guerra, e ha scelto di farla finita."
    if s16god == True:
        show end 16 onlayer master
        with dissolve
        y "Per quelli che si chiedono dove sia finito Dio, in questa guerra..."
    if s16man == True:
        show end 16 onlayer master
        with dissolve
        y "Per quelli che si chiedono dove sia finito l'uomo, in questa guerra..."
    if s2prisongood == True:
        show end 15 onlayer master
        with dissolve
        y "... E per chi non ha confessato, nemmeno sotto tortura."
    if s2prisonbad == True:
        show end 15 onlayer master
        with dissolve
        y "... E per chi non ha potuto far altro che confessare, sotto tortura."
    if s2torture == True:
        show end 15 onlayer master
        with dissolve
        y "... E per chi non potrà far altro che confessare, sotto tortura."
    if s14sciopero == True:
        show end 14 sciopero onlayer master
        with dissolve
        y "Per chi ha scelto di scioperare, a qualunque costo, per il pane e per la pace..."
    if s14nosciopero == True:
        show end 14 nosciopero onlayer master
        with dissolve
        y "Per chi ha scelto un tozzo di pane oggi, piuttosto che la pace domani..."
    if s15good == True:
        show end 13 good onlayer master
        with dissolve
        y "... E per chi è protetto dai suoi cari, senza nemmeno che lo sappia."
    if s15bad == True:
        show end 13 bad onlayer master
        with dissolve
        y "... E per chi origlia da dietro una porta, senza mai capirci nulla."
    if s12good == True:
        show end 12 onlayer master
        with dissolve
        y "Per chi ha avuto il coraggio di disobbedire..."
    if s12bad == True:
        show end 12 onlayer master
        with dissolve
        y "Per chi non ha avuto il coraggio di disobbedire..."
    if s11good == True:
        show end 11 onlayer master
        with dissolve
        y "... E per chi mette la sua vita al servizio della giusta causa."
    if s11bad == True:
        show end 11 onlayer master
        with dissolve
        y "... E per chi continuerà a vivere ricordato per il suo coraggio."
    show end 10 onlayer master
    with dissolve
    y "Per quelli che scelgono di fare la fame, pur di rimanere insieme..."
    show end 9 onlayer master
    with dissolve
    y "... E per chi sarà per sempre la voce di chi non c'è più."
    if s13bacio == True:
        show end 8 bacio onlayer master
        with dissolve
        y "Per coloro che si amano, e che per dirselo scelgono il momento peggiore, il più segreto, il più sicuro..."
    if s13nobacio == True:
        show end 8 nobacio onlayer master
        with dissolve
        y "Per coloro che si amano, anche senza dirselo..."
    show end 7 onlayer master
    with dissolve
    y "... E per chi ha dovuto fare la scelta più difficile, al posto di qualcun altro."
    if s6good == True:
        show end 6 onlayer master
        with dissolve
        y "Per chi è stato risparmiato..."
    if s6bad == True:
        show end 6 onlayer master
        with dissolve
        y "Per chi è stato preso..."
    show end 5 onlayer master
    with dissolve
    y "... E per chi non dimentica."
    show end 4 onlayer master
    with dissolve
    y "Per chi pagherà, e nei suoi incubi sta già pagando..."
    if s3good == True:
        show end 3 onlayer master
        with dissolve
        y "... E per chi ha il dono di non saper leggere tra le righe."
    if s3bad == True:
        show end 3 onlayer master
        with dissolve
        y "... E per chi, suo malgrado, sa leggere tra le righe."
    show end 2 onlayer master
    with dissolve
    y "Per chi corre, e non si ferma, perché sa che sta facendo la cosa giusta, anche se non sa, davvero, perché..."
    show end 1 onlayer master
    with dissolve
    y "... E per chi, come me, pensa che venti mesi siano troppi, per resistere a una guerra così grottesca."
    y "..."
    y "Oggi è il 24 aprile 1945..."
    y "Dove sarò, domani?"
    y "Dove sarò, oggi, tra 70 anni?"
    y "Ancora in un cinema a dimenticare, o a ricordare?"
    y "Ancora... uomo?"
    scene black onlayer master
    with fade
    jump mese0

label mese0:
    stop music fadeout 3.0
    scene black onlayer master
    $ renpy.pause(4.0, hard=True)
    scene c00 onlayer master with fade
    $ renpy.pause(4.0, hard=True)
    scene black onlayer master with fade

    play sound "audio/voice/01_RESISTENZA.mp3"
    centered "{size=36}{i}Cos'è la Resistenza, se non, semplicemente,\nla forma più 'radicale' di esistenza?{/i}{/size}{p=6.0}{nw}"
    play music "audio/0_Finale.mp3" fadein 3.0
    play sound "audio/voice/02_RESISTENZA.mp3"
    centered "{size=36}{i}Resistere - come a una tempesta, facendo leva su se stessi, sulla propria forza;\ned, eventualmente, su quella di altre forze con la nostra combinate.{/i}{/size}{p=9.0}{nw}"
    play sound "audio/voice/03_RESISTENZA.mp3"
    centered "{size=36}{i}È una resistenza molteplice e innominabile,\nquella di cui noi, oggi, abbiamo bisogno.{/i}{/size}{p=6.5}{nw}"
    play sound "audio/voice/04_RESISTENZA.mp3"
    centered "{size=36}{i}A questo serve ripercorrere le storie di chi è stato esemplare nella sua etica,\nnel suo saper tracciare fedelmente la propria forma:\nper inventarne di nuove.{/i}{/size}{p=11.0}{nw}"






    centered "{size=36}da {i}Eravamo come voi\nStorie di ragazzi che scelsero di resistere{/i}\n\ndi Marco Rovelli{/size}{p=5.5}{nw}"
    $ renpy.pause(2.0, hard=True)
    scene credits1 onlayer master
    $ renpy.pause(6.0, hard=True)
    scene credits2 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits3 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits4 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits5 onlayer master with dissolve
    $ renpy.pause(12.0, hard=True)
    scene credits6 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits7 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits8 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits9 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits10 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits11 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits12 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits13 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits14 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits15 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits16 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits17 onlayer master with dissolve
    $ renpy.pause(6.0, hard=True)
    scene credits18 onlayer master with dissolve
    $ renpy.pause(16.0, hard=True)
    scene black onlayer master with fade
    $ renpy.pause(6.0, hard=True)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
