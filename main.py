import sys
from graph_builder import load_metro_graph
from station_selector import get_station_code_by_name


def main():
    csv_path = 'processed_stations.csv'

    print("\n" + "=" * 60)
    print(f"\033[94m{'🎉 Hello There! 🚆'.center(50)}\033[0m")

    print("=" * 60 + "\n")
    
    print("Building metro graph from CSV...")
    print("\n🌟  Welcome to the Singapore Metro Station  🌟")

    g = load_metro_graph(csv_path)
    start_code = get_station_code_by_name(g, "Enter starting station name: ")
    dest_code = get_station_code_by_name(g, "Enter destination station name: ")

    print("\nLeast stops route:\n")
    g.bfs(start_code)
    g.bfs_shortest_path(dest_code)
    print("=" * 50)

    print("\nFastest route (by time):\n")
    g.dijkstra(start_code)
    g.print_dijkstra_path(dest_code)
    print("=" * 50)

    # Exit banner

    print("\n" + "=" * 60)
    print("🎉 \033[94mThank you for using the Singapore Trip Planner!\033[0m 🚆")
    print("=" * 60 + "\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)  