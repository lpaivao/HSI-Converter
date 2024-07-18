import numpy as np
import matplotlib.pyplot as plt

def hsi_to_rgb(H, S, I):
    H = float(H)
    S = float(S)
    I = float(I)
        
    if H < 120:
        B = I * (1 - S)
        R = I * (1 + (S * np.cos(np.radians(H))) / (np.cos(np.radians(60 - H))))
        G = 3 * I - (R + B)
    elif H < 240:
        H = H - 120
        R = I * (1 - S)
        G = I * (1 + (S * np.cos(np.radians(H))) / (np.cos(np.radians(60 - H))))
        B = 3 * I - (R + G)
    else:
        H = H - 240
        G = I * (1 - S)
        B = I * (1 + (S * np.cos(np.radians(H))) / (np.cos(np.radians(60 - H))))
        R = 3 * I - (G + B)
        
    R = max(0, min(255, int(R * 255)))
    G = max(0, min(255, int(G * 255)))
    B = max(0, min(255, int(B * 255)))

    return (R, G, B)

def show_color(rgb):
    fig, ax = plt.subplots(figsize=(2, 2), subplot_kw=dict(xticks=[], yticks=[], frame_on=False))
    ax.set_title('HSI to RGB')
    ax.imshow([[rgb]])
    plt.show()

# Teste da função
h, s, i = 69, 1, 0.2  # Exemplo de valores HSI
rgb = hsi_to_rgb(h, s, i)
print(f"HSI({h}, {s}, {i}) -> RGB{rgb}")

# Mostrar a cor graficamente
show_color(tuple(c / 255 for c in rgb))
