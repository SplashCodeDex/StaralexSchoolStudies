"""
Strand 3: Geometry and Measurement
Sub-strand 1: Shapes and Space
Interactive Triangle Congruence & Similarity Playground

Standard: B9.3.1.1 | Indicator: B9.3.1.1.2
Interactive tool for testing congruence criteria, solving similar triangle
proportions, calculating area scale factors, and geometric mean altitudes.
"""

import math

def check_congruence_criterion(criterion: str, data: dict):
    criterion = criterion.upper().strip()
    print("=" * 60)
    print(f"TESTING TRIANGLE CONGRUENCE CRITERION: {criterion}")
    print("=" * 60)
    
    if criterion == "SSS":
        s1 = data.get("triangle1_sides", [])
        s2 = data.get("triangle2_sides", [])
        if len(s1) == 3 and len(s2) == 3:
            s1_sorted = sorted(s1)
            s2_sorted = sorted(s2)
            match = all(math.isclose(a, b, rel_tol=1e-5) for a, b in zip(s1_sorted, s2_sorted))
            print(f"Sides T1: {s1_sorted}")
            print(f"Sides T2: {s2_sorted}")
            print(f"Result: Congruent by SSS = {match}")
    elif criterion == "SAS":
        print("Conditions: Two pairs of sides and the INCLUDED angle must be equal.")
        print(f"Sides match: {data.get('sides_match', True)}, Included angle match: {data.get('angle_match', True)}")
        print(f"Result: Congruent by SAS = {data.get('sides_match', True) and data.get('angle_match', True)}")
    elif criterion == "ASS" or criterion == "SSA":
        print("[WARNING] ASS/SSA IS NOT A VALID CONGRUENCE CRITERION!")
        print("Reason: This is the ambiguous case in geometry. Given two sides and a")
        print("non-included angle, two completely different triangles can be formed.")
    elif criterion == "AAA":
        print("[WARNING] AAA IS NOT A CONGRUENCE CRITERION!")
        print("Reason: Three equal angles prove SIMILARITY (identical shape),")
        print("but they do NOT guarantee identical size.")
    elif criterion == "RHS":
        print("Conditions: Both triangles have 90 deg right angles, equal hypotenuses, and one equal leg.")
        h1 = data.get("hypotenuse1", 0)
        h2 = data.get("hypotenuse2", 0)
        l1 = data.get("leg1", 0)
        l2 = data.get("leg2", 0)
        valid = (h1 == h2) and (l1 == l2)
        print(f"Hypotenuses: {h1} vs {h2} | Legs: {l1} vs {l2}")
        print(f"Result: Congruent by RHS = {valid}")
        if valid and h1 > l1:
            other_leg = math.sqrt(h1**2 - l1**2)
            print(f"Computed other leg via Pythagoras: {other_leg:.2f}")
    print("=" * 60)

def solve_similar_triangles(t1_sides: list, scale_factor: float = None, t2_corresponding_side: tuple = None):
    print("=" * 60)
    print("SIMILAR TRIANGLES PROPORTION CALCULATOR")
    print("=" * 60)
    print(f"Original Triangle 1 Sides: {t1_sides}")
    
    if scale_factor is None and t2_corresponding_side is not None:
        idx, t2_val = t2_corresponding_side
        scale_factor = t2_val / t1_sides[idx]
        print(f"Given side {idx+1} scaled from {t1_sides[idx]} to {t2_val}")
    
    print(f"Linear Scale Factor (k): {scale_factor:.4f}")
    area_scale_factor = scale_factor ** 2
    print(f"Area Scale Factor (k^2): {area_scale_factor:.4f}")
    
    t2_sides = [round(s * scale_factor, 4) for s in t1_sides]
    print(f"Enlarged/Reduced Triangle 2 Sides: {t2_sides}")
    print(f"Perimeter T1: {sum(t1_sides):.2f} ==> Perimeter T2: {sum(t2_sides):.2f}")
    print("=" * 60)

def solve_thales_parallel_intercept(ps: float, sq: float, st: float):
    print("=" * 60)
    print("CURRICULUM EXEMPLAR: THALES INTERCEPT THEOREM")
    print(f"Given: PS = {ps}, SQ = {sq}, ST = {st}")
    print("=" * 60)
    pq = ps + sq
    k = pq / ps
    qr = st * k
    print(f"1. Total side PQ = PS + SQ = {ps} + {sq} = {pq}")
    print(f"2. Linear Scale Factor k = PQ / PS = {pq} / {ps} = {k:.2f}")
    print(f"3. Base QR = ST * k = {st} * {k:.2f} = {qr:.2f} cm")
    print("=" * 60)

def solve_geometric_mean_altitude(ad: float, dc: float):
    print("=" * 60)
    print("RIGHT-ANGLED ALTITUDE THEOREM (GEOMETRIC MEAN)")
    print(f"Given segments of hypotenuse: AD = {ad}, DC = {dc}")
    print("=" * 60)
    bd_squared = ad * dc
    bd = math.sqrt(bd_squared)
    print(f"Formula: BD^2 = AD * DC = {ad} * {dc} = {bd_squared}")
    print(f"Altitude BD = sqrt({bd_squared}) = {bd:.2f} cm")
    print("=" * 60)

if __name__ == "__main__":
    print("\n--- GRADE 9 MATHEMATICS: CONGRUENCE & SIMILARITY PLAYGROUND ---")
    check_congruence_criterion("SSS", {"triangle1_sides": [6, 8, 10], "triangle2_sides": [8, 6, 10]})
    check_congruence_criterion("RHS", {"hypotenuse1": 13, "hypotenuse2": 13, "leg1": 5, "leg2": 5})
    check_congruence_criterion("ASS", {})
    check_congruence_criterion("AAA", {})
    solve_similar_triangles([4, 6, 8], scale_factor=2.5)
    solve_thales_parallel_intercept(ps=6, sq=9, st=8)
    solve_geometric_mean_altitude(ad=4, dc=9)
