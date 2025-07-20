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
        caminho = r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, caminho, 0, winreg.KEY_SET_VALUE) as chave: winreg.SetValueEx(chave, "srvcomment", 0, winreg.REG_SZ, nova_descricao)

        print(f"\n Descrição alterada com sucesso para: {nova_descricao}")
        return True

    except PermissionError:
        print("\n Permissão negada: execute o script como administrador.")
    except Exception as e:
        print(f"\n Erro inesperado ao alterar a descrição: {e}")
    
    return False

def reiniciar_servico_lanman():

    if os.system("net stop lanmanserver") == 0 and os.system("net start lanmanserver") == 0:
        print("\n Serviço reiniciado")
    else:
        print("\n Reinicie manualmente depois")

def main():
    if not verificar_admin():
        print(" Este script precisa ser executado como administrador.")
        return
    
    while True:
        os.system("cls")
        print("\n" + "="*50)
        print("=== Mudar Descrição do Computador - v1.2.1 ===")
        print("="*50)

        print("\n Digite a nova descrição ou '0' para voltar ao menu anterior:")
        nova_desc = input("> ").strip()

        if nova_desc == '0':
            return  # Retorna ao menu anterior
        
        if not nova_desc:
            print(" A descrição não pode estar vazia.")
            input("\nPressione Enter para continuar...")
            continue
        
        if len(nova_desc) > 256:
            print("\n Descrição muito longa (Máximo 256 caracteres) ")
            input("\nPressione Enter para continuar...")
            continue
        
        if alterar_descricao_local(nova_desc):
            resposta = input("\n Deseja reiniciar o serviço 'lanmanserver' agora? (s/n): ").lower()
            if resposta == 's':
                reiniciar_servico_lanman()
            else:
                print(" Você pode reiniciar manualmente o serviço mais tarde.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()


""" Version: 1.2.1
Creator: João Malfatti """