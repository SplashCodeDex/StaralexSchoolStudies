"""
Strand 3: Geometry and Measurement
Sub-strand 1: Shapes and Space
Interactive Polygon Angle Playground & Calculator

Standard: B9.3.1.1 | Indicator: B9.3.1.1.1
Use this interactive script to experiment with polygon angle theorems,
triangulation, reverse solvers, and tessellation checks.
"""

def get_polygon_name(n: int) -> str:
    names = {
        3: "Triangle (Trigon)",
        4: "Quadrilateral (Tetragon)",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon (Septagon)",
        8: "Octagon",
        9: "Nonagon (Enneagon)",
        10: "Decagon",
        11: "Undecagon (Hendecagon)",
        12: "Dodecagon",
        15: "Pentadecagon",
        20: "Icosagon",
    }
    return names.get(n, f"{n}-gon")

def analyze_polygon(n: int):
    if n < 3:
        print("[Error] A polygon must possess at least 3 sides.")
        return
    
    name = get_polygon_name(n)
    diagonals_from_one_vertex = n - 3
    total_diagonals = n * (n - 3) // 2
    num_triangles = n - 2
    interior_sum = (n - 2) * 180
    each_ext = 360 / n
    each_int = interior_sum / n
    
    print("=" * 60)
    print(f"GEOMETRIC ANALYSIS FOR: {name.upper()} (n = {n})")
    print("=" * 60)
    print(f"1. Name of Polygon:                   {name}")
    print(f"2. Number of Sides (n):               {n}")
    print(f"3. Number of Vertices:                {n}")
    print(f"4. Diagonals from one vertex (n - 3): {diagonals_from_one_vertex}")
    print(f"5. Total Diagonals [n(n-3)/2]:        {total_diagonals}")
    print(f"6. Triangulation Triangles (n - 2):   {num_triangles}")
    print(f"7. Total Interior Angle Sum (S):      {interior_sum} deg")
    print(f"   Formula: ({n} - 2) * 180 deg = {num_triangles} * 180 deg = {interior_sum} deg")
    print(f"8. Regular Polygon Each Interior:     {each_int:.2f} deg")
    print(f"9. Regular Polygon Each Exterior:     {each_ext:.2f} deg")
    print(f"10. Linear Pair Check (Int + Ext):    {each_int + each_ext:.2f} deg (180 deg)")
    
    # Tessellation check
    if 360 % each_int == 0:
        tiles_at_vertex = int(360 // each_int)
        print(f"11. Tessellation Capability:           YES! Exactly {tiles_at_vertex} tiles fit around each vertex.")
    else:
        gap = 360 - (int(360 // each_int) * each_int)
        print(f"11. Tessellation Capability:           NO. Leaves an angular gap of {gap:.2f} deg at the vertex.")
    print("=" * 60)

def find_polygon_from_exterior(ext_angle: float):
    if ext_angle <= 0 or ext_angle >= 180:
        print("[Error] Exterior angle must be strictly between 0 and 180 degrees.")
        return
    n = 360 / ext_angle
    print("-" * 50)
    print(f"REVERSE DEDUCTION FROM EXTERIOR ANGLE: {ext_angle} deg")
    print(f"Calculation: n = 360 / {ext_angle} = {n}")
    if n.is_integer() and n >= 3:
        n_int = int(n)
        print(f"Result: Valid regular polygon exists with {n_int} sides: {get_polygon_name(n_int)}.")
    else:
        print(f"Result: No regular polygon exists (n = {n:.2f} is not an integer >= 3).")
    print("-" * 50)

def find_polygon_from_interior(int_angle: float):
    if int_angle <= 0 or int_angle >= 180:
        print("[Error] Interior angle must be strictly between 0 and 180 degrees.")
        return
    ext_angle = 180 - int_angle
    print("-" * 50)
    print(f"REVERSE DEDUCTION FROM INTERIOR ANGLE: {int_angle} deg")
    print(f"Step 1: Exterior Angle = 180 - {int_angle} = {ext_angle} deg")
    print(f"Step 2: n = 360 / {ext_angle} = {360 / ext_angle}")
    find_polygon_from_exterior(ext_angle)

def solve_curriculum_hexagon_problem():
    print("=" * 60)
    print("OFFICIAL CURRICULUM EXEMPLAR: IRREGULAR HEXAGON")
    print("Angles: 120, (5x - 6), (4x + 14), 7x, (8x - 8), 6x")
    print("=" * 60)
    n = 6
    s = (n - 2) * 180
    print(f"1. Theoretical Angle Sum: ({n} - 2) * 180 = {s} deg")
    print("2. Grouping variable coefficients: 5 + 4 + 7 + 8 + 6 = 30x")
    print("3. Grouping constants: 120 - 6 + 14 - 8 = 120")
    print("4. Equation: 30x + 120 = 720")
    print("5. 30x = 600 ==> x = 20")
    x = 20
    angles = [120, 5*x - 6, 4*x + 14, 7*x, 8*x - 8, 6*x]
    print(f"6. Calculated Angles: {angles}")
    print(f"7. Sum Verification: {sum(angles)} deg (Match = {sum(angles) == s})")
    print("=" * 60)

if __name__ == "__main__":
    print("\n--- GRADE 9 MATHEMATICS: POLYGON ANGLE PLAYGROUND ---")
    analyze_polygon(5)   # Pentagon
    analyze_polygon(6)   # Hexagon
    analyze_polygon(8)   # Octagon
    find_polygon_from_interior(156) # Exemplar 3
    solve_curriculum_hexagon_problem()
