import sys

DEBUG = not False
TARGETS = [ 10.0, 10.1, 10.2, 10.3, 10.4 ]

if __name__ == "__main__":
    data = sys.argv[1:]
    if len(data) != len(TARGETS):
        print(
                f"[-] invalid result vector length: len({data}) = {len(data)}, expected: {len(TARGETS)}",
                file=sys.stderr
                )

    converted_data = []
    for item in data:
        try:
            converted_item = round(float(item), 2)
            converted_data.append(converted_item)
        except ValueError:
            print(
                    f"[-] item '{item}' cannot be converted to type float",
                    file=sys.stderr
                    )
            sys.exit(1)

    total_delta_diameter = 0
    for result, target in zip(converted_data, TARGETS):
        if DEBUG: print(f"[*] expected {target:.2f} - result {result:.2f}")
        total_delta_diameter += target - result

    average_delta_diameter = total_delta_diameter / len(converted_data)
    average_radius_compensation = average_delta_diameter / 2

    print(f"X-Y hole/contour compensation: {average_radius_compensation} (Radius)")
