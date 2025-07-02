











screen say(who, what, side_image=None, two_window=False):


    if not two_window:


        window:
            id "window"

            has vbox
            style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:


        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox
                style "say_vbox"

                text what id "what"


    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


    use quick_menu









screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        has vbox
        style "menu"
        spacing 2

        for caption, action, chosen in items:

            if action:

                button:
                    action action
                    style "menu_choice_button"

                    text caption style "menu_choice"

            else:
                text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text clear


    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)









screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu







screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        style "nvl_vbox"


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox
                spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu







screen main_menu():
    tag menu




    window:
        xpadding 0
        ypadding 0
        add "mainmenu"



    frame:
        style_group "mm"
        xalign .00
        yalign 1.0

        has vbox

        textbutton _("NUOVA PARTITA") action Start()
        textbutton _("CARICA PARTITA") action ShowMenu("load")
        textbutton _("OPZIONI") action ShowMenu("preferences")

        textbutton _("CREDITS") action ShowMenu("credits")
        textbutton _("ESCI DAL GIOCO") action Quit(confirm=False)

init -2:


    style mm_button:
        size_group "mm"









screen navigation():


    window:
        style "gm_root"


    frame:
        style_group "gm_nav"
        xalign .00
        yalign 1.0

        has vbox

        textbutton _("INDIETRO") action Return()
        textbutton _("OPZIONI") action ShowMenu("preferences")
        textbutton _("SALVA PARTITA") action ShowMenu("save")
        textbutton _("CARICA PARTITA") action ShowMenu("load")
        textbutton _("TORNA ALL'INIZIO") action MainMenu()

        textbutton _("ESCI DAL GIOCO") action Quit()

init -2:


    style gm_nav_button:
        size_group "gm_nav"













screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox



        hbox:
            style_group "file_picker_nav"

            textbutton _("PRECEDENTI"):
                action FilePagePrevious()

            textbutton _("AUTO"):
                action FilePage("auto")

            textbutton _("RAPIDI"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("SUCCESSIVI"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5


        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"


            for i in range(1, columns * rows + 1):


                button:
                    action FileAction(i)
                    xfill True

                    has hbox


                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():
    tag menu



    use navigation
    use file_picker

screen load():
    tag menu



    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text








screen preferences():
    tag menu



    use navigation


    grid 3 1:
        style_group "prefs"
        xfill True


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("VISUALIZZA")
                textbutton _("FINESTRA") action Preference("display", "window")
                textbutton _("SCHERMO INTERO") action Preference("display", "fullscreen")
























































        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("VOLUME MUSICA")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("VOLUME SUONO")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("LINGUA")
                textbutton "ITALIANO" action Language(None)
                textbutton "ENGLISH" action Language("english")

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 480
        xalign 1.0

    style soundtest_button:
        xalign 1.0








screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("SÌ") action yes_action
            textbutton _("NO") action no_action


    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"







screen quick_menu():


    hbox:
        style_group "quick"

        xalign 1.0
        yalign 0.0


        textbutton _("Salva") action ShowMenu('save')
        textbutton _("Salva rapido") action QuickSave()
        textbutton _("Carica rapido") action QuickLoad()



        textbutton _("Opzioni") action ShowMenu('preferences')

init -2:
    style quick_button is default:

        background None
        xpadding 5

    style quick_button_text is default:

        size 8
        idle_color "#cccccc"
        hover_color "#ffffff"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
