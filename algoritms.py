# Бинарный поиск
def binary_search(arr, item):
    low = 0
    high = len(arr)-1
    
    while low <= high:
        mid = round((low + high) / 2)
        print(mid)
        guess = arr[mid]
        print(guess)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

binary_search([1, 3, 6, 7, 15, 41, 50, 55, 100], 50)


# Поиск минимума 
def find_Smallest(arr):
    smallest = arr[0]
    id_smallest = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            id_smallest = i
    return id_smallest

# Сортировка выбором
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        id_smallest = find_Smallest(arr)
        newArr.append(arr.pop(id_smallest))
    return newArr

selectionSort([5, 1, 4, 4, 2, 1, 3, 6])


# Сумма элементов в списке (рекурсия)
def summ(x):
    total = 0
    if x == []:
        return 0
    else:    
        return x[0] + summ(x[1:])

summ([5, 4, 2, 1, 3])


# Подсчёт элементов в списке (рекурсия)
def count(x):
    number = 0
    if x == []:
        return 0
    else:
        number = 1
        return number + count(x[1:])

count([5, 1, 4, 4, 2, 1, 3, 6])


# Поиск максимума (рекурсия)
def find_maximum(x):
    if len(x) == 2:
        return x[0] if x[0] > x[1] else x[1]
    sub_max = find_maximum(x[1:])
    return x[0] if x[0] > sub_max else sub_max

find_maximum([5, 1, 4, 4, 2, 1, 3, 6])


# Быстрая сортировка (рекурсия)
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)

quicksort([10, 4, 10, 30, 18, 145, 46])


# Возврат данных из кэша
cashe = {}
def get_cashe(url):
    if cashe.get(url):
        return cashe[url]
    else:
        data = get_data_from_server(url)
        cashe[url] = data
        return data
    
    
# Поиск в ширину
graph = {}
graph['you'] = ['Alice', 'Bob', 'Claire']
graph['Bob'] = ['Anuj', 'Peggy']
graph['Alice'] = ['Peggy']
graph['Claire'] = ['Thom', 'Jonny']
graph['Anuj'] = []
graph['Peggy'] = []
graph['Thom'] = []
graph['Jonny'] = []

def person_is_seller(name):
    return name[-1] == 'm'


from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' это продавец манго')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search('you')


# Алгоритм Дейкстры
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

# Создание таблицы стоимостей
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# Код создания хеш-таблицы родителей
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# Массив всех уже обработанных узлов.
processed = []

def find_lower_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
        
#Алгоритм Дейкстры
node = find_lower_cost_node(costs)
while node is not None:
    print(node)
    cost = costs[node]
    neighbors = graph[node]
    print('neighbors', processed)
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lower_cost_node(costs)
costs



states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)
final_stations


# Сортировка пузырьком
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                print(nums[i])
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
                swapped = True
nums = [100, 39, 1000, 28, 65]
bubble_sort(nums)
print(nums)


# Последовательность Фиабоначчи с Мемоизацией
cashe = {0: 0, 1: 1}
def fibonacci(n):
    if n in cashe:
        return cashe[n]
    else:
        f = fibonacci(n-1) + fibonacci(n-2)
        cashe[n] = f
        return f
fibonacci(50)






