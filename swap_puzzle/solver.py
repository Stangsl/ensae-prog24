from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    @staticmethod
    def get_solution(grid):
        L=[]
        for i in range (grid.n*grid.m):
            a,b=grid.find(i)
            if i%grid.m==0: #cas particulier si "i" doit aller tout à droite
                L+=get_swap_droite(a,b,grid.m-b) #faire self.m-b swap à droite
            if i%grid.m<b:   
                L+=get_swap_gauche(a,b,b-(i%grid.m)) #faire position moins reste swaps à gauche
            if i%grid.m>b:
                L+=get_swap_droite(a,b,i%grid.m-b) #faire reste moins positions swaps à droite
            if i//grid.n+1<a:
                L+=get_swap_haut(a,b,a-(i//grid.n+1)) #faire position moins quotient swaps en haut
        swap_seq(L)
        return(L)
            
                      
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """

