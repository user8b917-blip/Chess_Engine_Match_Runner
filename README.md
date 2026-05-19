# Chess Engine Match Runner

Script compacto para partidas automáticas entre engines de xadrez usando python-chess e Stockfish.

## Recursos

- Duas engines independentes
- Depth separado
- Hash e Threads separados
- Suporte a FEN personalizada
- Exportação automática de PGN
- Código simples e estável

## Configuração

```python
WHITE_ENGINE = "/caminho/da/engine"
BLACK_ENGINE = "/caminho/da/engine"

START_FEN = "FEN"

WHITE_DEPTH = 18
BLACK_DEPTH = 18

WHITE_HASH = 512
BLACK_HASH = 512

WHITE_THREADS = 1
BLACK_THREADS = 1
```
