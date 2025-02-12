# Bubblesort
## Beschreibung

Bubblesort ist ein Sortierungsalgorithmus. Bei dieser Vorgehensweise zur Ordnung einer Liste von Zahlen wird diese wiederholt von Anfang bis Ende durchlaufen. Bei jedem Durchlauf werden die Zahlen paarweise verglichen und anschließend basierend auf der Sortierungsrichtung wenn nötig vertauscht. Nach jedem Durchlauf kann eine Zahl mehr am Ende der Liste als richtig sortiert markiert werden und der nächste Durchlauf muss nur noch bis ausschließlich zu dieser Zahl gehen.

## Pseudocode

```python
Bubblesort(Liste A)
    für n von 0 bis Länge(A) - 1
        für j von 1 bis Länge(A) - n
            wenn A[j] < A[j-1]
                Vertausche A[j] und A[j-1]
    
    Return A
```
