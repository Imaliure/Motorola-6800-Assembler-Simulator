# assembler/parser.py

# Örnek Motorola 6800 komut seti
INSTRUCTION_SET = {
    "LDAA": "86",   # Load Accumulator A
    "STAA": "97",   # Store Accumulator A
    "LDAB": "C6",   # Load Accumulator B
    "STAB": "D7",   # Store Accumulator B
    "JMP": "7E",    # Jump
    "JSR": "BD",    # Jump to Subroutine
    "ADDA": "8B",   # Add to Accumulator A
    "SUBA": "80",   # Subtract from Accumulator A
    "BRA": "20",    # Branch Always
    "BEQ": "27",    # Branch if Equal
    "BNE": "26",    # Branch if Not Equal
    "RTS": "39",    # Return from Subroutine
}

def is_valid_instruction(line):
    if not line:
        return False

    parts = line.split()
    mnemonic = parts[0].upper()

    return mnemonic in INSTRUCTION_SET

def validate_code(code_lines):
    result = []
    for idx, line in enumerate(code_lines, start=1):
        valid = is_valid_instruction(line)
        result.append((idx, line, valid))
    return result
