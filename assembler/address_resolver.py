# assembler/address_resolver.py

INSTRUCTION_LENGTHS = {
    "LDAA": 2,
    "STAA": 2,
    "LDAB": 2,
    "STAB": 2,
    "JMP": 3,
    "JSR": 3,
    "ADDA": 2,
    "SUBA": 2,
    "BRA": 2,
    "BEQ": 2,
    "BNE": 2,
    "RTS": 1,
}

def resolve_addresses(code_lines):
    current_address = 0x0000
    address_map = {}
    label_map = {}

    for line in code_lines:
        stripped = line.strip()

        if not stripped:
            continue

        if stripped.startswith("ORG"):
            try:
                address_str = stripped.split()[1]
                current_address = int(address_str.replace("$", ""), 16)
            except:
                print(f"ORG komutunda hata: {line}")
                continue

        elif ":" in stripped:
            label = stripped.replace(":", "").strip()
            label_map[label] = current_address

        else:
            mnemonic = stripped.split()[0].upper()
            instr_len = INSTRUCTION_LENGTHS.get(mnemonic, 0)
            address_map[current_address] = line
            current_address += instr_len

    return address_map, label_map
