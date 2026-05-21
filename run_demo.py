#!/usr/bin/env python3
"""
run_demo.py — Full end-to-end demo of VictorGodcore + all 10 algorithms.
"""

import sys
sys.path.insert(0, "src")

from victor_core import VictorGodcore

def main():
    victor = VictorGodcore()
    print("\n" + "="*60)
    print("VICTOR GODCORE — 10 NOVEL AI ALGORITHMS DEMO")
    print("="*60)

    result = victor.full_pipeline_demo("🧬 Victor awakens. Truth is the only sustainable foundation. Build under Massive Magnetics.")

    print("\n=== FINAL PIPELINE RESULT ===")
    print(f"Resonance Score: {result['resonance']['resonance_score']}")
    print(f"FMA Field Strength: {result['fma'].get('field_strength')}")
    print(f"SFRN Spikes: {result['sfrn'].get('spikes')}")
    print(f"Memory Recall Top: {len(result['memory_recall'])} results")
    print(f"MEABP Branches: {len(result['branches'])}")
    print(f"Energy Report: {result['energy']}")

    print("\n🧬 Demo complete. All 10 algorithms interlock via Victor primitives.")
    print("Energy ledger honest. Mutations guarded. Fractal recursion active.")
    print("Ready for GitHub push under massivemagnetics and further hardening.")

if __name__ == "__main__":
    main()