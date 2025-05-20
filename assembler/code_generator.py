# assembler/code_generator.py

OPCODES = {
    "LDAA": "86",   # Immediate
    "STAA": "B7",   # Direct
    "LDAB": "C6",
    "STAB": "D7",
    "JMP": "7E",
    "JSR": "BD",
    "ADDA": "BB",
    "SUBA": "B0",
    "BRA": "20",
    "BEQ": "27",
    "BNE": "26",
    "RTS": "39",
}

def generate_object_code(code_lines, label_map):
    object_lines = []

    for line in code_lines:
        stripped = line.strip()

        # ORG, END, boş veya label satırları atla
        if not stripped or stripped.startswith("ORG") or stripped == "END" or stripped.endswith(":"):
            object_lines.append(("", stripped))
            continue

        parts = stripped.split(maxsplit=1)
        mnemonic = parts[0].upper()
        operand = parts[1] if len(parts) > 1 else None

        opcode = OPCODES.get(mnemonic, "??")

        machine_code = ""
        if operand:
            operand = operand.replace("#", "").replace("$", "")

            # Label varsa adresi çek
            if operand in label_map:
                operand_addr = label_map[operand]
                operand_hex = f"{operand_addr:04X}"
                machine_code = opcode + operand_hex
            else:
                try:
                    value = int(operand, 16)
                    if value <= 0xFF:
                        machine_code = opcode + f"{value:02X}"
                    else:
                        machine_code = opcode + f"{value:04X}"
                except:
                    machine_code = opcode + "??"
        else:
            machine_code = opcode

        object_lines.append((machine_code, stripped))

    return object_lines
