
import os, chess, chess.engine, chess.pgn
from datetime import datetime

# =====================

WHITE_ENGINE = "/content/stockfish/stockfish-ubuntu-x86-64-avx2"
BLACK_ENGINE = "/content/stockfish/stockfish-ubuntu-x86-64-avx2"

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

WHITE_DEPTH = 18
BLACK_DEPTH = 18

WHITE_HASH = 512
BLACK_HASH = 512

WHITE_THREADS = 1
BLACK_THREADS = 1

# =====================

os.system("pkill stockfish")

ew = chess.engine.SimpleEngine.popen_uci(WHITE_ENGINE)
eb = chess.engine.SimpleEngine.popen_uci(BLACK_ENGINE)

try:

    ew.configure({
        "Hash": WHITE_HASH,
        "Threads": WHITE_THREADS
    })

    eb.configure({
        "Hash": BLACK_HASH,
        "Threads": BLACK_THREADS
    })

    board = chess.Board(START_FEN)

    game = chess.pgn.Game()

    # PGN mínimo
    game.headers["FEN"] = START_FEN
    game.headers["SetUp"] = "1"

    node = game
    ply = 1

    while not board.is_game_over():

        engine = ew if board.turn else eb
        depth = WHITE_DEPTH if board.turn else BLACK_DEPTH

        info = engine.analyse(
            board,
            chess.engine.Limit(depth=depth)
        )

        move = info["pv"][0]

        print(
            f"[{ply}] "
            f"d{depth} "
            f"| Eval: {info['score'].white()}"
        )

        board.push(move)

        node = node.add_variation(move)

        ply += 1

    game.headers["Result"] = board.result()

    name = (
        "match_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".pgn"
    )

    with open(name, "w", encoding="utf-8") as f:
        game.accept(chess.pgn.FileExporter(f))

    print("\nResultado:", board.result())
    print("PGN:", name)

finally:

    ew.quit()
    eb.quit()