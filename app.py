from flask import Flask, render_template, request, jsonify
from assembler.simulator import Simulator

app = Flask(__name__)
sim = Simulator()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form.get("code", "")
        lines = code.strip().splitlines()
        try:
            sim.reset()
            sim.execute(lines)
            registers = sim.registers
            memory = sim.memory
            return jsonify({
                "status": "success",
                "registers": registers,
                "memory": {hex(addr): hex(val) for addr, val in memory.items()}
            })
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)