import json
import matplotlib.pyplot as plt

def render(latex: str, path: str, dpi: int = 300) -> None:
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, f'${latex}$', fontsize=20)
    fig.savefig(path, dpi=dpi, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)

# TODO rekursiv auf example_data anwenden, mit vorherigem Einlesen der JSON

if __name__ == '__main__':
    render(r'\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}', 'formel.png')
