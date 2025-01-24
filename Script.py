#  ##  ###  #######  ##  ###           #######  ##  ###  #######  ##  ###  #######   ## #
#  #######  ##       ##  ###             ###    #######  ##   ##  ##  ###  ##        ## #
#  #######  ##       ##  ###             ###    #######  ##   ##  ##  ###  ##        ## #
#  ### ###  #######  ##  ###             ###    ### ###  ##  ###  ##  ###  #######  ### #
#  ##  ###  ###      ##  ###             ###    ##  ###  ##  ###  ## ####  ###      ### #
#  ##  ###  ###      ##  ###             ###    ##  ###  ##  ###   #####   ###      ### #
#  ##  ###  #######  #######           #######  ##  ###  #######    ###    #######  ###### #

# Desenvolvido por Renan Dourado 
# Este codigo foi desenvolvido para Desligar o computador depois de 1h se não houver acesso 
import os
import time
from pynput import mouse, keyboard

# Variáveis para monitorar a atividade
last_activity_time = time.time()
inactive_time_limit = 3600   # Tempo de inatividade de 1h de relogio 

def on_move(x, y):
    global last_activity_time
    last_activity_time = time.time()

def on_click(x, y, button, pressed):
    global last_activity_time
    last_activity_time = time.time()

def on_scroll(x, y, dx, dy):
    global last_activity_time
    last_activity_time = time.time()

def on_press(key):
    global last_activity_time
    last_activity_time = time.time()

# Configura o listener para o teclado e o mouse
listener_mouse = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
listener_keyboard = keyboard.Listener(on_press=on_press)

listener_mouse.start()
listener_keyboard.start()

# Monitoramento contínuo
while True:
    time.sleep(1)  # Espera 1 segundo antes de checar novamente
    
    # Verifica se houve inatividade por mais tempo que o limite
    if time.time() - last_activity_time > inactive_time_limit:
        print("Inatividade detectada. Desligando o sistema...")
        os.system("shutdown /s /t 0")  # Comando para desligar o Windows
        break


#Git Hub do Desenvolvedor: https://github.com/renandourd0
