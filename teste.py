from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# Função para obter o controle de volume do sistema
def get_system_volume_control():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == "explorer.exe":
            return cast(session.SimpleAudioVolume, POINTER(ISimpleAudioVolume))

# Função para aumentar o volume
def increase_volume():
    volume_control = get_system_volume_control()
    if volume_control:
        current_volume = volume_control.GetMasterVolume()
        volume_control.SetMasterVolume(current_volume + 0.1, None)

# Função para diminuir o volume
def decrease_volume():
    volume_control = get_system_volume_control()
    if volume_control:
        current_volume = volume_control.GetMasterVolume()
        volume_control.SetMasterVolume(current_volume - 0.1, None)

# Exemplo de utilização
increase_volume()  # Aumentar o volume
#decrease_volume()  # Diminuir o volume
