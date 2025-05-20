class Simulator:
    def __init__(self):
        self.memory = {}
        self.registers = {'A': 0, 'B': 0}
        self.labels = {}
        self.pc = 0  # Program counter

    def reset(self):
        self.memory.clear()
        self.registers = {'A': 0, 'B': 0}
        self.pc = 0

    def parse_immediate(self, operand):
        """Immediate (#) operatöründen sonra gelen değeri çözümler."""
        raw_val = operand[1:]  # Remove '#'
        if raw_val.startswith("$"):
            return int(raw_val.replace("$", "0x"), 16)
        else:
            return int(raw_val, 0)

    def parse_address(self, operand):
        """Bellek adresini çözümler."""
        return int(operand.replace("$", "0x"), 16)

    def execute(self, lines):
        self.labels = {
            line.split(":")[0].strip(): idx
            for idx, line in enumerate(lines)
            if ":" in line
        }

        self.pc = 0
        while self.pc < len(lines):
            try:
                line = lines[self.pc].strip()

                # Boş satır, yorum, label veya assembler direktifi ise atla
                if not line or line.startswith(";") or line.endswith(":") or \
                line.upper().startswith("ORG") or line.upper().startswith("END"):
                    self.pc += 1
                    continue

                tokens = line.split()
                instr = tokens[0].upper()
                operand = tokens[1] if len(tokens) > 1 else None

                if instr == "LDAA" and operand.startswith("#$"):
                    self.registers['A'] = int(operand[2:], 16)

                elif instr == "LDAB" and operand.startswith("#$"):
                    self.registers['B'] = int(operand[2:], 16)

                elif instr == "STAA" and operand.startswith("$"):
                    addr = int(operand[1:], 16)
                    self.memory[addr] = self.registers['A']

                elif instr == "STAB" and operand.startswith("$"):
                    addr = int(operand[1:], 16)
                    self.memory[addr] = self.registers['B']

                elif instr == "ADDA" and operand.startswith("#$"):
                    self.registers['A'] = (self.registers['A'] + int(operand[2:], 16)) & 0xFF

                elif instr == "SUBA" and operand.startswith("#$"):
                    self.registers['A'] = (self.registers['A'] - int(operand[2:], 16)) & 0xFF

                elif instr == "JMP":
                    if operand in self.labels:
                        self.pc = self.labels[operand]
                        continue
                    else:
                        raise ValueError(f"Etiket bulunamadı: {operand}")

                elif instr == "BRA":
                    if operand in self.labels:
                        self.pc = self.labels[operand]
                        continue
                    else:
                        raise ValueError(f"Etiket bulunamadı: {operand}")

                elif instr == "BEQ":
                    if self.registers['A'] == 0:
                        if operand in self.labels:
                            self.pc = self.labels[operand]
                            continue
                        else:
                            raise ValueError(f"Etiket bulunamadı: {operand}")

                elif instr == "BNE":
                    if self.registers['A'] != 0:
                        if operand in self.labels:
                            self.pc = self.labels[operand]
                            continue
                        else:
                            raise ValueError(f"Etiket bulunamadı: {operand}")

                else:
                    raise ValueError(f"Bilinmeyen komut: {instr}")

                self.pc += 1

            except Exception as e:
                raise Exception(f"Satır {self.pc + 1}: {lines[self.pc]} -> {e}")



    def get_output(self):
        output = []

        output.append("=== Register Durumu ===")
        for reg, val in self.registers.items():
            output.append(f"Register {reg} = {val}")

        output.append("\n=== Hafıza Durumu ===")
        for addr in sorted(self.memory):
            output.append(f"Memory[{hex(addr)}] = {self.memory[addr]}")

        return "\n".join(output)
