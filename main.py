import flet as ft
from function_rec import recording_mic
from function_rec import stop_rec
from function_rec import save_recording
from time import sleep

def main(page: ft.Page):
    page.window_width= 320
    page.window_height= 520
    page.theme_mode= ft.ThemeMode.SYSTEM
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER

    ######## SALVANDO AUDIO ########
    def recording_save_wav(e):
        for i in range(5, -1, -1):
            c = i
            h2.value = f'Salvando em {c}'
            page.update()
            sleep(1)
        save_recording(rec_name.value)
        h2.value = 'Audio Salvo!'
        page.update()
        sleep(2)
        rec_name.visible= False
        save.visible= False
        h2.visible= False
        play.visible= True
        page.update()

    ######## PLAY ########
    def play_rec_mic(e):
        play.visible= False
        stop.visible= True
        mic.src= './assets/mic_yes_rec.png'
        page.update()
        recording_mic()
        mic.src= './assets/mic_no_rec.png'
        page.update()
        
    ######## STOP ########
    def stop_rec_mic(e):
        stop.visible= False
        play.visible= False
        h1.value= 'Play for REC'
        page.update()
        stop_rec()
        save_and_rename(e)

    ######## RENOMEAR GRAVACAO ########
    def save_and_rename(e):
        rec_name.visible= True
        h2.visible= True
        save.visible= True
        page.update()
        
    ######## RENOMEAR GRAVACAO ########
    rec_name   = ft.TextField(
         value= '.wav',
         border_color= '#caff42',
         border_radius= 16,
         width= 150,
         height= 40,
         color= '#caff42',
         cursor_color= '#caff42',
         cursor_height= 20,
         autofocus= True,
         visible= False
     )

    ######## IMAGEM DO MICROFONE ########
    mic = ft.Image(
        src= './assets/mic_no_rec.png',
        width= 150
    ) 

    ######## PLAY FOR REC TEXT ########
    h1 = ft.Text(
        value= 'Play for REC',
        color= '#caff42',
        size= 25
    )

    ######## NOMEAR GRAVACAO ########
    h2 = ft.Text(
        'Nome para a nova gravacao.',
        color= '#caff42',
        size= 15,
        visible= False
    )

    ######## BOTAO SALVAR ########
    save = ft.ElevatedButton(
        text= 'SAVE',
        bgcolor= '#caff42',
        height= 40,
        width= 90,
        color=ft.colors.BLACK54,
        visible= False,
        on_click= recording_save_wav
    )

    ######## BOTAO DE PLAY ########
    play = ft.IconButton(
        icon=ft.icons.PLAY_ARROW,
        icon_size= 50,
        icon_color= '#caff42',
        on_click= play_rec_mic,
        visible= True
        )
    
    ######## BOTAO DE STOP ########
    stop = ft.IconButton(
        icon=ft.icons.STOP,
        icon_size= 50,
        icon_color= '#caff42',
        on_click= stop_rec_mic,
        visible= False
        )
    
    page.add(
        ft.Row(
            alignment= ft.MainAxisAlignment.START,
            controls=[
                ft.Text('Recording', size= 20, color='#caff42a2')
            ]
        ),
        mic,
        h1,
        ft.Row([
            h2,
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            rec_name,
            save
        ], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([
            play,
            stop
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)

