"""
This is the grid module. It contains the Grid class and its associated methods.
"""
import random
import matplotlib.pyplot as plt
from itertools import permutations
from graph import Graph    

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        L=[list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)]
        if self.state==L :
            print("the grid is sorted")
        else :
            print("the grid still not sorted")
        return(self.state==L)

        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean comparing "self.state" to the grid sorted , created by a nested loop (descending columns and then descending rows)

        """

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        i,j=cell1[0],cell1[1]
        a,b=cell2[0],cell2[1]
        if (abs(i-a)<2 and abs(j-b<2)):
            self.state[i][j],self.state[a][b]=self.state[a][b],self.state[i][j]
        else :
            print("this swap is not possible")
        return()
    ######################We chose to implement methods that : find an int ("i" in [1;n*m]) in the grid , return several swaps to a same direction , we also made "get" methods that return the sequences of these "several swaps to a same direction". 

    
    def swap_droite(self,a,b,k):
        self.swap_seq(self.get_swap_droite(a,b,k))
        return()
    
    def get_swap_droite(self,a,b,k):
        l=[]
        for i in range (k):
            l+=[((a,b+k-1),(a,b+k))]
        return(l)
    
    def swap_gauche(self,a,b,k):
        self.swap_seq(self.get_swap_gauche(a,b,k))
        return()
    
    def get_swap_gauche(self,a,b,k):
        l=[]
        for i in range (k):
            l+=[((a,b+k-1),(a,b+k-2))]
        return(l)
    
    def swap_haut(self,a,b,k):
        self.swap_seq(self.get_swap_haut(a,b,k))
        return()
    
    def get_swap_haut(self,a,b,k):
        l=[]
        for i in range (k):
            l+=[((a+k-1,b),(a+k-2,b))]
        return(l)
    
    def swap_bas(self,a,b,k):
        self.swap_seq(self.get_swap_bas(a,b,k))
        return()
    
    def get_swap_bas(self,a,b,k):
        l=[]
        for i in range (k):
            l+=[((a+k-1,b),(a+k,b))]
        return(l)
    
    def find(self,p):
        a=0
        b=0
        while self.state[a][b] != p:
            if b<self.n-1:
                b+=1
            else :
                b=0
                a+=1
            if a>self.m-1:
                return(str(p),"not found in the grid")
        return(a,b)

    #########################
    def swap_seq(self, cell_pair_list):
        for k in range(len(cell_pair_list)):
            self.swap(cell_pair_list[k][0],cell_pair_list[k][1])
        return()
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
    #########################Q4 , graphic representation of grids using numpy and matplotlib
    
    def grid_show(self):
        for i in range(self.m):
            for j in range(self.n):
                ax.text(j, i, str(self.state[i][j]), ha='center', va='center', color='black', fontsize=12)
    # Add numbers to each cell
        ax.axis('off')
    # Hide axes
        plt.show()
        return()
    #########################
    #########################Q6 grids -> nodes
    @staticmethod
    def perm(n): #renvoie une liste P composée de (n!) listes, chacune étant une permutation de 1,2,...,n 
        L = [k for k in range(1,n+1)]
        P = list(permutations(L))
        return P

    def get_tuple_grid(self):
        s=[]
        for i in range (self.m):
            for j in range (self.n):
                s.append(self.state[i][j])
        return(tuple(s))
     #Returns an unhashed tuple of ints corresponding to a node (considering a grid)
        
    def get_neighbors_cell(self, cell):
        neighbors = []
        row, col = cell[0],cell[1]
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # Possible directions: right, left, up, down.
        for a,b in directions:
            new_row,new_col = row + a,col + b
            if 0 <= new_row < self.n and 0 <= new_col < self.m: #Makes sure assumed neighbor exists in the grid.
                self.swap((row, col),(new_row,new_col))
                neighbors.append(self.state)
                self.swap((row, col),(new_row,new_col)) #Swap back
        return neighbors
    #returns a list that contains all neighbors of the cell entered , used in get_neighbors
    
    def get_neighbors(self):
        L=[]
        for i in range (self.n):
            for j in range (self.m):
                if i%2==0 and j%2==0: #lignes et colonnes paires
                    L+= self.get_neighbors_cell(i,j)
                if i%2==1 and j%2==1:#lignes et colonnes impaires
                    L+= self.get_neighbors_cell(i,j)
        return L
    #returns a list that contains all neighbors of the node without repetitions (all edges possible considering a node)
    #########################

    def etats_possibles (self): #renvoie une liste d'états possibles chacun sous la forme de tuples de tuples
         etats = []
         P = grid.perm(self.n*self.m)
        for k in P:
            grid = list(k)
            etat = []
            for i in range (1,self.m-1): #on différencie les lignes
                etat.append(tuple(grid[(k-1)*self.n:k*self.n]))
            etat = tuple(etat) #on transforme la liste de tuples en tuple de tuples
            etats.append(etat)
        return etats

    def grid_to_graph(self): #convertit en liste les tuples pour pouvoir trouver les voisins et ajouter les edges
        etats = self.etats_possibles()
        graph = Graph(etats)
        for etat in etats:
            liste_etat = [] 
            for i in range(len(etat)):
                liste_etat.append([etat[i][j] for j in range(len(etat[i]))])
            grille = Grid(self.m,self.n,liste_etat)
            L = grille.get_neighbors()
            for g in L:
                graph.add_edge(grid.get_tuple_grid(),g.get_tuple_grid())
        return graph
    
    #amélioration du bfs (constrution adaptée au node considéré comme src):
    def nombres_etats_necessaires (self):
        L=[self.state]
        i=0
            while [list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)] not in L: #on souhaite passer des noeuds aux suivants (atteignable en 1 seul swap) on regarde  que la grille rangée n'est pas apparue pour savoir combien d'edges il faudra considérer , cela évite d'avoir à créer l'ensemble des noeuds possibles dans la majortié des cas
                for l in L:
                L = [x for x in L if x != self.state] + self.get_neighbors(l) #enlever l'état de départ qui ne sert qu'à initier la boucle for
                L=list(set(L)) #supprimer les doublons inutiles
                i+=1
        return i # renvoi le nombre d'edges minimal qu'il faudra faire pour pouvoir éxectuer bfs sur self.state
    
    def etats_necessaires (self):
        L=[self.state]
            for k in range (self.nombres_etats_necessaires()):
                for l in L:
                        L=+ self.get_neighbors(l) # liste de grilles du réseau du départ à la destination
        return([tuple(self.get_tuple_grid(z) for z in o) for o in L]) #renvoyer un tuple de "grid transformée tuples"
    
    def grid_to_graph_improved(self): #convertit en liste les tuples pour pouvoir trouver les voisins et ajouter les edges sans avoir considérés d'edges inutiles
        etats = self.etats_necessaires()
        graph = Graph(etats)
        for etat in etats:
            liste_etat = [] 
            for i in range(len(etat)):
                liste_etat.append([etat[i][j] for j in range(len(etat[i]))])
            grille = Grid(self.m,self.n,liste_etat)
            L = grille.get_neighbors()
            for g in L:
                graph.add_edge(grid.get_tuple_grid(),g.get_tuple_grid())
        return graph

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid
