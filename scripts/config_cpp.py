import sys
import re

def parse_value(v):
    v = v.strip()

    # gpio_x handling
    if v.startswith("gpio_"):
        n = int(v[5:])
        if n == 0:
            return "PIN_ZERO"
        return str(n)

    # boolean
    if v.lower() in ("true", "false"):
        return v.lower()

    # integer
    if re.fullmatch(r"-?\d+", v):
        return v

    # string
    return f"\"{v}\""


def parse_config(filename):
    data = {}
    section = None

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1].strip()
                data.setdefault(section, {})
                continue

            if "=" in line and section:
                k, v = line.split("=", 1)
                data[section][k.strip()] = parse_value(v)

    return data


def emit_cpp(data):
    print("inline void applyPreferred(Config& c) {")
    for section, values in data.items():
        print(f"\n    // [{section}]")
        for k, v in values.items():
            if v.startswith('"'):   # string
                print(f"    strcpy(c.{section}.{k}, {v});")
            else:
                print(f"    c.{section}.{k} = {v};")
    print("}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python config_to_cpp.py config.txt")
        sys.exit(1)

    cfg = parse_config(sys.argv[1])
    emit_cpp(cfg)
