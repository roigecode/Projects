
from manim import *
from math import sqrt, exp, pi, erf
from manim.mobject.mobject import T
from manim.utils import scale
import csv
import numpy as np


class MainFunction(MovingCameraScene):
    def construct(self):
        title(self)
        self.wait()
        longcallandshortcall(self)
        self.wait()
        longcallspread(self)
        self.wait(3)


# +--------+ #
# | TITLE: | #
# +--------+ #

def title(self):
    title = Tex(r"What is a",r" Long (Bull/Debit) Call Vertical Spread?")
    title[1].set_color_by_gradient([ORANGE,PINK,PURPLE])
    
    t1 = Tex(r"A Call option is a financial contract that gives its",r" buyer (holder) ",r"the", r" \underline{right} to buy  ", r" the underlying security at a specified price price within a specific time period. Alternatively, it gives its", r" seller (writer) ",r"the ",r"\underline{obligation} to sell",r" the security at a specified price at expiration.", font_size=35)

    t1[1].set_color_by_gradient([GREEN_C,BLUE_C])
    t1[3].set_color_by_gradient([GREEN_C,BLUE_C])
    t1[5].set_color_by_gradient([ORANGE,RED_C])
    t1[7].set_color_by_gradient([ORANGE,RED_C])

    lc = Tex(r"Let's see an example for a ",r" bought (long) Call", r" and one \\ for a ", r" sold (short) Call")
    lc[1].set_color_by_gradient([GREEN_C,BLUE_C])
    lc[3].set_color_by_gradient([ORANGE,RED_C])

    sr = SurroundingRectangle(title[1]).set_color_by_gradient([ORANGE,PINK,PURPLE])
    # PLAYS:
    self.play(Write(title))
    self.wait()
    self.play(Write(sr))
    self.wait()
    self.play(Unwrite(title), Uncreate(sr))
    self.wait()
    self.play(Write(t1))
    self.wait(7)
    self.play(Unwrite(t1))
    self.wait()
    self.play(Write(lc))
    self.wait(2)
    self.play(Unwrite(lc))


# +------------------------+ #
# | LONG CALL & SHORT CALL | #
# +------------------------+ #

