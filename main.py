from manim import *

class PascalsWager(Scene):
    def construct(self):
        table = Table(
            [["Heaven", "Hell"],
                ["Nothing", "Nothing"]],
            row_labels=[Text("God Exists"), Text("God Does Not Exist")],
            col_labels=[Text("Belief"), Text("Unbelief")]
        )
