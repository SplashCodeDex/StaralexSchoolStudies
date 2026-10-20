"""
Grade 9 Computing - Strand 1: Introduction to Computing
Sub-strand 1: Components of Computers and Computer Systems
Lesson 01: Next-Generation Computers and Supercomputing Interactive Playground
"""

import sys
import time
import math
import random


def clear_banner():
    print("=" * 72)
    print("   GRADE 9 COMPUTING: LESSON 01 INTERACTIVE STUDY PLAYGROUND")
    print("   Topic: Next-Generation Computing, Google Sycamore & Supercomputers")
    print("=" * 72)


def classical_vs_qubit_demo():
    print("\n--- [DEMONSTRATION 1: CLASSICAL BIT VS QUANTUM BIT (QUBIT)] ---")
    print("In classical computing, a bit is either 0 or 1.")
    print("In quantum computing, a qubit exists in a superposition of BOTH 0 and 1.")
    print("-" * 72)

    bit_state = random.choice([0, 1])
    print(f"Classical Bit value: {bit_state} (Deterministic, definite state)")

    print("\nSimulating a Qubit in Superposition State |psi> = a|0> + b|1>...")
    print("Before measurement, the qubit holds probabilities of being 0 and 1.")

    # Random amplitude probabilities
    prob_zero = round(random.uniform(0.1, 0.9), 2)
    prob_one = round(1.0 - prob_zero, 2)

    print(f"Current Quantum Probability -> P(0) = {prob_zero * 100:.1f}%, P(1) = {prob_one * 100:.1f}%")
    input("\nPress [ENTER] to measure the qubit (collapse the wave function)... ")

    # Wave function collapse
    collapsed_state = 0 if random.random() < prob_zero else 1
    print(f"Measurement Result: The qubit collapsed into definite state: {collapsed_state}")
    print("Note: Before observation, all possible answers were evaluated in parallel.")


def exponential_scaling_demo():
    print("\n--- [DEMONSTRATION 2: EXPONENTIAL SCALING (2^n POWER)] ---")
    print("A classical register of 'n' bits can only store ONE number at a time.")
    print("A quantum register of 'n' qubits can store 2^n numbers SIMULTANEOUSLY.")
    print("-" * 72)

    try:
        n_qubits = int(input("Enter number of qubits to evaluate (e.g. 1 to 53): ").strip())
        if n_qubits < 1:
            print("Please enter a positive integer.")
            return
        if n_qubits > 100:
            print("Number too high for quick demonstration. Capping at 100.")
            n_qubits = 100
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    simultaneous_states = 2 ** n_qubits
    print(f"\nResults for {n_qubits} Qubits:")
    print(f"Classical Bits: Can hold 1 of {simultaneous_states:,} states at any given moment.")
    print(f"Quantum Qubits: Can hold ALL {simultaneous_states:,} states AT THE EXACT SAME TIME.")

    if n_qubits >= 53:
        print("\n[HISTORICAL FACT]")
        print("Google Sycamore operated with 53 active qubits.")
        print(f"Total simultaneous states in Sycamore = 2^53 = {2**53:,}")
        print("That is over 9 quadrillion simultaneous values in a single calculation cycle.")


def sycamore_vs_summit_comparison():
    print("\n--- [DEMONSTRATION 3: GOOGLE SYCAMORE VS IBM SUMMIT SPEED BENCHMARK] ---")
    print("Benchmark: Random Quantum Circuit Sampling")
    print("-" * 72)

    sycamore_seconds = 200
    summit_years = 10000
    summit_seconds = summit_years * 365.25 * 24 * 3600

    print(f"Google Sycamore Execution Time : {sycamore_seconds} seconds (3 minutes and 20 seconds)")
    print(f"IBM Summit Classical Estimate   : {summit_years:,} years (~{summit_seconds:,.0f} seconds)")

    speedup = summit_seconds / sycamore_seconds
    print(f"\nCalculated Speedup Ratio        : Sycamore was ~{speedup:,.0f} times faster.")
    print("\nThis astronomical difference illustrates the concept of 'Quantum Supremacy'")
    print("(solving a problem on a quantum computer that is infeasible on any classical computer).")


def interactive_theory_quiz():
    print("\n--- [INTERACTIVE THEORY QUIZ: LESSON 01 CHECKPOINT] ---")
    print("Answer each question to test your mastery. Type your answer or selection.")
    print("-" * 72)

    questions = [
        {
            "q": "1. What is the fundamental unit of information in a quantum computer called?",
            "ans": "qubit",
            "full": "Qubit (Quantum Bit)"
        },
        {
            "q": "2. How many physical qubits were built into the Google Sycamore processor?",
            "ans": "54",
            "full": "54 physical qubits"
        },
        {
            "q": "3. How many qubits were operational during Google Sycamore's milestone test?",
            "ans": "53",
            "full": "53 operational qubits"
        },
        {
            "q": "4. How many seconds did Google Sycamore take to finish the benchmark calculation?",
            "ans": "200",
            "full": "200 seconds"
        },
        {
            "q": "5. What term describes a quantum processor outperforming any classical supercomputer?",
            "ans": "quantum supremacy",
            "alt": "quantum advantage",
            "full": "Quantum Supremacy (or Quantum Advantage)"
        }
    ]

    score = 0
    for item in questions:
        print(f"\n{item['q']}")
        user_ans = input("Your Answer: ").strip().lower()

        is_correct = (item['ans'] in user_ans) or (item.get('alt') and item['alt'] in user_ans)
        if is_correct:
            print(f"CORRECT. (Detail: {item['full']})")
            score += 1
        else:
            print(f"INCORRECT. The expected answer is: {item['full']}")

    print("\n" + "=" * 72)
    print(f"Quiz Completed! Your Score: {score} / {len(questions)}")
    if score == len(questions):
        print("Mastery achieved! You are ready to proceed to Lesson 02.")
    else:
        print("Review the lesson notes to reinforce the missed questions.")
    print("=" * 72)


def main():
    while True:
        clear_banner()
        print("\nSelect a study activity:")
        print("  1. Classical Bit vs Quantum Qubit Demonstration")
        print("  2. Exponential State Scaling Calculator (2^n)")
        print("  3. Google Sycamore vs Classical Supercomputer Benchmark")
        print("  4. Interactive Theory Quiz (Day 1 Checkpoint)")
        print("  0. Exit Playground")

        choice = input("\nEnter choice (0-4): ").strip()

        if choice == "1":
            classical_vs_qubit_demo()
        elif choice == "2":
            exponential_scaling_demo()
        elif choice == "3":
            sycamore_vs_summit_comparison()
        elif choice == "4":
            interactive_theory_quiz()
        elif choice == "0":
            print("\nExiting playground. Good luck with your studies!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 0 and 4.")

        input("\nPress [ENTER] to return to main menu...")


if __name__ == "__main__":
    main()
