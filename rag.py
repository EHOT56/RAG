import os
from rapidfuzz import fuzz



def get_docs():
    docs = []
    for file in os.listdir("docs"):
        if file.endswith("txt"):
            docs.append(file)
    return docs


if __name__ == "__main__":
    docs_names = get_docs()
    
    files = {}
    for dock_name in docs_names:
        with open("docs/" + dock_name, "r", encoding="utf-8") as file:
            files[dock_name] = file.readlines()

    while True:
        prompt = input("Enter your prompt: ")
        candidates = []
        for file_name in files:
            for i, line in enumerate(files[file_name]):
                chance = fuzz.partial_ratio(line, prompt)
                candidates.append((chance, line, i+1, file_name)) # chance, text, line number
        
        candidates.sort(key = lambda x: x[0], reverse=True)
        print("TOP 3 CANDIDATES:")
        for i in range(3):
            print(f"chance: {candidates[i][0]:.2f}%, file name: {candidates[i][3]}, line №:{candidates[i][2]}, text: {candidates[i][1]}")
        
        if candidates[0][0] < 5:
            print("Nav pietiekami informācijas avotas")
        else:
            print(f"Atrasts fragments: {candidates[0][1]}")