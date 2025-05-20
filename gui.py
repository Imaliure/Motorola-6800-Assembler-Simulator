# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from assembler.parser import validate_code
from assembler.address_resolver import resolve_addresses
from assembler.code_generator import generate_object_code
from assembler.simulator import Simulator

class AssemblerGUI:
    def __init__(self, root):
        self.root = root
        self.simulator = Simulator()
        self.root.title("Motorola 6800 Assembler")

        # Kod giriş kutusu
        self.input_text = scrolledtext.ScrolledText(root, width=60, height=20)
        self.input_text.grid(row=0, column=0, padx=10, pady=10)

        # Object kod çıkışı
        self.output_text = scrolledtext.ScrolledText(root, width=60, height=20, state='disabled')
        self.output_text.grid(row=0, column=1, padx=10, pady=10)

        # Butonlar
        self.load_btn = tk.Button(root, text="Kod Yükle", command=self.load_code)
        self.load_btn.grid(row=1, column=0, sticky="w", padx=10)

        self.assemble_btn = tk.Button(root, text="Derle", command=self.assemble_code)
        self.assemble_btn.grid(row=1, column=0, sticky="e", padx=10)

        # Register / Memory göstergesi
        self.sim_output = scrolledtext.ScrolledText(root, width=60, height=10, state='disabled')
        self.sim_output.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def load_code(self):
        file_path = filedialog.askopenfilename(filetypes=[("Assembly Files", "*.asm")])
        if file_path:
            with open(file_path, "r") as f:
                code = f.read()
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert(tk.END, code)

    def assemble_code(self):
        code = self.input_text.get("1.0", tk.END).strip().splitlines()

        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.sim_output.config(state='normal')
        self.sim_output.delete("1.0", tk.END)

        try:
            # Kod doğrulama
            validation = validate_code(code)

            # Label adres çözümlemesi ve nesne kodu üretimi
            _, label_map = resolve_addresses(code)
            object_code = generate_object_code(code, label_map)

            # Nesne kodlarını yazdır
            self.output_text.insert(tk.END, "=== Nesne Kodu (Object Code) ===\n")
            for (machine, source) in object_code:
                self.output_text.insert(tk.END, f"{machine:<10} ; {source}\n")

            # Simülasyonu başlat
            self.simulator.reset()
            self.simulator.execute(code)

            # Simülasyon sonuçlarını yazdır
            self.sim_output.insert(tk.END, "=== Register Durumu ===\n")
            self.sim_output.insert(tk.END, f"Register A: {self.simulator.registers['A']}\n")
            self.sim_output.insert(tk.END, f"Register B: {self.simulator.registers['B']}\n")

            self.sim_output.insert(tk.END, "\n=== Hafıza Durumu ===\n")
            for addr in sorted(self.simulator.memory.keys()):
                val = self.simulator.memory[addr]
                self.sim_output.insert(tk.END, f"{hex(addr)}: {hex(val)}\n")

        except Exception as e:
            # Hata varsa kullanıcıya bildir
            self.sim_output.insert(tk.END, f"HATA: {e}\n")

        self.output_text.config(state='disabled')
        self.sim_output.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = AssemblerGUI(root)
    root.mainloop()
