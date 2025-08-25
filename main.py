from manim import *

class PascalsWagerMatrix(Scene):
    def construct(self):
        table_one = Table(
            [["Heaven", "Hell"],
                ["Nothing", "Nothing"]],
            row_labels=[Text("God Exists"), Text("God Does Not Exist")],
            col_labels=[Text("Belief"), Text("Unbelief")]
        )
        self.play(Create(table_one, run_time=5))
        self.wait(10)
        table_two = Table(
            [[r"\infty", r"-\infty"],
             [r"-c", r"+c"]],
             row_labels=[Text("God Exists"), Text("God Does Not Exist")],
             col_labels=[Text("Belief"), Text("Unbelief")],
             element_to_mobject=MathTex
        )

        self.play(Transform(table_one, table_two))
        self.wait(1)

        self.play(table_one.animate.scale(0.5).to_edge(UP))
        self.wait(1)

        explanation_pt_one = Text("(Where c is a finite number.)", font_size=24).next_to(table_one, DOWN, buff=0.5)
        explanation_pt_two = Text("The infinite gain of belief outweighs whatever finite loss exists.", font_size=24).next_to(explanation_pt_one, DOWN, buff=0.3)
        explanation_pt_three = Text("Furthermore, the finite gain of unbelief is outweighed by its potential infinite loss.", font_size=24).next_to(explanation_pt_two, DOWN, buff=0.3)
        explanation_pt_four = Text("Thus, the only rational decision is to believe in God.", font_size=24, color=YELLOW).next_to(explanation_pt_three, DOWN, buff=0.3)

        self.play(Write(explanation_pt_one))
        self.wait(2)
        self.play(Write(explanation_pt_two))
        self.wait(2)
        self.play(Write(explanation_pt_three))
        self.wait(2)
        self.play(Write(explanation_pt_four))
        self.wait(2)