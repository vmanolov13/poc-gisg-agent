import time

def run_agent():
    print("MCP Agent started...")
    while True:
        # Simulate some work
        print("Agent heartbeat")
        time.sleep(10)

if __name__ == "__main__":
    run_agent()