def longcallandshortcall(self):
    # +------------+ #
    # | LONG CALL: | #
    # +------------+ #
    
    fs = 17
    e = 2.71828182846

    ax = Axes(
        x_range=[405, 535, 5],
        y_range=[-1000, 6300, 10000],
        tips=False,
        x_axis_config={"include_numbers": True, "font_size": fs},
        y_axis_config={"include_numbers": False, "font_size": fs}
    )

    labels = ax.get_y_axis_label(Tex(r"P\&L [\$]", font_size=20))
    y2 = MathTex(r"-847", font_size=fs).move_to(ax.c2p(405, -847))
    y2.shift(LEFT*0.5)
    ly1 = Line(ax.c2p(425, 0), ax.c2p(427, 0), stroke_width=0.9).move_to(ax.c2p(405, -847))

    x_vals = [405, 465, 535]
    y_vals = [-847, -847, 6109]
    graph = ax.plot_line_graph(x_values=x_vals, y_values=y_vals, add_vertex_dots=False, stroke_width=0.9).set_color(WHITE)

    line_1 = DashedLine(ax.c2p(465,-847), ax.c2p(465,0), color=WHITE, stroke_width=0.9)
    arrow1 = Arrow(ax.c2p(465, 5000), ax.c2p(465, 0), buff=0.3, stroke_width=2, max_tip_length_to_length_ratio=0.06)
    bc = Tex(r"+1 Call@465", font_size=25).move_to(ax.c2p(465, 5000))
    price = Tex(r"-847", font_size=20).move_to(ax.c2p(405,-847))
    price.shift(LEFT*0.5)

    # POLYGRAMS: Shade P&L areas:
    areatot1 = Polygram([ax.c2p(405, 0), ax.c2p(405, -847), ax.c2p(465, -847), ax.c2p(473.5, 0)], stroke_opacity=0, fill_color=PURE_RED, fill_opacity=0.5)
    areatot2 = Polygram([ax.c2p(473.5, 0), ax.c2p(535, 0), ax.c2p(535, 6109)], stroke_opacity=0, fill_color=PURE_GREEN, fill_opacity=0.5)
    
    areatot1.set_color_by_gradient([PURE_RED, PINK])
    areatot2.set_color_by_gradient([BLUE, PURE_GREEN])

    # PDF:
    pdf = ax.plot(lambda x: PDF_lc(x)).set_color(PINK)
    pdf_text = Tex(r"37d",font_size=15).set_color(PINK).move_to(ax.c2p(473.5,6700))
    
    # Plotting the Standar Deviations (1st & 2nd):
    # 1SD: 440 // 500
    sd11 = DashedLine(ax.c2p(440,-1000), ax.c2p(440,6600), dash_length=0.075).set_color(PINK)
    sd12 = DashedLine(ax.c2p(500,-1000), ax.c2p(500,6600), dash_length=0.075).set_color(PINK)

    sd11_text = MathTex(r"-1\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(440,-1200))
    sd12_text = MathTex(r"1\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(500,-1200))

    # 2SD: 410 // 530
    sd21 = DashedLine(ax.c2p(410,-1000), ax.c2p(410,6600), stroke_width=0.9, dashed_ratio=0.4).set_color(PINK)
    sd22 = DashedLine(ax.c2p(530,-1000), ax.c2p(530,6600), stroke_width=0.9, dashed_ratio=0.4).set_color(PINK)

    sd21_text = MathTex(r"-2\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(410,-1200))
    sd22_text = MathTex(r"2\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(530,-1200)) 
    #profdot = Dot(ax.c2p(405, sigm(405)), radius=0.055).set_color(WHITE)

    # LONG CALL PLAYS:
    self.play(Write(ax),Write(labels),Write(line_1), Create(areatot1), Create(areatot2), Write(ly1),Write(graph))
    self.wait(0.5)
    self.play(Write(bc), Write(arrow1),Write(price),Rotate(ly1, PI))
    self.wait(2)
    self.play(Write(pdf),Write(pdf_text),Write(sd11),Write(sd12),Write(sd11_text),Write(sd12_text),Write(sd21),Write(sd22),Write(sd21_text),Write(sd22_text))
    self.wait(3)
    self.play(FadeOut(ax),FadeOut(labels),FadeOut(line_1),FadeOut(areatot1),FadeOut(areatot2),FadeOut(ly1),FadeOut(graph),FadeOut(bc),FadeOut(arrow1), FadeOut(pdf),FadeOut(pdf_text),FadeOut(sd11),FadeOut(sd12),FadeOut(sd11_text),FadeOut(sd12_text),FadeOut(sd21),FadeOut(sd22),FadeOut(sd21_text),FadeOut(sd22_text))

    # +-------------+ #
    # | SHORT CALL: | #
    # +-------------+ #
    ax2 = Axes(
        x_range=[405, 535, 5],
        y_range=[-4140, 1000, 10000],
        tips=False,
        x_axis_config={"include_numbers": True, "font_size": fs},
        y_axis_config={"include_numbers": False, "font_size": fs}
    )

    labels = ax2.get_y_axis_label(Tex(r"P\&L [\$]", font_size=20))
    y2 = MathTex(r"360", font_size=fs).move_to(ax2.c2p(405, 360))
    y2.shift(LEFT*0.5)
    ly1 = Line(ax2.c2p(425, 0), ax2.c2p(427, 0), stroke_width=0.9).move_to(ax2.c2p(405, 360))

    x_vals = [405, 480, 535]
    y_vals = [360, 360, -4140]
    graph = ax2.plot_line_graph(x_values=x_vals, y_values=y_vals, add_vertex_dots=False, stroke_width=0.9).set_color(WHITE)

    line_1 = DashedLine(ax2.c2p(480,360), ax2.c2p(480,0), color=WHITE, stroke_width=0.9)
    arrow1 = Arrow(ax2.c2p(480, -4000), ax2.c2p(480, -250), buff=0.3, stroke_width=2, max_tip_length_to_length_ratio=0.06)
    bc = Tex(r"-1 Call@480", font_size=25).move_to(ax2.c2p(480, -4000))

    price = Tex(r"360", font_size=20).move_to(ax2.c2p(405,360))
    price.shift(LEFT*0.5)

    areatot1 = Polygram([ax2.c2p(405, 0), ax2.c2p(405, 360), ax2.c2p(480, 360), ax2.c2p(484.6, 0)], stroke_opacity=0, fill_color=PURE_RED, fill_opacity=0.5)
    areatot2 = Polygram([ax2.c2p(484.5, 0), ax2.c2p(535, 0), ax2.c2p(535, -4140)], stroke_opacity=0, fill_color=PURE_GREEN, fill_opacity=0.5)
    
    areatot1.set_color_by_gradient([PURE_GREEN,BLUE])
    areatot2.set_color_by_gradient([PINK, PURE_RED])

    # PDF:
    pdf = ax2.plot(lambda x: PDF_sc(x)).set_color(PINK)
    pdf_text = Tex(r"37d",font_size=15).set_color(PINK).move_to(ax2.c2p(483.6,1200))
    
    # Plotting the Standar Deviations (1st & 2nd):
    # 1SD: 440 // 500
    sd11 = DashedLine(ax2.c2p(440,-4140), ax2.c2p(440,1000), dash_length=0.075).set_color(PINK)
    sd12 = DashedLine(ax2.c2p(500,-4140), ax2.c2p(500,1000), dash_length=0.075).set_color(PINK)

    sd11_text = MathTex(r"-1\sigma", font_size=fs).set_color(PINK).move_to(ax2.c2p(440,-4500))
    sd12_text = MathTex(r"1\sigma", font_size=fs).set_color(PINK).move_to(ax2.c2p(500,-4500))

    # 2SD: 410 // 530
    sd21 = DashedLine(ax2.c2p(410,-4140), ax2.c2p(410,1000), stroke_width=0.9, dashed_ratio=0.4).set_color(PINK)
    sd22 = DashedLine(ax2.c2p(530,-4140), ax2.c2p(530,1000), stroke_width=0.9, dashed_ratio=0.4).set_color(PINK)

    sd21_text = MathTex(r"-2\sigma", font_size=fs).set_color(PINK).move_to(ax2.c2p(410,-4500))
    sd22_text = MathTex(r"2\sigma", font_size=fs).set_color(PINK).move_to(ax2.c2p(530,-4500)) 
    #profdot = Dot(ax.c2p(405, sigm(405)), radius=0.055).set_color(WHITE)
    
    # SHORT CALL PLAYS:
    self.play(Write(ax2),Write(labels),Write(line_1), Create(areatot1), Create(areatot2), Write(ly1),Write(graph))
    self.wait(0.5)
    self.play(Write(bc), Write(arrow1), Write(price),Rotate(ly1, PI))
    self.wait(2)
    self.play(Write(pdf),Write(pdf_text),Write(sd11),Write(sd12),Write(sd11_text),Write(sd12_text),Write(sd21),Write(sd22),Write(sd21_text),Write(sd22_text))
    self.wait(3)
    self.play(FadeOut(ax2),FadeOut(labels),FadeOut(line_1),FadeOut(areatot1),FadeOut(areatot2),FadeOut(ly1),FadeOut(graph),FadeOut(bc),FadeOut(arrow1), FadeOut(pdf),FadeOut(pdf_text),FadeOut(sd11),FadeOut(sd12),FadeOut(sd11_text),FadeOut(sd12_text),FadeOut(sd21),FadeOut(sd22),FadeOut(sd21_text),FadeOut(sd22_text))
    self.wait(2)

    comb = Tex(r"Now let's combine both strategies to get the ",r"Long Call Vertical Spread",r"!", font_size=30)
    comb[1].set_color_by_gradient([ORANGE,PINK,PURPLE])
    self.play(Write(comb))
    self.wait(2)
    self.play(Unwrite(comb))
    self.wait()


# +------------------+ #
# | LONG CALL SPREAD | #
# +------------------+ #

def longcallspread(self):
    # FONT-SIZE FOR AXES:
    fs = 17
    e = 2.71828182846

    ax = Axes(
        x_range=[405, 535, 5],
        y_range=[-1000, 900, 10000],
        tips=False,
        x_axis_config={"include_numbers": True, "font_size": fs},
        y_axis_config={"include_numbers": False, "font_size": fs}
    )

    labels = ax.get_y_axis_label(Tex(r"P\&L [\$]", font_size=20))

    y1 = MathTex(r"653", font_size=fs).move_to(ax.c2p(405, 653))
    y2 = MathTex(r"-847", font_size=fs).move_to(ax.c2p(405, -847))
    y1.shift(LEFT*0.5)
    y2.shift(LEFT*0.5)

    ly1 = Line(ax.c2p(425, 0), ax.c2p(427, 0), stroke_width=0.9).move_to(ax.c2p(405, 653))
    ly2 = Line(ax.c2p(425, 0), ax.c2p(427, 0), stroke_width=0.9).move_to(ax.c2p(405, -847))

    BE = 473.5

    # Plot the Long Call Spread:
    x_vals = [405, 465, 480, 535]
    y_vals = [-847, -847, 653, 653]
    graph = ax.plot_line_graph(x_values=x_vals, y_values=y_vals, add_vertex_dots=False, stroke_width=0.9).set_color(WHITE)

    # POLYGRAMS: Shade the areas in their respective color:
    areatot1 = Polygram([ax.c2p(405, 0), ax.c2p(405, -847), ax.c2p(465, -847), ax.c2p(473.5, 0)], stroke_opacity=0, fill_color=PURE_RED, fill_opacity=0.5)
    areatot2 = Polygram([ax.c2p(473.5, 0), ax.c2p(535, 0), ax.c2p(535, 653), ax.c2p(480, 653)], stroke_opacity=0, fill_color=PURE_GREEN, fill_opacity=0.5)

    areatot1.set_color_by_gradient([PURE_RED, PINK])
    areatot2.set_color_by_gradient([BLUE, PURE_GREEN])

    # Strike prices lines:
    line_1 = DashedLine(ax.coords_to_point(465, 0), ax.c2p(465, -847), stroke_width=0.9)
    line_2 = DashedLine(ax.c2p(480, 0), ax.c2p(480, 653), stroke_width=0.9)

    # Options Text:
    longcall = Tex(r"+1 Call@465", font_size=20).move_to(ax.c2p(465, 653))
    shortput = Tex(r"-1 Call@480", font_size=20).move_to(ax.c2p(480, -847))
    ar1 = Arrow(ax.c2p(465, 653), ax.c2p(465, 0), buff=0.2, stroke_width=2, max_tip_length_to_length_ratio=0.1)
    ar2 = Arrow(ax.c2p(480, -847), ax.c2p(480, -100), buff=0.2, stroke_width=2, max_tip_length_to_length_ratio=0.1)

    # Sigmoid and PDF function:
    def sigm(x):
        return (1500/(1+e**(-0.1*x+47.35)))-847

    sigmoid = ax.plot(lambda x : (1500/(1+e**(-0.1*x+47.35)))-847).set_color(ORANGE)
    pdf = ax.plot(lambda x: PDF_cs(x)).set_color(PINK)
    pdf_text = Tex(r"37d",font_size=15).set_color(PINK).move_to(ax.c2p(473.5,1000))
    
    # Plotting the Standar Deviations (1st & 2nd):
    # 1SD: 440 // 500
    sd11 = DashedLine(ax.c2p(440,-1000), ax.c2p(440,900), dash_length=0.05).set_color(PINK)
    sd12 = DashedLine(ax.c2p(500,-1000), ax.c2p(500,900), dash_length=0.05).set_color(PINK)

    sd11_text = MathTex(r"-1\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(440,-1100))
    sd12_text = MathTex(r"1\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(500,-1100))

    # 2SD: 410 // 530
    sd21 = DashedLine(ax.c2p(410,-1000), ax.c2p(410,900), stroke_width=0.9, dashed_ratio=0.6).set_color(PINK)
    sd22 = DashedLine(ax.c2p(530,-1000), ax.c2p(530,900), stroke_width=0.9, dashed_ratio=0.6).set_color(PINK)

    sd21_text = MathTex(r"-2\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(410,-1100))
    sd22_text = MathTex(r"2\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(530,-1100)) 
    profdot = Dot(ax.c2p(405, sigm(405)), radius=0.055).set_color(WHITE)

    # PLAYS:
    self.play(Write(ax), Create(areatot1), Create(areatot2), Create(graph), Write(labels), Write(y1), Write(y2))
    self.play(Write(ly1), Write(ly2))
    self.play(Rotate(ly1, PI), Rotate(ly2, PI), Create(line_1), Create(line_2))
    self.play(Write(longcall), Write(ar1), Write(ar2), Write(shortput))
    self.wait()
    self.play(Write(sigmoid), Write(pdf), Write(pdf_text))
    self.play(FadeOut(line_1), FadeOut(line_2), Write(sd11),Write(sd12),Write(sd21),Write(sd22),Write(sd11_text),Write(sd12_text),Write(sd21_text),Write(sd22_text))
    self.wait(0.5)
    self.play(Write(profdot))
    self.play(MoveAlongPath(profdot, sigmoid, rate_func=rate_functions.smooth), run_time=3)


def PDF_normal(x, mu, sigma,k):
    return exp(-(((k*x)-mu)**2)/(2*sigma**2))/(sigma*sqrt(2*pi))

def PDF_cs(x):
    return 900*sqrt(2*pi)*exp(-(((1*x)-473.5)**2)/(2*25**2))/(sqrt(2*pi))

def PDF_lc(x):
    return 6500*sqrt(2*pi)*exp(-(((1*x)-473.5)**2)/(2*25**2))/(sqrt(2*pi))

def PDF_sc(x):
    return 1200*sqrt(2*pi)*exp(-(((1*x)-483.6)**2)/(2*25**2))/(sqrt(2*pi))
