from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QLineEdit,QTextEdit,QComboBox,QPushButton,QFormLayout,QSpinBox,QDoubleSpinBox,QFrame,QHBoxLayout,QMainWindow,QStackedWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
from numerix.core import complex_numbers,algebra,calculus,matrices,graphing,regression,statistics

class Page(QWidget):
    def __init__(self,title,subtitle):
        super().__init__(); self.v=QVBoxLayout(self); self.v.setContentsMargins(28,24,28,24); self.v.setSpacing(12)
        h=QLabel(title); h.setObjectName("pageTitle"); self.v.addWidget(h)
        s=QLabel(subtitle); s.setObjectName("subtitle"); s.setWordWrap(True); self.v.addWidget(s)
        self.form=QFormLayout(); self.v.addLayout(self.form)
        self.out=QTextEdit(); self.out.setReadOnly(True); self.out.setPlaceholderText("Results appear here.")
    def line(self,placeholder,default=""):
        w=QLineEdit(default); w.setPlaceholderText(placeholder); return w
    def combo(self,items):
        w=QComboBox(); w.addItems(items); return w
    def button(self,label,fn):
        b=QPushButton(label); b.clicked.connect(fn); self.v.addWidget(b)
    def output(self):
        self.v.addWidget(QLabel("RESULT")); self.v.addWidget(self.out)
    def run(self,fn):
        try: self.out.setPlainText(str(fn()))
        except Exception as e: self.out.setPlainText("Calculation error:\n"+str(e))

class Dashboard(Page):
    def __init__(self):
        super().__init__("Mathematical Computing Studio","A unified workspace for symbolic mathematics, numerical analysis and visual exploration.")
        for n,t,d in [("01","Complex Numbers","Arithmetic and complex properties"),("02","Algebra Solver","Simplify, expand, factor and solve"),("03","Calculus Studio","Derivatives, integrals and limits"),("04","Matrix Operations","Matrix arithmetic and properties"),("05","Graphing Studio","Plot functions of x"),("06","Regression Lab","Linear model and fit metrics"),("07","Statistics","Descriptive data analysis")]:
            card=QFrame(); card.setObjectName("featureCard"); row=QHBoxLayout(card)
            num=QLabel(n); num.setObjectName("number"); col=QVBoxLayout(); title=QLabel(t); title.setObjectName("cardTitle"); desc=QLabel(d); desc.setObjectName("subtitle"); col.addWidget(title); col.addWidget(desc); row.addWidget(num); row.addLayout(col,1); self.v.addWidget(card)
        self.v.addStretch()

class Complex(Page):
    def __init__(self):
        super().__init__("Complex Number Lab","Use i for the imaginary unit, for example 3 + 2*i.")
        self.a=self.line("First value"); self.b=self.line("Second value"); self.op=self.combo(["Add","Subtract","Multiply","Divide"])
        for l,w in [("Number A",self.a),("Number B",self.b),("Operation",self.op)]: self.form.addRow(l,w)
        self.button("Calculate",lambda:self.run(lambda:complex_numbers.calculate(self.a.text(),self.b.text(),self.op.currentText())))
        self.output()

class Algebra(Page):
    def __init__(self):
        super().__init__("Algebra & Equation Solver","Simplify, expand, factor or solve equations such as x**2 - 4 = 0.")
        self.e=self.line("Expression or equation"); self.var=self.line("Variable","x"); self.op=self.combo(["Simplify","Expand","Factor","Solve"])
        for l,w in [("Expression",self.e),("Variable",self.var),("Operation",self.op)]: self.form.addRow(l,w)
        self.button("Run operation",self.calc); self.output()
    def calc(self):
        op=self.op.currentText()
        fn={"Simplify":algebra.simplify,"Expand":algebra.expand,"Factor":algebra.factor,"Solve":lambda s:algebra.solve(s,self.var.text())}[op]
        self.run(lambda:fn(self.e.text()))

