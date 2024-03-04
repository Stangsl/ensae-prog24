"""
This is the grid module. It contains the Grid class and its associated methods.
"""
#TO DO : commande find , commandes swap haut , droite ...
import random

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
            if b<self.m:
                b+=1
            else :
                b=0
                a+=1
            if a>self.n:
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
    import matplotlib.pyplot as plt    
    def grid_show(self):
        for i in range(self.n):
            for j in range(self.m):
                ax.text(j, i, str(self.state[i][j]), ha='center', va='center', color='black', fontsize=12)
    # Add numbers to each cell
        ax.axis('off')
    # Hide axes
        plt.show()
        return()
    #########################
    #########################Q6 grids -> nodes
    def get_nodes(self):
        nodes = []
        for i in range(self.n):
            for j in range(self.m):
                nodes += [self.state[i][j]]
        return nodes
     #Returns a list of ints containing all nodes corresponding to all cells of the grid.
        
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
    #returns a list that corresponds to every neighbors of the cell entered (cell entered as a tuple and neighbors are , for the moment , returned in a list of "cell as tuples" --> into dico? ).
    def get_neighbors(self):
        L=[]
        for i in range (self.n):
            for j in range (self.m):
                if i%2==0 and if j%2==0: #lignes paires
                    L+= self.get_neighbors_cell(i,j)
                if i%2==1 and if j%2==1:
                    L+= self.get_neighbors_cell(i,j)
        return(L)
    #returns a list that corresponds to every neighbours of the node (edges between every nodes)
    #########################
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
