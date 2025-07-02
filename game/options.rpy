








init -1 python hide:





    config.developer = False



    config.screen_width = 1920
    config.screen_height = 1080




    config.window_title = u"Venti Mesi - Twenty Months"



    config.name = "VentiMesi-ENG-ITA"
    config.version = "1.0"










    theme.threeD(
        
        

        
        widget = "#000000",

        
        widget_hover = "#961d1e",

        
        widget_text = "#dcdfd6",

        
        
        widget_selected = "#ffffff",

        
        disabled = "#919994",

        
        disabled_text = "#B6BFB9",

        
        label = "#ffffff",

        
        frame = "#6f7571",

        
        
        
        mm_root = "images/TITLE SCREEN.png",

        
        
        
        gm_root = "images/TITLE SCREEN.png",

        
        
        rounded_window = False,

        
        
        
        )































    style.window.yminimum = 100


























    style.default.font = "Vitesse-Book.ttf"



    style.default.size = 34











    config.has_sound = True



    config.has_music = True



    config.has_voice = False

















    config.main_menu_music = "audio/21_intro.mp3"












    config.help = "README.html"






    config.enter_transition = None


    config.exit_transition = None


    config.intra_transition = None


    config.main_game_transition = None


    config.game_main_transition = None


    config.end_splash_transition = None


    config.end_game_transition = None


    config.after_load_transition = None


    config.window_show_transition = None


    config.window_hide_transition = None


    config.adv_nvl_transition = dissolve


    config.nvl_adv_transition = dissolve


    config.enter_yesno_transition = None


    config.exit_yesno_transition = None


    config.enter_replay_transition = None


    config.exit_replay_transition = None


    config.say_attribute_transition = None





python early:
    config.save_directory = "VentiMesi-1439209163"

init -1 python hide:









    config.default_fullscreen = True
    config.default_language = "english"



    config.default_text_cps = 0



    config.default_afm_time = 10




    style.menu_choice.size = 34
    style.button_text.size = 34
    style.pref_label_text.size = 34
    style.yesno_label_text.size = 34
    style.file_picker_text.size = 34
    style.quick_button_text.size = 24
    style.label_text.size = 34
    config.window_icon = "images/icon.png"




init python:




    build.directory_name = "VentiMesi-ENG-ITA"




    build.executable_name = "VentiMesi"



    build.include_update = False





























    build.classify('**.rpy', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



    build.classify('game/**.png', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpt', 'archive')




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