class Calculus(Page):
    def __init__(self):
        super().__init__("Calculus Studio","Symbolic differentiation, integration and limits.")
        self.e=self.line("Expression, e.g. sin(x)*x**2"); self.var=self.line("Variable","x"); self.op=self.combo(["Differentiate","Integrate","Limit"]); self.order=QSpinBox(); self.order.setRange(1,10); self.point=self.line("Limit point","0")
        for l,w in [("Expression",self.e),("Variable",self.var),("Operation",self.op),("Derivative order",self.order),("Limit point",self.point)]: self.form.addRow(l,w)
        self.button("Calculate",self.calc); self.output()
    def calc(self):
        op=self.op.currentText()
        fn={"Differentiate":lambda:calculus.differentiate(self.e.text(),self.var.text(),self.order.value()),"Integrate":lambda:calculus.integrate(self.e.text(),self.var.text()),"Limit":lambda:calculus.limit(self.e.text(),self.var.text(),self.point.text())}[op]
        self.run(fn)

class Matrix(Page):
    def __init__(self):
        super().__init__("Matrix Operations","Use semicolons between rows and commas between entries. Example: 1,2;3,4.")
        self.a=self.line("Matrix A"); self.b=self.line("Matrix B"); self.op=self.combo(["Add","Multiply","Determinant","Inverse","Transpose"])
        for l,w in [("Matrix A",self.a),("Matrix B",self.b),("Operation",self.op)]: self.form.addRow(l,w)
        self.button("Calculate",lambda:self.run(lambda:matrices.calculate(self.a.text(),self.b.text(),self.op.currentText()))); self.output()

class Graph(Page):
    def __init__(self):
        super().__init__("Graphing Studio","Plot a real-valued expression in x.")
        self.e=self.line("Function, e.g. sin(x)"); self.start=QDoubleSpinBox(); self.start.setRange(-1e6,1e6); self.start.setValue(-10); self.end=QDoubleSpinBox(); self.end.setRange(-1e6,1e6); self.end.setValue(10)
        for l,w in [("f(x)",self.e),("Start x",self.start),("End x",self.end)]: self.form.addRow(l,w)
        self.button("Plot function",self.plot); self.fig=Figure(figsize=(7,3),tight_layout=True); self.canvas=Canvas(self.fig); self.canvas.setMinimumHeight(270); self.v.addWidget(self.canvas,1); self.output()
    def plot(self):
        def work():
            xs,ys=graphing.sample(self.e.text(),self.start.value(),self.end.value())
            self.fig.clear(); ax=self.fig.add_subplot(111); ax.plot(xs,ys,lw=2); ax.axhline(0,lw=.7); ax.axvline(0,lw=.7); ax.grid(True,alpha=.25); ax.set_xlabel("x"); ax.set_ylabel("f(x)"); self.canvas.draw(); return "Graph plotted successfully."
        self.run(work)

class Regression(Page):
    def __init__(self):
        super().__init__("Regression Lab","Fit simple linear regression to paired numeric observations.")
        self.x=self.line("x values, e.g. 1,2,3,4"); self.y=self.line("y values, e.g. 2,4,5,8")
        self.form.addRow("X observations",self.x); self.form.addRow("Y observations",self.y); self.button("Fit linear model",self.calc)
        self.fig=Figure(figsize=(7,3),tight_layout=True); self.canvas=Canvas(self.fig); self.canvas.setMinimumHeight(250); self.v.addWidget(self.canvas,1); self.output()
    def calc(self):
        def work():
            r=regression.fit([float(v) for v in self.x.text().split(",")],[float(v) for v in self.y.text().split(",")])
            self.fig.clear(); ax=self.fig.add_subplot(111); ax.scatter(r["x"],r["y"],label="Observations"); idx=r["x"].argsort(); ax.plot(r["x"][idx],r["predictions"][idx],label="Linear fit"); ax.legend(); ax.grid(True,alpha=.25); self.canvas.draw()
            return f'y = {r["slope"]:.5g}x + {r["intercept"]:.5g}\nR² = {r["r2"]:.5f}\nRMSE = {r["rmse"]:.5f}'
        self.run(work)

