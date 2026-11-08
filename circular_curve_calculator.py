
import math


def calculate_curve(radius, angle, pi_chainage, interval):
    """Calculate the elements of a simple circular curve."""

    # Convert the intersection angle from degrees to radians
    delta = math.radians(angle)
    half_delta = delta / 2

    # Calculate the main curve elements
    tangent = radius * math.tan(half_delta)
    curve_length = radius * delta
    long_chord = 2 * radius * math.sin(half_delta)
    external = radius * (1 / math.cos(half_delta) - 1)
    mid_ordinate = radius * (1 - math.cos(half_delta))

    # Calculate the beginning and end chainages
    pc_chainage = pi_chainage - tangent
    pt_chainage = pc_chainage + curve_length

    # Display the calculated results
    print("\n" + "=" * 55)
    print(" SIMPLE CIRCULAR CURVE SETTING-OUT RESULTS")
    print("=" * 55)

    print(f"Radius (R):              {radius:.3f} m")
    print(f"Intersection angle:      {angle:.3f} degrees")
    print(f"Tangent length (T):      {tangent:.3f} m")
    print(f"Curve length (L):        {curve_length:.3f} m")
    print(f"Long chord (LC):         {long_chord:.3f} m")
    print(f"External distance (E):   {external:.3f} m")
    print(f"Mid-ordinate (M):        {mid_ordinate:.3f} m")
    print(f"PI chainage:             {pi_chainage:.3f} m")
    print(f"PC chainage:             {pc_chainage:.3f} m")
    print(f"PT chainage:             {pt_chainage:.3f} m")

    # Generate setting-out points at regular arc intervals
    print("\nSETTING-OUT TABLE")
    print("-" * 75)
    print(
        f"{'Point':<8}{'Arc dist. (m)':<17}"
        f"{'Chainage (m)':<17}{'Chord (m)':<15}"
        f"{'Deflection (deg)':<18}"
    )
    print("-" * 75)


    distance = 0.0
    point_number = 0

    while True:
        # Include each interval and the final PT
        point_number += 1
        arc_distance = min(distance, curve_length)

        # Chord from PC to the point
        chord = 2 * radius * math.sin(
            arc_distance / (2 * radius)
        )

        # Cumulative deflection angle from the tangent at PC
        deflection = math.degrees(
            arc_distance / (2 * radius)
        )

        chainage = pc_chainage + arc_distance

        print(
            f"P{point_number:<7}"
            f"{arc_distance:<17.3f}"
            f"{chainage:<17.3f}"
            f"{chord:<15.3f}"
            f"{deflection:<18.5f}"
        )

        # Stop after printing the final point
        if arc_distance >= curve_length:
            break

        distance += interval


        # Cumulative deflection angle from the tangent at PC
        deflection = math.degrees(
            arc_distance / (2 * radius)
        )

        chainage = pc_chainage + arc_distance

        print(
            f"P{point_number:<7}"
            f"{arc_distance:<17.3f}"
            f"{chainage:<17.3f}"
            f"{chord:<15.3f}"
            f"{deflection:<18.5f}"
        )

        if arc_distance == curve_length:
            break

        distance += interval

        # Ensure the final point is included
        if distance >= curve_length:
            distance = curve_length

    print("=" * 55)


def main():
    print("SIMPLE CIRCULAR CURVE SETTING-OUT CALCULATOR")

    try:
        radius = float(input("Enter radius in metres: "))
        angle = float(input("Enter intersection angle in degrees: "))
        pi_chainage = float(input("Enter PI chainage in metres: "))
        interval = float(input("Enter setting-out interval in metres: "))

        # Validate the inputs
        if radius <= 0:
            raise ValueError("Radius must be greater than zero.")

        if not 0 < angle < 180:
            raise ValueError("Angle must be greater than 0 and less than 180 degrees.")

        if pi_chainage < 0:
            raise ValueError("PI chainage cannot be negative.")

        if interval <= 0:
            raise ValueError("Setting-out interval must be greater than zero.")

        tangent = radius * math.tan(math.radians(angle / 2))

        if pi_chainage < tangent:
            raise ValueError(
                "PI chainage is too small: the calculated PC chainage is negative."
            )

        calculate_curve(radius, angle, pi_chainage, interval)

    except ValueError as error:
        print(f"\nInput error: {error}")


if __name__ == "__main__":
    main()
