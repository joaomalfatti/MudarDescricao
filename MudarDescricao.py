import winreg
import os
import ctypes

def verificar_admin():
    """Verifica se o script está sendo executado como administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def alterar_descricao_local(nova_descricao):
    try:
        chave_registro = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters",
            0,
            winreg.KEY_SET_VALUE
        )

        winreg.SetValueEx(chave_registro, "srvcomment", 0, winreg.REG_SZ, nova_descricao)
        winreg.CloseKey(chave_registro)

        print(f"\n Descrição alterada com sucesso para: {nova_descricao}")
        return True

    except PermissionError:
        print("\n Permissão negada: execute o script como administrador.")
    except Exception as e:
        print(f"\n Erro inesperado ao alterar a descrição: {e}")
    
    return False

def reiniciar_servico_lanman():
    print("\n Reiniciando serviço 'lanmanserver'...")
    resultado = os.system(" net stop lanmanserver && net start lanmanserver")
    if resultado == 0:
        print(" Serviço reiniciado com sucesso.")
    else:
        print(" Não foi possível reiniciar o serviço. Tente reiniciar manualmente.")

def main():
    if not verificar_admin():
        print(" Este script precisa ser executado como administrador.")
        return
    
    os.system("cls")
    print("\n" + "="*50)
    print("=== Mudar Descrição do Computador - v1.1.1 ===")
    print("="*50)

    descricao = input("\n Qual nome você deseja colocar como descrição do computador? ").strip()

    if not descricao:
        print(" A descrição não pode estar vazia.")
        return

    if alterar_descricao_local(descricao):
        resposta = input("\n Deseja reiniciar o serviço 'lanmanserver' agora? (s/n): ").lower()
        if resposta == 's':
            reiniciar_servico_lanman()
        else:
            print(" Você pode reiniciar manualmente o serviço mais tarde.")

if __name__ == "__main__":
    main()


""" Version: 1.1.1
Creator: João Malfatti """