class Stats(Page):
    def __init__(self):
        super().__init__("Statistics Workspace","Descriptive statistics for comma-separated numeric values.")
        self.values=self.line("Values, e.g. 4,7,7,9,12"); self.form.addRow("Dataset",self.values)
        self.button("Calculate statistics",lambda:self.run(lambda:"\n".join(f"{k}: {v}" for k,v in statistics.describe([float(v) for v in self.values.text().split(",")]).items()))); self.output()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("NUMERIX | Mathematical Computing Studio"); self.resize(1320,850); self.setMinimumSize(1000,680)
        shell=QWidget(); self.setCentralWidget(shell); outer=QHBoxLayout(shell); outer.setContentsMargins(0,0,0,0); outer.setSpacing(0)
        side=QFrame(); side.setObjectName("sidebar"); side.setFixedWidth(240); sl=QVBoxLayout(side); sl.setContentsMargins(18,24,18,18)
        brand=QLabel("NUMERIX"); brand.setObjectName("brand"); tag=QLabel("MATHEMATICAL COMPUTING"); tag.setObjectName("tagline"); sl.addWidget(brand); sl.addWidget(tag); sl.addSpacing(20)
        self.stack=QStackedWidget(); self.buttons=[]
        pages=[("Overview",Dashboard()),("Complex Numbers",Complex()),("Algebra Solver",Algebra()),("Calculus Studio",Calculus()),("Matrix Operations",Matrix()),("Graphing Studio",Graph()),("Regression Lab",Regression()),("Statistics",Stats())]
        for i,(name,page) in enumerate(pages):
            b=QPushButton(name); b.setObjectName("nav"); b.setCheckable(True); b.clicked.connect(lambda checked=False,n=i:self.go(n)); sl.addWidget(b); self.buttons.append(b); self.stack.addWidget(page)
        sl.addStretch(); content=QVBoxLayout(); top=QFrame(); top.setObjectName("topbar"); tl=QHBoxLayout(top); tl.addWidget(QLabel("WORKSPACE")); tl.addStretch(); status=QLabel("LOCAL SESSION"); status.setObjectName("status"); tl.addWidget(status); content.addWidget(top); content.addWidget(self.stack,1); outer.addWidget(side); outer.addLayout(content,1)
        self.setStyleSheet("QMainWindow,QWidget{background:#10141D;color:#E8EDF5;font-family:Segoe UI;font-size:13px} #sidebar{background:#0B0F17;border-right:1px solid #283244} #brand{font-size:27px;font-weight:800;letter-spacing:2px;color:#F5F7FB} #tagline{color:#8794A8;font-size:9px;letter-spacing:1.2px} #nav{text-align:left;padding:12px;border:0;border-radius:8px;background:transparent;color:#AAB5C6} #nav:hover{background:#1A2230;color:white} #nav:checked{background:#25334A;color:white;border-left:3px solid #83A0FF} #topbar{background:#121925;border-bottom:1px solid #283244;padding:8px} #status{color:#9BE2C1;background:#18352D;padding:6px 10px;border-radius:9px} #pageTitle{font-size:26px;font-weight:700;color:#F5F7FB} #subtitle{color:#96A2B5} #featureCard{background:#171F2C;border:1px solid #2B394D;border-radius:12px;padding:12px} #number{color:#8EA9FF;font-size:20px;font-weight:800;padding:8px} #cardTitle{font-size:15px;font-weight:700;color:#F4F6FA} QLineEdit,QTextEdit,QComboBox,QSpinBox,QDoubleSpinBox{background:#171F2C;border:1px solid #344155;border-radius:7px;padding:9px;color:#F2F5FA} QPushButton{background:#5477C8;color:white;border:0;border-radius:7px;padding:10px 18px;font-weight:700} QPushButton:hover{background:#6689DA}")
        self.go(0)
    def go(self,n):
        self.stack.setCurrentIndex(n)
        for i,b in enumerate(self.buttons): b.setChecked(i==n)
