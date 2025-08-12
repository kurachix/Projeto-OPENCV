#---------------------#
import os
import time
import cv2
inverter = None
escolha = None 
#---------------------#

def limpar():
    os.system("cls")  

def inicio():
    limpar()
    print(50 * "-")
    print("BEM-VINDO A DEMONSTRAÇÃO DO OPEN CV".center(50))
    print(50 * "-")
    time.sleep(2)
    limpar()

def menu():
    print(50 * "-")
    print("MENU DE TESTES DO OPEN CV".center(50))
    print("ESCOLHA SUA OPÇÃO PARA PROSSEGUIR".center(50))
    print(50 * "-")
    print("1 -> Abrir Webcam")
    print("2 -> Tirar Foto")
    print("3 -> Abrir Imagens salvas no Sistema")
    print("4 -> Inverter Cores de uma Imagem")
    print("5 -> Sair do Software")
    print(50 * "-")
    escolha = int(input("QUAL OPÇÃO DESEJA SELECIONAR?\n-> "))
    return escolha

def inverter():
    limpar()
    print(30* "-")
    print("MENU DE INVERSÃO DE CORES".center(30))
    print(30* "-")
    print("1-> Inverter Cores Padrão")
    print("2-> Escala de Cinza e Branco")
    print("3-> ColorMap *Cores Falsas")

    inverter = int(input("Qual Opção deseja escolher?\n ->"))

    if inverter == 1:
        img = cv2.imread(r"C:\Users\Aluno02\Downloads\download1.jfif")
        img_invertida = cv2.bitwise_not(img)

        cv2.imshow("Imagem Invertida", img_invertida)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif inverter == 2:
        img = cv2.imread(r"C:\Users\Aluno02\Downloads\download1.jfif")
        cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Escala de Cinza", cinza)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif inverter == 3:
        img = cv2.imread(r"C:\Users\Aluno02\Downloads\download1.jfif", 0)  # lê em escala de cinza
        colorida = cv2.applyColorMap(img, cv2.COLORMAP_JET)

        cv2.imshow("Colormap", colorida)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def abrir_o_carlos():
    image1 = cv2.imread(r"C:\Users\Aluno02\Downloads\download1.jfif")
    # r de RAW STRINGS(STRINGS BRUTAS)

    if image1 is None: #Se no caminho que passei nao tiver nada, vai ocorrer esse print
        print("Erro ao carregar a imagem. Verifique o caminho e a extensão do arquivo.")
    else: #se no caminho que passei tiver algo executará esses comandos abaixo
        cv2.imshow("Abrindo imagem", image1) #esse comando exibe a imagem na tela
        cv2.waitKey(0) #Enquanto nenhuma tecla for pressionada, a imagem continuará aberta, 0 significa indefinidamente
        cv2.destroyAllWindows() #fecha as janelas.

def tirar_foto():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Não foi possível acessar a webcam.")
        return

    ret, frame = cap.read()  # Captura um único frame
    cap.release()  # Libera a câmera imediatamente

    if ret:
        cv2.imshow("Foto Capturada - Pressione qualquer tecla", frame)
        cv2.waitKey(0)  # Espera o usuário pressionar uma tecla
        cv2.destroyAllWindows()
    else:
        print("Erro ao capturar a imagem.")


def abrir_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Não foi possível acessar a webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar o frame.")
            break

        cv2.imshow("Webcam - Pressione 'q' para sair", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def opcoes(escolha):
    if escolha == 1:
        limpar()
        abrir_webcam()
        limpar()
    if escolha == 2:
        limpar()
        tirar_foto()
        limpar()
    if escolha == 3:
        limpar()
        abrir_o_carlos()
        limpar()
    if escolha == 4:
        limpar()
        inverter()
        limpar()
#---------------------#
def principal():
    escolha = 0
    while escolha != 5:
        escolha = menu()
        opcoes(escolha)

inicio()
principal()







