import simpy
import random

def turnaround(env, flight_id, gate, durations):
    """Simulate an aircraft turnaround."""
    start = env.now
    for task, duration in durations.items():
        d = random.gauss(duration, duration * 0.1)
        yield env.timeout(d)
    total = env.now - start
    print(f"{flight_id} finished in {total:.1f} min")
    return total

def run_simulation(n_flights=5):
    env = simpy.Environment()
    durations = {
        "disembarking": 15,
        "cleaning": 20,
        "fueling": 25,
        "boarding": 30
    }
    for i in range(n_flights):
        env.process(turnaround(env, f"Flight_{i+1}", "GateA", durations))
        yield_delay = random.uniform(5, 10)
        env.timeout(yield_delay)
    env.run()
    print("Simulation complete.")

if __name__ == "__main__":
    run_simulation()

