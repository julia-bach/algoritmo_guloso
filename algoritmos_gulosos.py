import json
import heapq

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def dijkstra(graph, start, end):
    priority_queue = [(0, start, [])]
    shortest_distances = {start: 0}
    
    while priority_queue:
        cost, current_city, path = heapq.heappop(priority_queue)
        
        if current_city == end:
            return path + [current_city], cost
        
        for neighbor, distance in graph.get(current_city, {}).items():
            new_cost = cost + distance
            if neighbor not in shortest_distances or new_cost < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor, path + [current_city]))
    
    return None, float("inf")

def main():
    # test_example.json é usado para testes, facilitando a verificação do funcionamento do algoritmo
    # json_file = "test_example.json"
    json_file = "cities.json"
    graph = load_data(json_file)
    
    start = input("Digite a cidade de origem: ")
    end = input("Digite a cidade de destino: ")
    
    if start not in graph or end not in graph:
        print("Erro: Uma das cidades informadas não está no banco de dados.")
        return
    
    path, total_distance = dijkstra(graph, start, end)
    
    if path:
        print("\nMenor caminho encontrado:\n")
        for i in range(len(path) - 1):
            print(f"{path[i]}  -->  {path[i+1]}: {graph[path[i]][path[i+1]]} km")
        print(f"\nDistância total: {total_distance} km\n")
    else:
        print("Não foi possível encontrar um caminho entre as cidades informadas.")

if __name__ == "__main__":
    main()
