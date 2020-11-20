import eel

w = 0
s = 0
stop = False

@eel.expose
def start():
    global w
    global stop
    stop = False
    while w > 0:
        eel.update_time(str(w) + ' menit')
        eel.sleep(60)
        w -= 1
    if w == 0:
        eel.update_time(str(w) + ' menit')
        eel.update_status('Selesai Mencuci!')

@eel.expose
def stop():
    global w
    global stop
    stop = True
    w = 0
    eel.update_time(str(w) + ' menit')

@eel.expose
def stop_animasi():
    eel.update_status('Berhenti Mencuci')

@eel.expose
def animasi():
    global w
    global stop
    stop = False
    while w > 0 and stop == False:
        for i in range(3):
            if i == 0:
                eel.update_status('Sedang Mencuci.')
                eel.sleep(1)
            elif i == 1:
                eel.update_status('Sedang Mencuci..')
                eel.sleep(1)
            elif i == 2:
                eel.update_status('Sedang Mencuci...')
                eel.sleep(1)

@eel.expose
def tambah_waktu():
    global w
    w += 1
    waktu = str(w) + ' menit'
    eel.update_time(waktu)

@eel.expose
def kurang_waktu():
    global w
    w -= 1
    waktu = str(w) + ' menit'
    eel.update_time(waktu)

@eel.expose
def tambah_temp():
    global s
    s += 1
    temp = str(s) + '°C'
    eel.update_temp(temp)

@eel.expose
def kurang_temp():
    global s
    s -= 1
    temp = str(s) + '°C'
    eel.update_temp(temp)

@eel.expose
def custom():
    eel.update_status('Custom Mode')

@eel.expose
def synthetic():
    global w
    global s
    w = 30
    s = 32
    eel.update_status('Synthtetic Mode')
    eel.update_time(str(w) + ' menit')
    eel.update_temp(str(s) + '°C')

@eel.expose
def wool():
    global w
    global s
    w = 30
    s = 23
    eel.update_status('Wool Mode')
    eel.update_time(str(w) + ' menit')
    eel.update_temp(str(s) + '°C')

@eel.expose
def cotton():
    global w
    global s
    w = 30
    s = 34
    eel.update_status('Cotton Mode')
    eel.update_time(str(w) + ' menit')
    eel.update_temp(str(s) + '°C')

@eel.expose
def quick_wash():
    global w
    global s
    w = 15
    s = 40
    eel.update_status('Quick Wash')
    eel.update_time(str(w) + ' menit')
    eel.update_temp(str(s) + '°C')

@eel.expose
def daily_wash():
    global w
    global s
    w = 30
    s = 35
    eel.update_status('Daily Wash')
    eel.update_time(str(w) + ' menit')
    eel.update_temp(str(s) + '°C')

@eel.expose
def on():
    eel.update_status("Niner's Tech")
    eel.sleep(1)
    eel.update_status("Niner's Tech.")
    eel.sleep(1)
    eel.update_status("Niner's Tech..")
    eel.sleep(1)
    eel.update_status('Halo, User!')

@eel.expose
def off():
    global w
    global s
    w = 0
    s = 0
    eel.update_time(str(w) + ' menit')
    eel.update_temp(str(s) + '°C')
    eel.update_status("Mematikan Mesin")
    eel.sleep(1)
    eel.update_status('Selamat Tinggal!')
    eel.sleep(1)
    eel.window_close()
    exit()

eel.init('web')
eel.start('index.html', size=(700, 200))