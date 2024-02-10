from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    #A first solving method that finds every int "i" in [1;n*m] and puts "i" to its place then "i"+1 ... so that there are only right or left swaps depending on where "i" is found and then it remains only swaps to the top to fix "i" to its place.
    @staticmethod
    def get_solution(grid):
        L=[]
        for i in range (grid.n*grid.m):
            a,b=grid.find(i)
            if i%grid.m==0: #cas particulier si "i" doit aller tout à droite
                L+=grid.get_swap_droite(a,b,grid.m-b) #faire self.m-b swap à droite
            if i%grid.m<b:   
                L+=grid.get_swap_gauche(a,b,b-(i%grid.m)) #faire position moins reste swaps à gauche
            if i%grid.m>b:
                L+=grid.get_swap_droite(a,b,i%grid.m-b) #faire reste moins positions swaps à droite
            if i//grid.n+1<a:
                L+=grid.get_swap_haut(a,b,a-(i//grid.n+1)) #faire position moins quotient swaps en haut
        return(L)
            
                      
        """
        Solves the grid (by using swap_seq with the sequence "L") and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """

